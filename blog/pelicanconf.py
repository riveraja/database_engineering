AUTHOR = 'Jericho Rivera'
SITENAME = 'Jericho\'s log'
SITESUBTITLE = 'a database engineer\'s throughts and ramblings...'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = 'en'

GITHUB_URL = 'https://github.com/riveraja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/jerichorivera'),
          ('linkedin', 'https://www.linkedin.com/in/riveraja/'),
          ('github', 'https://github.com/riveraja'),)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
THEME_STATIC_DIR = 'themes'
THEME = 'themes/Peli-Kiera'
USE_FOLDER_AS_CATEGORY = True
TYPOGRIPHY = True
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
