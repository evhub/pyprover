#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x82517e53

# Compiled with Coconut version 1.2.2-post_dev7 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------

# Imports:

from pyprover.constants import imp_sym
from pyprover.constants import and_sym
from pyprover.constants import or_sym
from pyprover.constants import forall_sym
from pyprover.constants import exists_sym

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

@_coconut_tco
def sub_once(obj, subs):
    """Performs one substitution of subs into obj."""
    raise _coconut_tail_call(obj.substitute, subs, counter=counter(1))

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
    for key, val in _coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: dict1.items(), lambda: dict2.items()))):
        if key not in out:
            out[key] = val
        elif out[key] != val:
            return None
    return out
