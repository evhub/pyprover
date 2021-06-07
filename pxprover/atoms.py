#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa510900d

# Compiled with Coconut version 1.5.0-post_dev58 [Fish License]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
    _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
    import __coconut__ as _coconut__coconut__
    _coconut__coconut__.__name__ = _coconut_full_module_name
    for _coconut_v in vars(_coconut__coconut__).values():
        if getattr(_coconut_v, "__module__", None) == str("__coconut__"):
            try:
                _coconut_v.__module__ = _coconut_full_module_name
            except AttributeError:
                type(_coconut_v).__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)
# Compiled Coconut: -----------------------------------------------------------

# Imports:

from contextlib import contextmanager

from pxprover.tools import props
from pxprover.tools import terms

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
    @_coconut_tco
    def __hash__(self):
# type: (...) -> int
        return _coconut_tail_call(str(self).__hash__)

    def __lt__(self, other):
# type: (...) -> int
        return str(self) < str(other)

    def __gt__(self, other):
# type: (...) -> int
        return str(self) > str(other)

    def __ge__(self, other):
# type: (...) -> int
        return str(self) >= str(other)

    def __le__(self, other):
# type: (...) -> int
        return str(self) <= str(other)


# Derived Classes:

_coconut_call_set_names(Vars)
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

_coconut_call_set_names(LowercasePropositions)
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

_coconut_call_set_names(UppercasePropositions)
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

_coconut_call_set_names(LowercaseVariables)
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

_coconut_call_set_names(UppercaseVariables)
class StandardMath(Vars): pass
_coconut_call_set_names(StandardMath)
for name, var in _coconut.itertools.chain.from_iterable(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: LowercaseVariables.items(), lambda: UppercasePropositions.items()))):
    setattr(StandardMath, name, var)
