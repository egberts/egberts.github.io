#!/Usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import pprint

# developing_site = True
developing_site = True
## Defines whether Pelican should use document-relative URLs or not.
## Only set this to True when developing/ testing and only if you
## fully understand the effect it can have on links/feeds.
# RELATIVE_URLS = True if developing_site else False
RELATIVE_URLS = True if developing_site else False
PDF_PROCESSOR = False


## Base URL of your web site. Not defined by default, so it is best
## to specify your SITEURL; if you do not, feeds will not be generated
## with properly-formed URLs. If your site is available via HTTPS, this
## setting should begin with https:// — otherwise use http://.
## Then append your domain, with no trailing slash at the end.
## Example: SITEURL = 'https://example.com'
## Only following allowed in SITEURL:
##    * HTTP protocol (https://)
##    * HTTP domain (example.com)
##    * TCP port (if not 80 with http: or 443 with https)
SITEURL = 'http://egberts.github.io'
SITE_SUBPATH = 'egberts'
SITE_DIR = ''
SITE_URL_TOP_LVL = '/'   # do not use double-slash here
if len(SITE_SUBPATH):
    # Do not let SITE_DIR be an absolute file path
    SITE_DIR = SITE_SUBPATH + '/'
    if RELATIVE_URLS:
        SITE_URL_TOP_LVL = '/' + SITE_SUBPATH + '/'
    else:
        SITE_URL_TOP_LVL = SITEURL + '/' + SITE_SUBPATH + '/'

THEME_DIRNAME = 'theme'
DRAFTS_DIRNAME = 'drafts'
ARTICLES_DIRNAME = 'articles'
PAGES_DIRNAME = 'pages'
TAGS_DIRNAME = 'tags'
CATEGORIES_DIRNAME = 'categories'
AUTHORS_DIRNAME = 'authors'
ARCHIVES_DIRNAME = 'archives'
DRAFT_ARTICLES_DIRNAME = DRAFTS_DIRNAME + '/' + ARTICLES_DIRNAME
DRAFT_PAGES_DIRNAME = DRAFTS_DIRNAME + '/' + PAGES_DIRNAME


############################
## Local content filesystem
############################
PATH = 'content'
##  Theme
THEME = 'themes/bootstrap2-dark'
## a list of directories and files to look at for pages, relative to PATH.
PAGE_PATHS = ['pages']
## A list of directories and files to look at for articles, relative to PATH.
ARTICLE_PATHS = ['articles']
## Get rid of author pages (since I'm the only author) and the archives page
## (since I'm doing that manually)
# DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'analytics',
DIRECT_TEMPLATES = ('index', CATEGORIES_DIRNAME, TAGS_DIRNAME, ARCHIVES_DIRNAME)
TEMPLATE_PAGES = {'feed.json': 'feed.json'}
# PAGINATED_TEMPLATES = { 'tag': None, 'category': None, 'author': None}
#
#  $PWD/content
#    +- theme/bootstrap2-dark
#.   +- articles
#.   +- pages


##------------------------------------
## Pelican Settings
##------------------------------------
# LOG_FILTER = [(logging.WARN, 'TAG_SAVE_AS is set to False')]

## Website info settings
AUTHOR = ''
EACH_SLUG_HAS_SUBDIR = False

## Your site name
SITENAME = 'Egberts'

TIMEZONE = 'EST5EDT'
## Tweet this, do not include '@' prefix here
TWITTER_USERNAME='egbertst'

MINIBIO = 'Just a high-speed network backend kind of guy doing deep processing of compiler languages, and detection of malwares'
DESCRIPTION = 'Egberts conducts researches on bleeding edges of malicious behaviors and its applicability toward multiple compiler languages.  Researching for many customers.'
DEFAULT_LANG = 'en'

## Google Analytics
GOOGLE_ANALYTICS = ''

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

## General settings
ABSOLUTE_SITEURL = SITEURL
DUCKDUCKGO_CUSTOM_SEARCH_SIDEBAR = True
# DATE_FORMATS = ''
# DEFAULT_DATE_FORMAT = ''

