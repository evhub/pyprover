#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xab8f9220

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

from pyprover.logic import Proposition
from pyprover.logic import Constant
from pyprover.logic import Implies
from pyprover.logic import wff
from pyprover.logic import bot

# Functions:

@_coconut_tco
def props(names):
    """Constructs propositions from a space-seperated string of names."""
    raise _coconut_tail_call(map, Proposition, names.split())

@_coconut_tco
def terms(names):
    """Constructs constants from a space-seperated string of names."""
    raise _coconut_tail_call(map, Constant, names.split())

def solve(expr, **kwargs):
    """Converts to CNF and performs all possible resolutions."""
    return expr.simplify(dnf=False, **kwargs).resolve(**kwargs)
strict_solve = _coconut.functools.partial(solve, nonempty_universe=False)

def no_proof_of(givens, conclusion):
    """Finds a formula that represents the givens not implying the conclusion."""
    if wff(givens):
        givens = (givens,)
    else:
        givens = tuple(givens)
    return ~Implies(*(givens + (conclusion,)))

def proves(givens, conclusion, **kwargs):
    """Determines if the givens prove the conclusion."""
    return (_coconut.functools.partial(solve, **kwargs))(no_proof_of(givens, conclusion)) == bot
strict_proves = _coconut.functools.partial(proves, nonempty_universe=False)

def iff(a, b, **kwargs):
    """Determines if a is true if and only if b."""
    a = a.simplify(dnf=False, **kwargs)
    b = b.simplify(dnf=False, **kwargs)
    return (_coconut.functools.partial(proves, **kwargs))(a, b) and (_coconut.functools.partial(proves, **kwargs))(b, a)
strict_iff = _coconut.functools.partial(iff, nonempty_universe=False)

@_coconut_tco
def simplify(expr, *exprs, **kwargs):
    """Simplify the given expression[s]."""
    if exprs:
        raise _coconut_tail_call((tuple), (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))((expr,) + exprs))
    else:
        raise _coconut_tail_call(expr.simplify, **kwargs)
strict_simplify = _coconut.functools.partial(simplify, nonempty_universe=False)

def simplest_form(expr, **kwargs):
    """Finds the shortest simplification for the given expression."""
    cnf_expr = expr.simplify(dnf=False, **kwargs)
    dnf_expr = cnf_expr.simplify(dnf=True, **kwargs)
    if len(cnf_expr) <= len(dnf_expr):
        return cnf_expr
    else:
        return dnf_expr
strict_simplest_form = _coconut.functools.partial(simplest_form, nonempty_universe=False)

@_coconut_tco
def simplest_solution(expr, **kwargs):
    """Finds the shortest resolved simplification for the given expression."""
    raise _coconut_tail_call((_coconut.functools.partial(simplest_form, **kwargs)), (_coconut.functools.partial(solve, **kwargs))(expr))
strict_simplest_solution = _coconut.functools.partial(simplest_solution, nonempty_universe=False)

@_coconut_tco
def sub_in(expr, subs):
    """Substitutes expressions or booleans into the given expression."""
    raise _coconut_tail_call(expr.substitute, subs)
