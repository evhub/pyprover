#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xffed8cc9

# Compiled with Coconut version 1.2.2-post_dev4 [Colonel]

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

from pyprover.constants import imp_sym  # line 2
from pyprover.constants import and_sym  # line 2
from pyprover.constants import or_sym  # line 2
from pyprover.constants import forall_sym  # line 2
from pyprover.constants import exists_sym  # line 3

# Functions:

def unorderd_eq(list1, list2):  # line 13
    if len(list1) != len(list2):  # line 14
        return False  # line 15
    for x in list1:  # line 16
        if x not in list2:  # line 17
            return False  # line 18
    return True  # line 19

def quote(expr):  # line 21
    """Adds parentheses in the presence of Imp, And, Or, ForAll, and Exists."""  # line 22
    expr_str = str(expr)  # line 23
    if (imp_sym in expr_str or and_sym in expr_str or or_sym in expr_str or forall_sym in expr_str or exists_sym in expr_str):  # line 24
        return "(" + expr_str + ")"  # line 29
    else:  # line 30
        return expr_str  # line 31

def log_simplification(old, new, debug=False, **kwargs):  # line 33
    """If there was simplification done, displays a message."""  # line 34
    if debug:  # line 35
        old_str = str(old)  # line 36
        new_str = str(new)  # line 37
        if old_str != new_str:  # line 38
            print(old_str, "=>", new_str)  # line 39
