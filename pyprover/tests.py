#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x836062fa

# Compiled with Coconut version 3.2.0-post_dev19
# This file was compiled from tests.coco by the Coconut compiler; edit that file rather than this one.
# For a guide to writing Coconut, see http://coconut.readthedocs.io/en/develop/llms.txt (or run 'coconut --ai-docs').

"""The PyProver test suite (run with pytest)."""

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

import warnings  #5 (line in Coconut source)

import pytest  #7 (line in Coconut source)

from pyprover import FA  #9 (line in Coconut source)
from pyprover import TE  #9 (line in Coconut source)
from pyprover import top  #9 (line in Coconut source)
from pyprover import bot  #9 (line in Coconut source)
from pyprover import And  #9 (line in Coconut source)
from pyprover import Or  #9 (line in Coconut source)
from pyprover import Imp  #9 (line in Coconut source)
from pyprover import Iff  #9 (line in Coconut source)
from pyprover import Eq  #9 (line in Coconut source)
from pyprover import Prop  #9 (line in Coconut source)
from pyprover import Const  #9 (line in Coconut source)
from pyprover import Var  #9 (line in Coconut source)
from pyprover import Func  #9 (line in Coconut source)
from pyprover import proves  #9 (line in Coconut source)
from pyprover import strict_proves  #9 (line in Coconut source)
from pyprover import prove  #9 (line in Coconut source)
from pyprover import strict_prove  #9 (line in Coconut source)
from pyprover import proves_and_proved_by  #9 (line in Coconut source)
from pyprover import simplify  #9 (line in Coconut source)
from pyprover import strict_simplify  #9 (line in Coconut source)
from pyprover import simplest_form  #9 (line in Coconut source)
from pyprover import substitute  #9 (line in Coconut source)
from pyprover import nnf  #9 (line in Coconut source)
from pyprover import cnf  #9 (line in Coconut source)
from pyprover import dnf  #9 (line in Coconut source)
from pyprover import prenex  #9 (line in Coconut source)
from pyprover import skolemize  #9 (line in Coconut source)
from pyprover import valid  #9 (line in Coconut source)
from pyprover import satisfiable  #9 (line in Coconut source)
from pyprover import countermodel  #9 (line in Coconut source)
from pyprover import solve  #9 (line in Coconut source)
from pyprover import unify  #9 (line in Coconut source)
from pyprover import expr  #9 (line in Coconut source)
from pyprover import wff  #9 (line in Coconut source)
from pyprover import ParseError  #9 (line in Coconut source)
from pyprover import props  #9 (line in Coconut source)
from pyprover import terms  #9 (line in Coconut source)
from pyprover import use_ascii  #9 (line in Coconut source)
from pyprover import use_unicode  #9 (line in Coconut source)
from pyprover.__main__ import main  #50 (line in Coconut source)
from pyprover.atoms import lowercase  #51 (line in Coconut source)
from pyprover.atoms import uppercase  #51 (line in Coconut source)


# Atoms:

A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = props(uppercase)  #59 (line in Coconut source)
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = terms(lowercase)  #60 (line in Coconut source)


# Tests:

def test_propositional_logic():  #65 (line in Coconut source)
    """Runs propositional logic tests."""  #66 (line in Coconut source)
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = props(lowercase)  #67 (line in Coconut source)

# constructive theorems
    assert (proves)(e & f, e)  #70 (line in Coconut source)
    assert (proves)(e & f, f)  #71 (line in Coconut source)
    assert (proves)((e >> f, f >> g, e), g)  #72 (line in Coconut source)
    assert (proves)((e >> (f >> g), e >> f, e), g)  #73 (line in Coconut source)
    assert (proves)((e >> f, f >> g), e >> g)  #74 (line in Coconut source)
    assert (proves)(e >> (f >> g), f >> (e >> g))  #75 (line in Coconut source)
    assert (proves)(e >> (f >> g), (e >> f) >> (e >> g))  #76 (line in Coconut source)
    assert (proves)(e, f >> e)  #77 (line in Coconut source)
    assert (proves)(top, e >> (f >> e))  #78 (line in Coconut source)
    assert (proves)(e >> (f & g), (e >> f) & (e >> g))  #79 (line in Coconut source)
    assert (proves)(e >> (f >> g), (e & f) >> g)  #80 (line in Coconut source)
    assert (proves)((e & f) >> g, e >> (f >> g))  #81 (line in Coconut source)
    assert (proves)((e >> f) >> g, (e & f) >> g)  #82 (line in Coconut source)
    assert (proves)(e & (f >> g), (e >> f) >> g)  #83 (line in Coconut source)
    assert (proves)(e, e | f)  #84 (line in Coconut source)
    assert (proves)(f, e | f)  #85 (line in Coconut source)
    assert (proves)(e | f, f | e)  #86 (line in Coconut source)
    assert (proves)(f >> g, (e | f) >> (e | g))  #87 (line in Coconut source)
    assert (proves)(e, e | e)  #88 (line in Coconut source)
    assert (proves)(e, ~~e)  #89 (line in Coconut source)
    assert (proves)(~e, e >> f)  #90 (line in Coconut source)
    assert (proves)(e >> f, ~f >> ~e)  #91 (line in Coconut source)
    assert (proves)(e | f, ~(~e & ~f))  #92 (line in Coconut source)
    assert (proves)(e & f, ~(~e | ~f))  #93 (line in Coconut source)
    assert (proves)(~(e | f), ~e & ~f)  #94 (line in Coconut source)
    assert (proves)(~e & ~f, ~(e | f))  #95 (line in Coconut source)
    assert (proves)(~e | ~f, ~(e & f))  #96 (line in Coconut source)
    assert (proves)(top, ~(e & ~e))  #97 (line in Coconut source)
    assert (proves)(e & ~e, f)  #98 (line in Coconut source)
    assert (proves)(~f, f >> g)  #99 (line in Coconut source)
    assert (proves)((f >> g, ~f >> g), g)  #100 (line in Coconut source)
    assert (proves)(g, f >> g)  #101 (line in Coconut source)
    assert (proves)((f, ~(f & g)), ~g)  #102 (line in Coconut source)
    assert (proves)((p >> r, p >> ~r), ~p)  #103 (line in Coconut source)
    assert (proves)(top, (p >> ~p) >> ~p)  #104 (line in Coconut source)
    assert (proves)(bot, a)  #105 (line in Coconut source)
    assert (proves)(bot, top)  #106 (line in Coconut source)
    assert (proves)(a, top)  #107 (line in Coconut source)

# classical theorems
    assert (proves)(~~e, e)  #110 (line in Coconut source)
    assert (proves)(top, e | ~e)  #111 (line in Coconut source)
    assert (proves)(top, ((e >> f) >> e) >> e)  #112 (line in Coconut source)
    assert (proves)(~f >> ~e, e >> f)  #113 (line in Coconut source)
    assert (proves)(~(~e & ~f), e | f)  #114 (line in Coconut source)
    assert (proves)(~(~e | ~f), e & f)  #115 (line in Coconut source)
    assert (proves)(~(e & f), ~e | ~f)  #116 (line in Coconut source)
    assert (proves)(top, (e >> f) | (f >> e))  #117 (line in Coconut source)
    assert (proves)(top, (~~a | a) >> a)  #118 (line in Coconut source)
    assert (proves)(p >> r, (f >> r) | (p >> g))  #119 (line in Coconut source)
    assert (proves)(~(f >> g), f & ~g)  #120 (line in Coconut source)
    assert (proves)(top, (~f >> bot) >> f)  #121 (line in Coconut source)
    assert (proves)(f >> g, ~f | g)  #122 (line in Coconut source)
    assert (proves)(top, r & s | (~r | ~s))  #123 (line in Coconut source)
    assert (proves)(f >> g, g | ~f)  #124 (line in Coconut source)
    assert (proves)((a & b) >> ~c, ~a | ~b | ~c)  #125 (line in Coconut source)
    assert (proves)(f >> (g >> h), ~f | ~g | h)  #126 (line in Coconut source)