## Pelican processing settings
##
## Content Generaton
##   Articles
##   Pages
##   Drafts
##   Tags
##   Categories
##   Feeds
##   Indexes
## Static files


# INTRASITE_LINK_REGEX = ''

##-----------------------------------------------
## HTML layout
##-----------------------------------------------

## If set to True, several typographical improvements will be
## incorporated into the generated HTML via the Typogrify
## library, which can be installed via: pip install typogrify
TYPOGRIFY = False  # Nice typographic things

## sidebar - links - Blogrolls
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('SPLIT-CODE.COM', 'http://split-code.com/external_blogs.html'),
         ('Hexacorn', 'http://www.hexacorn.com/blog/'),
         ('Möbius Strip RE', 'https://www.msreverseengineering.com/blog/'),
         ("Dr. Fu's",
'http://fumalwareanalysis.blogspot.com/p/malware-analysis-tutorials-reverse.html'),
         ('Metova','https://metova.com/category/security/'),
         ('Quarkslab','https://blog.quarkslab.com/category/reverseengineering.html'),
         ('Reddit RE','https://www.reddit.com/r/ReverseEngineering/comments/is2et/can_we_collect_interesting_reverse_engineering/'),
         ('0x1338','http://0x1338.blogspot.com/'),
        )

## HTML layout - sidebar - Social links
## Social widget
SOCIAL_LABELS = (('e-mail', 'fas fa-envelope', 'mailto:egbert (a)(at) github.com'),
          ('Twitter', 'fab fa-twitter', 'https://twitter.com/egbertst'),
          ('GitHub', 'fab fa-github-square', 'https://github.com/egberts'),
          ('StackOverflow', 'fab fa-stack-overflow', 'https://stackoverflow.com/users/4379130/egbert-s'),
         )
SOCIAL = (('fas fa-envelope', 'mailto:egberts at github.com'),
          ('fab fa-github-square', 'https://github.com/egberts'),
          ('fab fa-stack-overflow', 'https://stackoverflow.com/users/4379130/egbert-s'),
          ('fab fa-linkedin', 'https://www.linkedin.com/in/1dyftm7u')
         )

#############################################################################
## Readers
#############################################################################

IGNORE_FILES = ['.#*',
   # prevents pelican from trying to parse notebook checkpoint files
                '.ipynb_checkpoints']

READERS = {'html': None}  # Don't parse HTML files
## Cache
LOAD_CONTENT_CACHE = False if developing_site else True


#############################################################################
## Output Generation
#############################################################################

OUTPUT_PATH = 'output'
## Delete the output directory, and all of its contents, before generating new
## files. This can be useful in preventing
## older, unnecessary files from persisting in your output. However, this is a
## destructive setting and should be
## handled with extreme care.
DELETE_OUTPUT_DIRECTORY = True
## Set to True if you want to copy the articles and pages in
## their original format (e.g. Markdown or reStructured-
## Text) to the specified OUTPUT_PATH.
OUTPUT_SOURCES = False

## Controls the extension that will be used by the SourcesGenerator.
## Defaults to .text. If not a valid string the default value will be used.
OUTPUT_SOURCES_EXTENSION = '.txt'

# processor output
THEME_STATIC_DIR = SITE_DIR + THEME_DIRNAME
THEME_STATIC_URL = SITE_URL_TOP_LVL + THEME_DIRNAME
BRAND_URL = SITE_URL_TOP_LVL + 'index.html'

