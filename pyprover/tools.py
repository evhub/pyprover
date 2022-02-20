#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x121e085c

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

from pyprover.logic import Proposition  #3 (line num in coconut source)
from pyprover.logic import Constant  #3 (line num in coconut source)
from pyprover.logic import Implies  #3 (line num in coconut source)
from pyprover.logic import wff  #3 (line num in coconut source)
from pyprover.logic import bot  #3 (line num in coconut source)

# Functions:

@_coconut_tco  #13 (line num in coconut source)
def props(names):  #13 (line num in coconut source)
    """Constructs propositions from a space-seperated string of names."""  #14 (line num in coconut source)
    return _coconut_tail_call(map, Proposition, names.split())  #15 (line num in coconut source)


@_coconut_tco  #17 (line num in coconut source)
def terms(names):  #17 (line num in coconut source)
    """Constructs constants from a space-seperated string of names."""  #18 (line num in coconut source)
    return _coconut_tail_call(map, Constant, names.split())  #19 (line num in coconut source)


@_coconut_tco  #21 (line num in coconut source)
def cnf(expr, **kwargs):  #21 (line num in coconut source)
    """Converts an expression to CNF."""  #22 (line num in coconut source)
    return _coconut_tail_call(expr.simplify, dnf=False, **kwargs)  #23 (line num in coconut source)


@_coconut_tco  #25 (line num in coconut source)
def dnf(expr, **kwargs):  #25 (line num in coconut source)
    """Converts an expression to DNF."""  #26 (line num in coconut source)
    return _coconut_tail_call(expr.simplify, dnf=True, **kwargs)  #27 (line num in coconut source)


@_coconut_tco  #29 (line num in coconut source)
def solve(expr, **kwargs):  #29 (line num in coconut source)
    """Converts to CNF and performs all possible resolutions."""  #30 (line num in coconut source)
    return _coconut_tail_call(((cnf)(expr, **kwargs)).resolve, **kwargs)  #31 (line num in coconut source)

strict_solve = _coconut.functools.partial(solve, nonempty_universe=False)  #32 (line num in coconut source)

@_coconut_tco  #34 (line num in coconut source)
def skolemize(expr, **kwargs):  #34 (line num in coconut source)
    """Converts to CNF and skolemizes all variables."""  #35 (line num in coconut source)
    return _coconut_tail_call(solve, expr, just_skolemize=True, **kwargs)  #36 (line num in coconut source)

strict_skolemize = _coconut.functools.partial(skolemize, nonempty_universe=False)  #37 (line num in coconut source)

def no_proof_of(givens, conclusion):  #39 (line num in coconut source)
    """Finds a formula that represents the givens not implying the conclusion."""  #40 (line num in coconut source)
    if wff(givens):  #41 (line num in coconut source)
        givens = (givens,)  #42 (line num in coconut source)
    else:  #43 (line num in coconut source)
        givens = tuple(givens)  #44 (line num in coconut source)
    return ~Implies(*(givens + (conclusion,)))  #45 (line num in coconut source)


def proves(givens, conclusion, **kwargs):  #47 (line num in coconut source)
    """Determines if the givens prove the conclusion."""  #48 (line num in coconut source)
    return (solve)(no_proof_of(givens, conclusion), **kwargs) == bot  #49 (line num in coconut source)

strict_proves = _coconut.functools.partial(proves, nonempty_universe=False)  #50 (line num in coconut source)

def iff(a, b):  #52 (line num in coconut source)
    """Creates a formula for a implies b and b implies a."""  #53 (line num in coconut source)
    assert wff(a), a  #54 (line num in coconut source)
    assert wff(b), b  #55 (line num in coconut source)
    return a >> b & b >> a  #56 (line num in coconut source)


def proves_and_proved_by(a, b, **kwargs):  #58 (line num in coconut source)
    """Determines if a is true if and only if b."""  #59 (line num in coconut source)
    a = cnf(a, **kwargs)  #60 (line num in coconut source)
    b = cnf(b, **kwargs)  #61 (line num in coconut source)
    return (_coconut.functools.partial(proves, **kwargs))(a, b) and (_coconut.functools.partial(proves, **kwargs))(b, a)  #62 (line num in coconut source)

strict_proves_and_proved_by = _coconut.functools.partial(proves_and_proved_by, nonempty_universe=False)  #63 (line num in coconut source)

@_coconut_tco  #65 (line num in coconut source)
def simplify(expr, *exprs, **kwargs):  #65 (line num in coconut source)
    """Simplify the given expression[s]."""  #66 (line num in coconut source)
    if exprs:  #67 (line num in coconut source)
        return _coconut_tail_call((tuple), (map)(lambda x: x.simplify(**kwargs), (expr,) + exprs))  #68 (line num in coconut source)
    else:  #69 (line num in coconut source)
        return _coconut_tail_call(expr.simplify, **kwargs)  #70 (line num in coconut source)

strict_simplify = _coconut.functools.partial(simplify, nonempty_universe=False)  #71 (line num in coconut source)

def simplest_form(expr, **kwargs):  #73 (line num in coconut source)
    """Finds the shortest simplification for the given expression."""  #74 (line num in coconut source)
    cnf_expr = cnf(expr, **kwargs)  #75 (line num in coconut source)
    dnf_expr = dnf(expr, **kwargs)  #76 (line num in coconut source)
    if len(cnf_expr) <= len(dnf_expr):  #77 (line num in coconut source)
        return cnf_expr  #78 (line num in coconut source)
    else:  #79 (line num in coconut source)
        return dnf_expr  #80 (line num in coconut source)

strict_simplest_form = _coconut.functools.partial(simplest_form, nonempty_universe=False)  #81 (line num in coconut source)

@_coconut_tco  #83 (line num in coconut source)
def simplest_solution(expr, **kwargs):  #83 (line num in coconut source)
    """Finds the shortest resolved simplification for the given expression."""  #84 (line num in coconut source)
    return _coconut_tail_call((simplest_form), (solve)(expr, **kwargs), **kwargs)  #85 (line num in coconut source)

strict_simplest_solution = _coconut.functools.partial(simplest_solution, nonempty_universe=False)  #86 (line num in coconut source)

@_coconut_tco  #88 (line num in coconut source)
def substitute(expr, subs, **kwargs):  #88 (line num in coconut source)
    """Substitutes expressions or booleans into the given expression."""  #89 (line num in coconut source)
    return _coconut_tail_call(expr.substitute, subs, **kwargs)  #90 (line num in coconut source)