# other theorems
    assert (proves)(t & (t >> d) | ~t & ~(t >> d), d)  #129 (line in Coconut source)
    assert (proves)((f >> g, c >> d), (f | c) >> (g | d))  #130 (line in Coconut source)
    assert (proves)((f >> g) >> h, f >> (g >> h))  #131 (line in Coconut source)
    assert (proves)(top, p >> (s >> p))  #132 (line in Coconut source)
    assert (proves)(~f | (f >> g), ~f | g)  #133 (line in Coconut source)
    assert (proves)((~f, g >> f), ~g)  #134 (line in Coconut source)
    assert (proves)((p >> s, r >> t, ~s | ~t), ~p | ~r)  #135 (line in Coconut source)
    assert (proves)(top, ~~(f | ~f))  #136 (line in Coconut source)
    assert (proves)(top, ~~(~~f >> f))  #137 (line in Coconut source)
    assert (proves)((p | r, ~p), r)  #138 (line in Coconut source)
    assert (proves)((f | g, ~f), g)  #139 (line in Coconut source)
    assert (proves)((t | ~a, ~a | ~t), ~a)  #140 (line in Coconut source)
    assert (proves)(top, ~~((~f >> bot) >> f))  #141 (line in Coconut source)
    assert (proves)((s & h | ~s & ~h) & ~(s & h) | (s & ~h | ~s & h) & (s & h), ~s & ~h)  #142 (line in Coconut source)
    assert (proves)(~a | ~b | ~c, (a & b) >> ~c)  #143 (line in Coconut source)
    assert (proves)(~p, p >> bot)  #144 (line in Coconut source)
    assert (proves)((a | b, ~a | c), b | c)  #145 (line in Coconut source)
    assert (proves)(top, (f & g) >> g)  #146 (line in Coconut source)
    assert (proves)((p >> s, r >> t, p | r), s | t)  #147 (line in Coconut source)
    assert (proves)(top, ~p >> (p >> s))  #148 (line in Coconut source)
    assert (proves)(f >> g, ((f & g) >> f) | (f >> (f & g)))  #149 (line in Coconut source)
    assert (proves)((f | ~f) >> g, ~~g)  #150 (line in Coconut source)
    assert (proves)(p >> r, p >> (p & r))  #151 (line in Coconut source)
    assert (proves)((s & h | ~s & ~h) & (h | s) | (s & ~h | ~s & h) & ~(h | s), s & h)  #152 (line in Coconut source)
    assert (proves)(~(f >> g), g >> f)  #153 (line in Coconut source)
    assert (proves)((f >> g) & (f >> h), f >> (g & h))  #154 (line in Coconut source)
    assert (proves)((s & h | ~s & ~h) & (~s & ~h) | (s & ~h | ~s & h) & ~(~s & ~h), ~(s & h))  #155 (line in Coconut source)
    assert (proves)(top, (p >> (s >> e)) >> ((p >> s) >> (p >> e)))  #156 (line in Coconut source)
    assert (proves)(top, p >> p)  #157 (line in Coconut source)
    assert (proves)(~f, ~(f & g))  #158 (line in Coconut source)
    assert (proves)(f >> ~f, ~f)  #159 (line in Coconut source)
    assert (proves)(f >> g, ~g >> ~f)  #160 (line in Coconut source)
    assert (f & g) >> f  #161 (line in Coconut source)
    assert (proves)((f >> (t & a | ~t & ~a), t & ~f | ~t & f, g >> (t & ~a | ~t & a), t & g | ~t & ~g), ~a)  #162 (line in Coconut source)
    assert (proves)(t & (~t & ~a) | ~t & ~(~t & ~a), a)  #163 (line in Coconut source)
    assert (proves)(~f | ~g | h, f >> (g >> h))  #164 (line in Coconut source)

# invalid theorems
    assert not (proves)(e >> (f >> g), (e >> f) >> g)  #167 (line in Coconut source)
    assert not (proves)((e & f) >> g, (e >> f) >> g)  #168 (line in Coconut source)
    assert not (proves)((e >> f) >> g, e & (f >> g))  #169 (line in Coconut source)
    assert not (proves)(e, e & f)  #170 (line in Coconut source)
    assert not (proves)(e | f, e & f)  #171 (line in Coconut source)
    assert not (proves)(e | top, e)  #172 (line in Coconut source)
    assert not (proves)(e, e & bot)  #173 (line in Coconut source)
    assert not (proves)(top, bot)  #174 (line in Coconut source)

# other tests
    assert And() == top  #177 (line in Coconut source)
    assert Or() == bot  #178 (line in Coconut source)
    assert (proves)((), top)  #179 (line in Coconut source)
    assert (proves)((a ^ b, a), ~b)  #180 (line in Coconut source)
    assert (proves_and_proved_by)(f >> (g >> h), (f & g) >> h)  #181 (line in Coconut source)
    assert (proves_and_proved_by)(bot, a & ~a)  #182 (line in Coconut source)
    assert (proves_and_proved_by)(top, a | ~a)  #183 (line in Coconut source)
    assert (simplify)(top & bot) == bot  #184 (line in Coconut source)
    assert simplify(a & a, b & b) == (a, b)  #185 (line in Coconut source)
    assert (simplest_form)(a ^ b) == (b | a) & (~a | ~b)  #186 (line in Coconut source)
    assert (simplest_form)((s & h | ~s & ~h) & ~(s & h) | (s & ~h | ~s & h) & (s & h)) == ~s & ~h  #187 (line in Coconut source)
    assert (simplify)((substitute)(a ^ b, _coconut.dict(((a, True), (b, False))))) == top  #188 (line in Coconut source)
    assert (simplify)((substitute)(a ^ b, _coconut.dict(((a, top), (b, top))))) == bot  #189 (line in Coconut source)
    assert e << f == f >> e  #190 (line in Coconut source)



def test_predicate_logic():  #193 (line in Coconut source)
    """Runs predicate logic tests."""  #194 (line in Coconut source)

# basic tests
    assert (simplify)(FA(x, F)) == F  #197 (line in Coconut source)
    assert (simplify)(TE(x, F)) == F  #198 (line in Coconut source)
    assert (simplify)(FA(x, F(x)) & G) == FA(y, F(y) & G)  #199 (line in Coconut source)
    assert (simplify)(FA(x, F(x)) | G) == FA(y, F(y) | G)  #200 (line in Coconut source)
    assert (simplify)(TE(x, F(x)) & G) == TE(y, F(y) & G)  #201 (line in Coconut source)
    assert (simplify)(TE(x, F(x)) | G) == TE(y, F(y) | G)  #202 (line in Coconut source)
    assert FA(x, F(f(x))) == FA(y, F(f(y)))  #203 (line in Coconut source)
    assert TE(x, F(f(x))) == TE(y, F(f(y)))  #204 (line in Coconut source)

