#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xd6d4a64

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

from pxprover.logic import Proposition
from pxprover.logic import Constant
from pxprover.logic import Implies
from pxprover.logic import wff
from pxprover.logic import bot

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
    return (solve)(no_proof_of(givens, conclusion), **kwargs) == bot
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
        return _coconut_tail_call((tuple), (map)(lambda x: x.simplify(**kwargs), (expr,) + exprs))
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
    return _coconut_tail_call((simplest_form), (solve)(expr, **kwargs), **kwargs)
strict_simplest_solution = _coconut.functools.partial(simplest_solution, nonempty_universe=False)

@_coconut_tco
def substitute(expr, subs, **kwargs):
    """Substitutes expressions or booleans into the given expression."""
    return _coconut_tail_call(expr.substitute, subs, **kwargs)
