#!/usr/bin/env python

from searcher import Searcher
from pynotify import URGENCY_CRITICAL as CRIT
from time import sleep, asctime
import pickle
import pynotify

POST_FILE = "/home/vinay/.new_posts.txt"
POLL_FREQ = 180

def main():

    if POST_FILE.startswith("@"):
        print "Please set the POST_FILE variable"
        return

    if not POLL_FREQ:
        print "Please set the poll frequency. (should be atleast 45)"
        return

    s = Searcher(POLL_FREQ)
    s.add_subreddit("forhire")
    s.add_subreddit("jobbit")
    s.add_subreddit("jobs4Bitcoins")

    pynotify.init("Job Searcher")

    while True:
        new_posts = s.get_new_posts()

        if(new_posts):
            for subreddit in new_posts:
                if(len(new_posts[subreddit]) < 5):
                    for post in new_posts[subreddit]:
                        n = pynotify.Notification(subreddit.display_name, post)
                        n.set_urgency(CRIT)
                        n.show()
                        print subreddit.display_name + " : " + post

                else:
                    fp = open(POST_FILE, "a")
                    fp.write(asctime())
                    for post in new_posts[subreddit]:
                        fp.write(subreddit.display_name + " : " + post + "\n")
                    fp.close()
                    n = pynotify.Notification("New Posts!", "Too many new posts! New posts have been saved to ~/.new_posts.txt")
                    n.set_urgency(CRIT)
                    n.show()
        sleep(s.poll_int)


if __name__ == "__main__":
    main()