# constructive theorems
    assert (proves)(TE(x, bot), bot)  #207 (line in Coconut source)
    assert (proves)(top, FA(x, top))  #208 (line in Coconut source)
    assert (proves)(FA(x, R(x) >> S(x)), FA(y, R(y)) >> FA(z, S(z)))  #209 (line in Coconut source)
    assert (proves)(FA(x, R(x) & S(x)), FA(y, R(y)) & FA(z, S(z)))  #210 (line in Coconut source)
    assert (proves)((FA(x, R(x) >> S(x)), TE(y, R(y))), TE(z, S(z)))  #211 (line in Coconut source)
    assert (proves)(TE(x, R(x) & S(x)), TE(y, R(y)) & TE(z, S(z)))  #212 (line in Coconut source)
    assert (proves)(TE(x, R(x)) | TE(y, S(y)), TE(z, R(z) | S(z)))  #213 (line in Coconut source)
    assert (proves)(TE(x, R(x) | S(x)), TE(y, R(y)) | TE(z, S(z)))  #214 (line in Coconut source)
    assert (proves)(FA(x, R(x)), ~TE(y, ~R(y)))  #215 (line in Coconut source)
    assert (proves)(TE(x, ~R(x)), ~FA(y, R(y)))  #216 (line in Coconut source)
    assert (proves)(FA(x, ~R(x)), ~TE(y, R(y)))  #217 (line in Coconut source)
    assert (proves)(~TE(x, R(x)), FA(y, ~R(y)))  #218 (line in Coconut source)
    assert (proves)(R(j), TE(x, R(x)))  #219 (line in Coconut source)

# classical theorems
    assert (proves)(~TE(x, ~R(x)), FA(y, R(y)))  #222 (line in Coconut source)
    assert (proves)(~FA(x, ~R(x)), TE(y, R(y)))  #223 (line in Coconut source)
    assert (proves)(~FA(x, R(x)), TE(y, ~R(y)))  #224 (line in Coconut source)
    assert (proves)(FA(x, ~~D(x)), FA(x, D(x)))  #225 (line in Coconut source)
    assert (proves)(~TE(x, R(x)), FA(y, ~R(y)))  #226 (line in Coconut source)
    assert (proves)(top, TE(x, D(x)) | FA(x, ~D(x)))  #227 (line in Coconut source)
    assert (proves)(top, TE(x, ~D(x)) | FA(x, D(x)))  #228 (line in Coconut source)
    assert (proves)(top, TE(x, D(x) >> FA(y, D(y))))  #229 (line in Coconut source)
    assert (proves)(TE(x, ~~D(x)), TE(x, D(x)))  #230 (line in Coconut source)
    assert (proves)(FA(x, C(x) | D(x)), FA(x, C(x)) | TE(x, D(x)))  #231 (line in Coconut source)

# other theorems
    assert (proves)(FA(x, H(j) >> T(x)), H(j) >> FA(x, T(x)))  #234 (line in Coconut source)
    assert (proves)(TE(x, R(x) >> B(x)), FA(x, R(x)) >> TE(x, B(x)))  #235 (line in Coconut source)
    assert (proves)(~FA(x, bot), TE(x, top))  #236 (line in Coconut source)
    assert (proves)(FA(x, TE(y, F(y) | G(x))), FA(x, G(x) | TE(x, F(x))))  #237 (line in Coconut source)
    assert (proves)((FA(x, FA(y, FA(z, (S(x, y) & S(y, z)) >> S(x, z)))), ~TE(x, S(x, x))), FA(x, FA(y, S(x, y) >> ~S(y, x))))  #238 (line in Coconut source)
    assert (proves)(FA(x, G(x)) | FA(x, B(x)), FA(x, G(x) | B(x)))  #239 (line in Coconut source)
    assert (proves)(TE(z, FA(k, P(z, k))), FA(y, TE(x, P(x, y))))  #240 (line in Coconut source)
    assert (proves)(TE(x, C(x) & B(x)), TE(x, B(x) & C(x)))  #241 (line in Coconut source)
    assert (proves)(TE(x, C(x, i) & B(x, j)), TE(x, C(x, i) >> B(x, j)))  #242 (line in Coconut source)
    assert (proves)(FA(x, C(x) & B(x)), FA(x, B(x) & C(x)))  #243 (line in Coconut source)
    assert (proves)(FA(x, C(x) & B(x)), FA(x, C(x)) & FA(x, B(x)))  #244 (line in Coconut source)
    assert (proves)(FA(x, bot), ~TE(x, top))  #245 (line in Coconut source)
    assert (proves)((~TE(x, G(x)) | FA(x, F(x)), C(j) >> FA(x, D(x))), FA(y, FA(z, ~G(z) | F(y) & C(j) >> D(y))))  #246 (line in Coconut source)
    assert (proves)(FA(x, G(x)) | TE(x, F(x)), FA(x, TE(y, F(y) | G(x))))  #247 (line in Coconut source)
    assert (proves)((P | TE(x, W)) >> FA(z, R), FA(z, FA(x, (P | W) >> R)))  #248 (line in Coconut source)
    assert (proves)((TE(x, ~F(x)), FA(x, F(x))), bot)  #249 (line in Coconut source)
    assert (proves)((FA(x, ~F(x)), FA(x, F(x))), FA(x, bot))  #250 (line in Coconut source)
    assert (proves)(TE(x, F(x)) | TE(x, G(x)), TE(x, TE(y, F(x) | G(y))))  #251 (line in Coconut source)
    assert (proves)(TE(x, FA(y, P(x, y))), FA(y, TE(x, P(x, y))))  #252 (line in Coconut source)
    assert (proves)(TE(x, FA(y, bot)), bot)  #253 (line in Coconut source)
    assert (proves)(top, FA(x, TE(y, top)))  #254 (line in Coconut source)
    assert (proves)(FA(x, TE(y, F(y)) | G(x)), FA(x, TE(y, F(y) | G(x))))  #255 (line in Coconut source)
    assert (proves)(TE(x, FA(y, F(y) & G(x))), TE(x, FA(y, F(y)) & G(x)))  #256 (line in Coconut source)
    assert (proves)(TE(x, ~R(x)), TE(y, R(y) >> (R(j) & R(k))))  #257 (line in Coconut source)
    assert (proves)(P(c), TE(x, P(x)))  #258 (line in Coconut source)
    assert (proves)(P(c), TE(x, top))  #259 (line in Coconut source)
    assert (proves)(P(c) & ~P(c), TE(x, top))  #260 (line in Coconut source)
    assert (proves)(P(c) | ~P(c), TE(x, top))  #261 (line in Coconut source)

# invalid theorems
    assert not (proves)(FA(x, R(x)) >> FA(y, S(y)), FA(z, R(z) >> S(z)))  #264 (line in Coconut source)
    assert not (proves)(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))  #265 (line in Coconut source)
    assert not (proves)(TE(x, R(x)), FA(y, R(y)))  #266 (line in Coconut source)

