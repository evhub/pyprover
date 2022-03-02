#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb3f8f8b1

# Compiled with Coconut version 2.0.0-a_dev47 [How Not to Be Seen]

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
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple
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
    return len(list1) == len(list2) and set(list1) == set(list2)  #14 (line num in coconut source)


def quote(expr, in_quantifier=False):  #16 (line num in coconut source)
    """Adds parentheses in the presence of Imp, And, Or, ForAll, and Exists."""  #17 (line num in coconut source)
    expr_str = str(expr)  #18 (line num in coconut source)
    if in_quantifier and (expr_str.startswith(forall_sym) or expr_str.startswith(exists_sym)):  #19 (line num in coconut source)
        return expr_str  #22 (line num in coconut source)
    elif (imp_sym in expr_str or and_sym in expr_str or or_sym in expr_str or forall_sym in expr_str or exists_sym in expr_str):  #23 (line num in coconut source)
        return "(" + expr_str + ")"  #28 (line num in coconut source)
    else:  #29 (line num in coconut source)
        return expr_str  #30 (line num in coconut source)


def log_simplification(old, new, debug=False, **kwargs):  #32 (line num in coconut source)
    """If there was simplification done, displays a message."""  #33 (line num in coconut source)
    if debug:  #34 (line num in coconut source)
        old_str = str(old)  #35 (line num in coconut source)
        new_str = str(new)  #36 (line num in coconut source)
        if old_str != new_str:  #37 (line num in coconut source)
            print(old_str, "=>", new_str)  #38 (line num in coconut source)


def log_resolution(x, y, resolution, debug=False, **kwargs):  #40 (line num in coconut source)
    """Display a message of a resolution that was performed."""  #41 (line num in coconut source)
    if debug:  #42 (line num in coconut source)
        print(x, "+", y, "=>", resolution)  #43 (line num in coconut source)


def rem_var(var, subs):  #45 (line num in coconut source)
    """Deletes any substitutions of var in subs."""  #46 (line num in coconut source)
    newsubs = subs.copy()  #47 (line num in coconut source)
    try:  #48 (line num in coconut source)
        del newsubs[var.constant()]  #49 (line num in coconut source)
    except KeyError:  #50 (line num in coconut source)
        pass  #51 (line num in coconut source)
    try:  #52 (line num in coconut source)
        del newsubs[var.variable()]  #53 (line num in coconut source)
    except KeyError:  #54 (line num in coconut source)
        pass  #55 (line num in coconut source)
    return newsubs  #56 (line num in coconut source)


class Counter(_coconut.object):  #58 (line num in coconut source)
    def __init__(self, num=-1):  #59 (line num in coconut source)
        self.num = num  #60 (line num in coconut source)

    def inc(self):  #61 (line num in coconut source)
        assert not self.done(), self.num  #62 (line num in coconut source)
        self.num -= 1  #63 (line num in coconut source)

    def done(self):  #64 (line num in coconut source)
        return self.num == 0  #65 (line num in coconut source)


_coconut_call_set_names(Counter)  #67 (line num in coconut source)
@_coconut_tco  #67 (line num in coconut source)
def sub_once(obj, subs):  #67 (line num in coconut source)
    """Performs one substitution of subs into obj."""  #68 (line num in coconut source)
    return _coconut_tail_call(obj.substitute, subs, counter=Counter(1))  #69 (line num in coconut source)


def can_sub(kwargs):  #71 (line num in coconut source)
    """Determines if the counter in kwargs allows for another sub."""  #72 (line num in coconut source)
    _coconut_match_to_0 = kwargs  #73 (line num in coconut source)
    _coconut_match_check_0 = False  #73 (line num in coconut source)
    _coconut_match_set_name_counter = _coconut_sentinel  #73 (line num in coconut source)
    if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #73 (line num in coconut source)
        _coconut_match_temp_0 = _coconut_match_to_0.get("counter", _coconut_sentinel)  #73 (line num in coconut source)
        if _coconut_match_temp_0 is not _coconut_sentinel:  #73 (line num in coconut source)
            _coconut_match_set_name_counter = _coconut_match_temp_0  #73 (line num in coconut source)
            _coconut_match_check_0 = True  #73 (line num in coconut source)
    if _coconut_match_check_0:  #73 (line num in coconut source)
        if _coconut_match_set_name_counter is not _coconut_sentinel:  #73 (line num in coconut source)
            counter = _coconut_match_set_name_counter  #73 (line num in coconut source)
    if _coconut_match_check_0:  #73 (line num in coconut source)
        return not counter.done()  #74 (line num in coconut source)
    else:  #75 (line num in coconut source)
        return True  #76 (line num in coconut source)


