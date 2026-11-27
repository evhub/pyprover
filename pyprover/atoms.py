#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x52316721

# Compiled with Coconut version 3.2.0-post_dev19
# This file was compiled from atoms.coco by the Coconut compiler; edit that file rather than this one.
# For a guide to writing Coconut, see http://coconut.readthedocs.io/en/develop/llms.txt (or run 'coconut --ai-docs').

"""Namespaces of single-letter propositions and terms."""

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop, annotations
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev19', '39', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get('__coconut__')
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules['_coconut_cached__coconut__'] = _coconut_cached__coconut__
        del _coconut_sys.modules['__coconut__']
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and _coconut_os.path.exists(_coconut_os.path.join(_coconut_file_dir, "__init__.py")):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == '__coconut__':  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == '__coconut__':  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning, _coconut_lazy_module, _coconut_lazy_get, _coconut_type, _coconut_assert_msg
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and '__coconut_cache__' in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != '__coconut_cache__':
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------



# Imports:

from contextlib import contextmanager  #5 (line in Coconut source)

from pyprover.tools import props  #7 (line in Coconut source)
from pyprover.tools import terms  #7 (line in Coconut source)


# Base class:

class Vars():  #15 (line in Coconut source)
    """A namespace of propositions or terms that can be put into globals()."""  #16 (line in Coconut source)

    @classmethod  #18 (line in Coconut source)
    def items(cls):  #19 (line in Coconut source)
        for name in dir(cls):  #20 (line in Coconut source)
            if not name.startswith("_") and name not in ("items", "add_to", "use", "use_in", "using"):  #21 (line in Coconut source)
                yield name, getattr(cls, name)  #22 (line in Coconut source)


    @classmethod  #24 (line in Coconut source)
    def add_to(cls, globs):  #25 (line in Coconut source)
        """Put the variables into the given namespace (e.g. globals())."""  #26 (line in Coconut source)
        for name, var in cls.items():  #27 (line in Coconut source)
            globs[name] = var  #28 (line in Coconut source)


    use = add_to  #30 (line in Coconut source)

    @classmethod  #32 (line in Coconut source)
    @contextmanager  #33 (line in Coconut source)
    def use_in(cls, globs):  #34 (line in Coconut source)
        """Temporarily put the variables into the given namespace (e.g. globals())."""  #35 (line in Coconut source)
        prevars = {}  #36 (line in Coconut source)
        for name, var in cls.items():  #37 (line in Coconut source)
            if name in globs:  #38 (line in Coconut source)
                prevars[name] = globs[name]  #39 (line in Coconut source)
            globs[name] = var  #40 (line in Coconut source)
        try:  #41 (line in Coconut source)
            yield  #42 (line in Coconut source)
        finally:  #43 (line in Coconut source)
            for name, _ in cls.items():  #44 (line in Coconut source)
                if name in prevars:  #45 (line in Coconut source)
                    globs[name] = prevars[name]  #46 (line in Coconut source)
                else:  #47 (line in Coconut source)
                    del globs[name]  #48 (line in Coconut source)


    using = use_in  #50 (line in Coconut source)


lowercase = "a b c d e f g h i j k l m n o p q r s t u v w x y z"  #53 (line in Coconut source)
uppercase = lowercase.upper()  #54 (line in Coconut source)


# Derived classes:

class LowercasePropositions(Vars):  #59 (line in Coconut source)
    """Propositions named a through z."""  #60 (line in Coconut source)
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = props(lowercase)  #61 (line in Coconut source)

class UppercasePropositions(Vars):  #63 (line in Coconut source)
    """Propositions named A through Z."""  #64 (line in Coconut source)
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = props(uppercase)  #65 (line in Coconut source)

class LowercaseVariables(Vars):  #67 (line in Coconut source)
    """Constants (which can be quantified over or called as functions) named a through z."""  #68 (line in Coconut source)
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = terms(lowercase)  #69 (line in Coconut source)

class UppercaseVariables(Vars):  #71 (line in Coconut source)
    """Constants (which can be quantified over or called as functions) named A through Z."""  #72 (line in Coconut source)
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = terms(uppercase)  #73 (line in Coconut source)

class StandardMath(LowercaseVariables, UppercasePropositions):  #75 (line in Coconut source)
    """Uppercase propositions/predicates and lowercase constants/variables/functions."""  #76 (line in Coconut source)
