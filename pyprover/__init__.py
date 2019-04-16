#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x13d12b2f

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
