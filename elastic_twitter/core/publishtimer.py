# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:05:53 2016

@author: Parag Guruji, paragguruji@gmail.com
"""
import os
import logging
from elasticsearch_dsl.connections import connections
from dateutil import parser
import pandas as pd
from elastic-twitter.

DAY_MAP = {0:'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}


class PublishTimer:
    '''Class that represents an agent which computes best time to publish for given user and provides API to access it 
    '''
    def __init__(self,
                 authorized_app_name='Data-better365',
                 user_id='19900726', 
                 oauth_token=
                     "19900726-juj60PJsX9FriRp2vMVRKT5sF0H2kYsJTD3m38T7J",
                 oauth_token_secret=
                     "Qfs3u9DOpTYRR1oq26rrDYEmiOKZ1KCUZmQHFMDsT5K7y",
                 es_host_list=['localhost:9400'],
                 es_timeout=40,
                 logger_name="PublishTimerLogger",
                 log_filename="PublishTimer.log"):
        
        #Set up logger
        self.log_dir = os.path.join(os.getcwd(), 'logs')
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.log_path = os.path.join(self.log_dir, log_filename)
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        self.logFormatter = logging.Formatter('%(asctime)s - %(name)s - \
        %(levelname)s - %(message)s')
        self.logHandler = logging.FileHandler(filename=self.log_path, mode='a')
        self.logHandler.setLevel(logging.INFO)
        self.logHandler.setFormatter(self.logFormatter)
        self.logger.addHandler(self.logHandler)

        # Start logging       
        self.logger.info("\n\nPublishTimer Logs .........\n")

                
        es_client = connections.create_connection(hosts=['localhost:9400'], timeout=40)
      
        