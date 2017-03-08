#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xea37708c

# Compiled with Coconut version 1.2.2-post_dev4 [Colonel]

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

from contextlib import contextmanager  # line 3

from pyprover.tools import props  # line 4
from pyprover.tools import terms  # line 5

# Base Class:

class Vars(_coconut.object):  # line 12
    @classmethod  # line 13
    def items(cls):  # line 14
        for name, var in vars(cls).items():  # line 15
            if not name.startswith("_"):  # line 16
                yield name, var  # line 17
    @classmethod  # line 18
    def use(cls, globs=None):  # line 19
        """Put variables into the global namespace."""  # line 20
        if globs is None:  # line 21
            globs = globals()  # line 22
        for name, var in cls.items():  # line 23
            globs[name] = var  # line 24
    @classmethod  # line 25
    @contextmanager  # line 25
    def using(cls, globs=None):  # line 27
        """Temporarilty put variables into the global namespace."""  # line 28
        if globs is None:  # line 29
            globs = globals()  # line 30
        prevars = {}  # line 31
        for name, var in cls.items():  # line 32
            if name in globs:  # line 33
                prevars[name] = globs[name]  # line 34
            globs[name] = var  # line 35
        try:  # line 36
            yield  # line 37
        finally:  # line 38
            for name, var in cls.items():  # line 39
                if name in prevars:  # line 40
                    globs[name] = prevars[name]  # line 41
                else:  # line 42
                    del globs[name]  # line 43

# Derived Classes:

class LowercasePropositions(Vars):  # line 47
    a, b, c = props("a b c")  # line 48
    d, e, f = props("d e f")  # line 49
    g, h, i = props("g h i")  # line 50
    j, k, l = props("j k l")  # line 51
    m, n, o = props("m n o")  # line 52
    p, q, r = props("p q r")  # line 53
    s, t, u = props("s t u")  # line 54
    v, w, x = props("v w x")  # line 55
    y, z = props("y z")  # line 56

class UppercasePropositions(Vars):  # line 58
    A, B, C = props("A B C")  # line 59
    D, E, F = props("D E F")  # line 60
    G, H, I = props("G H I")  # line 61
    J, K, L = props("J K L")  # line 62
    M, N, O = props("M N O")  # line 63
    P, Q, R = props("P Q R")  # line 64
    S, T, U = props("S T U")  # line 65
    V, W, X = props("V W X")  # line 66
    Y, Z = props("Y Z")  # line 67

class LowercaseVariables(Vars):  # line 69
    a, b, c = terms("a b c")  # line 70
    d, e, f = terms("d e f")  # line 71
    g, h, i = terms("g h i")  # line 72
    j, k, l = terms("j k l")  # line 73
    m, n, o = terms("m n o")  # line 74
    p, q, r = terms("p q r")  # line 75
    s, t, u = terms("s t u")  # line 76
    v, w, x = terms("v w x")  # line 77
    y, z = terms("y z")  # line 78

class UppercaseVariables(Vars):  # line 80
    A, B, C = terms("A B C")  # line 81
    D, E, F = terms("D E F")  # line 82
    G, H, I = terms("G H I")  # line 83
    J, K, L = terms("J K L")  # line 84
    M, N, O = terms("M N O")  # line 85
    P, Q, R = terms("P Q R")  # line 86
    S, T, U = terms("S T U")  # line 87
    V, W, X = terms("V W X")  # line 88
    Y, Z = terms("Y Z")  # line 89

class StandardMath(Vars): pass  # line 91
for name, var in _coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: LowercaseVariables.items(), lambda: UppercasePropositions.items()))):  # line 92
    setattr(StandardMath, name, var)  # line 93