# non-empty universe theorems
    assert (proves)(top, TE(x, top))  #269 (line in Coconut source)
    assert (proves)(top, TE(x, D(x) >> FA(y, D(y))))  #270 (line in Coconut source)
    assert (proves)((R(j), FA(x, R(x) >> S(x))), S(j))  #271 (line in Coconut source)
    assert (proves)(FA(x, R(x)) >> FA(y, S(y)), TE(x, FA(y, ~R(x) | S(y))))  #272 (line in Coconut source)
    assert (proves)(FA(x, R(x)), TE(y, R(y)))  #273 (line in Coconut source)
    assert (proves)((T(i), FA(x, T(x) >> T(s(x)))), T(s(i)))  #274 (line in Coconut source)
    assert (proves)(top, TE(x, R(x) >> (R(j) & R(k))))  #275 (line in Coconut source)
    assert (proves)((FA(x, ~F(x)), FA(x, F(x))), bot)  #276 (line in Coconut source)

# equality theorems
    assert (proves)(top, Eq(a, a))  #279 (line in Coconut source)
    assert (proves)(Eq(a, b) & Eq(b, c), Eq(a, c))  #280 (line in Coconut source)
    assert (proves)(Eq(a, b) & Eq(b, c), Eq(c, a))  #281 (line in Coconut source)
    assert (proves)(Eq(a, b) & F(a), F(b))  #282 (line in Coconut source)
    assert (proves)((Eq(a, b) | Eq(a, c), F(a)), F(b) | F(c))  #283 (line in Coconut source)
    assert (proves)(FA(x, Eq(a, x)), Eq(a, b))  #284 (line in Coconut source)
    assert (proves)(Eq(a, b), Eq(b, a))  #285 (line in Coconut source)
    assert (proves)(Eq(a, b), Eq(f(a), f(b)))  #286 (line in Coconut source)


def test_empty_universe():  #288 (line in Coconut source)
    """Runs predicate logic tests in a potentially empty universe."""  #289 (line in Coconut source)

# basic tests
    assert (strict_simplify)(FA(x, F)) != F  #292 (line in Coconut source)
    assert (strict_simplify)(TE(x, F)) != F  #293 (line in Coconut source)
    assert (strict_simplify)(FA(x, F(x)) & G) != FA(y, F(y) & G)  #294 (line in Coconut source)
    assert (strict_simplify)(FA(x, F(x)) | G) == FA(y, F(y) | G)  #295 (line in Coconut source)
    assert (strict_simplify)(TE(x, F(x)) & G) == TE(y, F(y) & G)  #296 (line in Coconut source)
    assert (strict_simplify)(TE(x, F(x)) | G) != TE(y, F(y) | G)  #297 (line in Coconut source)

# constructive theorems
    assert (strict_proves)(TE(x, bot), bot)  #300 (line in Coconut source)
    assert (strict_proves)(top, FA(x, top))  #301 (line in Coconut source)
    assert (strict_proves)(FA(x, R(x) >> S(x)), FA(y, R(y)) >> FA(z, S(z)))  #302 (line in Coconut source)
    assert (strict_proves)(FA(x, R(x) & S(x)), FA(y, R(y)) & FA(z, S(z)))  #303 (line in Coconut source)
    assert (strict_proves)((FA(x, R(x) >> S(x)), TE(y, R(y))), TE(z, S(z)))  #304 (line in Coconut source)
    assert (strict_proves)(TE(x, R(x) & S(x)), TE(y, R(y)) & TE(z, S(z)))  #305 (line in Coconut source)
    assert (strict_proves)(TE(x, R(x)) | TE(y, S(y)), TE(z, R(z) | S(z)))  #306 (line in Coconut source)
    assert (strict_proves)(TE(x, R(x) | S(x)), TE(y, R(y)) | TE(z, S(z)))  #307 (line in Coconut source)
    assert (strict_proves)(FA(x, R(x)), ~TE(y, ~R(y)))  #308 (line in Coconut source)
    assert (strict_proves)(TE(x, ~R(x)), ~FA(y, R(y)))  #309 (line in Coconut source)
    assert (strict_proves)(FA(x, ~R(x)), ~TE(y, R(y)))  #310 (line in Coconut source)
    assert (strict_proves)(~TE(x, R(x)), FA(y, ~R(y)))  #311 (line in Coconut source)
    assert (strict_proves)(R(j), TE(x, R(x)))  #312 (line in Coconut source)

# classical theorems
    assert (strict_proves)(~TE(x, ~R(x)), FA(y, R(y)))  #315 (line in Coconut source)
    assert (strict_proves)(~FA(x, ~R(x)), TE(y, R(y)))  #316 (line in Coconut source)
    assert (strict_proves)(~FA(x, R(x)), TE(y, ~R(y)))  #317 (line in Coconut source)
    assert (strict_proves)(FA(x, ~~D(x)), FA(x, D(x)))  #318 (line in Coconut source)
    assert (strict_proves)(~TE(x, R(x)), FA(y, ~R(y)))  #319 (line in Coconut source)
    assert (strict_proves)(top, TE(x, D(x)) | FA(x, ~D(x)))  #320 (line in Coconut source)
    assert (strict_proves)(top, TE(x, ~D(x)) | FA(x, D(x)))  #321 (line in Coconut source)
    assert (strict_proves)(TE(x, top), TE(x, D(x) >> FA(y, D(y))))  #322 (line in Coconut source)
    assert (strict_proves)(TE(x, ~~D(x)), TE(x, D(x)))  #323 (line in Coconut source)
    assert (strict_proves)(FA(x, C(x) | D(x)), FA(x, C(x)) | TE(x, D(x)))  #324 (line in Coconut source)

