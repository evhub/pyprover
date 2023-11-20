#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xd0a75b24

# Compiled with Coconut version 3.0.3-post_dev33

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.0.3-post_dev33', '', False)
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and str('__coconut_cache__') in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != str('__coconut_cache__'):
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

# Imports:

from pyprover.logic import Proposition  #3 (line in Coconut source)
from pyprover.logic import Constant  #3 (line in Coconut source)
from pyprover.logic import Implies  #3 (line in Coconut source)
from pyprover.logic import wff  #3 (line in Coconut source)
from pyprover.logic import bot  #3 (line in Coconut source)

# Functions:

@_coconut_tco  #13 (line in Coconut source)
def props(names):  #13 (line in Coconut source)
    """Constructs propositions from a space-seperated string of names."""  #14 (line in Coconut source)
    return _coconut_tail_call(map, Proposition, names.split())  #15 (line in Coconut source)


@_coconut_tco  #17 (line in Coconut source)
def terms(names):  #17 (line in Coconut source)
    """Constructs constants from a space-seperated string of names."""  #18 (line in Coconut source)
    return _coconut_tail_call(map, Constant, names.split())  #19 (line in Coconut source)


@_coconut_tco  #21 (line in Coconut source)
def prop_simp(expr, **kwargs):  #21 (line in Coconut source)
    """Simplify the propositional parts of expr."""  #22 (line in Coconut source)
    return _coconut_tail_call(expr.simplify, prenex_exists=False, prenex_foralls=False, **kwargs)  #23 (line in Coconut source)


@_coconut_tco  #25 (line in Coconut source)
def prenex(expr, **kwargs):  #25 (line in Coconut source)
    """Convert expr to prenex normal form."""  #26 (line in Coconut source)
    return _coconut_tail_call(expr.simplify(prenex_exists=True, prenex_foralls=False, **kwargs).simplify, prenex_exists=True, prenex_foralls=True, **kwargs)  #27 (line in Coconut source)

strict_prenex = _coconut_partial(prenex, nonempty_universe=False)  #28 (line in Coconut source)

@_coconut_tco  #30 (line in Coconut source)
def cnf(expr, **kwargs):  #30 (line in Coconut source)
    """Converts an expression to CNF."""  #31 (line in Coconut source)
    return _coconut_tail_call(prenex, expr, dnf=False, **kwargs)  #32 (line in Coconut source)

strict_cnf = _coconut_partial(cnf, nonempty_universe=False)  #33 (line in Coconut source)

@_coconut_tco  #35 (line in Coconut source)
def dnf(expr, **kwargs):  #35 (line in Coconut source)
    """Converts an expression to DNF."""  #36 (line in Coconut source)
    return _coconut_tail_call(prenex, expr, dnf=True, **kwargs)  #37 (line in Coconut source)

strict_dnf = _coconut_partial(dnf, nonempty_universe=False)  #38 (line in Coconut source)

@_coconut_tco  #40 (line in Coconut source)
def solve(expr, **kwargs):  #40 (line in Coconut source)
    """Converts to CNF and performs all possible resolutions."""  #41 (line in Coconut source)
    return _coconut_tail_call(((cnf)(expr, **kwargs)).resolve, **kwargs)  #42 (line in Coconut source)

strict_solve = _coconut_partial(solve, nonempty_universe=False)  #43 (line in Coconut source)

@_coconut_tco  #45 (line in Coconut source)
def skolemize(expr, **kwargs):  #45 (line in Coconut source)
    """Converts to CNF and skolemizes all variables."""  #46 (line in Coconut source)
    return _coconut_tail_call(solve, expr, just_skolemize=True, **kwargs)  #47 (line in Coconut source)

strict_skolemize = _coconut_partial(skolemize, nonempty_universe=False)  #48 (line in Coconut source)

