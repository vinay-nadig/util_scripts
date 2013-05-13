#!/usr/bin/env python
from BeautifulSoup import BeautifulSoup
import re
import urllib
import argparse
import sys
import os

# Global data
subreddit_url = ""
sort_and_download = 1
image_limit = 0
time_frame = 'hour'
upvote_limit = 0
download_folder = '.'

def initialize_parser():
    parser = argparse.ArgumentParser(description = 'Download images from a subreddit')
    parser.add_argument('--url', '-u', help="url of the subreddit")
    parser.add_argument('-s', '--sort', action="store_false", help="Sort by upvotes and download. Default = top to bottom")
    parser.add_argument('-l', '--limit', help="number of images to download", type=int, default=1000)
    parser.add_argument('-d', '--directory', help="directory to save the images", default='os.getcwd()', nargs='?')


def main():
    initialize_parser()

main()
