#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x519dacc2

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

from pxprover.constants import imp_sym
from pxprover.constants import and_sym
from pxprover.constants import or_sym
from pxprover.constants import forall_sym
from pxprover.constants import exists_sym

# Functions:

def unorderd_eq(list1, list2):
    if len(list1) != len(list2):
        return False
    for x in list1:
        if x not in list2:
            return False
    return True

def quote(expr, in_quantifier=False):
    """Adds parentheses in the presence of Imp, And, Or, ForAll, and Exists."""
    expr_str = str(expr)
    if in_quantifier and (expr_str.startswith(forall_sym) or expr_str.startswith(exists_sym)):
        return expr_str
    elif (imp_sym in expr_str or and_sym in expr_str or or_sym in expr_str or forall_sym in expr_str or exists_sym in expr_str):
        return "(" + expr_str + ")"
    else:
        return expr_str

def log_simplification(old, new, debug=False, **kwargs):
    """If there was simplification done, displays a message."""
    if debug:
        old_str = str(old)
        new_str = str(new)
        if old_str != new_str:
            print(old_str, "=>", new_str)

def rem_var(var, subs):
    """Deletes any substitutions of var in subs."""
    newsubs = subs.copy()
    try:
        del newsubs[var.constant()]
    except KeyError:
        pass
    try:
        del newsubs[var.variable()]
    except KeyError:
        pass
    return newsubs

class counter(_coconut.object):
    def __init__(self, num=-1):
        self.num = num
    def inc(self):
        assert not self.done(), self.num
        self.num -= 1
    def done(self):
        return self.num == 0

_coconut_call_set_names(counter)
@_coconut_tco
def sub_once(obj, subs):
    """Performs one substitution of subs into obj."""
    return _coconut_tail_call(obj.substitute, subs, counter=counter(1))

def can_sub(kwargs):
    """Determines if the counter in kwargs allows for another sub."""
    try:
        return not kwargs["counter"].done()
    except KeyError:
        return True

def do_sub(kwargs):
    """Increments the counter in kwargs."""
    try:
        kwargs["counter"].inc()
    except KeyError:
        pass

def merge_dicts(dict1, dict2):
    """Merge dictionaries if there are no conflicts, otherwise None."""
    out = {}
    for key, val in _coconut.itertools.chain.from_iterable(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: dict1.items(), lambda: dict2.items()))):
        if key not in out:
            out[key] = val
        elif out[key] != val:
            return None
    return out
