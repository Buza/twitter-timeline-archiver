#
# TTimeline.py : A simple script for archiving your Twitter timeline.
#
# This script is designed to archive your friends timeline (i.e. all of the
# Tweets you see that were posted by the people you follow).
#
# It is intended to run as a cron job -- with a frequency dependent
# upon how many people you follow and how often they post.
#
# Every day, this script will create a new file of the format MM_DD_YYYY.dat, 
# which is a serialized dictionary indexed by Tweet ID of all of the Tweets
# posted by the people you follow. This dictionary contains every Tweet posted
# on a given day.
#
# Dependencies:
#   python-twitter : http://code.google.com/p/python-twitter/
#

import time
import pickle
import twitter

my_consumer_key = CONSUMER_KEY
my_consumer_secret = CONSUMER_SECRET
my_access_token_key = ACCESS_TOKEN
my_access_token_secret = ACCESS_SECRET

def step(dict, now, _page, api):
    foundCount = 0
    results = api.GetFriendsTimeline(count=100, page=_page)
    for status in results:
        item = status.AsDict()
        tmp = time.strptime(item['created_at'],'%a %b %d %H:%M:%S +0000 %Y')

        #We're only interested in Tweets that were posted today.
        if now.tm_mon == tmp.tm_mon and now.tm_mday == tmp.tm_mday and now.tm_year == tmp.tm_year:
          if(dict.has_key(str(item['id']))):
            continue
          else:
            foundCount = foundCount + 1
            dict[str(item['id'])] = item
    _page = _page + 1
    return foundCount

if __name__ == '__main__':
    _page = 1
    _api = twitter.Api(consumer_key=my_consumer_key,
                           consumer_secret=my_consumer_secret,
                           access_token_key=my_access_token_key,
                           access_token_secret=my_access_token_secret,
                           debugHTTP=False)

    now = time.localtime()

    tweetdict = {}
    try:
      filename = "%d_%d_%d.dat" % (now.tm_mon, now.tm_mday, now.tm_year)
      tweetfile = open(filename, 'r+')
      tweetdict = pickle.load(tweetfile)
      tweetfile.close()
    except:
      pass

    tweetfile = open(filename, 'w+')
    while step(tweetdict, now, _page, _api):
      _page = _page + 1
      continue

    pickle.dump(tweetdict, tweetfile)
    tweetfile.close()
