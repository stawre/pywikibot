# -*- coding: utf-8  -*-
"""Family module for Wikia."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 7f58539534b92fe56adf09a62f628e85be700a5f $'

from pywikibot import family
from pywikibot.tools import deprecated


# The Wikia Search family
# user-config.py: usernames['wikia']['wikia'] = 'User name'
class Family(family.SingleSiteFamily):

    """Family class for Wikia."""

    name = u'wikia'
    domain = 'www.wikia.com'

    @deprecated('APISite.version()')
    def version(self, code):
        """Return the version for this family."""
        return "1.19.20"

    def scriptpath(self, code):
        """Return the script path for this family."""
        return ''

    def apipath(self, code):
        """Return the path to api.php for this family."""
        return '/api.php'
