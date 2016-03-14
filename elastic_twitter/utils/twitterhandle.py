# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:53:31 2016

@author: Parag Guruji, paragguruji@gmail.com
"""

from twython import Twython, TwythonError
import json
import logging
import os

class TwitterHandle:
    'Base class for twitter data engine'

    def __init__(self, 
                 app_name,
                 logger_name="TwitterHandleLogger",
                 auth_filename="TwitterHandle.auth", 
                 log_filename="TwitterHandle.log"):
        """Create a twitter handle for given app. 
            Authentication information to be supplied through json file \
            specified by auth_path
        """
        # Create data and logs dirs if absent
        self.data_dir = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.log_dir = os.path.join(os.getcwd(), 'logs')
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            
        # Set auth_path, log_path and register logger
        self.auth_path = os.path.join(self.data_dir, auth_filename)
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
        self.logger.info("\n\nTwitterHandle Logs .........\n")
        
        # Create a twitter-handle for given app_name
        self.handle = self.get_twitter_handle(app_name)

      
    def get_twitter_handle(self,
                           app_name,
                           oauth_token=None,
                           oauth_token_secret=None):
        """Returns a Twython object for given app name using authentication \
        info
           specified in file at auth_path (default: data/twython_auth.json)
           :param app_name: name of the registered twitter app for \
           authentication
        """
        try:
            auth_data = json.loads(open(self.auth_path).read())       
        except IOError as ioe:
            self.logger.error(ioe.message, 
                              exc_info=True, 
                              extra={'auth_path': self.auth_path})
            return None
        except Exception as ie:
            self.logger.error(ie.message, 
                              exc_info=True, 
                              extra={'auth_path': self.auth_path})
            return None
        if not auth_data.has_key(app_name):
            self.logger.warning("App name '"+ app_name +"' not Registered. \
            Use add_app to register.", exc_info=False)
            return None
        try:
            if not (oauth_token is None or oauth_token_secret is None):
                auth_data['oauth_token'] = oauth_token
                auth_data['oauth_token_secret'] = oauth_token_secret
            twython_obj = Twython(**auth_data[app_name])
            self.logger.info("twython object created:" + twython_obj.__repr__())            
            return twython_obj
        except TwythonError as e:
            self.logger.error(e.message + "\nCheck Twython's init signature \
            vs config data in data/twython_auth.json for correct keyword-args",
                exc_info=True, extra=auth_data[app_name])
            return None
    

    def add_app(self, 
                app_name, 
                app_key,
                app_secret, 
                oauth_token, 
                oauth_token_secret):
        """Adds an entry to json file specified by self.auth_path.
           Overwrites if entry exists. 
            :Returns: 0 on success, -1 on failure
        """
        entry = {app_name: {
                    "oauth_token_secret": oauth_token_secret, 
                    "app_secret": app_secret, 
                    "oauth_token": oauth_token, 
                    "app_key": app_key}}
        try:
            auth_data = json.loads(open(self.auth_path).read())
            auth_data.update(entry)
            with open(self.auth_path, "w") as f:
                json.dump(auth_data, f)
        except Exception as ie:
            self.logger.error(ie.message, 
                              exc_info=True, 
                              extra={'auth_path': self.auth_path})
            return -1
        return 0
        
        
    def remove_app(self, app_name):
        """Removes and returns as dict an entry from json file specified by \
        self.auth_path, if exists.
        """
        try:
            auth_data = json.loads(open(self.auth_path).read())
            entry = {app_name: auth_data.pop(app_name, None)}
            with open(self.auth_path, "w") as f:
                json.dump(auth_data, f)
            return entry
        except Exception as ie:
            self.logger.error(ie.message, 
                              exc_info=True, 
                              extra={'auth_path': self.auth_path})
        return {"app_name": None}
        
        