def do_sub(kwargs):  #78 (line num in coconut source)
    """Increments the counter in kwargs."""  #79 (line num in coconut source)
    _coconut_match_to_1 = kwargs  #80 (line num in coconut source)
    _coconut_match_check_1 = False  #80 (line num in coconut source)
    _coconut_match_set_name_counter = _coconut_sentinel  #80 (line num in coconut source)
    if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #80 (line num in coconut source)
        _coconut_match_temp_1 = _coconut_match_to_1.get("counter", _coconut_sentinel)  #80 (line num in coconut source)
        if _coconut_match_temp_1 is not _coconut_sentinel:  #80 (line num in coconut source)
            _coconut_match_set_name_counter = _coconut_match_temp_1  #80 (line num in coconut source)
            _coconut_match_check_1 = True  #80 (line num in coconut source)
    if _coconut_match_check_1:  #80 (line num in coconut source)
        if _coconut_match_set_name_counter is not _coconut_sentinel:  #80 (line num in coconut source)
            counter = _coconut_match_set_name_counter  #80 (line num in coconut source)
    if _coconut_match_check_1:  #80 (line num in coconut source)
        counter.inc()  #81 (line num in coconut source)


def unify_elems(a, b, elems_getter, **kwargs):  #83 (line num in coconut source)
    """Find the most general unifier of the elements in a and b."""  #84 (line num in coconut source)
    subs = {}  #85 (line num in coconut source)
    for i, x in enumerate(elems_getter(a)):  #86 (line num in coconut source)
        y = elems_getter(b)[i]  #87 (line num in coconut source)
        unif = x.find_unification(y, **kwargs)  #88 (line num in coconut source)
        if unif is None:  #89 (line num in coconut source)
            return None  #90 (line num in coconut source)
        for var, sub in unif.items():  #91 (line num in coconut source)
            _coconut_match_to_2 = subs  #92 (line num in coconut source)
            _coconut_match_check_2 = False  #92 (line num in coconut source)
            _coconut_match_set_name_prev_sub = _coconut_sentinel  #92 (line num in coconut source)
            if _coconut.isinstance(_coconut_match_to_2, _coconut.abc.Mapping):  #92 (line num in coconut source)
                _coconut_match_temp_2 = _coconut_match_to_2.get(var, _coconut_sentinel)  #92 (line num in coconut source)
                if _coconut_match_temp_2 is not _coconut_sentinel:  #92 (line num in coconut source)
                    _coconut_match_set_name_prev_sub = _coconut_match_temp_2  #92 (line num in coconut source)
                    _coconut_match_check_2 = True  #92 (line num in coconut source)
            if _coconut_match_check_2:  #92 (line num in coconut source)
                if _coconut_match_set_name_prev_sub is not _coconut_sentinel:  #92 (line num in coconut source)
                    prev_sub = _coconut_match_set_name_prev_sub  #92 (line num in coconut source)
            if _coconut_match_check_2:  #92 (line num in coconut source)
                mgu = prev_sub.find_unification(sub, **kwargs)  #93 (line num in coconut source)
                if mgu is None:  #94 (line num in coconut source)
                    return None  #95 (line num in coconut source)
                elif mgu:  #96 (line num in coconut source)
                    new_a = a.substitute(mgu, **kwargs)  #97 (line num in coconut source)
                    new_b = b.substitute(mgu, **kwargs)  #98 (line num in coconut source)
                    new_unif = new_a.find_unification(new_b, **kwargs)  #99 (line num in coconut source)
                    if new_unif is None:  #100 (line num in coconut source)
                        return None  #101 (line num in coconut source)
                    mgu.update(new_unif)  #102 (line num in coconut source)
                    return mgu  #103 (line num in coconut source)
            else:  #104 (line num in coconut source)
                subs[var] = sub  #105 (line num in coconut source)
    return subs  #106 (line num in coconut source)