if EACH_SLUG_HAS_SUBDIR:
    ARTICLES_URL = SITE_URL_TOP_LVL + ARTICLES_DIRNAME + '/'
    #NEW_ARTICLES_URL = ARTICLES_URL
    PAGES_URL = SITE_URL_TOP_LVL + PAGES_DIRNAME + '/'
    TAGS_URL = SITE_URL_TOP_LVL + TAGS_DIRNAME + '/'
    CATEGORIES_URL = SITE_URL_TOP_LVL + CATEGORIES_DIRNAME + '/'
    AUTHORS_URL = SITE_URL_TOP_LVL + AUTHORS_DIRNAME + '/'
    ARCHIVES_URL = SITE_URL_TOP_LVL + ARCHIVES_DIRNAME + '/'
    DRAFT_ARTICLES_URL = SITE_URL_TOP_LVL + DRAFT_ARTICLES_DIRNAME + '/'
    DRAFT_PAGES_URL = SITE_URL_TOP_LVL + DRAFT_PAGES_DIRNAME + '/'

    ARTICLE_URL = ARTICLES_URL + '{slug}/'
    PAGE_URL = PAGES_URL + '{slug}/'
    TAG_URL = TAGS_URL + '{slug}/'
    CATEGORY_URL = CATEGORIES_URL + '{slug}/'
    ARCHIVE_URL = ARCHIVES_URL + '{slug}/'
    AUTHOR_URL = AUTHORS_URL + '{slug}/'
    DRAFT_URL = DRAFT_ARTICLES_URL + '{slug}/'
    DRAFT_PAGE_URL = DRAFT_PAGES_URL + '{slug}/'

    ####INDEX_SAVE_AS = SITE_DIR + ARTICLES_DIRNAME + '/index.html'    # ARTICLES_SAVE_AS
    INDEX_SAVE_AS = SITE_DIR + ARTICLES_DIRNAME + '/index.html'    # ARTICLES_SAVE_AS
    PAGES_SAVE_AS = SITE_DIR + PAGES_DIRNAME + '/index.html'
    TAGS_SAVE_AS = SITE_DIR + TAGS_DIRNAME + '/index.html'
    CATEGORIES_SAVE_AS = SITE_DIR + CATEGORIES_DIRNAME + '/index.html'
    ARCHIVES_SAVE_AS = SITE_DIR + ARCHIVES_DIRNAME + '/index.html'
    AUTHORS_SAVE_AS = SITE_DIR + AUTHORS_DIRNAME + '/index.html'

    ARTICLE_SAVE_AS = SITE_DIR + ARTICLES_DIRNAME + '/{slug}/index.html'
    PAGE_SAVE_AS = SITE_DIR + PAGES_DIRNAME + '/{slug}/index.html'
    TAG_SAVE_AS = SITE_DIR + TAGS_DIRNAME + '/{slug}/index.html'
    CATEGORY_SAVE_AS = SITE_DIR + CATEGORIES_DIRNAME + '/{slug}/index.html'
    ARCHIVE_SAVE_AS = SITE_DIR + ARCHIVES_DIRNAME + '/{slug}/index.html'
    AUTHOR_SAVE_AS = SITE_DIR + AUTHORS_DIRNAME + '/{slug}/index.html'
    DRAFT_SAVE_AS = SITE_DIR + DRAFT_ARTICLES_DIRNAME + '/{slug}/index.html'
    DRAFT_PAGE_SAVE_AS = SITE_DIR + DRAFT_PAGES_DIRNAME + '/{slug}/index.html'
    AUTHORS_URL = AUTHORS_URL + '/index.html/'
    AUTHOR_URL = AUTHORS_URL + '/{slug}/index.html'
    AUTHORS_SAVE_AS = SITE_DIR + AUTHORS_DIRNAME + '/index.html'
    AUTHOR_SAVE_AS = SITE_DIR + AUTHORS_DIRNAME + '/{slug}/index.html'
