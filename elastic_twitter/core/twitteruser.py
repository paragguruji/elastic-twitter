# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:33:06 2016

@author: Parag Guruji, paragguruji@gmail.com
"""

import os
import logging
import time
import datetime

from twython import TwythonError, TwythonAuthError, TwythonRateLimitError
from elasticsearch_dsl.connections import connections
from elastic-twitter.elastic_twitter.utils.twitterhandle import TwitterHandle
from elastic-twitter.elastic_twitter.utils.es.doc_types import Tweet


SESSION_DURATION_MINUTES = 15
SESSION_TIMELINE_REQUEST_LIMIT = 180
SESSION_FOLLOWER_IDS_REQUEST_LIMIT = 15
RETRY_LIMIT = 3

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
                 es_host_list=['localhost:9400'],
                 es_timeout=20,
                 logger_name="TwitterUserLogger",
                 log_filename="TwitterUser.log"):
        """Create a TwitterHandle for given oauth_token and oauth_token_secret
        """
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
        self.logger.info("\n\nTwitterUser Logs .........\n")
        
        # Set up twitter handle
        self.user_id = user_id
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.handle = TwitterHandle(app_name=authorized_app_name)
        self.handle.handle = self.handle.get_twitter_handle(
                                app_name=authorized_app_name,
                                oauth_token=self.oauth_token,
                                oauth_token_secret=self.oauth_token_secret)
        # Set up Elasticsearch
        self.es_client = connections.create_connection(hosts=es_host_list,
                                                       timeout=es_timeout)
        
        # Set up timeline request session
        self.timeline_session_start_time = datetime.datetime.now()
        self.timeline_session_end_time = self.timeline_session_start_time + \
            datetime.timedelta(minutes=SESSION_DURATION_MINUTES)
        self.timeline_request_count = 0
        
        # Set up follower_ids request session
        self.follower_ids_session_start_time = datetime.datetime.now()
        self.follower_ids_session_end_time = \
            self.follower_ids_session_start_time + \
            datetime.timedelta(minutes=SESSION_DURATION_MINUTES)        
        self.follower_ids_request_count = 0
        
        # Set up counts for logging purpose       
        self.tweet_per_follower_count = 0
        self.timeline_request_record = 0
        self.follower_ids_request_record = 0


    def fetch_timeline(self, **kwargs):
        """Fetches list of tweets from user-timeline
            :Returns: [list] list of dicts of tweet objects 
            :param twitter_handle: [Twython] a valid authenticated Twython object 
                :default: self.handle.handle
            :param user_id: [long] user_id of twitter user whose timeline is to be fetched
                :default: self.user_id
            :param count: [int] number of tweets
                :default: 200
            :param trim_user: [boolean] Twitter API trim_user option
                :default: True
            :param exclude_replies: [boolean] Twitter API exclude_replies option
                :default: False
            :param include_rts: [boolean] Twitter API include_rts option
                :default: True
            :param since_id: [long] Twitter API since_id option. give priority to max_id
                :default: None
            :param max_id: [long] Twitter API max_id option. has priority over since_id
                :default: None
        """
        twitter_handle  = kwargs.get('twitter_handle', self.handle.handle)
        user_id         = kwargs.get('user_id', self.user_id)
        count           = kwargs.get('count', 200)
        trim_user       = kwargs.get('trim_user', True)
        exclude_replies = kwargs.get('exclude_replies', False)
        include_rts     = kwargs.get('include_rts', True)
        since_id        = kwargs.get('since_id', None)
        max_id          = kwargs.get('max_id', None)
        
        if datetime.datetime.now() >= self.timeline_session_end_time:
                self.timeline_session_start_time  = datetime.datetime.now()
                self.timeline_session_end_time = \
                    self.timeline_session_start_time + \
                    datetime.timedelta(minutes=SESSION_DURATION_MINUTES)
                self.timeline_request_count = 0
        elif self.timeline_request_count >= SESSION_TIMELINE_REQUEST_LIMIT:
            sleep_time = (self.timeline_session_end_time - \
                            datetime.datetime.now()).total_seconds() + 60                
            self.logger.info("Sleeping in fetch_timeline for " + \
                                    str(sleep_time) + " seconds" + \
                                    "\n\tsession_timeline_reqs: " + \
                                    str(self.timeline_request_count) + \
                                    "\n\ttotal_timeline_reqs: " + \
                                    str(self.timeline_request_record) + \
                                    "\n\tsession_follower_ids_reqs: " + \
                                    str(self.follower_ids_request_count) + \
                                    "\n\ttotal_follower_ids_reqs: " + \
                                    str(self.follower_ids_request_record) )
            time.sleep(sleep_time)
            return self.fetch_timeline(**kwargs)
        self.timeline_request_count += 1
        self.timeline_request_record += 1
        status_word = 'SUCCESS'
        try:
            if max_id:
                tweet_list= twitter_handle.get_user_timeline(
                                user_id=user_id,
                                count=count,
                                trim_user=trim_user,
                                exclude_replies=exclude_replies,
                                include_rts=include_rts,
                                max_id=max_id)
            elif since_id:
                tweet_list= twitter_handle.get_user_timeline(
                                user_id=user_id,
                                count=count,
                                trim_user=trim_user,
                                exclude_replies=exclude_replies,
                                include_rts=include_rts,
                                since_id=since_id)
            else:
                tweet_list= twitter_handle.get_user_timeline(
                                user_id=user_id,
                                count=count,
                                trim_user=trim_user,
                                exclude_replies=exclude_replies,
                                include_rts=include_rts)
        except TwythonAuthError as tae:
            self.logger.warning(tae.message + str(kwargs),
                                exc_info=True,
                                extra=kwargs)
            tweet_list = []
            status_word = 'TwythonAuthError'
        except TwythonRateLimitError as trle:
            self.logger.warning(trle.message + str(kwargs), 
                                  exc_info=True, 
                                  extra=kwargs )
            sleep_time = SESSION_DURATION_MINUTES * 60
            self.logger.info("Unexpected Rate Limit Occured. \
            Sleeping in fetch_timeline for " + \
                                    str(sleep_time) + " seconds" + \
                                    "\n\tsession_timeline_reqs: " + \
                                    str(self.timeline_request_count) + \
                                    "\n\ttotal_timeline_reqs: " + \
                                    str(self.timeline_request_record) + \
                                    "\n\tsession_follower_ids_reqs: " + \
                                    str(self.follower_ids_request_count) + \
                                    "\n\ttotal_follower_ids_reqs: " + \
                                    str(self.follower_ids_request_record) )
            time.sleep(sleep_time)
            tweet_list = []
            status_word = 'TwythonRateLimitError'
        if tweet_list:
            self.logger.info(str(len(tweet_list)) + "Tweets from id:" + \
                            str(tweet_list[-1].get('id')) + " through id:" + \
                            str(tweet_list[0].get('id')) + " fetched.")
        return tweet_list, status_word


    def fetching_stint(self, **kwargs):
        """Mediator function to fetch max 200 tweets for given **kwargs
            :Returns:   on success: [long] tweet_id of oldest tweet from tweet_list returned by fetch_timeline.
                        on failure: [int] -1 when empty list/None is recieved.
        """
        tweet_list, status_word = self.fetch_timeline(**kwargs)
        if tweet_list:            
            for tweet in tweet_list:
                self.save_tweet(tweet)
            return tweet_list[-1].get('id', 0)
        elif status_word == 'TwythonAuthError':
            return -2
        elif status_word == 'TwythonRateLimitError':
            return -3
        return -1


    def fetch_profile(self, **kwargs):
        '''Fetches profile of this user with options given in **kwargs'''
        count = kwargs.get('count', 200)
        while count:
            if count > 200:
                kwargs['count'] = 200
            else:
                kwargs['count'] = count
            max_id = self.fetching_stint(**kwargs)
            if max_id == kwargs.get('max_id', 1):
                return max_id
            elif max_id == -1:
                return kwargs['max_id']
            else:
                kwargs['max_id'] = max_id
                if count > 200:                
                    count -= 200
                else:
                    count = 0
        return kwargs['max_id']


    def purge_key_deep(self, a_dict, key):
        """Removes given key from all nested levels of a_dict
        """
        try:
            a_dict.pop(key)
        except KeyError:
            pass
        for k in a_dict.keys():
            if isinstance(a_dict[k], dict):
                a_dict[k] = self.purge_key_deep(a_dict[k], key)
        return a_dict
            

    def save_tweet(self, tweet_dict):
        """Saves one tweet object to ES in the index of name tweet-index-<YEAR>-<#WEEK>"""
        INDEX_NAME = self.get_tweet_index()

        tweet_dict = self.purge_key_deep(tweet_dict, 'media')
        tweet_dict = self.purge_key_deep(tweet_dict, 'urls')
        tweet_dict = self.purge_key_deep(tweet_dict, 'url')
        
        time_str = tweet_dict.get('created_at', '')
        if time_str:
            tweet_dict['created_at'] = datetime.datetime.strptime(time_str, 
                                        "%a %b %d %H:%M:%S +0000 %Y")
        else:
            tweet_dict['created_at'] = None

        tweet_dict.update({u'_id': tweet_dict.get(u'id', "00000"), 
                           u'_index': INDEX_NAME})        
        tweet = Tweet(**tweet_dict)
        res = tweet.save()
        self.tweet_per_follower_count+=1
        if res:
            self.logger.info(" Success: tweet #" + \
                                str(self.tweet_per_follower_count) + \
                " for user_id: " + str(tweet_dict['user']['id']) + \
                " saved in index: " + INDEX_NAME + \
                " tweet_id: " + str(tweet_dict['id']))
        else:
            self.logger.error(" Failure: tweet #" + \
                                str(self.tweet_per_follower_count) + \
                " for user_id: " + str(tweet_dict['user']['id']) + \
                " not saved in index: " + INDEX_NAME + \
                " tweet_id: " + str(tweet_dict['id']))
 

    #move to utils    
    def get_tweet_index(self):
        """Generates ES index name for tweet object from current time as tweet-index-<YEAR>-<#WEEK>
        """
        return 'tweets-index-' + '-'.join(
                        [str(l) for 
                             l in list(
                                 datetime.date.isocalendar(
                                     datetime.datetime.now()))][:2])


    def list_follower_ids(self, **kwargs):
        """Return a list of ids of all followers of user specified by
           user_id or screen_name keyword_args. 
           If user_id is valid, screen_name is ignored. 
           If both are invalid, raises ValueError 
           :param user_id: (optional) user_id of target user
           :param screen_name: (optional) screen_name of target user
           :param count: (optional) #followers to fetch ids of.
        """
        followers_ids = []
        next_cursor = -1
        
        while next_cursor:
            if datetime.datetime.now() >= self.follower_ids_session_end_time:
                self.follower_ids_session_start_time  = datetime.datetime.now()
                self.follower_ids_session_end_time = \
                    self.follower_ids_session_start_time + \
                    datetime.timedelta(minutes=SESSION_DURATION_MINUTES)
                self.follower_ids_request_count = 0
            elif self.follower_ids_request_count >= \
                    SESSION_FOLLOWER_IDS_REQUEST_LIMIT:
                sleep_time = (self.follower_ids_session_end_time - \
                                datetime.datetime.now()).total_seconds() + 60                
                self.logger.info("Sleeping in def list_follower_ids for " + \
                                    str(sleep_time) + " seconds" + \
                                    "\n\tsession_timeline_reqs: " + \
                                    str(self.timeline_request_count) + \
                                    "\n\ttotal_timeline_reqs: " + \
                                    str(self.timeline_request_record) + \
                                    "\n\tsession_follower_ids_reqs: " + \
                                    str(self.follower_ids_request_count) + \
                                    "\n\ttotal_follower_ids_reqs: " + \
                                    str(self.follower_ids_request_record) )
                time.sleep(sleep_time)
                continue
            self.follower_ids_request_count += 1
            self.follower_ids_request_record += 1
            try:
                res_dict = self.handle.handle.get_followers_ids(
                                        user_id = kwargs.get(
                                            'user_id', None),
                                        screen_name = kwargs.get(
                                            'screen_name', None),                                            
                                        stringify_ids = False,
                                        count = kwargs.get('count', 5000),
                                        cursor = next_cursor)
                next_cursor = res_dict['next_cursor']
                followers_ids += res_dict['ids']
            except TwythonRateLimitError as trle:
                self.logger.error(trle.message + str(kwargs), 
                                  exc_info=True, 
                                  extra=kwargs)
                continue
            except TwythonError as te:
                self.logger.error(te.message + str(kwargs), 
                                  exc_info=True, 
                                  extra=kwargs)
        followers_ids = list(set(followers_ids))
        return followers_ids
        

    def fetch_follower_timelines(self, 
                                 user_id=None,
                                 followers_count=5000, 
                                 tweets_count=3000):
        """Extracts and saves to ES the tweet objects from timelines of followers of a user
            :param user_id: [long] user_id of target user
                :default: self.user_id
            :param followers_count: [long] #followers
            :param tweets_count: [long] #tweets to fetch per follower
        """
        if not user_id:
            user_id = self.user_id
        user_id_list = self.list_follower_ids(**{'user_id': user_id, 
                                                 'count':followers_count})
        self.logger.info("List of " + str(len(user_id_list)) + \
                            " followers fetched for user_id: " + str(user_id))
        for follower_id in user_id_list:    
            self.tweet_per_follower_count = 0
            self.fetch_profile(user_id=follower_id, count=tweets_count)
            self.logger.info("follower #" +\
                str(user_id_list.index(follower_id) + 1) + \
                " timeline fetched. follower_id: " + str(follower_id) + \
                " #tweets: " + str(self.tweet_per_follower_count))
                
                
if __name__=='__main__':
    userobj = TwitterUser()
    #userobj.fetch_profile(user_id=userobj.user_id, count=3000)
    #userobj.logger.info("profile of user_id: " + \
                        #str(userobj.user_id) + " fetched.")                    
    #userobj.fetch_follower_timelines(followers_count=7000)
    