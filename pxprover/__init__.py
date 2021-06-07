#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb93e4175

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

from pxprover.logic import ForAll
from pxprover.logic import Exists
from pxprover.logic import FA
from pxprover.logic import TE
from pxprover.logic import top
from pxprover.logic import bot
from pxprover.logic import true
from pxprover.logic import false
from pxprover.logic import Not
from pxprover.logic import Imp
from pxprover.logic import Or
from pxprover.logic import And
from pxprover.logic import Eq
from pxprover.tools import props
from pxprover.tools import terms
from pxprover.tools import solve
from pxprover.tools import strict_solve
from pxprover.tools import no_proof_of
from pxprover.tools import proves
from pxprover.tools import strict_proves
from pxprover.tools import proves_and_proved_by
from pxprover.tools import strict_proves_and_proved_by
from pxprover.tools import iff
from pxprover.tools import simplify
from pxprover.tools import strict_simplify
from pxprover.tools import simplest_form
from pxprover.tools import strict_simplest_form
from pxprover.tools import simplest_solution
from pxprover.tools import strict_simplest_solution
from pxprover.tools import substitute
from pxprover.atoms import LowercasePropositions
from pxprover.atoms import UppercasePropositions
from pxprover.atoms import LowercaseVariables
from pxprover.atoms import UppercaseVariables
from pxprover.atoms import StandardMath
from pxprover.parser import expr

# Main:

StandardMath.use(globals())
