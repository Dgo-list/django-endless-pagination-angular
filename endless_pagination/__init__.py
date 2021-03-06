"""Django pagination tools supporting Ajax, multiple and lazy pagination,
Twitter-style and Digg-style pagination.
"""

from __future__ import unicode_literals


VERSION = (1, 2)


def get_version():
    """Return the Django Endless Pagination Angular version as a string."""
    return '.'.join(map(str, VERSION))