# other theorems
    assert (strict_proves)(FA(x, H(j) >> T(x)), H(j) >> FA(x, T(x)))  #327 (line in Coconut source)
    assert (strict_proves)(TE(x, R(x) >> B(x)), FA(x, R(x)) >> TE(x, B(x)))  #328 (line in Coconut source)
    assert (strict_proves)(~FA(x, bot), TE(x, top))  #329 (line in Coconut source)
    assert (strict_proves)(FA(x, TE(y, F(y) | G(x))), FA(x, G(x) | TE(x, F(x))))  #330 (line in Coconut source)
    assert (strict_proves)((FA(x, FA(y, FA(z, (S(x, y) & S(y, z)) >> S(x, z)))), ~TE(x, S(x, x))), FA(x, FA(y, S(x, y) >> ~S(y, x))))  #331 (line in Coconut source)
    assert (strict_proves)(FA(x, G(x)) | FA(x, B(x)), FA(x, G(x) | B(x)))  #332 (line in Coconut source)
    assert (strict_proves)(TE(z, FA(k, P(z, k))), FA(y, TE(x, P(x, y))))  #333 (line in Coconut source)
    assert (strict_proves)(TE(x, C(x) & B(x)), TE(x, B(x) & C(x)))  #334 (line in Coconut source)
    assert (strict_proves)(TE(x, C(x, i) & B(x, j)), TE(x, C(x, i) >> B(x, j)))  #335 (line in Coconut source)
    assert (strict_proves)(FA(x, C(x) & B(x)), FA(x, B(x) & C(x)))  #336 (line in Coconut source)
    assert (strict_proves)(FA(x, C(x) & B(x)), FA(x, C(x)) & FA(x, B(x)))  #337 (line in Coconut source)
    assert (strict_proves)(FA(x, bot), ~TE(x, top))  #338 (line in Coconut source)
    assert (strict_proves)((~TE(x, G(x)) | FA(x, F(x)), C(j) >> FA(x, D(x))), FA(y, FA(z, ~G(z) | F(y) & C(j) >> D(y))))  #339 (line in Coconut source)
    assert (strict_proves)(FA(x, G(x)) | TE(x, F(x)), FA(x, TE(y, F(y) | G(x))))  #340 (line in Coconut source)
    assert (strict_proves)((P | TE(x, W)) >> FA(z, R), FA(z, FA(x, (P | W) >> R)))  #341 (line in Coconut source)
    assert (proves)(TE(x, F(x)) | TE(x, G(x)), TE(x, TE(y, F(x) | G(y))))  #342 (line in Coconut source)
    assert (proves)(TE(x, FA(y, P(x, y))), FA(y, TE(x, P(x, y))))  #343 (line in Coconut source)
    assert (proves)(TE(x, FA(y, bot)), bot)  #344 (line in Coconut source)
    assert (proves)(top, FA(x, TE(y, top)))  #345 (line in Coconut source)
    assert (proves)(FA(x, TE(y, F(y)) | G(x)), FA(x, TE(y, F(y) | G(x))))  #346 (line in Coconut source)
    assert (proves)(TE(x, FA(y, F(y) & G(x))), TE(x, FA(y, F(y)) & G(x)))  #347 (line in Coconut source)
    assert (strict_proves)(TE(x, ~R(x)), TE(y, R(y) >> (R(j) & R(k))))  #348 (line in Coconut source)
    assert (strict_proves)(P(c), TE(x, P(x)))  #349 (line in Coconut source)
    assert (strict_proves)(P(c), TE(x, top))  #350 (line in Coconut source)
    assert (strict_proves)(P(c) & ~P(c), TE(x, top))  #351 (line in Coconut source)
    assert (strict_proves)(P(c) | ~P(c), TE(x, top))  #352 (line in Coconut source)

# invalid theorems
    assert not (strict_proves)(FA(x, R(x)) >> FA(y, S(y)), FA(z, R(z) >> S(z)))  #355 (line in Coconut source)
    assert not (strict_proves)(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))  #356 (line in Coconut source)
    assert not (strict_proves)(TE(x, R(x)), FA(y, R(y)))  #357 (line in Coconut source)

# non-empty universe theorems
    assert not (strict_proves)(top, TE(x, top))  #360 (line in Coconut source)
    assert not (strict_proves)(top, TE(x, D(x) >> FA(y, D(y))))  #361 (line in Coconut source)
    assert (strict_proves)((R(j), FA(x, R(x) >> S(x))), S(j))  # j exists  #362 (line in Coconut source)
    assert not (strict_proves)(FA(x, R(x)) >> FA(y, S(y)), TE(x, FA(y, ~R(x) | S(y))))  #363 (line in Coconut source)
    assert not (strict_proves)(FA(x, R(x)), TE(y, R(y)))  #364 (line in Coconut source)
    assert (strict_proves)((T(i), FA(x, T(x) >> T(s(x)))), T(s(i)))  # i exists  #365 (line in Coconut source)
    assert (strict_proves)(top, TE(x, R(x) >> (R(j) & R(k))))  # j and k exist  #366 (line in Coconut source)
    assert not (strict_proves)(top, TE(x, R(x) >> FA(y, R(y))))  #367 (line in Coconut source)
    assert not (strict_proves)((FA(x, ~F(x)), FA(x, F(x))), bot)  #368 (line in Coconut source)

# equality theorems
    assert (strict_proves)(top, Eq(a, a))  #371 (line in Coconut source)
    assert (strict_proves)(Eq(a, b) & Eq(b, c), Eq(a, c))  #372 (line in Coconut source)
    assert (strict_proves)(Eq(a, b) & Eq(b, c), Eq(c, a))  #373 (line in Coconut source)
    assert (strict_proves)(Eq(a, b) & F(a), F(b))  #374 (line in Coconut source)
    assert (strict_proves)((Eq(a, b) | Eq(a, c), F(a)), F(b) | F(c))  #375 (line in Coconut source)
    assert (strict_proves)(FA(x, Eq(a, x)), Eq(a, b))  #376 (line in Coconut source)
    assert (strict_proves)(Eq(a, b), Eq(b, a))  #377 (line in Coconut source)
    assert (strict_proves)(Eq(a, b), Eq(f(a), f(b)))  #378 (line in Coconut source)


def test_parser():  #380 (line in Coconut source)
    """Tests math notation parsing."""  #381 (line in Coconut source)
    assert expr(r"A") == A  #382 (line in Coconut source)
    assert expr(r"F(x)") == F(x)  #383 (line in Coconut source)
    assert expr(r"F(f(x))") == F(f(x))  #384 (line in Coconut source)
    assert expr(r"A x. F(x)") == FA(x, F(x))  #385 (line in Coconut source)
    assert expr(r"A x. E y. F(x) \/ G(y)") == FA(x, TE(y, F(x) | G(y)))  #386 (line in Coconut source)
    assert expr(r"F(i) /\ A x. G(x)") == F(i) & FA(x, G(x))  #387 (line in Coconut source)
    assert expr(r"F -> G -> H") == F >> (G >> H)  #388 (line in Coconut source)
    assert expr(r"~F(x)") == ~F(x)  #389 (line in Coconut source)
    assert expr(r"-G(x) /\ F(x)") == ~G(x) & F(x)  #390 (line in Coconut source)
    assert expr(r"A /\ (B \/ C)") == A & (B | C)  #391 (line in Coconut source)
    assert expr(r"a = b") == Eq(a, b)  #392 (line in Coconut source)
    assert expr(r"forall x: A, B(x)") == FA(x, A(x) >> B(x))  #393 (line in Coconut source)
    assert expr(r"exists x: A, B(x)") == TE(x, A(x) & B(x))  #394 (line in Coconut source)
    assert expr(r"Q(x, x', x'')") == Q(Const("x"), Const("x'"), Const("x''"))  #395 (line in Coconut source)



def test_sort():  #398 (line in Coconut source)
    """Tests Sorting on predicates."""  #399 (line in Coconut source)
    assert (sorted)([expr("B"), expr("A")]) == [expr("A"), expr("B")]  #400 (line in Coconut source)



def test_regression():  #403 (line in Coconut source)
    """Test hard cases to avoid regressions."""  #404 (line in Coconut source)
    assert (proves)(expr("FA x, ~P(x, x)"), expr("~FA u, FA v, P(g(f(v)), g(u))"))  #405 (line in Coconut source)
    e1 = expr("∀z,∃x, ¬((Q(z)∧Q(x)))")  #406 (line in Coconut source)
    e2 = expr("∃z,∀x, ¬((Q(x)∧Q(z)))")  #407 (line in Coconut source)
    assert not (strict_proves)(e1, e2)  #408 (line in Coconut source)
    assert (strict_proves)(e2, e1)  #409 (line in Coconut source)
    e3 = expr("∃y,∃z,∀x, (Q(x,z)->Q(y,x))")  #410 (line in Coconut source)
    e4 = expr("∀y,∃x, ((R(x,z)∧R(x))->R(y))")  #411 (line in Coconut source)
    assert (strict_proves)(e3, e4)  #412 (line in Coconut source)
    assert not (strict_proves)(e4, e3)  #413 (line in Coconut source)
    assert expr("Q(?x) & P(?y)").find_unification(expr("Q(a) & P(b)")) == _coconut.dict(((Var("x"), Const("a")), (Var("y"), Const("b"))))  #414 (line in Coconut source)




