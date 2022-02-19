#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x402d75b6

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

from pyprover.constants import imp_sym  #3 (line num in coconut source)
from pyprover.constants import and_sym  #3 (line num in coconut source)
from pyprover.constants import or_sym  #3 (line num in coconut source)
from pyprover.constants import forall_sym  #3 (line num in coconut source)
from pyprover.constants import exists_sym  #3 (line num in coconut source)

# Functions:

def unorderd_eq(list1, list2):  #13 (line num in coconut source)
    if len(list1) != len(list2):  #14 (line num in coconut source)
        return False  #15 (line num in coconut source)
    for x in list1:  #16 (line num in coconut source)
        if x not in list2:  #17 (line num in coconut source)
            return False  #18 (line num in coconut source)
    return True  #19 (line num in coconut source)


def quote(expr, in_quantifier=False):  #21 (line num in coconut source)
    """Adds parentheses in the presence of Imp, And, Or, ForAll, and Exists."""  #22 (line num in coconut source)
    expr_str = str(expr)  #23 (line num in coconut source)
    if in_quantifier and (expr_str.startswith(forall_sym) or expr_str.startswith(exists_sym)):  #24 (line num in coconut source)
        return expr_str  #27 (line num in coconut source)
    elif (imp_sym in expr_str or and_sym in expr_str or or_sym in expr_str or forall_sym in expr_str or exists_sym in expr_str):  #28 (line num in coconut source)
        return "(" + expr_str + ")"  #33 (line num in coconut source)
    else:  #34 (line num in coconut source)
        return expr_str  #35 (line num in coconut source)


def log_simplification(old, new, debug=False, **kwargs):  #37 (line num in coconut source)
    """If there was simplification done, displays a message."""  #38 (line num in coconut source)
    if debug:  #39 (line num in coconut source)
        old_str = str(old)  #40 (line num in coconut source)
        new_str = str(new)  #41 (line num in coconut source)
        if old_str != new_str:  #42 (line num in coconut source)
            print(old_str, "=>", new_str)  #43 (line num in coconut source)


def log_resolution(x, y, resolution, debug=False, **kwargs):  #45 (line num in coconut source)
    """Display a message of a resolution that was performed."""  #46 (line num in coconut source)
    if debug:  #47 (line num in coconut source)
        print(x, "+", y, "=>", resolution)  #48 (line num in coconut source)


def rem_var(var, subs):  #50 (line num in coconut source)
    """Deletes any substitutions of var in subs."""  #51 (line num in coconut source)
    newsubs = subs.copy()  #52 (line num in coconut source)
    try:  #53 (line num in coconut source)
        del newsubs[var.constant()]  #54 (line num in coconut source)
    except KeyError:  #55 (line num in coconut source)
        pass  #56 (line num in coconut source)
    try:  #57 (line num in coconut source)
        del newsubs[var.variable()]  #58 (line num in coconut source)
    except KeyError:  #59 (line num in coconut source)
        pass  #60 (line num in coconut source)
    return newsubs  #61 (line num in coconut source)


class counter(_coconut.object):  #63 (line num in coconut source)
    def __init__(self, num=-1):  #64 (line num in coconut source)
        self.num = num  #65 (line num in coconut source)

    def inc(self):  #66 (line num in coconut source)
        assert not self.done(), self.num  #67 (line num in coconut source)
        self.num -= 1  #68 (line num in coconut source)

    def done(self):  #69 (line num in coconut source)
        return self.num == 0  #70 (line num in coconut source)


_coconut_call_set_names(counter)  #72 (line num in coconut source)
@_coconut_tco  #72 (line num in coconut source)
def sub_once(obj, subs):  #72 (line num in coconut source)
    """Performs one substitution of subs into obj."""  #73 (line num in coconut source)
    return _coconut_tail_call(obj.substitute, subs, counter=counter(1))  #74 (line num in coconut source)


def can_sub(kwargs):  #76 (line num in coconut source)
    """Determines if the counter in kwargs allows for another sub."""  #77 (line num in coconut source)
    try:  #78 (line num in coconut source)
        return not kwargs["counter"].done()  #79 (line num in coconut source)
    except KeyError:  #80 (line num in coconut source)
        return True  #81 (line num in coconut source)


def do_sub(kwargs):  #83 (line num in coconut source)
    """Increments the counter in kwargs."""  #84 (line num in coconut source)
    try:  #85 (line num in coconut source)
        kwargs["counter"].inc()  #86 (line num in coconut source)
    except KeyError:  #87 (line num in coconut source)
        pass  #88 (line num in coconut source)


def merge_dicts(dict1, dict2):  #90 (line num in coconut source)
    """Merge dictionaries if there are no conflicts, otherwise None."""  #91 (line num in coconut source)
    out = {}  #92 (line num in coconut source)
    for key, val in _coconut.itertools.chain.from_iterable(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: dict1.items(), lambda: dict2.items()))):  #93 (line num in coconut source)
        if key not in out:  #94 (line num in coconut source)
            out[key] = val  #95 (line num in coconut source)
        elif out[key] != val:  #96 (line num in coconut source)
            return None  #97 (line num in coconut source)
    return out  #98 (line num in coconut source)
