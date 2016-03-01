# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:04:20 2016

@author: Parag Guruji, paragguruji@gmail.com
"""

from elasticsearch_dsl import DocType, String, Date, Boolean, analyzer
import datetime

tweet_analyzer = analyzer('tweet_analyzer',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["tweet_analyzer"]
)


class Tweet(DocType):
    """DocType for saving a tweet in ES
    """
    id_str = String()
    saved_at = Date()
    obsolete = Boolean

        
    class Meta:
        index = 'tweet-index'


    def save(self, **kwargs):
        self.id_str = kwargs['idstr']
        self.obsolete = False
        self.saved_at = datetime.now()
        return super.save(**kwargs)
