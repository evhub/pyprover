#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x446e4c5b

# Compiled with Coconut version 2.0.0-a_dev45 [How Not to Be Seen]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:  # type: ignore
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
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == str("__coconut__"):
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Imports:

from contextlib import contextmanager  #3 (line num in coconut source)

from pyprover.tools import props  #5 (line num in coconut source)
from pyprover.tools import terms  #5 (line num in coconut source)


# Base Class:

class Vars(_coconut.object):  #13 (line num in coconut source)
    @classmethod  #14 (line num in coconut source)
    def items(cls):  #15 (line num in coconut source)
        for name in dir(cls):  #16 (line num in coconut source)
            if not name.startswith("_"):  #17 (line num in coconut source)
                var = getattr(cls, name)  #18 (line num in coconut source)
                yield name, var  #19 (line num in coconut source)


    @classmethod  #21 (line num in coconut source)
    def add_to(cls, globs):  #22 (line num in coconut source)
        """Put variables into the global namespace."""  #23 (line num in coconut source)
        for name, var in cls.items():  #24 (line num in coconut source)
            globs[name] = var  #25 (line num in coconut source)


    use = add_to  #27 (line num in coconut source)

    @classmethod  #29 (line num in coconut source)
    @contextmanager  #30 (line num in coconut source)
    def use_in(cls, globs):  #31 (line num in coconut source)
        """Temporarilty put variables into the global namespace."""  #32 (line num in coconut source)
        prevars = {}  #33 (line num in coconut source)
        for name, var in cls.items():  #34 (line num in coconut source)
            if name in globs:  #35 (line num in coconut source)
                prevars[name] = globs[name]  #36 (line num in coconut source)
            globs[name] = var  #37 (line num in coconut source)
        try:  #38 (line num in coconut source)
            yield  #39 (line num in coconut source)
        finally:  #40 (line num in coconut source)
            for name, var in cls.items():  #41 (line num in coconut source)
                if name in prevars:  #42 (line num in coconut source)
                    globs[name] = prevars[name]  #43 (line num in coconut source)
                else:  #44 (line num in coconut source)
                    del globs[name]  #45 (line num in coconut source)


    using = use_in  #47 (line num in coconut source)

    @_coconut_tco  #49 (line num in coconut source)
    def __hash__(self):  #49 (line num in coconut source)
#type: (...) -> int
        return _coconut_tail_call((hash), str(self))  #50 (line num in coconut source)


    def __lt__(self, other):  #52 (line num in coconut source)
#type: (...) -> int
        return str(self) < str(other)  #53 (line num in coconut source)


    def __gt__(self, other):  #55 (line num in coconut source)
#type: (...) -> int
        return str(self) > str(other)  #56 (line num in coconut source)


    def __ge__(self, other):  #58 (line num in coconut source)
#type: (...) -> int
        return str(self) >= str(other)  #59 (line num in coconut source)


    def __le__(self, other):  #61 (line num in coconut source)
#type: (...) -> int
        return str(self) <= str(other)  #62 (line num in coconut source)


# Derived Classes:


_coconut_call_set_names(Vars)  #67 (line num in coconut source)
class LowercasePropositions(Vars):  #67 (line num in coconut source)
    a, b, c = props("a b c")  #68 (line num in coconut source)
    d, e, f = props("d e f")  #69 (line num in coconut source)
    g, h, i = props("g h i")  #70 (line num in coconut source)
    j, k, l = props("j k l")  #71 (line num in coconut source)
    m, n, o = props("m n o")  #72 (line num in coconut source)
    p, q, r = props("p q r")  #73 (line num in coconut source)
    s, t, u = props("s t u")  #74 (line num in coconut source)
    v, w, x = props("v w x")  #75 (line num in coconut source)
    y, z = props("y z")  #76 (line num in coconut source)

_coconut_call_set_names(LowercasePropositions)  #78 (line num in coconut source)
class UppercasePropositions(Vars):  #78 (line num in coconut source)
    A, B, C = props("A B C")  #79 (line num in coconut source)
    D, E, F = props("D E F")  #80 (line num in coconut source)
    G, H, I = props("G H I")  #81 (line num in coconut source)
    J, K, L = props("J K L")  #82 (line num in coconut source)
    M, N, O = props("M N O")  #83 (line num in coconut source)
    P, Q, R = props("P Q R")  #84 (line num in coconut source)
    S, T, U = props("S T U")  #85 (line num in coconut source)
    V, W, X = props("V W X")  #86 (line num in coconut source)
    Y, Z = props("Y Z")  #87 (line num in coconut source)

_coconut_call_set_names(UppercasePropositions)  #89 (line num in coconut source)
class LowercaseVariables(Vars):  #89 (line num in coconut source)
    a, b, c = terms("a b c")  #90 (line num in coconut source)
    d, e, f = terms("d e f")  #91 (line num in coconut source)
    g, h, i = terms("g h i")  #92 (line num in coconut source)
    j, k, l = terms("j k l")  #93 (line num in coconut source)
    m, n, o = terms("m n o")  #94 (line num in coconut source)
    p, q, r = terms("p q r")  #95 (line num in coconut source)
    s, t, u = terms("s t u")  #96 (line num in coconut source)
    v, w, x = terms("v w x")  #97 (line num in coconut source)
    y, z = terms("y z")  #98 (line num in coconut source)

_coconut_call_set_names(LowercaseVariables)  #100 (line num in coconut source)
class UppercaseVariables(Vars):  #100 (line num in coconut source)
    A, B, C = terms("A B C")  #101 (line num in coconut source)
    D, E, F = terms("D E F")  #102 (line num in coconut source)
    G, H, I = terms("G H I")  #103 (line num in coconut source)
    J, K, L = terms("J K L")  #104 (line num in coconut source)
    M, N, O = terms("M N O")  #105 (line num in coconut source)
    P, Q, R = terms("P Q R")  #106 (line num in coconut source)
    S, T, U = terms("S T U")  #107 (line num in coconut source)
    V, W, X = terms("V W X")  #108 (line num in coconut source)
    Y, Z = terms("Y Z")  #109 (line num in coconut source)

_coconut_call_set_names(UppercaseVariables)  #111 (line num in coconut source)
class StandardMath(LowercaseVariables, UppercasePropositions): pass  #111 (line num in coconut source)

_coconut_call_set_names(StandardMath)  #113 (line num in coconut source)
