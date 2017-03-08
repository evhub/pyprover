#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf60bcc84

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

from pyprover.logic import Proposition  # line 2
from pyprover.logic import Constant  # line 2
from pyprover.logic import Implies  # line 2
from pyprover.logic import wff  # line 2
from pyprover.logic import bot  # line 3

# Functions:

@_coconut_tco  # line 12
def props(names):  # line 12
    """Constructs propositions from a space-seperated string of names."""  # line 14
    raise _coconut_tail_call(map, Proposition, names.split())  # line 15

@_coconut_tco  # line 16
def terms(names):  # line 16
    """Constructs constants from a space-seperated string of names."""  # line 18
    raise _coconut_tail_call(map, Constant, names.split())  # line 19

def solve(expr, **kwargs):  # line 20
    """Converts to CNF and performs all possible resolutions."""  # line 22
    return expr.simplify(dnf=False, **kwargs).resolve(**kwargs)  # line 23
strict_solve = _coconut.functools.partial(solve, nonempty_universe=False)  # line 24

def no_proof_of(givens, conclusion):  # line 25
    """Finds a formula that represents the givens not implying the conclusion."""  # line 27
    if wff(givens):  # line 28
        givens = (givens,)  # line 29
    else:  # line 30
        givens = tuple(givens)  # line 31
    return ~Implies(*(givens + (conclusion,)))  # line 32

def proves(givens, conclusion, **kwargs):  # line 33
    """Determines if the givens prove the conclusion."""  # line 35
    return (_coconut.functools.partial(solve, **kwargs))(no_proof_of(givens, conclusion)) == bot  # line 36
strict_proves = _coconut.functools.partial(proves, nonempty_universe=False)  # line 37

def iff(a, b, **kwargs):  # line 38
    """Determines if a is true if and only if b."""  # line 40
    a = a.simplify(dnf=False, **kwargs)  # line 41
    b = b.simplify(dnf=False, **kwargs)  # line 42
    return (_coconut.functools.partial(proves, **kwargs))(a, b) and (_coconut.functools.partial(proves, **kwargs))(b, a)  # line 43
strict_iff = _coconut.functools.partial(iff, nonempty_universe=False)  # line 44

@_coconut_tco  # line 45
def simplify(expr, *exprs, **kwargs):  # line 46
    """Simplify the given expression[s]."""  # line 47
    if exprs:  # line 48
        raise _coconut_tail_call((tuple), (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))((expr,) + exprs))  # line 49
    else:  # line 50
        raise _coconut_tail_call(expr.simplify, **kwargs)  # line 51
strict_simplify = _coconut.functools.partial(simplify, nonempty_universe=False)  # line 52

def simplest_form(expr, **kwargs):  # line 54
    """Finds the shortest simplification for the given expression."""  # line 55
    cnf_expr = expr.simplify(dnf=False, **kwargs)  # line 56
    dnf_expr = cnf_expr.simplify(dnf=True, **kwargs)  # line 57
    if len(cnf_expr) <= len(dnf_expr):  # line 58
        return cnf_expr  # line 59
    else:  # line 60
        return dnf_expr  # line 61
strict_simplest_form = _coconut.functools.partial(simplest_form, nonempty_universe=False)  # line 62

@_coconut_tco  # line 63
def simplest_solution(expr, **kwargs):  # line 63
    """Finds the shortest resolved simplification for the given expression."""  # line 65
    raise _coconut_tail_call((_coconut.functools.partial(simplest_form, **kwargs)), (_coconut.functools.partial(solve, **kwargs))(expr))  # line 66
strict_simplest_solution = _coconut.functools.partial(simplest_solution, nonempty_universe=False)  # line 67

@_coconut_tco  # line 68
def sub_in(expr, subs):  # line 68
    """Substitutes expressions or booleans into the given expression."""  # line 70
    raise _coconut_tail_call(expr.substitute, subs)  # line 71