else:
    # do not create a subdirectory for each web pages
    ARTICLES_URL_PATH = SITE_URL_TOP_LVL + ARTICLES_DIRNAME
    PAGES_URL_PATH = SITE_URL_TOP_LVL + PAGES_DIRNAME
    DRAFT_ARTICLES_URL_PATH = SITE_URL_TOP_LVL + DRAFT_ARTICLES_DIRNAME
    DRAFT_PAGES_URL_PATH = SITE_URL_TOP_LVL + DRAFT_PAGES_DIRNAME
    TAGS_URL_PATH = SITE_URL_TOP_LVL + TAGS_DIRNAME
    CATEGORIES_URL_PATH = SITE_URL_TOP_LVL + CATEGORIES_DIRNAME
    AUTHORS_URL_PATH = SITE_URL_TOP_LVL + AUTHORS_DIRNAME
    ARCHIVES_URL_PATH = SITE_URL_TOP_LVL + ARCHIVES_DIRNAME

    ARTICLES_URL = ARTICLES_URL_PATH + '/index.html'
    PAGES_URL = PAGES_URL_PATH + '/index.html'
    DRAFTS_URL = DRAFT_ARTICLES_URL_PATH + '/index.html'
    DRAFT_PAGES_URL = DRAFT_PAGES_URL_PATH + '/index.html'
    TAGS_URL = TAGS_URL_PATH + '/index.html'
    CATEGORIES_URL = CATEGORIES_URL_PATH + '/index.html'
    AUTHORS_URL = AUTHORS_URL_PATH + '/index.html'
    ARCHIVES_URL = ARCHIVES_URL_PATH + '/index.html'

    ARTICLE_URL = ARTICLES_URL_PATH + '/{slug}.html'
    PAGE_URL = PAGES_URL_PATH + '/{slug}.html'
    DRAFT_URL = DRAFT_ARTICLES_URL_PATH + '/{slug}.html'
    DRAFT_PAGE_URL = DRAFT_PAGES_URL_PATH + '/{slug}.html'
    TAG_URL = TAGS_URL_PATH + '/{slug}.html'
    CATEGORY_URL = CATEGORIES_URL_PATH + '/{slug}.html'
    AUTHOR_URL = AUTHORS_URL_PATH + '/{slug}.html'
    ARCHIVE_URL = ARCHIVES_URL_PATH + '/{slug}.html'

    ARTICLE_SAVE_AS = SITE_DIR + ARTICLES_DIRNAME + '/{slug}.html'
    PAGE_SAVE_AS = SITE_DIR + PAGES_DIRNAME + '/{slug}.html'
    DRAFT_SAVE_AS = SITE_DIR + DRAFT_ARTICLES_DIRNAME + '/{slug}.html'
    DRAFT_PAGE_SAVE_AS = SITE_DIR + DRAFT_PAGES_DIRNAME + '/{slug}.html'
    TAG_SAVE_AS = SITE_DIR + TAGS_DIRNAME + '/{slug}.html'
    CATEGORY_SAVE_AS = SITE_DIR + CATEGORIES_DIRNAME + '/{slug}.html'
    AUTHOR_SAVE_AS = SITE_DIR + AUTHORS_DIRNAME + '/{slug}.html'
    ARCHIVE_SAVE_AS = SITE_DIR + ARCHIVES_DIRNAME + '/{slug}.html'

    #  INDEX_SAVE_AS = SITE_DIR + ARTICLES_DIRNAME + '/index.html' # ARTICLES_SAVE_AS
    INDEX_SAVE_AS = SITE_DIR + ARTICLES_DIRNAME + '/index.html'    # ARTICLES_SAVE_AS
    PAGES_SAVE_AS = SITE_DIR + PAGES_DIRNAME + '/index.html'
    DRAFTS_SAVE_AS = SITE_DIR + DRAFTS_DIRNAME + '/index.html'
    DRAFT_PAGES_SAVE_AS = SITE_DIR + DRAFT_PAGES_DIRNAME + '/index.html'
    TAGS_SAVE_AS = SITE_DIR + TAGS_DIRNAME + '/index.html'
    CATEGORIES_SAVE_AS = SITE_DIR + CATEGORIES_DIRNAME + '/index.html'
    AUTHORS_SAVE_AS = SITE_DIR + AUTHORS_DIRNAME + '/index.html'
    ARCHIVES_SAVE_AS = SITE_DIR + ARCHIVES_DIRNAME + '/index.html'

if len(AUTHOR) == 0:
    AUTHOR_URL = ''
    AUTHORS_URL = ''
    AUTHOR_SAVE_AS = ''
    AUTHORS_SAVE_AS = ''

