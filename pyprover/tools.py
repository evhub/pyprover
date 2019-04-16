#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x9af0aef

# Compiled with Coconut version 1.4.0-post_dev29 [Ernest Scribbler]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel, _coconut_assert
from __coconut__ import *
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

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
    return _coconut_tail_call(map, Proposition, names.split())

@_coconut_tco
def terms(names):
    """Constructs constants from a space-seperated string of names."""
    return _coconut_tail_call(map, Constant, names.split())

@_coconut_tco
def solve(expr, **kwargs):
    """Converts to CNF and performs all possible resolutions."""
    return _coconut_tail_call(expr.simplify(dnf=False, **kwargs).resolve, **kwargs)
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
    return solve(no_proof_of(givens, conclusion), **kwargs) == bot
strict_proves = _coconut.functools.partial(proves, nonempty_universe=False)

def iff(a, b):
    """Creates a formula for a implies b and b implies a."""
    assert wff(a), a
    assert wff(b), b
    return a >> b & b >> a

def proves_and_proved_by(a, b, **kwargs):
    """Determines if a is true if and only if b."""
    a = a.simplify(dnf=False, **kwargs)
    b = b.simplify(dnf=False, **kwargs)
    return (_coconut.functools.partial(proves, **kwargs))(a, b) and (_coconut.functools.partial(proves, **kwargs))(b, a)
strict_proves_and_proved_by = _coconut.functools.partial(proves_and_proved_by, nonempty_universe=False)

@_coconut_tco
def simplify(expr, *exprs, **kwargs):
    """Simplify the given expression[s]."""
    if exprs:
        return _coconut_tail_call((tuple), map(lambda x: x.simplify(**kwargs), (expr,) + exprs))
    else:
        return _coconut_tail_call(expr.simplify, **kwargs)
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
    return _coconut_tail_call(simplest_form, solve(expr, **kwargs), **kwargs)
strict_simplest_solution = _coconut.functools.partial(simplest_solution, nonempty_universe=False)

@_coconut_tco
def substitute(expr, subs, **kwargs):
    """Substitutes expressions or booleans into the given expression."""
    return _coconut_tail_call(expr.substitute, subs, **kwargs)
