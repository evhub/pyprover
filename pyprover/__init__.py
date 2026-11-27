#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x1cf94757

# Compiled with Coconut version 3.2.0-post_dev19
# This file was compiled from __init__.coco by the Coconut compiler; edit that file rather than this one.
# For a guide to writing Coconut, see http://coconut.readthedocs.io/en/develop/llms.txt (or run 'coconut --ai-docs').

"""PyProver: a theorem prover for first-order logic with equality.

`from pyprover import *` imports everything below along with the uppercase
letters A-Z as propositions/predicates and the lowercase letters a-z as
constants/variables/functions."""

# Coconut Header: -------------------------------------------------------------

import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev19', '3', True)
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
from __coconut__ import _coconut_call_set_names, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning, _coconut_lazy_module, _coconut_lazy_get, _coconut_type, _coconut_assert_msg
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

from pyprover.constants import version as __version__  # NOQA  #9 (line in Coconut source)
from pyprover.constants import use_unicode  # NOQA  #9 (line in Coconut source)
from pyprover.constants import use_ascii  # NOQA  #9 (line in Coconut source)
from pyprover.logic import Expr  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Term  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Top  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Bot  # NOQA  #14 (line in Coconut source)
from pyprover.logic import top  # NOQA  #14 (line in Coconut source)
from pyprover.logic import bot  # NOQA  #14 (line in Coconut source)
from pyprover.logic import true  # NOQA  #14 (line in Coconut source)
from pyprover.logic import false  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Prop  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Proposition  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Pred  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Predicate  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Eq  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Equals  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Not  # NOQA  #14 (line in Coconut source)
from pyprover.logic import And  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Or  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Imp  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Implies  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Iff  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Quantifier  # NOQA  #14 (line in Coconut source)
from pyprover.logic import ForAll  # NOQA  #14 (line in Coconut source)
from pyprover.logic import FA  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Exists  # NOQA  #14 (line in Coconut source)
from pyprover.logic import TE  # NOQA  #14 (line in Coconut source)
from pyprover.logic import EX  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Const  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Constant  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Var  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Variable  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Func  # NOQA  #14 (line in Coconut source)
from pyprover.logic import Function  # NOQA  #14 (line in Coconut source)
from pyprover.logic import wff  # NOQA  #14 (line in Coconut source)
from pyprover.logic import isvar  # NOQA  #14 (line in Coconut source)
from pyprover.logic import substitute  # NOQA  #14 (line in Coconut source)
from pyprover.logic import unify  # NOQA  #14 (line in Coconut source)
from pyprover.logic import free_terms  # NOQA  #14 (line in Coconut source)
from pyprover.logic import free_consts  # NOQA  #14 (line in Coconut source)
from pyprover.logic import free_vars  # NOQA  #14 (line in Coconut source)
from pyprover.logic import size  # NOQA  #14 (line in Coconut source)
from pyprover.normal import nnf  # NOQA  #56 (line in Coconut source)
from pyprover.normal import prop_simp  # NOQA  #56 (line in Coconut source)
from pyprover.normal import prenex  # NOQA  #56 (line in Coconut source)
from pyprover.normal import strict_prenex  # NOQA  #56 (line in Coconut source)
from pyprover.normal import cnf  # NOQA  #56 (line in Coconut source)
from pyprover.normal import strict_cnf  # NOQA  #56 (line in Coconut source)
from pyprover.normal import dnf  # NOQA  #56 (line in Coconut source)
from pyprover.normal import strict_dnf  # NOQA  #56 (line in Coconut source)
from pyprover.normal import simplify  # NOQA  #56 (line in Coconut source)
from pyprover.normal import strict_simplify  # NOQA  #56 (line in Coconut source)
from pyprover.normal import simplest_form  # NOQA  #56 (line in Coconut source)
from pyprover.normal import strict_simplest_form  # NOQA  #56 (line in Coconut source)
from pyprover.normal import skolemize  # NOQA  #56 (line in Coconut source)
from pyprover.normal import strict_skolemize  # NOQA  #56 (line in Coconut source)
from pyprover.normal import universal_closure  # NOQA  #56 (line in Coconut source)
from pyprover.prover import Proof  # NOQA  #73 (line in Coconut source)
from pyprover.prover import ProofStep  # NOQA  #73 (line in Coconut source)
from pyprover.prover import Countermodel  # NOQA  #73 (line in Coconut source)
from pyprover.prover import prove  # NOQA  #73 (line in Coconut source)
from pyprover.prover import strict_prove  # NOQA  #73 (line in Coconut source)
from pyprover.prover import proves  # NOQA  #73 (line in Coconut source)
from pyprover.prover import strict_proves  # NOQA  #73 (line in Coconut source)
from pyprover.tools import props  # NOQA  #82 (line in Coconut source)
from pyprover.tools import terms  # NOQA  #82 (line in Coconut source)
from pyprover.tools import variables  # NOQA  #82 (line in Coconut source)
from pyprover.tools import iff  # NOQA  #82 (line in Coconut source)
from pyprover.tools import no_proof_of  # NOQA  #82 (line in Coconut source)
from pyprover.tools import proves_and_proved_by  # NOQA  #82 (line in Coconut source)
from pyprover.tools import strict_proves_and_proved_by  # NOQA  #82 (line in Coconut source)
from pyprover.tools import equivalent  # NOQA  #82 (line in Coconut source)
from pyprover.tools import valid  # NOQA  #82 (line in Coconut source)
from pyprover.tools import satisfiable  # NOQA  #82 (line in Coconut source)
from pyprover.tools import countermodel  # NOQA  #82 (line in Coconut source)
from pyprover.tools import solve  # NOQA  #82 (line in Coconut source)
from pyprover.tools import strict_solve  # NOQA  #82 (line in Coconut source)
from pyprover.tools import simplest_solution  # NOQA  #82 (line in Coconut source)
from pyprover.tools import strict_simplest_solution  # NOQA  #82 (line in Coconut source)
from pyprover.atoms import Vars  # NOQA  #99 (line in Coconut source)
from pyprover.atoms import LowercasePropositions  # NOQA  #99 (line in Coconut source)
from pyprover.atoms import UppercasePropositions  # NOQA  #99 (line in Coconut source)
from pyprover.atoms import LowercaseVariables  # NOQA  #99 (line in Coconut source)
from pyprover.atoms import UppercaseVariables  # NOQA  #99 (line in Coconut source)
from pyprover.atoms import StandardMath  # NOQA  #99 (line in Coconut source)
from pyprover.parser import ParseError  # NOQA  #107 (line in Coconut source)
from pyprover.parser import expr  # NOQA  #107 (line in Coconut source)
from pyprover.parser import parse  # NOQA  #107 (line in Coconut source)

# Main:

StandardMath.use(globals())  #115 (line in Coconut source)
