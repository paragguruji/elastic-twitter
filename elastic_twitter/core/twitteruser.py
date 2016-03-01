# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:33:06 2016

@author: Parag Guruji, paragguruji@gmail.com
"""

from elastic_twitter.utils.twitterhandle import TwitterHandle
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, Q
from elastic_twitter.utils.es.doc_types import Tweet
import datetime

class TwitterUser:
    '''Class to fetch data of one twitter user
    '''
    def __init__(self,
                 authorized_app_name='Data-better365',
                 user_id='19900726', 
                 oauth_token=
                     "19900726-juj60PJsX9FriRp2vMVRKT5sF0H2kYsJTD3m38T7J",
                 oauth_token_secret=
                     "Qfs3u9DOpTYRR1oq26rrDYEmiOKZ1KCUZmQHFMDsT5K7y",
                 es_host_list=['localhost'],
                 es_timeout=20):
        """Create a TwitterHandle for given oauth_token and oauth_token_secret
        """
        self.user_id = user_id
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.handle = TwitterHandle(app_name=authorized_app_name)
        self.handle.handle = self.handle.get_twitter_handle(
                                app_name=authorized_app_name,
                                oauth_token=self.oauth_token,
                                oauth_token_secret=self.oauth_token_secret)
        self.es_client = connections.create_connection(hosts=es_host_list,
                                                       timeout=es_timeout)
    
    
    def fetch_profile(self, **kwargs):
        '''Fetches profile of this user with options given in **kwargs'''
        tweet_list= self.handle.handle.get_user_timeline(user_id=self.user_id,
                                                         count=200,
                                                         trim_user=True,
                                                         exclude_replies=False,
                                                         include_rts=True)
        return tweet_list
        
        
    def save_tweet(self, tweet_dict):
        Tweet.init()
        tweet_dict.update({'meta': {'id': tweet_dict['id'], 
                                   'index':self.get_tweet_index()}})        
        tweet = Tweet(**tweet_dict)
        tweet.save()

    #move to utils    
    def get_tweet_index(self):
        return 'tweets-index-' + '-'.join(
                        [str(l) for 
                             l in list(
                                 datetime.date.isocalendar(
                                     datetime.datetime.now()))][:2])    
        