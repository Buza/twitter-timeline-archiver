twitter-timeline-archiver
=========================

A simple script for archiving your Twitter timeline.

This script is designed to archive your friends timeline (i.e. all of the
Tweets you see that were posted by the people you follow).

It is intended to run as a cron job -- with a frequency dependent
upon how many people you follow and how often they post.

Every day, this script will create a new file of the format MM_DD_YYYY.dat,
which is a serialized dictionary indexed by Tweet ID of all of the Tweets
posted by the people you follow. This dictionary contains every Tweet posted
on a given day.

Dependencies
============

python-twitter: http://code.google.com/p/python-twitter/
