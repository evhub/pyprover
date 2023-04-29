#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xdd4c8bf7

# Compiled with Coconut version 3.0.0-a_dev36

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
_coconut_header_info = ('3.0.0-a_dev36', '', False)
import os as _coconut_os
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
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in
if _coconut_pop_path:
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Imports:

sys = _coconut_sys  #3 (line in Coconut source)

# Utilities:

def first_encodeable(symbols):  #7 (line in Coconut source)
    for sym in symbols:  #8 (line in Coconut source)
        try:  #9 (line in Coconut source)
            if hasattr(sys.stdout, "encoding") and sys.stdout.encoding is not None:  #10 (line in Coconut source)
                sym.encode(sys.stdout.encoding)  #11 (line in Coconut source)
            else:  #12 (line in Coconut source)
                sym.encode()  #13 (line in Coconut source)
        except UnicodeEncodeError:  #14 (line in Coconut source)
            pass  #15 (line in Coconut source)
        else:  #16 (line in Coconut source)
            return sym  #17 (line in Coconut source)
    raise ValueError("No encodable symbol in " + repr(symbols))  #18 (line in Coconut source)

# Installation:


version = "0.6.2"  #22 (line in Coconut source)
requirements = ["pyparsing",]  #23 (line in Coconut source)
classifiers = ["Development Status :: 3 - Alpha", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries :: Python Modules", "Operating System :: OS Independent"]  #26 (line in Coconut source)

# Symbols:

all_top_syms = "top", "\u22a4", "\u252c", "true"  #35 (line in Coconut source)
top_sym = (first_encodeable)(all_top_syms)  #36 (line in Coconut source)

all_bot_syms = "bot", "\u22a5", "\u2534", "_|_", "false"  #38 (line in Coconut source)
bot_sym = (first_encodeable)(all_bot_syms)  #39 (line in Coconut source)

all_not_syms = "~", "\xac", "-", "not"  #41 (line in Coconut source)
not_sym = (first_encodeable)(all_not_syms)  #42 (line in Coconut source)

all_imp_syms = "->", "\u2192", ">>"  #44 (line in Coconut source)
imp_sym = (first_encodeable)(all_imp_syms)  #45 (line in Coconut source)

all_and_syms = "&", "\u2227", "/\\", "and"  #47 (line in Coconut source)
and_sym = (first_encodeable)(all_and_syms)  #48 (line in Coconut source)

all_or_syms = "|", "\u2228", "\\/", "or"  #50 (line in Coconut source)
or_sym = (first_encodeable)(all_or_syms)  #51 (line in Coconut source)

all_forall_syms = "FA", "\u2200", "fa", "forall", "A", "Fa"  #53 (line in Coconut source)
forall_sym = (first_encodeable)(all_forall_syms)  #54 (line in Coconut source)

all_exists_syms = "EX", "\u2203", "ex", "exists", "E", "Ex", "TE", "te", "Te"  #56 (line in Coconut source)
exists_sym = (first_encodeable)(all_exists_syms)  #57 (line in Coconut source)

empty_var = "_"  #59 (line in Coconut source)