def test_soundness():  #418 (line in Coconut source)
    """Tests that invalid inferences (which old versions accepted) are rejected."""  #419 (line in Coconut source)
    assert not (proves)(FA(x, P(x) | Q(x)), FA(x, P(x)) | FA(x, Q(x)))  #420 (line in Coconut source)
    assert (proves)(FA(x, P(x)) | FA(x, Q(x)), FA(x, P(x) | Q(x)))  #421 (line in Coconut source)
    assert not (proves)(TE(x, P(x)) & TE(x, Q(x)), TE(x, P(x) & Q(x)))  #422 (line in Coconut source)
    assert not (proves)(FA(x, TE(y, R(x, y))), TE(y, FA(x, R(x, y))))  #423 (line in Coconut source)
    assert (proves)(TE(y, FA(x, R(x, y))), FA(x, TE(y, R(x, y))))  #424 (line in Coconut source)
    assert not (proves)(Eq(a, b), P(a))  #425 (line in Coconut source)
    assert not (proves)((Eq(a, b), P(c)), P(a))  #426 (line in Coconut source)
    assert not (proves)(top, ~Eq(a, b))  #427 (line in Coconut source)
    assert not (proves)(top, Eq(a, b))  #428 (line in Coconut source)
    assert not (proves)(~Eq(a, b), Eq(a, b))  #429 (line in Coconut source)
    assert not (proves)(FA(x, P(x) >> P(f(x))), P(a))  #430 (line in Coconut source)
    assert not (proves)((P(a), FA(x, P(x) >> P(f(x)))), P(b))  #431 (line in Coconut source)



def test_issue_6():  #434 (line in Coconut source)
    """Tests the examples from https://github.com/evhub/pyprover/issues/6."""  #435 (line in Coconut source)
    three = TE(x, TE(y, TE(z, P(x) & P(y) & P(z) & ~Eq(x, y) & ~Eq(y, z))))  #436 (line in Coconut source)
    assert not (strict_proves)(P(a), three)  #437 (line in Coconut source)
    assert not (proves)(P(a), three)  #438 (line in Coconut source)
    assert not (proves)((P(a), P(b)), three)  #439 (line in Coconut source)
    assert (proves)((P(a), P(b), ~Eq(a, b)), three)  #440 (line in Coconut source)
    distinct3 = TE(x, TE(y, TE(z, P(x) & P(y) & P(z) & ~Eq(x, y) & ~Eq(y, z) & ~Eq(x, z))))  #441 (line in Coconut source)
    assert not (proves)((P(a), P(b), ~Eq(a, b)), distinct3)  #442 (line in Coconut source)
    assert (proves)((P(a), P(b), P(c), ~Eq(a, b), ~Eq(b, c), ~Eq(a, c)), distinct3)  #443 (line in Coconut source)
    result = prove((P(a), P(b)), three)  #444 (line in Coconut source)
    assert result.status == "disproved", _coconut_assert_msg('result.status == "disproved"', 'result.status', result.status)  #445 (line in Coconut source)
    assert result.countermodel is not None, _coconut_assert_msg('result.countermodel is not None', 'result.countermodel', result.countermodel)  #446 (line in Coconut source)



def test_equality():  #449 (line in Coconut source)
    """Tests reasoning about equality."""  #450 (line in Coconut source)
    assert (proves)(FA(x, Eq(f(f(x)), x)), FA(x, TE(y, Eq(f(y), x))))  #451 (line in Coconut source)
    assert (proves)((FA(x, Eq(f(x), g(x))), P(f(a))), P(g(a)))  #452 (line in Coconut source)
    assert (proves)((Eq(a, b), Eq(f(a), c)), Eq(f(b), c))  #453 (line in Coconut source)
    assert (proves)((Eq(a, b), FA(x, FA(y, P(x, y) >> Q(y)))), P(a, a) >> Q(b))  #454 (line in Coconut source)
    assert (proves)(FA(x, FA(y, Eq(x, y))), FA(x, P(x)) | FA(x, ~P(x)))  #455 (line in Coconut source)
    assert not (proves)(FA(x, TE(y, ~Eq(x, y))), bot)  #456 (line in Coconut source)
# group theory: a left identity that is also a right identity
    group = (FA(x, Eq(m(e, x), x)), FA(x, Eq(m(i(x), x), e)), FA(x, FA(y, FA(z, Eq(m(m(x, y), z), m(x, m(y, z)))))))  #458 (line in Coconut source)
    assert (proves)(group, FA(x, Eq(m(x, e), x)))  #463 (line in Coconut source)



def test_proofs():  #466 (line in Coconut source)
    """Tests proof objects."""  #467 (line in Coconut source)
    result = prove((FA(x, R(x) >> S(x)), R(j)), S(j))  #468 (line in Coconut source)
    assert result  #469 (line in Coconut source)
    assert result.status == "proved", _coconut_assert_msg('result.status == "proved"', 'result.status', result.status)  #470 (line in Coconut source)
    assert result.steps[-1].formula == bot, _coconut_assert_msg('result.steps[-1].formula == bot', 'result.steps[-1].formula', result.steps[-1].formula, 'bot', bot)  #471 (line in Coconut source)
    assert "premise 1" in str(result)  #472 (line in Coconut source)
    assert "negated conclusion" in result.tree()  #473 (line in Coconut source)
    assert result.to_dot().startswith("digraph")  #474 (line in Coconut source)
    assert str(result.steps[-1]).endswith("]")  #475 (line in Coconut source)
    assert prove(E >> F, F).status == "disproved"  #476 (line in Coconut source)
    assert not prove(E >> F, F)  #477 (line in Coconut source)
    assert strict_prove(top, TE(x, top)).status == "disproved"  #478 (line in Coconut source)
    assert "empty universe" in str(strict_prove(top, TE(x, top)))  #479 (line in Coconut source)
# an undecidable search gives up with "unknown" and a warning
    hard = (FA(x, P(x) >> P(f(x))), P(a))  #481 (line in Coconut source)
    assert prove(hard, P(b), timeout=0.2).status in ("unknown", "disproved")  #482 (line in Coconut source)
    with warnings.catch_warnings(record=True) as caught:  #483 (line in Coconut source)
        warnings.simplefilter("always")  #484 (line in Coconut source)
        assert not proves(FA(x, TE(y, R(x, y))), Eq(a, b), timeout=0.1, max_clauses=50)  #485 (line in Coconut source)
    assert all((issubclass(w.category, RuntimeWarning) for w in caught))  #486 (line in Coconut source)



def test_countermodels():  #489 (line in Coconut source)
    """Tests countermodel generation."""  #490 (line in Coconut source)
    model = countermodel(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))  #491 (line in Coconut source)
    assert model is not None, _coconut_assert_msg('model is not None', 'model', model)  #492 (line in Coconut source)
    assert len(model.domain) >= 2  #493 (line in Coconut source)
    assert "domain" in str(model)  #494 (line in Coconut source)
    assert countermodel(R(j), TE(x, R(x))) is None  #495 (line in Coconut source)



