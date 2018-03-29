#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'mythnc'
SITENAME = 'Warai Otoko'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'

DATE_FORMATS = {
    'en': '%Y-%m-%d',
}

# STATIC
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    #('Pelican', 'http://getpelican.com/'),
    #('Python.org', 'http://python.org/'),
    #('Jinja2', 'http://jinja.pocoo.org/'),
    #('You can modify those links in your config file', '#'),
 )

# Social widget
SOCIAL = (('Github', 'http://github.com/mythnc'),
)

DEFAULT_PAGINATION = 10

# Theme
THEME = '../pelican-themes/pelican-bootstrap3'

# Plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites', 'tag_cloud', 'tipue_search']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Menu items
MENUITEMS = [
    ('Archives', '/archives'),
    ('Categories', '/categories'),
    ('Tags', '/tags'),
]

DIRECT_TEMPLATES = (
    'index',
    'tags',
    'categories',
    'archives',
    'search',
)

# Article info
SHOW_DATE_MODIFIED = True
SHOW_ARTICLE_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True
SUMMARY_MAX_LENGTH = 7

# Sidebar
#DISABLE_SIDEBAR_TITLE_ICONS = True
HIDE_SIDEBAR = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
