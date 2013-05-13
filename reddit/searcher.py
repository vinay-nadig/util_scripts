#!/usr/bin/env python

from time import sleep
from datetime import datetime
from urllib2 import HTTPError
import praw
import pickle


class Searcher(object):
    def __init__(self, poll_int=300):
        self.r = praw.Reddit("Job posting poll app by /u/hobblegobber")
        self.dic_of_reddits = {}

        #Settings
        self.poll_int = poll_int

    def add_subreddit(self, subr=None):
        if(subr):
            subr_handler = self.r.get_subreddit(subr)
            try:
                subr_handler.description
            except HTTPError:
                return
            self.dic_of_reddits[subr_handler] = {"Last_Check" : None, "Cache" : None}

    def remove_subreddit(self, subr=None):
        if(subr):
            if(self.dic_of_reddits.has_key(subr)):
                self.dic_of_reddits.pop(subr)

    def set_poll_interval(self, intr=300):
        self.poll_int = intr

    def get_new_posts(self):
        # Returns a dictionary of posts
        # Format : {subreddit_object : list_of_new_posts}
        new_posts = {}
        for subreddit in self.dic_of_reddits:

            if not self.dic_of_reddits[subreddit]["Cache"]:
                temp = subreddit.get_new(limit=10)
                temp_cache = [submission.title for submission in temp]
                self.dic_of_reddits[subreddit]["Cache"] = temp_cache
                new_posts[subreddit] = temp_cache
            else:
                temp = subreddit.get_new(limit=10)
                temp_cache = [submission.title for submission in temp]
                new_subs = [x for x in temp_cache if x not in self.dic_of_reddits[subreddit]["Cache"]]
                now = datetime.now()
                self.dic_of_reddits[subreddit] = {"Last_Check" : now, "Cache" : temp_cache}
                new_posts[subreddit] = new_subs

        return new_posts


