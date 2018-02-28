# -*- coding: utf-8 -*-

"""
Utilities for processing a set of redirect specifications from a text file.

Redirects can be specified in a simple text-based format, in which each line
consists of three whitespace-delimited fields:

    <source path> <redirect type> <destination>

The redirect type can be one of the following:

    exact           - requests with paths that exactly match the specified
                      source path will be redirected to the destination URL.
    prefix          - requests with paths that start with the specified source
                      path will be redirected to URLs relative to the
                      destination URL.
    internal-exact  - same as `exact`, but the destination will be treated as
                      a route name rather than a URL.
    internal-prefix - same as `prefix`, but the destination will be treated as
                      a route name rather than a URL.

Lines that contain only whitespace, or which start with a '#' character, will
be ignored.
"""

from collections import namedtuple

branches = [False] * 10

class Redirect(namedtuple('Redirect', [
    'src',       # matching prefix (if prefix redirect) or path (if exact)
    'dst',       # route name (if internal redirect) or URL (if external)
    'prefix',    # prefix redirect if true, exact otherwise
    'internal',  # internal redirect if true, external otherwise
])):
    pass


class ParseError(Exception):
    pass


def lookup(redirects, request):
    """
    Check if a request matches any of a list of redirects.

    Returns None if the request does not match, and the URL to redirect to
    otherwise.
    """
    for r in redirects:
        if r.prefix and request.path.startswith(r.src):
            suffix = request.path.replace(r.src, '', 1)
            return _dst_root(request, r) + suffix
        elif not r.prefix and request.path == r.src:
            return _dst_root(request, r)
    return None


def parse(specs):
    """Parse a list of redirects from a sequence of redirect specifiers."""
    branches[0] = True
    result = []
    for line in specs:
        # Ignore comments and blank lines
        if line.startswith('#') or not line.strip():
            branches[1] = True
            continue

        try:
            branches[2] = True
            src, typ, dst = line.split(None, 3)
        except ValueError:
            branches[3] = True
            raise ParseError('invalid redirect specification: {!r}'.format(line))
        if typ == 'internal-exact':
            branches[4] = True
            r = Redirect(prefix=False, internal=True, src=src, dst=dst)
        elif typ == 'internal-prefix':
            branches[5] = True
            r = Redirect(prefix=True, internal=True, src=src, dst=dst)
        elif typ == 'exact':
            branches[6] = True
            r = Redirect(prefix=False, internal=False, src=src, dst=dst)
        elif typ == 'prefix':
            branches[7] = True
            r = Redirect(prefix=True, internal=False, src=src, dst=dst)
        else:
            branches[8] = True
            raise ParseError('unknown redirect type: {!r}'.format(typ))
        result.append(r)
    branches[9] = True
    return result


def _dst_root(request, redirect):
    if redirect.internal:
        return request.route_url(redirect.dst)
    else:
        return redirect.dst
