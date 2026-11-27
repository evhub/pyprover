#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x851c6e18

# Compiled with Coconut version 3.2.0-post_dev20
# This file was compiled from tools.coco by the Coconut compiler; edit that file rather than this one.
# For a guide to writing Coconut, see http://coconut.readthedocs.io/en/develop/llms.txt (or run 'coconut --ai-docs').

"""Convenience functions built on top of the prover and normal forms."""

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop, annotations
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev20', '39', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get('__coconut__')
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules['_coconut_cached__coconut__'] = _coconut_cached__coconut__
        del _coconut_sys.modules['__coconut__']
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and _coconut_os.path.exists(_coconut_os.path.join(_coconut_file_dir, "__init__.py")):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == '__coconut__':  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == '__coconut__':  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning, _coconut_lazy_module, _coconut_lazy_get, _coconut_type, _coconut_assert_msg
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and '__coconut_cache__' in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != '__coconut_cache__':
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------



# Imports:

from pyprover.constants import default_timeout  #5 (line in Coconut source)
from pyprover.constants import default_max_clauses  #5 (line in Coconut source)
from pyprover.logic import bot  #9 (line in Coconut source)
from pyprover.logic import Prop  #9 (line in Coconut source)
from pyprover.logic import Const  #9 (line in Coconut source)
from pyprover.logic import Var  #9 (line in Coconut source)
from pyprover.logic import Not  #9 (line in Coconut source)
from pyprover.logic import And  #9 (line in Coconut source)
from pyprover.logic import Imp  #9 (line in Coconut source)
from pyprover.logic import Iff  #9 (line in Coconut source)
from pyprover.normal import cnf  #19 (line in Coconut source)
from pyprover.normal import simplest_form  #19 (line in Coconut source)
from pyprover.prover import as_premises  #23 (line in Coconut source)
from pyprover.prover import prove  #23 (line in Coconut source)
from pyprover.prover import proves  #23 (line in Coconut source)


# Constructors:

def props(names: str) -> list:  #32 (line in Coconut source)
    """Construct propositions (which can be called to make predicates) from
    a space-separated string of names."""  #34 (line in Coconut source)
    return (list)((map)(Prop, names.split()))  #35 (line in Coconut source)


def terms(names: str) -> list:  #37 (line in Coconut source)
    """Construct constants (which can be called to make functions) from a
    space-separated string of names."""  #39 (line in Coconut source)
    return (list)((map)(Const, names.split()))  #40 (line in Coconut source)


def variables(names: str) -> list:  #42 (line in Coconut source)
    """Construct schematic ?variables from a space-separated string of names."""  #43 (line in Coconut source)
    return (list)((map)(Var, names.split()))  #44 (line in Coconut source)


def iff(a, b):  #46 (line in Coconut source)
    """Construct the biconditional a ↔ b."""  #47 (line in Coconut source)
    return Iff(a, b)  #48 (line in Coconut source)


# Proving:


def no_proof_of(givens, conclusion):  #53 (line in Coconut source)
    """Construct a formula that is satisfiable exactly when givens don't prove conclusion."""  #54 (line in Coconut source)
    return Not(Imp(And(*as_premises(givens)), conclusion))  #55 (line in Coconut source)


def proves_and_proved_by(a, b, **kwargs) -> bool:  #57 (line in Coconut source)
    """Determine whether a and b are logically equivalent."""  #58 (line in Coconut source)
    return proves(a, b, **kwargs) and proves(b, a, **kwargs)  #59 (line in Coconut source)


equivalent = proves_and_proved_by  #61 (line in Coconut source)

def strict_proves_and_proved_by(a, b, **kwargs) -> bool:  #63 (line in Coconut source)
    """Same as proves_and_proved_by, but doesn't assume that something exists."""  #64 (line in Coconut source)
    return proves_and_proved_by(a, b, nonempty_universe=False, **kwargs)  #65 (line in Coconut source)


def valid(expr, **kwargs) -> bool:  #67 (line in Coconut source)
    """Determine whether expr is true in every interpretation."""  #68 (line in Coconut source)
    return proves((), expr, **kwargs)  #69 (line in Coconut source)


def satisfiable(expr, **kwargs) -> bool:  #71 (line in Coconut source)
    """Determine whether expr is true in some interpretation."""  #72 (line in Coconut source)
    return not proves(expr, bot, **kwargs)  #73 (line in Coconut source)


def countermodel(givens, conclusion, nonempty_universe=True, timeout=default_timeout, max_clauses=default_max_clauses):  #75 (line in Coconut source)
    """Find a finite model in which givens are true but conclusion is false,
    or None if none could be found (which is always the case if the givens
    prove the conclusion)."""  #78 (line in Coconut source)
    return prove(givens, conclusion, nonempty_universe=nonempty_universe, timeout=timeout, max_clauses=max_clauses).countermodel  #79 (line in Coconut source)


def solve(expr, **kwargs):  #81 (line in Coconut source)
    """Return ⊥ if expr is unsatisfiable, else its conjunctive normal form."""  #82 (line in Coconut source)
    return cnf(expr, nonempty_universe=kwargs.get("nonempty_universe", True)) if satisfiable(expr, **kwargs) else bot  #83 (line in Coconut source)


def strict_solve(expr, **kwargs):  #85 (line in Coconut source)
    return solve(expr, nonempty_universe=False, **kwargs)  #85 (line in Coconut source)


def simplest_solution(expr, **kwargs):  #87 (line in Coconut source)
    """Return ⊥ if expr is unsatisfiable, else its simplest form."""  #88 (line in Coconut source)
    return simplest_form(expr, nonempty_universe=kwargs.get("nonempty_universe", True)) if satisfiable(expr, **kwargs) else bot  #89 (line in Coconut source)


def strict_simplest_solution(expr, **kwargs):  #91 (line in Coconut source)
    return simplest_solution(expr, nonempty_universe=False, **kwargs)  #91 (line in Coconut source)