# Useful if you are making your own home page

##--------------------------------
## Slug
##--------------------------------

## Specifies where you want the slug to be automatically generated
## from. Can be set to title to use the ‘Title:’ metadata tag or
## basename to use the article’s file name when creating the slug.
# SLUGIFY_SOURCE = ['title'] | 'basename'

# SLUG_REGEX_SUBSTITUTIONS = ''


#############################################################################
## Processor
#############################################################################

DEFAULT_PAGINATION = 10


##--------------------------------
## Templates
##--------------------------------
THEME_STATIC_DIR = SITE_DIR + 'theme'

##--------------------------------
## Pages generator
##--------------------------------

## A list of directories to exclude when looking for pages
## in addition to ARTICLE_PATHS.
PAGE_EXCLUDES = []

PAGE_ORDER_BY = 'date'
# PAGE_EXCLUDES = [ 'working_papers', 'reviews', ARTICLES_DIRNAME, 'software' ]

##--------------------------------
## Drafts (for pages)
## This only gets populated if any of the page content file has
## the metatag 'status: draft' included near beginning of its page file.
##--------------------------------

# There is no index page for draft pages.

##--------------------------------
## Articles (Blogs) generator
##--------------------------------
## A list of directories to exclude when looking for articles in
## addition to PAGE_PATHS.
# ARTICLE_EXCLUDES = []
ARTICLE_ORDER_BY = 'reversed-date'

## limit summary to 50 characters
## When creating a short summary of an article, this will be the
## default length (measured in words) of the text created. This only
## applies if your content does not otherwise specify a summary.
## Setting to None will cause the summary to be a copy of the original content.
SUMMARY_MAX_LENGTH = 50

##-------------------------------------
## Feed generation
##-------------------------------------
FEED_ALL_ATOM = None if developing_site else 'atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# RSS_FEED_SUMMARY_ONLY = False
# FEED_MAX_ITEMS = 30   # default is ALL


# ------------
# Site items
# ------------
MENUITEMS = [
             ('Articles', ARTICLES_URL),
             ('tags', TAGS_URL),
            ]


#-----------------
# Static Files Copying
#-----------------

## Static files are files other than articles and pages that are
## copied to the output folder as-is, without processing. You
## can control which static files are copied over with the
## STATIC_PATHS setting of the project’s pelicanconf.py
## file. Pelican’s default configuration includes the images
## directory for this, but others must be added manually. In
## addition, static files that are explicitly linked to are
## included.
##
## A list of directories (relative to PATH) in which to look
## for static files.  Such files will be copied to the output
## directory without modification. Articles, pages, and other
## content source files will normally be skipped, so it is
## safe for a directory to appear both here and in PAGE_PATHS
## or ARTICLE_PATHS.
## Pelican’s default settings include the “images” directory here.
STATIC_PATHS = [
    'images',
    'extra',  # this
]
# Take care not for EXTRA_PATH_METADATA to use absolute path in 'path' value
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/keybase.txt': {'path': 'keybase.txt'},
}


# handle WITH_FUTURE_DATES (designate article to draft based on date)
WITH_FUTURE_DATES = False



############################################################################
# Filters
############################################################################

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.smarty': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.footnotes': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'baselevel': 1},
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
        'markdown.extensions.headerid': {'level': 2}
    },
    'output_format': 'html5',
}


# ---------------
# Jinja filters
# ---------------
import jinja2
import markdown
from bs4 import BeautifulSoup

# Remove <p>s surrounding Markdown output
def md_single_line(text):
    p = '<p>'
    np = '</p>'
    md = markdown.markdown(text)
    if md.startswith(p) and md.endswith(np):
        md = md[len(p):-len(np)]
    return jinja2.Markup(md)

def md(text):
    return jinja2.Markup(markdown.markdown(text))

def pure_table(html):
    soup = BeautifulSoup(html, 'html.parser')

    for table_tag in soup.find_all('table'):
        table_tag['class'] = table_tag.get('class', []) + ['pure-table']

    return jinja2.Markup(soup)

