#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc526628

# Compiled with Coconut version 3.2.0-post_dev20
# This file was compiled from constants.coco by the Coconut compiler; edit that file rather than this one.
# For a guide to writing Coconut, see http://coconut.readthedocs.io/en/develop/llms.txt (or run 'coconut --ai-docs').

"""Constants and printing symbols used throughout PyProver."""

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop, annotations
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev20', '39', True)
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



# Installation:

version = "1.0.0"  #5 (line in Coconut source)


# Parsing symbols (every spelling accepted by the parser):

all_top_syms = "⊤", "top", "true", "┬"  #10 (line in Coconut source)
all_bot_syms = "⊥", "bot", "false", "┴", "_|_"  #11 (line in Coconut source)
all_not_syms = "¬", "~", "-", "!", "not"  #12 (line in Coconut source)
all_imp_syms = "→", "->", ">>", "=>", "implies"  #13 (line in Coconut source)
all_iff_syms = "↔", "<->", "<=>", "iff"  #14 (line in Coconut source)
all_and_syms = "∧", "&", "/\\", "and"  #15 (line in Coconut source)
all_or_syms = "∨", "|", "\\/", "or"  #16 (line in Coconut source)
all_eq_syms = "=",  #17 (line in Coconut source)
all_neq_syms = "≠", "!=", "/="  #18 (line in Coconut source)
all_forall_syms = "∀", "FA", "A", "forall", "fa", "Fa", "ForAll"  #19 (line in Coconut source)
all_exists_syms = "∃", "TE", "EX", "E", "exists", "ex", "Ex", "Te", "te", "Exists"  #20 (line in Coconut source)


# Printing symbols:

unicode_symbols = {"top": "⊤", "bot": "⊥", "not": "¬", "imp": " → ", "iff": " ↔ ", "and": " ∧ ", "or": " ∨ ", "eq": " = ", "neq": " ≠ ", "forall": "∀", "exists": "∃"}  #25 (line in Coconut source)

ascii_symbols = {"top": "top", "bot": "bot", "not": "~", "imp": " -> ", "iff": " <-> ", "and": " & ", "or": " | ", "eq": " = ", "neq": " != ", "forall": "FA ", "exists": "TE "}  #39 (line in Coconut source)

symbols = unicode_symbols.copy()  #53 (line in Coconut source)


def use_unicode() -> None:  #56 (line in Coconut source)
    """Print formulas using unicode logic symbols (the default)."""  #57 (line in Coconut source)
    symbols.update(unicode_symbols)  #58 (line in Coconut source)


def use_ascii() -> None:  #60 (line in Coconut source)
    """Print formulas using only ASCII characters."""  #61 (line in Coconut source)
    symbols.update(ascii_symbols)  #62 (line in Coconut source)


# Prover defaults:

# seconds
default_timeout = 10.0  # seconds  #67 (line in Coconut source)
default_max_clauses = 20000  #68 (line in Coconut source)
max_ground_clauses = 50000  #69 (line in Coconut source)
max_model_size = 6  #70 (line in Coconut source)
skolem_prefix = "sk"  #71 (line in Coconut source)
definition_prefix = "Def"  #72 (line in Coconut source)
