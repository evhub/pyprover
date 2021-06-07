#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xe1c55f55

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

sys = _coconut_sys

# Utilities:

def first_encodeable(symbols):
    for sym in symbols:
        try:
            if hasattr(sys.stdout, "encoding") and sys.stdout.encoding is not None:
                sym.encode(sys.stdout.encoding)
            else:
                sym.encode()
        except UnicodeEncodeError:
            pass
        else:
            return sym
    raise ValueError("No encodable symbol in " + repr(symbols))

# Installation:

version = "0.5.4"
requirements = ["pyparsing",]
classifiers = ["Development Status :: 3 - Alpha", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries :: Python Modules", "Operating System :: OS Independent",]

# Symbols:

all_top_syms = "top", "\u22a4", "\u252c", "true"
top_sym = (first_encodeable)(all_top_syms)

all_bot_syms = "bot", "\u22a5", "\u2534", "_|_", "false"
bot_sym = (first_encodeable)(all_bot_syms)

all_not_syms = "~", "\xac", "-", "not"
not_sym = (first_encodeable)(all_not_syms)

all_imp_syms = "->", "\u2192"
imp_sym = (first_encodeable)(all_imp_syms)

all_and_syms = "&", "\u2227", "/\\", "and"
and_sym = (first_encodeable)(all_and_syms)

all_or_syms = "|", "\u2228", "\\/", "or"
or_sym = (first_encodeable)(all_or_syms)

all_forall_syms = "FA", "fa", "forall", "A", "\u2200"
forall_sym = (first_encodeable)(all_forall_syms)

all_exists_syms = "TE", "te", "exists", "E", "\u2203"
exists_sym = (first_encodeable)(all_exists_syms)

empty_var = "_"
