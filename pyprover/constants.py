#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x7cd31c44

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

sys = _coconut_sys  #3 (line num in coconut source)

# Utilities:

def first_encodeable(symbols):  #7 (line num in coconut source)
    for sym in symbols:  #8 (line num in coconut source)
        try:  #9 (line num in coconut source)
            if hasattr(sys.stdout, "encoding") and sys.stdout.encoding is not None:  #10 (line num in coconut source)
                sym.encode(sys.stdout.encoding)  #11 (line num in coconut source)
            else:  #12 (line num in coconut source)
                sym.encode()  #13 (line num in coconut source)
        except UnicodeEncodeError:  #14 (line num in coconut source)
            pass  #15 (line num in coconut source)
        else:  #16 (line num in coconut source)
            return sym  #17 (line num in coconut source)
    raise ValueError("No encodable symbol in " + repr(symbols))  #18 (line num in coconut source)

# Installation:


version = "0.6.0"  #22 (line num in coconut source)
requirements = ["pyparsing",]  #23 (line num in coconut source)
classifiers = ["Development Status :: 3 - Alpha", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries :: Python Modules", "Operating System :: OS Independent"]  #26 (line num in coconut source)

# Symbols:

all_top_syms = "top", "\u22a4", "\u252c", "true"  #35 (line num in coconut source)
top_sym = (first_encodeable)(all_top_syms)  #36 (line num in coconut source)

all_bot_syms = "bot", "\u22a5", "\u2534", "_|_", "false"  #38 (line num in coconut source)
bot_sym = (first_encodeable)(all_bot_syms)  #39 (line num in coconut source)

all_not_syms = "~", "\xac", "-", "not"  #41 (line num in coconut source)
not_sym = (first_encodeable)(all_not_syms)  #42 (line num in coconut source)

all_imp_syms = "->", "\u2192", ">>"  #44 (line num in coconut source)
imp_sym = (first_encodeable)(all_imp_syms)  #45 (line num in coconut source)

all_and_syms = "&", "\u2227", "/\\", "and"  #47 (line num in coconut source)
and_sym = (first_encodeable)(all_and_syms)  #48 (line num in coconut source)

all_or_syms = "|", "\u2228", "\\/", "or"  #50 (line num in coconut source)
or_sym = (first_encodeable)(all_or_syms)  #51 (line num in coconut source)

all_forall_syms = "FA", "\u2200", "fa", "forall", "A", "Fa"  #53 (line num in coconut source)
forall_sym = (first_encodeable)(all_forall_syms)  #54 (line num in coconut source)

all_exists_syms = "EX", "\u2203", "ex", "exists", "E", "Ex", "TE", "te", "Te"  #56 (line num in coconut source)
exists_sym = (first_encodeable)(all_exists_syms)  #57 (line num in coconut source)

empty_var = "_"  #59 (line num in coconut source)
