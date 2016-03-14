# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:43:06 2016

@author: Parag Guruji, paragguruji@gmail.com
"""

from elasticsearch_dsl.connections import connections
from dateutil import parser
import pandas as pd
#import numpy as np
#import matplotlib.mlab as mlab
#import matplotlib.pyplot as plt
DAY_MAP = {0: 'mon', 1: 'tue', 2: 'wed', 3: 'thu', \
            4: 'fri', 5: 'sat', 6: 'sun'}

es_client = connections.create_connection(hosts=['localhost:9400'], timeout=40)

search_body =   { 
                    "filter" :
                    { 
                        "term" :
                        {
                            "user.id" : 19900726
                        }
                    },
                    "fields" : 
                    [
                        'id', 
                        'created_at', 
                        'retweet_count',
                        'favorite_count'
                    ],
                    "size" : 1
                }


res = es_client.search( index='_all', \
                        doc_type='tweet', \
                        body=search_body)
cnt = res['hits']['total']
if not cnt:
    print "No data in ES for user:", search_body['filter']['term']['user.id']
else:
    search_body["size"] = cnt
    res1 = es_client.search(body=search_body)
    for i in range(len(res1['hits']['hits'])):
        for k in res1['hits']['hits'][i]['fields'].keys():
            res1['hits']['hits'][i]['fields'][k] \
            = res1['hits']['hits'][i]['fields'][k][0]
        d = parser.parse(res1['hits']['hits'][i]['fields'].pop('created_at'))
        res1['hits']['hits'][i]['fields']['day'] = d.weekday()
        res1['hits']['hits'][i]['fields']['hour'] = d.hour
        res1['hits']['hits'][i]['fields']['minute'] = d.minute
        res1['hits']['hits'][i]['fields']['engagement'] \
        = res1['hits']['hits'][i]['fields'].get('retweet_count', 0) \
        + res1['hits']['hits'][i]['fields'].get('favorite_count', 0) * 100
    
    
    df = pd.concat( map(pd.DataFrame.from_dict, res1['hits']['hits']), \
                    axis=1)['fields'].T
    df = df.reset_index(drop=True)    
    
    cols_to_norm = ['engagement']
    df[cols_to_norm] = df[cols_to_norm].apply(lambda x: x/(x.max() - x.min()))

    df_daywise = [df[(df.day==i)][[ 'day', \
                                    'hour', \
                                    'minute', \
                                    'engagement' ]] for i in range(7)]
    out_dict = {'twitter_id': search_body['filter']['term']['user.id'], \
                'response': []}
    for df_i in df_daywise:
        response_dict = {}
        df_i['rank'] = df_i.engagement.rank(method='first', ascending=False)
        d = df_i.sort_values(by='rank').loc[df_i['rank'].isin(range(1, 51))]
        dt = d.T
        response_dict["day"] = DAY_MAP[dt[d.index[0]].day.astype(int)]
        response_dict["times"] = ['{}:{}'.format(\
                                            dt[i].hour.astype(int), \
                                            dt[i].minute.astype(int)) \
                                    for i in d.index]
        out_dict['response'].append(response_dict)
        
        
#    dft = df.T
#    mat = pd.DataFrame([[[0.0]*60]*7]*24)
#    
#    for i in df.index:
#        mat[dft[i].day.astype(int)]\
#            [dft[i].hour.astype(int)]\
#            [dft[i].minute.astype(int)] += dft[i].engagement






























#print "Plotting now...."
#
#N = len(df)
##menMeans = (20, 35, 30, 35, 27)
#
#ind = np.arange(N)  # the x locations for the groups
#width = 0.005       # the width of the bars
#
#fig, ax = plt.subplots()
#rects1 = ax.bar(ind, df['engagement'], width, color='g')
#
#ax.set_ylabel('Engagement Score')
#ax.set_title('Engagement Score VS Tweet Ids')
#ax.set_xticks(ind + width)
#ax.set_xticklabels(df['id'])
#
#def autolabel(rects):
#    # attach some text labels
#    i = 0    
#    for rect in rects:
#        i+=1
#        if not i%200:
#            continue
#        height = rect.get_height()
#        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
#                '%d' % int(height),
#                ha='center', va='bottom')
#
#autolabel(rects1)
##autolabel(rects2)
#
#plt.show()