def test_tools():  #498 (line in Coconut source)
    """Tests miscellaneous tools."""  #499 (line in Coconut source)
    assert valid(TE(x, D(x) >> FA(y, D(y))))  #500 (line in Coconut source)
    assert not valid(A)  #501 (line in Coconut source)
    assert satisfiable(A & ~B)  #502 (line in Coconut source)
    assert not satisfiable(A & ~A)  #503 (line in Coconut source)
    assert solve(A & ~A) == bot  #504 (line in Coconut source)
    assert solve(A & (A >> B)) == A & B  #505 (line in Coconut source)
    assert (proves_and_proved_by)(Iff(A, B), (A >> B) & (B >> A))  #506 (line in Coconut source)
    assert proves(Iff(A, B), Iff(B, A))  #507 (line in Coconut source)
    assert proves((Iff(A, B), A), B)  #508 (line in Coconut source)
    assert unify(F(Var("x"), b), F(a, Var("y"))) == _coconut.dict(((Var("x"), a), (Var("y"), b)))  #509 (line in Coconut source)
    assert unify(F(Var("x")), F(f(Var("x")))) is None  #510 (line in Coconut source)
    assert nnf(~(A >> B)) == A & ~B  #511 (line in Coconut source)
    assert nnf(~FA(x, F(x))) == TE(x, ~F(x))  #512 (line in Coconut source)
    assert prenex(FA(x, F(x)) | TE(y, G(y))) == FA(x, TE(y, F(x) | G(y)))  #513 (line in Coconut source)
    assert cnf(A | (B & C)) == (A | B) & (A | C)  #514 (line in Coconut source)
    assert dnf(A & (B | C)) == (A & B) | (A & C)  #515 (line in Coconut source)
    assert simplify(FA(x, F(x)) & FA(y, G(y))) == FA(x, F(x) & G(x))  #516 (line in Coconut source)
    assert simplify(TE(x, F(x)) | TE(y, G(y))) == TE(x, F(x) | G(x))  #517 (line in Coconut source)
    assert skolemize(FA(x, TE(y, F(x, y)))) == F(Var("x"), Func("sk1", Var("x")))  #518 (line in Coconut source)
    assert substitute(FA(x, F(x, y)), _coconut.dict(((y, x),))) == FA(z, F(z, x))  #519 (line in Coconut source)
    assert (proves_and_proved_by)(A ^ B, (A | B) & ~(A & B))  #520 (line in Coconut source)



def test_formulas():  #523 (line in Coconut source)
    """Tests formula construction, comparison, and printing."""  #524 (line in Coconut source)
    assert A & B & C == And(A, B, C) == C & B & A  #525 (line in Coconut source)
    assert A | B | C == Or(A, B, C)  #526 (line in Coconut source)
    assert Imp(A, B, C) == A >> (B >> C)  #527 (line in Coconut source)
    assert FA(x, y, F(x, y)) == FA(x, FA(y, F(x, y)))  #528 (line in Coconut source)
    assert FA(x, F(x)) == FA(y, F(y))  #529 (line in Coconut source)
    assert FA(x, FA(y, F(x, y))) != FA(x, FA(y, F(y, x)))  #530 (line in Coconut source)
    assert hash(FA(x, F(x))) == hash(FA(y, F(y)))  #531 (line in Coconut source)
    assert Eq(a, b) == Eq(b, a)  #532 (line in Coconut source)
    assert len({A & B, B & A, FA(x, F(x)), FA(y, F(y))}) == 2  #533 (line in Coconut source)
    assert bool(top) and not bool(bot)  #534 (line in Coconut source)
    assert str(FA(x, F(x) >> G(x))) == "∀x, F(x) → G(x)"  #535 (line in Coconut source)
    assert str((A | B) & ~C) == "(A ∨ B) ∧ ¬C"  #536 (line in Coconut source)
    assert str(~Eq(a, b)) == "a ≠ b"  #537 (line in Coconut source)
    assert str(F(Var("x"))) == "F(?x)"  #538 (line in Coconut source)
    assert repr((A | B) & ~C) == "(A | B) & ~C"  #539 (line in Coconut source)
    assert repr(FA(x, F(x) >> Eq(x, a))) == "FA(x, F(x) >> Eq(x, a))"  #540 (line in Coconut source)
    assert repr(Prop("Foo")(Const("bar"))) == "Prop('Foo')(Const('bar'))"  #541 (line in Coconut source)
    use_ascii()  #542 (line in Coconut source)
    try:  #543 (line in Coconut source)
        assert str(FA(x, F(x) >> ~G(x))) == "FA x, F(x) -> ~G(x)"  #544 (line in Coconut source)
    finally:  #545 (line in Coconut source)
        use_unicode()  #546 (line in Coconut source)
    with pytest.raises(TypeError):  #547 (line in Coconut source)
        A & 1  #548 (line in Coconut source)
    with pytest.raises(TypeError):  #549 (line in Coconut source)
        F("x", 1)  #550 (line in Coconut source)



ROUND_TRIP = ["A ∧ B ∨ C", "A ∧ (B ∨ C)", "A → B → C", "(A → B) → C", "A ↔ B", "¬¬A", "∀x, ∃y, F(x, y) ∧ G(f(x), y)", "(∀x, F(x)) ∧ G", "A ∨ (∀x, F(x))", "a = b ∧ f(a) ≠ b", "P(?x) → Q(?x)", "⊤ ∧ ⊥"]  #553 (line in Coconut source)

@pytest.mark.parametrize("text", ROUND_TRIP)  #568 (line in Coconut source)
def test_round_trip(text):  #569 (line in Coconut source)
    """Tests that printing and parsing are inverses."""  #570 (line in Coconut source)
    formula = expr(text)  #571 (line in Coconut source)
    assert str(formula) == text  #572 (line in Coconut source)
    assert expr(str(formula)) == formula  #573 (line in Coconut source)
    use_ascii()  #574 (line in Coconut source)
    try:  #575 (line in Coconut source)
        assert expr(str(formula)) == formula  #576 (line in Coconut source)
    finally:  #577 (line in Coconut source)
        use_unicode()  #578 (line in Coconut source)



def test_parse_errors():  #581 (line in Coconut source)
    """Tests parse error reporting."""  #582 (line in Coconut source)
    for bad in ["A ∧", "(A", "A B", "F(x", "f(x)", "∀X, F(X)", "A ∧ $"]:  #583 (line in Coconut source)
        with pytest.raises(ParseError):  #584 (line in Coconut source)
            expr(bad)  #585 (line in Coconut source)
    with pytest.raises(ParseError, match="position 4"):  #586 (line in Coconut source)
        expr("A ∧ ∧ B")  #587 (line in Coconut source)



