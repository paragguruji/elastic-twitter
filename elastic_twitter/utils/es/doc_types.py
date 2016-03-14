# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:04:20 2016

@author: Parag Guruji, paragguruji@gmail.com
"""

from elasticsearch_dsl import DocType, Date, String, analyzer, Boolean, Long
from elasticsearch.connection.http_urllib3 import ConnectionTimeout
import datetime

tweet_analyzer = analyzer('tweet_analyzer',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["tweet_analyzer"]
)


class Tweet(DocType):
    """DocType for saving a tweet in ES
    """
    saved_at = Date()
    outdated = String()
        
    #class Meta:
        #index = 'tweet-index'

    def save(self, **kwargs):
        #kwargs['outdated'] = False
        #kwargs['saved_at'] = datetime.datetime.now()
        self.saved_at = datetime.datetime.now()        
        self.outdated = "No"
        try:
            return super(Tweet, self).save(**kwargs)
        except ConnectionTimeout as ct:
            raw_input("ConnectionTimeout with Elasticsearch." + str(ct) +\
            "\nFix it and then continue.")
            self.save(**kwargs)





'''class Tweet(DocType):
    """DocType for saving a tweet in ES
    """
    def __init_(self, meta):
        super(Tweet, self).__init__(meta=meta)        
        #self.Meta.index = INDEX_NAME
        #self.Meta.id = self.id
        
    id_str = String()
    saved_at = Date()
    obsolete = Boolean


    def save(self, **kwargs):
        self.obsolete = False
        self.saved_at = datetime.datetime.now()
        return super(Tweet, self).save(**kwargs)
'''

class ATweet(DocType):
    """DocType for saving a tweet in ES
    """
    id_str                      = String(index='not_analyzed')
    hashtags                    = String(index='not_analyzed')
    user_mentions               = String(index='not_analyzed')
    text                        = String(analyzer='snowball')
    created_at                  = Date()
    retweeted                   = Boolean()
    is_quote_status             = Boolean()
    retweet_count               = Long()
    user_id_str                 = String(index='not_analyzed')
    in_reply_to_status_id_str   = String(index='not_analyzed')
    in_reply_to_user_id_str     = String(index='not_analyzed')
    lang                        = String(index='not_analyzed')
    