def no_proof_of(givens, conclusion):  #50 (line in Coconut source)
    """Finds a formula that represents the givens not implying the conclusion."""  #51 (line in Coconut source)
    if wff(givens):  #52 (line in Coconut source)
        givens = (givens,)  #53 (line in Coconut source)
    else:  #54 (line in Coconut source)
        givens = tuple(givens)  #55 (line in Coconut source)
    return ~Implies(*(givens + (conclusion,)))  #56 (line in Coconut source)


def proves(givens, conclusion, **kwargs):  #58 (line in Coconut source)
    """Determines if the givens prove the conclusion."""  #59 (line in Coconut source)
    return (solve)(no_proof_of(givens, conclusion), **kwargs) == bot  #60 (line in Coconut source)

strict_proves = _coconut_partial(proves, nonempty_universe=False)  #61 (line in Coconut source)

def iff(a, b):  #63 (line in Coconut source)
    """Creates a formula for a implies b and b implies a."""  #64 (line in Coconut source)
    assert wff(a), a  #65 (line in Coconut source)
    assert wff(b), b  #66 (line in Coconut source)
    return a >> b & b >> a  #67 (line in Coconut source)


def proves_and_proved_by(a, b, **kwargs):  #69 (line in Coconut source)
    """Determines if a is true if and only if b."""  #70 (line in Coconut source)
    a = cnf(a, **kwargs)  #71 (line in Coconut source)
    b = cnf(b, **kwargs)  #72 (line in Coconut source)
    return (_coconut_partial(proves, **kwargs))(a, b) and (_coconut_partial(proves, **kwargs))(b, a)  #73 (line in Coconut source)

strict_proves_and_proved_by = _coconut_partial(proves_and_proved_by, nonempty_universe=False)  #74 (line in Coconut source)

@_coconut_tco  #76 (line in Coconut source)
def simplify(expr, *exprs, **kwargs):  #76 (line in Coconut source)
    """Simplify the given expression[s]."""  #77 (line in Coconut source)
    if exprs:  #78 (line in Coconut source)
        return _coconut_tail_call((tuple), (map)(_coconut_partial(dnf, **kwargs), (expr,) + exprs))  #79 (line in Coconut source)
    else:  #80 (line in Coconut source)
        return _coconut_tail_call(dnf, expr, **kwargs)  #81 (line in Coconut source)

strict_simplify = _coconut_partial(simplify, nonempty_universe=False)  #82 (line in Coconut source)

def simplest_form(expr, **kwargs):  #84 (line in Coconut source)
    """Finds the shortest simplification for the given expression."""  #85 (line in Coconut source)
    cnf_expr = cnf(expr, **kwargs)  #86 (line in Coconut source)
    dnf_expr = dnf(expr, **kwargs)  #87 (line in Coconut source)
    if len(cnf_expr) <= len(dnf_expr):  #88 (line in Coconut source)
        return cnf_expr  #89 (line in Coconut source)
    else:  #90 (line in Coconut source)
        return dnf_expr  #91 (line in Coconut source)

strict_simplest_form = _coconut_partial(simplest_form, nonempty_universe=False)  #92 (line in Coconut source)

@_coconut_tco  #94 (line in Coconut source)
def simplest_solution(expr, **kwargs):  #94 (line in Coconut source)
    """Finds the shortest resolved simplification for the given expression."""  #95 (line in Coconut source)
    return _coconut_tail_call((simplest_form), (solve)(expr, **kwargs), **kwargs)  #96 (line in Coconut source)

strict_simplest_solution = _coconut_partial(simplest_solution, nonempty_universe=False)  #97 (line in Coconut source)

@_coconut_tco  #99 (line in Coconut source)
def substitute(expr, subs, **kwargs):  #99 (line in Coconut source)
    """Substitutes expressions or booleans into the given expression."""  #100 (line in Coconut source)
    return _coconut_tail_call(expr.substitute, subs, **kwargs)  #101 (line in Coconut source)
