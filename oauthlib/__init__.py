"""
    oauthlib
    ~~~~~~~~

    A generic, spec-compliant, thorough implementation of the OAuth
    request-signing logic.

    :copyright: (c) 2018 by The OAuthlib Community
    :license: BSD, see LICENSE for details.
"""
import logging
from logging import NullHandler

__author__ = 'The OAuthlib Community'
__version__ = '3.0.0-dev'

logging.getLogger('oauthlib').addHandler(NullHandler())
