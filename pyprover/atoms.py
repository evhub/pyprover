#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x8ed6d92a

# Compiled with Coconut version 3.0.3-post_dev33

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.0.3-post_dev33', '', False)
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and str('__coconut_cache__') in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != str('__coconut_cache__'):
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

# Imports:

from contextlib import contextmanager  #3 (line in Coconut source)

from pyprover.tools import props  #5 (line in Coconut source)
from pyprover.tools import terms  #5 (line in Coconut source)


# Base Class:

class Vars(_coconut.object):  #13 (line in Coconut source)
    @classmethod  #14 (line in Coconut source)
    def items(cls):  #15 (line in Coconut source)
        for name in dir(cls):  #16 (line in Coconut source)
            if not name.startswith("_"):  #17 (line in Coconut source)
                var = getattr(cls, name)  #18 (line in Coconut source)
                yield name, var  #19 (line in Coconut source)


    @classmethod  #21 (line in Coconut source)
    def add_to(cls, globs):  #22 (line in Coconut source)
        """Put variables into the global namespace."""  #23 (line in Coconut source)
        for name, var in cls.items():  #24 (line in Coconut source)
            globs[name] = var  #25 (line in Coconut source)


    use = add_to  #27 (line in Coconut source)

    @classmethod  #29 (line in Coconut source)
    @contextmanager  #30 (line in Coconut source)
    def use_in(cls, globs):  #31 (line in Coconut source)
        """Temporarilty put variables into the global namespace."""  #32 (line in Coconut source)
        prevars = _coconut.dict()  #33 (line in Coconut source)
        for name, var in cls.items():  #34 (line in Coconut source)
            if name in globs:  #35 (line in Coconut source)
                prevars[name] = globs[name]  #36 (line in Coconut source)
            globs[name] = var  #37 (line in Coconut source)
        try:  #38 (line in Coconut source)
            yield  #39 (line in Coconut source)
        finally:  #40 (line in Coconut source)
            for name, var in cls.items():  #41 (line in Coconut source)
                if name in prevars:  #42 (line in Coconut source)
                    globs[name] = prevars[name]  #43 (line in Coconut source)
                else:  #44 (line in Coconut source)
                    del globs[name]  #45 (line in Coconut source)


    using = use_in  #47 (line in Coconut source)

    @_coconut_tco  #49 (line in Coconut source)
    def __hash__(self):  #49 (line in Coconut source)
# type: (...) -> int
        return _coconut_tail_call((hash), str(self))  #50 (line in Coconut source)


    def __lt__(self, other):  #52 (line in Coconut source)
# type: (...) -> int
        return str(self) < str(other)  #53 (line in Coconut source)


    def __gt__(self, other):  #55 (line in Coconut source)
# type: (...) -> int
        return str(self) > str(other)  #56 (line in Coconut source)


    def __ge__(self, other):  #58 (line in Coconut source)
# type: (...) -> int
        return str(self) >= str(other)  #59 (line in Coconut source)


    def __le__(self, other):  #61 (line in Coconut source)
# type: (...) -> int
        return str(self) <= str(other)  #62 (line in Coconut source)


# Derived Classes:


_coconut_call_set_names(Vars)  #67 (line in Coconut source)
class LowercasePropositions(Vars):  #67 (line in Coconut source)
    a, b, c = props("a b c")  #68 (line in Coconut source)
    d, e, f = props("d e f")  #69 (line in Coconut source)
    g, h, i = props("g h i")  #70 (line in Coconut source)
    j, k, l = props("j k l")  #71 (line in Coconut source)
    m, n, o = props("m n o")  #72 (line in Coconut source)
    p, q, r = props("p q r")  #73 (line in Coconut source)
    s, t, u = props("s t u")  #74 (line in Coconut source)
    v, w, x = props("v w x")  #75 (line in Coconut source)
    y, z = props("y z")  #76 (line in Coconut source)

_coconut_call_set_names(LowercasePropositions)  #78 (line in Coconut source)
class UppercasePropositions(Vars):  #78 (line in Coconut source)
    A, B, C = props("A B C")  #79 (line in Coconut source)
    D, E, F = props("D E F")  #80 (line in Coconut source)
    G, H, I = props("G H I")  #81 (line in Coconut source)
    J, K, L = props("J K L")  #82 (line in Coconut source)
    M, N, O = props("M N O")  #83 (line in Coconut source)
    P, Q, R = props("P Q R")  #84 (line in Coconut source)
    S, T, U = props("S T U")  #85 (line in Coconut source)
    V, W, X = props("V W X")  #86 (line in Coconut source)
    Y, Z = props("Y Z")  #87 (line in Coconut source)

_coconut_call_set_names(UppercasePropositions)  #89 (line in Coconut source)
class LowercaseVariables(Vars):  #89 (line in Coconut source)
    a, b, c = terms("a b c")  #90 (line in Coconut source)
    d, e, f = terms("d e f")  #91 (line in Coconut source)
    g, h, i = terms("g h i")  #92 (line in Coconut source)
    j, k, l = terms("j k l")  #93 (line in Coconut source)
    m, n, o = terms("m n o")  #94 (line in Coconut source)
    p, q, r = terms("p q r")  #95 (line in Coconut source)
    s, t, u = terms("s t u")  #96 (line in Coconut source)
    v, w, x = terms("v w x")  #97 (line in Coconut source)
    y, z = terms("y z")  #98 (line in Coconut source)

_coconut_call_set_names(LowercaseVariables)  #100 (line in Coconut source)
class UppercaseVariables(Vars):  #100 (line in Coconut source)
    A, B, C = terms("A B C")  #101 (line in Coconut source)
    D, E, F = terms("D E F")  #102 (line in Coconut source)
    G, H, I = terms("G H I")  #103 (line in Coconut source)
    J, K, L = terms("J K L")  #104 (line in Coconut source)
    M, N, O = terms("M N O")  #105 (line in Coconut source)
    P, Q, R = terms("P Q R")  #106 (line in Coconut source)
    S, T, U = terms("S T U")  #107 (line in Coconut source)
    V, W, X = terms("V W X")  #108 (line in Coconut source)
    Y, Z = terms("Y Z")  #109 (line in Coconut source)

_coconut_call_set_names(UppercaseVariables)  #111 (line in Coconut source)
class StandardMath(LowercaseVariables, UppercasePropositions): pass  #111 (line in Coconut source)

_coconut_call_set_names(StandardMath)  #113 (line in Coconut source)
