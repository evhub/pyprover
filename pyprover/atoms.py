#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xcea92fde

# Compiled with Coconut version 1.2.2-post_dev5 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_tee, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------

# Imports:

from contextlib import contextmanager

from pyprover.tools import props
from pyprover.tools import terms

# Base Class:

class Vars(_coconut.object):
    @classmethod
    def items(cls):
        for name, var in vars(cls).items():
            if not name.startswith("_"):
                yield name, var
    @classmethod
    def use(cls, globs=None):
        """Put variables into the global namespace."""
        if globs is None:
            globs = globals()
        for name, var in cls.items():
            globs[name] = var
    @classmethod
    @contextmanager
    def using(cls, globs=None):
        """Temporarilty put variables into the global namespace."""
        if globs is None:
            globs = globals()
        prevars = {}
        for name, var in cls.items():
            if name in globs:
                prevars[name] = globs[name]
            globs[name] = var
        try:
            yield
        finally:
            for name, var in cls.items():
                if name in prevars:
                    globs[name] = prevars[name]
                else:
                    del globs[name]

# Derived Classes:

class LowercasePropositions(Vars):
    a, b, c = props("a b c")
    d, e, f = props("d e f")
    g, h, i = props("g h i")
    j, k, l = props("j k l")
    m, n, o = props("m n o")
    p, q, r = props("p q r")
    s, t, u = props("s t u")
    v, w, x = props("v w x")
    y, z = props("y z")

class UppercasePropositions(Vars):
    A, B, C = props("A B C")
    D, E, F = props("D E F")
    G, H, I = props("G H I")
    J, K, L = props("J K L")
    M, N, O = props("M N O")
    P, Q, R = props("P Q R")
    S, T, U = props("S T U")
    V, W, X = props("V W X")
    Y, Z = props("Y Z")

class LowercaseVariables(Vars):
    a, b, c = terms("a b c")
    d, e, f = terms("d e f")
    g, h, i = terms("g h i")
    j, k, l = terms("j k l")
    m, n, o = terms("m n o")
    p, q, r = terms("p q r")
    s, t, u = terms("s t u")
    v, w, x = terms("v w x")
    y, z = terms("y z")

class UppercaseVariables(Vars):
    A, B, C = terms("A B C")
    D, E, F = terms("D E F")
    G, H, I = terms("G H I")
    J, K, L = terms("J K L")
    M, N, O = terms("M N O")
    P, Q, R = terms("P Q R")
    S, T, U = terms("S T U")
    V, W, X = terms("V W X")
    Y, Z = terms("Y Z")

class StandardMath(Vars): pass
for name, var in _coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: LowercaseVariables.items(), lambda: UppercasePropositions.items()))):
    setattr(StandardMath, name, var)
