from __future__  import absolute_import

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-customshortuuidfield').version
except Exception:
    VERSION = 'unknown'

from .fields import CustomShortUUIDField