def test_parser_extras():  #590 (line in Coconut source)
    """Tests parser features beyond the basics."""  #591 (line in Coconut source)
    assert expr("A <-> B") == Iff(A, B)  #592 (line in Coconut source)
    assert expr("A x y. F(x, y)") == FA(x, FA(y, F(x, y)))  #593 (line in Coconut source)
    assert expr("forall x. exists y. F(x, y)") == FA(x, TE(y, F(x, y)))  #594 (line in Coconut source)
    assert expr("not A and B or C implies D") == ((~A & B) | C) >> D  #595 (line in Coconut source)
    assert expr("a != b") == ~Eq(a, b)  #596 (line in Coconut source)
    assert expr("E") == E  #597 (line in Coconut source)
    assert expr("A") == A  #598 (line in Coconut source)
    assert expr("E x. A(x)") == TE(x, A(x))  #599 (line in Coconut source)
    assert expr("F(i) /\\ A x. G(x)") == F(i) & FA(x, G(x))  #600 (line in Coconut source)
    assert expr("A x. F(x) -> G(x)") == FA(x, F(x) >> G(x))  #601 (line in Coconut source)
    assert expr("A ∨ ∀x, F(x)") == A | FA(x, F(x))  #602 (line in Coconut source)



def test_cli(capsys):  #605 (line in Coconut source)
    """Tests the command-line interface."""  #606 (line in Coconut source)
    assert main(["prove", "A x. F(x) -> G(x)", "F(a)", "G(a)"]) == 0  #607 (line in Coconut source)
    assert "Proved" in capsys.readouterr().out  #608 (line in Coconut source)
    assert main(["prove", "--tree", "A -> B", "B -> C", "A -> C"]) == 0  #609 (line in Coconut source)
    assert "⊥" in capsys.readouterr().out  #610 (line in Coconut source)
    assert main(["prove", "-q", "A -> B", "B"]) == 1  #611 (line in Coconut source)
    assert capsys.readouterr().out.strip() == "disproved"  #612 (line in Coconut source)
    assert main(["--ascii", "simplify", "(A -> B) /\\ A"]) == 0  #613 (line in Coconut source)
    assert capsys.readouterr().out.strip() == "A & B"  #614 (line in Coconut source)
    assert main(["cnf", "A | (B & C)"]) == 0  #615 (line in Coconut source)
    assert capsys.readouterr().out.strip() == "(A ∨ B) ∧ (A ∨ C)"  #616 (line in Coconut source)
    assert main(["prove", "A ∧"]) == 3  #617 (line in Coconut source)



def test_countermodels_are_genuine():  #620 (line in Coconut source)
    """Tests that every countermodel really satisfies the premises and falsifies the conclusion."""  #621 (line in Coconut source)
    problems = [(FA(x, P(x) | Q(x)), FA(x, P(x)) | FA(x, Q(x))), (TE(x, P(x)) & TE(x, Q(x)), TE(x, P(x) & Q(x))), (FA(x, TE(y, R(x, y))), TE(y, FA(x, R(x, y)))), ((P(a), FA(x, P(x) >> P(f(x)))), P(b)), ((P(a), P(b)), TE(x, TE(y, P(x) & P(y) & ~Eq(x, y)))), (FA(x, Eq(f(f(x)), x)), FA(x, Eq(f(x), x))), (expr("∀y,∃x, ((R(x,z)∧R(x))->R(y))"), expr("∃y,∃z,∀x, (Q(x,z)->Q(y,x))")), (FA(x, ~R(x, x)), FA(x, y, R(x, y) >> ~R(y, x)))]  #622 (line in Coconut source)
    for premise, conclusion in problems:  #632 (line in Coconut source)
        result = prove(premise, conclusion)  #633 (line in Coconut source)
        assert result.status == "disproved", (premise, conclusion)  #634 (line in Coconut source)
        model = result.countermodel  #635 (line in Coconut source)
        assert model is not None, _coconut_assert_msg('model is not None', 'model', model)  #636 (line in Coconut source)
        assert model.evaluate(premise if wff(premise) else And(*premise))  #637 (line in Coconut source)
        assert not model.evaluate(conclusion)  #638 (line in Coconut source)
# an irreflexive, transitive, serial relation only has infinite models
    infinite = FA(x, ~R(x, x)) & FA(x, y, z, (R(x, y) & R(y, z)) >> R(x, z)) & FA(x, TE(y, R(x, y)))  #640 (line in Coconut source)
    assert prove(infinite, bot, timeout=0.5).status == "unknown"  #641 (line in Coconut source)



def test_random_propositional():  #644 (line in Coconut source)
    """Tests the prover against truth tables on random propositional formulas."""  #645 (line in Coconut source)
    import random  #646 (line in Coconut source)
    from itertools import product  #647 (line in Coconut source)
    from pyprover.normal import satisfying_assignment  #648 (line in Coconut source)
    rng = random.Random(0)  #649 (line in Coconut source)
    atoms = [A, B, C, D]  #650 (line in Coconut source)
    def random_formula(depth):  #651 (line in Coconut source)
        if depth == 0 or rng.random() < 0.3:  #652 (line in Coconut source)
            return rng.choice(atoms + [top, bot])  #653 (line in Coconut source)
        _coconut_case_match_to_0 = rng.randrange(5)  #654 (line in Coconut source)
        _coconut_case_match_check_0 = False  #654 (line in Coconut source)
        if _coconut_case_match_to_0 == 0:  #654 (line in Coconut source)
            _coconut_case_match_check_0 = True  #654 (line in Coconut source)
        if _coconut_case_match_check_0:  #654 (line in Coconut source)
            return ~random_formula(depth - 1)  #656 (line in Coconut source)
        if not _coconut_case_match_check_0:  #657 (line in Coconut source)
            if _coconut_case_match_to_0 == 1:  #657 (line in Coconut source)
                _coconut_case_match_check_0 = True  #657 (line in Coconut source)
            if _coconut_case_match_check_0:  #657 (line in Coconut source)
                return random_formula(depth - 1) & random_formula(depth - 1)  #658 (line in Coconut source)
        if not _coconut_case_match_check_0:  #659 (line in Coconut source)
            if _coconut_case_match_to_0 == 2:  #659 (line in Coconut source)
                _coconut_case_match_check_0 = True  #659 (line in Coconut source)
            if _coconut_case_match_check_0:  #659 (line in Coconut source)
                return random_formula(depth - 1) | random_formula(depth - 1)  #660 (line in Coconut source)
        if not _coconut_case_match_check_0:  #661 (line in Coconut source)
            if _coconut_case_match_to_0 == 3:  #661 (line in Coconut source)
                _coconut_case_match_check_0 = True  #661 (line in Coconut source)
            if _coconut_case_match_check_0:  #661 (line in Coconut source)
                return random_formula(depth - 1) >> random_formula(depth - 1)  #662 (line in Coconut source)
        return Iff(random_formula(depth - 1), random_formula(depth - 1))  #663 (line in Coconut source)

    def truth(formula, values):  #664 (line in Coconut source)
        return (simplify)(substitute(formula, dict(zip(atoms, values)))) == top  #665 (line in Coconut source)

    for _ in range(150):  #666 (line in Coconut source)
        premise, conclusion = random_formula(3), random_formula(3)  #667 (line in Coconut source)
        expected = all((not truth(premise, values) or truth(conclusion, values) for values in product((True, False), repeat=len(atoms))))  #668 (line in Coconut source)
        assert proves(premise, conclusion) == expected, (premise, conclusion)  #672 (line in Coconut source)
        assert valid(Iff(simplify(premise), premise))  #673 (line in Coconut source)
        assert valid(Iff(cnf(premise), premise))  #674 (line in Coconut source)
        assert (satisfying_assignment(premise) is not None) == satisfiable(premise)  #675 (line in Coconut source)
