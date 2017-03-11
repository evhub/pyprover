#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x8b8fdc17

# Compiled with Coconut version 1.2.2-post_dev5 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_tee, _coconut_map, _coconut_partial
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

def add_sub(subs, oldvar, newvar):
    """Adds a substitution from newvar to oldvar."""
    newsubs = subs.copy()
    try:
        del newsubs[oldvar.constant()]
    except KeyError:
        pass
    try:
        del newsubs[oldvar.variable()]
    except KeyError:
        pass
    newsubs[oldvar] = newvar
    return newsubs
