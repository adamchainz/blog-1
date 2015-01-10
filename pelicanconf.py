#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'James'
SITENAME = u'James Cooke'
TAGLINE = u'London based Python developer'
SITEURL = ''
# LAZY TODO should move this to content.
PROFILE_IMG_URL = u'http://userserve-ak.last.fm/serve/126/5888928.jpg'

TIMEZONE = u'Europe/London'
DEFAULT_DATE_FORMAT = u'%b %d, %Y'

DEFAULT_LANG = u'en'
DEFAULT_CATEGORY = u'ZZZ Misc...'

# Turn off all feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
SOCIAL = (
    ('Twitter', 'https://twitter.com/jamesfublo'),
    ('GitHub', 'https://github.com/jamescooke'),
    ('Stack Overflow', 'http://stackoverflow.com/users/1286705/jamesc'),
)

MENUITEMS = [('Home', '/'), ('About', '/pages/hello-my-name-is-james.html'),]
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

TYPOGRIFY = True

THEME = '/home/james/active/droidstrap'

# Droidstrap specific config:
SHOW_SCM_LINKS = True
SCM_LINK_TEXT = 'View, comment, edit source on GitHub'
SCM_BASE_URL = 'https://github.com/jamescooke/blog/tree/master/'
