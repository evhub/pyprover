#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x1393054e

# Compiled with Coconut version 1.4.2-post_dev5 [Ernest Scribbler]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match
if _coconut_sys.version_info >= (3,):
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
