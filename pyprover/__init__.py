#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x78fad73

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

from pyprover.logic import ForAll
from pyprover.logic import Exists
from pyprover.logic import FA
from pyprover.logic import TE
from pyprover.logic import top
from pyprover.logic import bot
from pyprover.logic import true
from pyprover.logic import false
from pyprover.logic import Not
from pyprover.logic import Imp
from pyprover.logic import Or
from pyprover.logic import And
from pyprover.logic import Eq
from pyprover.tools import props
from pyprover.tools import terms
from pyprover.tools import solve
from pyprover.tools import strict_solve
from pyprover.tools import no_proof_of
from pyprover.tools import proves
from pyprover.tools import strict_proves
from pyprover.tools import proves_and_proved_by
from pyprover.tools import strict_proves_and_proved_by
from pyprover.tools import iff
from pyprover.tools import simplify
from pyprover.tools import strict_simplify
from pyprover.tools import simplest_form
from pyprover.tools import strict_simplest_form
from pyprover.tools import simplest_solution
from pyprover.tools import strict_simplest_solution
from pyprover.tools import substitute
from pyprover.atoms import LowercasePropositions
from pyprover.atoms import UppercasePropositions
from pyprover.atoms import LowercaseVariables
from pyprover.atoms import UppercaseVariables
from pyprover.atoms import StandardMath
from pyprover.parser import expr

# Main:

StandardMath.use(globals())