def fmt_date(value, fmt):
    return value.strftime(fmt)

def current_year(value):
    import time
    return(time.strftime("%Y"))

def jsonify(text):
    import json
    return json.dumps(text, ensure_ascii=False)

def titlify(text):
    soup_title = BeautifulSoup(text.replace('&nbsp;', ' '), 'html.parser')
    page_title = soup_title.get_text(' ', strip=True)
    return(page_title)

JINJA_FILTERS = {'md_single_line': md_single_line,
                 'md': md,
                 'pure_table': pure_table,
                 'fmt_date': fmt_date,
                 'current_year': current_year,
                 'jsonify': jsonify,
                 'titlify': titlify}

# Code Syntax Highlighter
PYGMENTS_STYLE = 'monokai'
PYGMENTS_STYLE = 'paraiso-dark'
# dict_keys(['lovelace', 'borland', 'paraiso-light', 'xcode', 'default',
# 'algol_nu', 'bw', 'vs', 'paraiso-dark', 'igor', 'vim', 'perldoc',
# 'rainbow_dash', 'pastie', 'arduino', 'rrt', 'tango', 'fruity', 'algol',
# 'manni', 'colorful', 'native', 'autumn', 'murphy', 'friendly', 'emacs',
# 'monokai', 'abap', 'trac'])
# code blocks with line numbers
# pygments options:
# https://pygments-doc.readthedocs.io/en/latest/formatters/html.html
# PYGMENTS_RST_OPTIONS = {'nowrap': False}
# PYGMENTS_RST_OPTIONS = {'linenos': False}  # no line numbers
# PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}  # copy-n-paste-friendly
# MD_EXTENSIONS = ['codehilite(css_class=highlight)']

# ----------------------------
# Other filters and snippets
# ----------------------------
# Make PHP snippets highlight without <?php
import pygments.lexers.web as pygweb
class MyPhpLexer(pygweb.PhpLexer):
    def __init__(self, **options):
        options['_startinline'] = True
        super().__init__(**options)
pygweb.PhpLexer = MyPhpLexer


############################################################################
## Plug-Ins
############################################################################
## ---------
## External Plugins
## ---------

## A list of directories where to look for plugins.
PLUGIN_PATHS = ['plugins']

## The list of plugins to load.
PLUGINS = ['collate_content', 'sitemap', 'dateish', 'just_table', 'code_include', 'tag_cloud']
if PDF_PROCESSOR:
    PLUGINS += [ 'pdf ' ]

#  dateish plugin
#  - what to look for inside markdown files in addition to "date:" for dates.
# DATEISH_PROPERTIES = ['created_date', 'idea_date']


# plugin: collate_content
#
# To limit which categories and subcategories are collated, set the
# `CATEGORIES_TO_COLLATE` option in your Pelican configuration file.
#
# If this option is present and is a list, only categories present
# in `CATEGORIES_TO_COLLATE` will be collated:
#
# CATEGORIES_TO_COLLATE = ['category-of-interest', 'another-cool-category']

# plugin: just_table
#
#  Insert [jtable] and use CSV approach to table creation in markdown
#
#     [jtable]
#     Year,Make,Model,Length
#     1994,Ford,E350,2.34
#     2000,Mercury,Cougar,2.38
#     [/jtable]

# plugin: sitemap
#
# Sitemap settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly',
        'pages': 'weekly'
    }
}

# plugin: tag_cloud
#
#
# TAG_CLOUD_STEPS is the range of bubble sizes to offer (1=fixed-bubble-size)
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 100
# TAG_CLOUD_SORTING = 'size'
#                    | 'size-rev'
#                    | 'alphabetically'
#                    | 'random'
#                    | 'alphabetically-rev'
TAG_CLOUD_SORTING = 'size'
TAG_CLOUD_BADGE = True

pp = pprint.PrettyPrinter(indent=4)
pp.pprint( globals())

# plugin: pdf
#
PDF_STYLE = ''
PDF_STYLE_PATH = ''

