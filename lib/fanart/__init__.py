__author__ = 'Andrea De Marco <24erre@gmail.com>'
__version__ = '1.4.0'
__classifiers__ = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries',
]
__copyright__ = "2012, %s " % __author__
__license__ = """
   Copyright %s.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
""" % __copyright__

__docformat__ = 'restructuredtext en'

__doc__ = """
:abstract: Python interface to fanart.tv API
:version: %s
:author: %s
:contact: http://z4r.github.com/
:date: 2012-04-04
:copyright: %s
""" % (__version__, __author__, __license__)

from six import iteritems

def values(obj):
    return [v for k, v in iteritems(obj.__dict__) if not k.startswith('_')]


BASEURL = 'http://webservice.fanart.tv/v3/%s/%s?api_key=%s'


class FORMAT(object):
    JSON = 'JSON'
    XML = 'XML'
    PHP = 'PHP'


class WS(object):
    MUSIC = 'music'
    MOVIE = 'movies'
    TV = 'tv'


class TYPE(object):
    ALL = 'all'

    class TV(object):
        ART = 'clearart'
        LOGO = 'clearlogo'
        CHARACTER = 'characterart'
        THUMB = 'tvthumb'
        SEASONTHUMB = 'seasonthumb'
        SEASONPOSTER = 'seasonposter'
        BACKGROUND = 'showbackground'
        HDLOGO = 'hdtvlogo'
        HDART = 'hdclearart'
        POSTER = 'tvposter'
        BANNER = 'tvbanner'

    class MUSIC(object):
        DISC = 'cdart'
        LOGO = 'musiclogo'
        BACKGROUND = 'artistbackground'
        COVER = 'albumcover'
        THUMB = 'artistthumb'

    class MOVIE(object):
        ART = 'movieart'
        LOGO = 'movielogo'
        DISC = 'moviedisc'
        POSTER = 'movieposter'
        BACKGROUND = 'moviebackground'
        HDLOGO = 'hdmovielogo'
        HDART = 'hdmovieclearart'
        BANNER = 'moviebanner'
        THUMB = 'moviethumb'


FORMAT_LIST = values(FORMAT)
WS_LIST = values(WS)
TYPE_LIST = values(TYPE.MUSIC) + values(TYPE.TV) + values(TYPE.MOVIE) + [TYPE.ALL]
MUSIC_TYPE_LIST = values(TYPE.MUSIC) + [TYPE.ALL]
TV_TYPE_LIST = values(TYPE.TV) + [TYPE.ALL]
MOVIE_TYPE_LIST = values(TYPE.MOVIE) + [TYPE.ALL]
