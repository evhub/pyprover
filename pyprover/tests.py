#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x1d3eec07

# Compiled with Coconut version 2.0.0-a_dev47 [How Not to Be Seen]

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
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Imports:

from pyprover.logic import FA  #3 (line num in coconut source)
from pyprover.logic import TE  #3 (line num in coconut source)
from pyprover.logic import top  #3 (line num in coconut source)
from pyprover.logic import bot  #3 (line num in coconut source)
from pyprover.logic import And  #3 (line num in coconut source)
from pyprover.logic import Or  #3 (line num in coconut source)
from pyprover.logic import Eq  #3 (line num in coconut source)
from pyprover.logic import Const  #3 (line num in coconut source)
from pyprover.logic import Var  #3 (line num in coconut source)
from pyprover.tools import proves  #14 (line num in coconut source)
from pyprover.tools import proves_and_proved_by  #14 (line num in coconut source)
from pyprover.tools import simplify  #14 (line num in coconut source)
from pyprover.tools import simplest_form  #14 (line num in coconut source)
from pyprover.tools import substitute  #14 (line num in coconut source)
from pyprover.tools import strict_simplify  #14 (line num in coconut source)
from pyprover.tools import strict_proves  #14 (line num in coconut source)
from pyprover.atoms import LowercasePropositions  #23 (line num in coconut source)
from pyprover.atoms import StandardMath  #23 (line num in coconut source)
from pyprover.parser import expr  #27 (line num in coconut source)


# Tests:

def test_propositional_logic():  #32 (line num in coconut source)
    """Runs propositional logic tests."""  #33 (line num in coconut source)
    with LowercasePropositions.use_in(globals()):  #34 (line num in coconut source)

# constructive theorems
        assert (proves)(e & f, e)  #37 (line num in coconut source)
        assert (proves)(e & f, f)  #38 (line num in coconut source)
        assert (proves)((e >> f, f >> g, e), g)  #39 (line num in coconut source)
        assert (proves)((e >> (f >> g), e >> f, e), g)  #40 (line num in coconut source)
        assert (proves)((e >> f, f >> g), e >> g)  #41 (line num in coconut source)
        assert (proves)(e >> (f >> g), f >> (e >> g))  #42 (line num in coconut source)
        assert (proves)(e >> (f >> g), (e >> f) >> (e >> g))  #43 (line num in coconut source)
        assert (proves)(e, f >> e)  #44 (line num in coconut source)
        assert (proves)(top, e >> (f >> e))  #45 (line num in coconut source)
        assert (proves)(e >> (f & g), (e >> f) & (e >> g))  #46 (line num in coconut source)
        assert (proves)(e >> (f >> g), (e & f) >> g)  #47 (line num in coconut source)
        assert (proves)((e & f) >> g, e >> (f >> g))  #48 (line num in coconut source)
        assert (proves)((e >> f) >> g, (e & f) >> g)  #49 (line num in coconut source)
        assert (proves)(e & (f >> g), (e >> f) >> g)  #50 (line num in coconut source)
        assert (proves)(e, e | f)  #51 (line num in coconut source)
        assert (proves)(f, e | f)  #52 (line num in coconut source)
        assert (proves)(e | f, f | e)  #53 (line num in coconut source)
        assert (proves)(f >> g, (e | f) >> (e | g))  #54 (line num in coconut source)
        assert (proves)(e, e | e)  #55 (line num in coconut source)
        assert (proves)(e, ~~e)  #56 (line num in coconut source)
        assert (proves)(~e, e >> f)  #57 (line num in coconut source)
        assert (proves)(e >> f, ~f >> ~e)  #58 (line num in coconut source)
        assert (proves)(e | f, ~(~e & ~f))  #59 (line num in coconut source)
        assert (proves)(e & f, ~(~e | ~f))  #60 (line num in coconut source)
        assert (proves)(~(e | f), ~e & ~f)  #61 (line num in coconut source)
        assert (proves)(~e & ~f, ~(e | f))  #62 (line num in coconut source)
        assert (proves)(~e | ~f, ~(e & f))  #63 (line num in coconut source)
        assert (proves)(top, ~(e & ~e))  #64 (line num in coconut source)
        assert (proves)(e & ~e, f)  #65 (line num in coconut source)
        assert (proves)(~f, f >> g)  #66 (line num in coconut source)
        assert (proves)((f >> g, ~f >> g), g)  #67 (line num in coconut source)
        assert (proves)(g, f >> g)  #68 (line num in coconut source)
        assert (proves)((f, ~(f & g)), ~g)  #69 (line num in coconut source)
        assert (proves)((p >> r, p >> ~r), ~p)  #70 (line num in coconut source)
        assert (proves)(top, (p >> ~p) >> ~p)  #71 (line num in coconut source)
        assert (proves)(bot, a)  #72 (line num in coconut source)
        assert (proves)(bot, top)  #73 (line num in coconut source)
        assert (proves)(a, top)  #74 (line num in coconut source)

# classical theorems
        assert (proves)(~~e, e)  #77 (line num in coconut source)
        assert (proves)(top, e | ~e)  #78 (line num in coconut source)
        assert (proves)(top, ((e >> f) >> e) >> e)  #79 (line num in coconut source)
        assert (proves)(~f >> ~e, e >> f)  #80 (line num in coconut source)
        assert (proves)(~(~e & ~f), e | f)  #81 (line num in coconut source)
        assert (proves)(~(~e | ~f), e & f)  #82 (line num in coconut source)
        assert (proves)(~(e & f), ~e | ~f)  #83 (line num in coconut source)
        assert (proves)(top, (e >> f) | (f >> e))  #84 (line num in coconut source)
        assert (proves)(top, (~~a | a) >> a)  #85 (line num in coconut source)
        assert (proves)(p >> r, (f >> r) | (p >> g))  #86 (line num in coconut source)
        assert (proves)(~(f >> g), f & ~g)  #87 (line num in coconut source)
        assert (proves)(top, (~f >> bot) >> f)  #88 (line num in coconut source)
        assert (proves)(f >> g, ~f | g)  #89 (line num in coconut source)
        assert (proves)(top, r & s | (~r | ~s))  #90 (line num in coconut source)
        assert (proves)(f >> g, g | ~f)  #91 (line num in coconut source)
        assert (proves)((a & b) >> ~c, ~a | ~b | ~c)  #92 (line num in coconut source)
        assert (proves)(f >> (g >> h), ~f | ~g | h)  #93 (line num in coconut source)

# other theorems
        assert (proves)(t & (t >> d) | ~t & ~(t >> d), d)  #96 (line num in coconut source)
        assert (proves)((f >> g, c >> d), (f | c) >> (g | d))  #97 (line num in coconut source)
        assert (proves)((f >> g) >> h, f >> (g >> h))  #98 (line num in coconut source)
        assert (proves)(top, p >> (s >> p))  #99 (line num in coconut source)
        assert (proves)(~f | (f >> g), ~f | g)  #100 (line num in coconut source)
        assert (proves)((~f, g >> f), ~g)  #101 (line num in coconut source)
        assert (proves)((p >> s, r >> t, ~s | ~t), ~p | ~r)  #102 (line num in coconut source)
        assert (proves)(top, ~~(f | ~f))  #103 (line num in coconut source)
        assert (proves)(top, ~~(~~f >> f))  #104 (line num in coconut source)
        assert (proves)((p | r, ~p), r)  #105 (line num in coconut source)
        assert (proves)((f | g, ~f), g)  #106 (line num in coconut source)
        assert (proves)((t | ~a, ~a | ~t), ~a)  #107 (line num in coconut source)
        assert (proves)(top, ~~((~f >> bot) >> f))  #108 (line num in coconut source)
        assert (proves)((s & h | ~s & ~h) & ~(s & h) | (s & ~h | ~s & h) & (s & h), ~s & ~h)  #109 (line num in coconut source)
        assert (proves)(~a | ~b | ~c, (a & b) >> ~c)  #110 (line num in coconut source)
        assert (proves)(~p, p >> bot)  #111 (line num in coconut source)
        assert (proves)((a | b, ~a | c), b | c)  #112 (line num in coconut source)
        assert (proves)(top, (f & g) >> g)  #113 (line num in coconut source)
        assert (proves)((p >> s, r >> t, p | r), s | t)  #114 (line num in coconut source)
        assert (proves)(top, ~p >> (p >> s))  #115 (line num in coconut source)
        assert (proves)(f >> g, ((f & g) >> f) | (f >> (f & g)))  #116 (line num in coconut source)
        assert (proves)((f | ~f) >> g, ~~g)  #117 (line num in coconut source)
        assert (proves)(p >> r, p >> (p & r))  #118 (line num in coconut source)
        assert (proves)((s & h | ~s & ~h) & (h | s) | (s & ~h | ~s & h) & ~(h | s), s & h)  #119 (line num in coconut source)
        assert (proves)(~(f >> g), g >> f)  #120 (line num in coconut source)
        assert (proves)((f >> g) & (f >> h), f >> (g & h))  #121 (line num in coconut source)
        assert (proves)((s & h | ~s & ~h) & (~s & ~h) | (s & ~h | ~s & h) & ~(~s & ~h), ~(s & h))  #122 (line num in coconut source)
        assert (proves)(top, (p >> (s >> e)) >> ((p >> s) >> (p >> e)))  #123 (line num in coconut source)
        assert (proves)(top, p >> p)  #124 (line num in coconut source)
        assert (proves)(~f, ~(f & g))  #125 (line num in coconut source)
        assert (proves)(f >> ~f, ~f)  #126 (line num in coconut source)
        assert (proves)(f >> g, ~g >> ~f)  #127 (line num in coconut source)
        assert (f & g) >> f  #128 (line num in coconut source)
        assert (proves)((f >> (t & a | ~t & ~a), t & ~f | ~t & f, g >> (t & ~a | ~t & a), t & g | ~t & ~g), ~a)  #129 (line num in coconut source)
        assert (proves)(t & (~t & ~a) | ~t & ~(~t & ~a), a)  #130 (line num in coconut source)
        assert (proves)(~f | ~g | h, f >> (g >> h))  #131 (line num in coconut source)

# invalid theorems
        assert not (proves)(e >> (f >> g), (e >> f) >> g)  #134 (line num in coconut source)
        assert not (proves)((e & f) >> g, (e >> f) >> g)  #135 (line num in coconut source)
        assert not (proves)((e >> f) >> g, e & (f >> g))  #136 (line num in coconut source)
        assert not (proves)(e, e & f)  #137 (line num in coconut source)
        assert not (proves)(e | f, e & f)  #138 (line num in coconut source)
        assert not (proves)(e | top, e)  #139 (line num in coconut source)
        assert not (proves)(e, e & bot)  #140 (line num in coconut source)
        assert not (proves)(top, bot)  #141 (line num in coconut source)

# other tests
        assert And() == top  #144 (line num in coconut source)
        assert Or() == bot  #145 (line num in coconut source)
        assert (proves)((), top)  #146 (line num in coconut source)
        assert (proves)((a ^ b, a), ~b)  #147 (line num in coconut source)
        assert (proves_and_proved_by)(f >> (g >> h), (f & g) >> h)  #148 (line num in coconut source)
        assert (proves_and_proved_by)(bot, a & ~a)  #149 (line num in coconut source)
        assert (proves_and_proved_by)(top, a | ~a)  #150 (line num in coconut source)
        assert (simplify)(top & bot) == bot  #151 (line num in coconut source)
        assert simplify(a & a, b & b) == (a, b)  #152 (line num in coconut source)
        assert (simplest_form)(a ^ b) == (b | a) & (~a | ~b)  #153 (line num in coconut source)
        assert (simplest_form)((s & h | ~s & ~h) & ~(s & h) | (s & ~h | ~s & h) & (s & h)) == ~s & ~h  #154 (line num in coconut source)
        assert (simplify)((substitute)(a ^ b, {a: True, b: False})) == top  #155 (line num in coconut source)
        assert (simplify)((substitute)(a ^ b, {a: top, b: top})) == bot  #156 (line num in coconut source)
        assert e << f == f >> e  #157 (line num in coconut source)



def test_predicate_logic():  #160 (line num in coconut source)
    """Runs predicate logic tests."""  #161 (line num in coconut source)
    with StandardMath.use_in(globals()):  #162 (line num in coconut source)

# basic tests
        assert (simplify)(FA(x, F)) == F  #165 (line num in coconut source)
        assert (simplify)(TE(x, F)) == F  #166 (line num in coconut source)
        assert (simplify)(FA(x, F(x)) & G) == FA(y, F(y) & G)  #167 (line num in coconut source)
        assert (simplify)(FA(x, F(x)) | G) == FA(y, F(y) | G)  #168 (line num in coconut source)
        assert (simplify)(TE(x, F(x)) & G) == TE(y, F(y) & G)  #169 (line num in coconut source)
        assert (simplify)(TE(x, F(x)) | G) == TE(y, F(y) | G)  #170 (line num in coconut source)
        assert FA(x, F(f(x))) == FA(y, F(f(y)))  #171 (line num in coconut source)
        assert TE(x, F(f(x))) == TE(y, F(f(y)))  #172 (line num in coconut source)
        assert TE(f, F(f(x))) == TE(g, F(g(x)))  #173 (line num in coconut source)

# constructive theorems
        assert (proves)(TE(x, bot), bot)  #176 (line num in coconut source)
        assert (proves)(top, FA(x, top))  #177 (line num in coconut source)
        assert (proves)(FA(x, R(x) >> S(x)), FA(y, R(y)) >> FA(z, S(z)))  #178 (line num in coconut source)
        assert (proves)(FA(x, R(x) & S(x)), FA(y, R(y)) & FA(z, S(z)))  #179 (line num in coconut source)
        assert (proves)((FA(x, R(x) >> S(x)), TE(y, R(y))), TE(z, S(z)))  #180 (line num in coconut source)
        assert (proves)(TE(x, R(x) & S(x)), TE(y, R(y)) & TE(z, S(z)))  #181 (line num in coconut source)
        assert (proves)(TE(x, R(x)) | TE(y, S(y)), TE(z, R(z) | S(z)))  #182 (line num in coconut source)
        assert (proves)(TE(x, R(x) | S(x)), TE(y, R(y)) | TE(z, S(z)))  #183 (line num in coconut source)
        assert (proves)(FA(x, R(x)), ~TE(y, ~R(y)))  #184 (line num in coconut source)
        assert (proves)(TE(x, ~R(x)), ~FA(y, R(y)))  #185 (line num in coconut source)
        assert (proves)(FA(x, ~R(x)), ~TE(y, R(y)))  #186 (line num in coconut source)
        assert (proves)(~TE(x, R(x)), FA(y, ~R(y)))  #187 (line num in coconut source)
        assert (proves)(R(j), TE(x, R(x)))  #188 (line num in coconut source)

# classical theorems
        assert (proves)(~TE(x, ~R(x)), FA(y, R(y)))  #191 (line num in coconut source)
        assert (proves)(~FA(x, ~R(x)), TE(y, R(y)))  #192 (line num in coconut source)
        assert (proves)(~FA(x, R(x)), TE(y, ~R(y)))  #193 (line num in coconut source)
        assert (proves)(FA(x, ~~D(x)), FA(x, D(x)))  #194 (line num in coconut source)
        assert (proves)(~TE(x, R(x)), FA(y, ~R(y)))  #195 (line num in coconut source)
        assert (proves)(top, TE(x, D(x)) | FA(x, ~D(x)))  #196 (line num in coconut source)
        assert (proves)(top, TE(x, ~D(x)) | FA(x, D(x)))  #197 (line num in coconut source)
        assert (proves)(top, TE(x, D(x) >> FA(y, D(y))))  #198 (line num in coconut source)
        assert (proves)(TE(x, ~~D(x)), TE(x, D(x)))  #199 (line num in coconut source)
        assert (proves)(FA(x, C(x) | D(x)), FA(x, C(x)) | TE(x, D(x)))  #200 (line num in coconut source)

# other theorems
        assert (proves)(FA(x, H(j) >> T(x)), H(j) >> FA(x, T(x)))  #203 (line num in coconut source)
        assert (proves)(TE(x, R(x) >> B(x)), FA(x, R(x)) >> TE(x, B(x)))  #204 (line num in coconut source)
        assert (proves)(~FA(x, bot), TE(x, top))  #205 (line num in coconut source)
        assert (proves)(FA(x, TE(y, F(y) | G(x))), FA(x, G(x) | TE(x, F(x))))  #206 (line num in coconut source)
        assert (proves)((FA(x, FA(y, FA(z, (S(x, y) & S(y, z)) >> S(x, z)))), ~TE(x, S(x, x))), FA(x, FA(y, S(x, y) >> ~S(y, x))))  #207 (line num in coconut source)
        assert (proves)(FA(x, G(x)) | FA(x, B(x)), FA(x, G(x) | B(x)))  #208 (line num in coconut source)
        assert (proves)(TE(z, FA(k, P(z, k))), FA(y, TE(x, P(x, y))))  #209 (line num in coconut source)
        assert (proves)(TE(x, C(x) & B(x)), TE(x, B(x) & C(x)))  #210 (line num in coconut source)
        assert (proves)(TE(x, C(x, i) & B(x, j)), TE(x, C(x, i) >> B(x, j)))  #211 (line num in coconut source)
        assert (proves)(FA(x, C(x) & B(x)), FA(x, B(x) & C(x)))  #212 (line num in coconut source)
        assert (proves)(FA(x, C(x) & B(x)), FA(x, C(x)) & FA(x, B(x)))  #213 (line num in coconut source)
        assert (proves)(FA(x, bot), ~TE(x, top))  #214 (line num in coconut source)
        assert (proves)((~TE(x, G(x)) | FA(x, F(x)), C(j) >> FA(x, D(x))), FA(y, FA(z, ~G(z) | F(y) & C(j) >> D(y))))  #215 (line num in coconut source)
        assert (proves)(FA(x, G(x)) | TE(x, F(x)), FA(x, TE(y, F(y) | G(x))))  #216 (line num in coconut source)
        assert (proves)((P | TE(x, W)) >> FA(z, R), FA(z, FA(x, (P | W) >> R)))  #217 (line num in coconut source)
        assert (proves)((TE(x, ~F(x)), FA(x, F(x))), bot)  #218 (line num in coconut source)
        assert (proves)((FA(x, ~F(x)), FA(x, F(x))), FA(x, bot))  #219 (line num in coconut source)
        assert (proves)(TE(x, F(x)) | TE(x, G(x)), TE(x, TE(y, F(x) | G(y))))  #220 (line num in coconut source)
        assert (proves)(TE(x, FA(y, P(x, y))), FA(y, TE(x, P(x, y))))  #221 (line num in coconut source)
        assert (proves)(TE(x, FA(y, bot)), bot)  #222 (line num in coconut source)
        assert (proves)(top, FA(x, TE(y, top)))  #223 (line num in coconut source)
        assert (proves)(FA(x, TE(y, F(y)) | G(x)), FA(x, TE(y, F(y) | G(x))))  #224 (line num in coconut source)
        assert (proves)(TE(x, FA(y, F(y) & G(x))), TE(x, FA(y, F(y)) & G(x)))  #225 (line num in coconut source)
        assert (proves)(TE(x, ~R(x)), TE(y, R(y) >> (R(j) & R(k))))  #226 (line num in coconut source)
        assert (proves)(P(c), TE(x, P(x)))  #227 (line num in coconut source)
        assert (proves)(P(c), TE(x, top))  #228 (line num in coconut source)
        assert (proves)(P(c) & ~P(c), TE(x, top))  #229 (line num in coconut source)
        assert (proves)(P(c) | ~P(c), TE(x, top))  #230 (line num in coconut source)

# invalid theorems
        assert not (proves)(FA(x, R(x)) >> FA(y, S(y)), FA(z, R(z) >> S(z)))  #233 (line num in coconut source)
        assert not (proves)(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))  #234 (line num in coconut source)
        assert not (proves)(TE(x, R(x)), FA(y, R(y)))  #235 (line num in coconut source)

# non-empty universe theorems
        assert (proves)(top, TE(x, top))  #238 (line num in coconut source)
        assert (proves)(top, TE(x, D(x) >> FA(y, D(y))))  #239 (line num in coconut source)
        assert (proves)((R(j), FA(x, R(x) >> S(x))), S(j))  #240 (line num in coconut source)
        assert (proves)(FA(x, R(x)) >> FA(y, S(y)), TE(x, FA(y, ~R(x) | S(y))))  #241 (line num in coconut source)
        assert (proves)(FA(x, R(x)), TE(y, R(y)))  #242 (line num in coconut source)
        assert (proves)((T(i), FA(x, T(x) >> T(s(x)))), T(s(i)))  #243 (line num in coconut source)
        assert (proves)(top, TE(x, R(x) >> (R(j) & R(k))))  #244 (line num in coconut source)
        assert (proves)((FA(x, ~F(x)), FA(x, F(x))), bot)  #245 (line num in coconut source)

# equality theorems
        assert (proves)(top, Eq(a, a))  #248 (line num in coconut source)
        assert (proves)(Eq(a, b) & Eq(b, c), Eq(a, c))  #249 (line num in coconut source)
        assert (proves)(Eq(a, b) & Eq(b, c), Eq(c, a))  #250 (line num in coconut source)
        assert (proves)(Eq(a, b) & F(a), F(b))  #251 (line num in coconut source)
        assert (proves)((Eq(a, b) | Eq(a, c), F(a)), F(b) | F(c))  #252 (line num in coconut source)
        assert (proves)(FA(x, Eq(a, x)), Eq(a, b))  #253 (line num in coconut source)
        assert (proves)(Eq(a, b), Eq(b, a))  #254 (line num in coconut source)
        assert (proves)(Eq(a, b), Eq(f(a), f(b)))  #255 (line num in coconut source)


def test_empty_universe():  #257 (line num in coconut source)
    """Runs predicate logic tests in a potentially empty universe."""  #258 (line num in coconut source)
    with StandardMath.use_in(globals()):  #259 (line num in coconut source)

# basic tests
        assert (strict_simplify)(FA(x, F)) != F  #262 (line num in coconut source)
        assert (strict_simplify)(TE(x, F)) != F  #263 (line num in coconut source)
        assert (strict_simplify)(FA(x, F(x)) & G) != FA(y, F(y) & G)  #264 (line num in coconut source)
        assert (strict_simplify)(FA(x, F(x)) | G) == FA(y, F(y) | G)  #265 (line num in coconut source)
        assert (strict_simplify)(TE(x, F(x)) & G) == TE(y, F(y) & G)  #266 (line num in coconut source)
        assert (strict_simplify)(TE(x, F(x)) | G) != TE(y, F(y) | G)  #267 (line num in coconut source)

# constructive theorems
        assert (strict_proves)(TE(x, bot), bot)  #270 (line num in coconut source)
        assert (strict_proves)(top, FA(x, top))  #271 (line num in coconut source)
        assert (strict_proves)(FA(x, R(x) >> S(x)), FA(y, R(y)) >> FA(z, S(z)))  #272 (line num in coconut source)
        assert (strict_proves)(FA(x, R(x) & S(x)), FA(y, R(y)) & FA(z, S(z)))  #273 (line num in coconut source)
        assert (strict_proves)((FA(x, R(x) >> S(x)), TE(y, R(y))), TE(z, S(z)))  #274 (line num in coconut source)
        assert (strict_proves)(TE(x, R(x) & S(x)), TE(y, R(y)) & TE(z, S(z)))  #275 (line num in coconut source)
        assert (strict_proves)(TE(x, R(x)) | TE(y, S(y)), TE(z, R(z) | S(z)))  #276 (line num in coconut source)
        assert (strict_proves)(TE(x, R(x) | S(x)), TE(y, R(y)) | TE(z, S(z)))  #277 (line num in coconut source)
        assert (strict_proves)(FA(x, R(x)), ~TE(y, ~R(y)))  #278 (line num in coconut source)
        assert (strict_proves)(TE(x, ~R(x)), ~FA(y, R(y)))  #279 (line num in coconut source)
        assert (strict_proves)(FA(x, ~R(x)), ~TE(y, R(y)))  #280 (line num in coconut source)
        assert (strict_proves)(~TE(x, R(x)), FA(y, ~R(y)))  #281 (line num in coconut source)
        assert (strict_proves)(R(j), TE(x, R(x)))  #282 (line num in coconut source)

# classical theorems
        assert (strict_proves)(~TE(x, ~R(x)), FA(y, R(y)))  #285 (line num in coconut source)
        assert (strict_proves)(~FA(x, ~R(x)), TE(y, R(y)))  #286 (line num in coconut source)
        assert (strict_proves)(~FA(x, R(x)), TE(y, ~R(y)))  #287 (line num in coconut source)
        assert (strict_proves)(FA(x, ~~D(x)), FA(x, D(x)))  #288 (line num in coconut source)
        assert (strict_proves)(~TE(x, R(x)), FA(y, ~R(y)))  #289 (line num in coconut source)
        assert (strict_proves)(top, TE(x, D(x)) | FA(x, ~D(x)))  #290 (line num in coconut source)
        assert (strict_proves)(top, TE(x, ~D(x)) | FA(x, D(x)))  #291 (line num in coconut source)
        assert (strict_proves)(TE(x, top), TE(x, D(x) >> FA(y, D(y))))  #292 (line num in coconut source)
        assert (strict_proves)(TE(x, ~~D(x)), TE(x, D(x)))  #293 (line num in coconut source)
        assert (strict_proves)(FA(x, C(x) | D(x)), FA(x, C(x)) | TE(x, D(x)))  #294 (line num in coconut source)

# other theorems
        assert (strict_proves)(FA(x, H(j) >> T(x)), H(j) >> FA(x, T(x)))  #297 (line num in coconut source)
        assert (strict_proves)(TE(x, R(x) >> B(x)), FA(x, R(x)) >> TE(x, B(x)))  #298 (line num in coconut source)
        assert (strict_proves)(~FA(x, bot), TE(x, top))  #299 (line num in coconut source)
        assert (strict_proves)(FA(x, TE(y, F(y) | G(x))), FA(x, G(x) | TE(x, F(x))))  #300 (line num in coconut source)
        assert (strict_proves)((FA(x, FA(y, FA(z, (S(x, y) & S(y, z)) >> S(x, z)))), ~TE(x, S(x, x))), FA(x, FA(y, S(x, y) >> ~S(y, x))))  #301 (line num in coconut source)
        assert (strict_proves)(FA(x, G(x)) | FA(x, B(x)), FA(x, G(x) | B(x)))  #302 (line num in coconut source)
        assert (strict_proves)(TE(z, FA(k, P(z, k))), FA(y, TE(x, P(x, y))))  #303 (line num in coconut source)
        assert (strict_proves)(TE(x, C(x) & B(x)), TE(x, B(x) & C(x)))  #304 (line num in coconut source)
        assert (strict_proves)(TE(x, C(x, i) & B(x, j)), TE(x, C(x, i) >> B(x, j)))  #305 (line num in coconut source)
        assert (strict_proves)(FA(x, C(x) & B(x)), FA(x, B(x) & C(x)))  #306 (line num in coconut source)
        assert (strict_proves)(FA(x, C(x) & B(x)), FA(x, C(x)) & FA(x, B(x)))  #307 (line num in coconut source)
        assert (strict_proves)(FA(x, bot), ~TE(x, top))  #308 (line num in coconut source)
        assert (strict_proves)((~TE(x, G(x)) | FA(x, F(x)), C(j) >> FA(x, D(x))), FA(y, FA(z, ~G(z) | F(y) & C(j) >> D(y))))  #309 (line num in coconut source)
        assert (strict_proves)(FA(x, G(x)) | TE(x, F(x)), FA(x, TE(y, F(y) | G(x))))  #310 (line num in coconut source)
        assert (strict_proves)((P | TE(x, W)) >> FA(z, R), FA(z, FA(x, (P | W) >> R)))  #311 (line num in coconut source)
        assert (proves)(TE(x, F(x)) | TE(x, G(x)), TE(x, TE(y, F(x) | G(y))))  #312 (line num in coconut source)
        assert (proves)(TE(x, FA(y, P(x, y))), FA(y, TE(x, P(x, y))))  #313 (line num in coconut source)
        assert (proves)(TE(x, FA(y, bot)), bot)  #314 (line num in coconut source)
        assert (proves)(top, FA(x, TE(y, top)))  #315 (line num in coconut source)
        assert (proves)(FA(x, TE(y, F(y)) | G(x)), FA(x, TE(y, F(y) | G(x))))  #316 (line num in coconut source)
        assert (proves)(TE(x, FA(y, F(y) & G(x))), TE(x, FA(y, F(y)) & G(x)))  #317 (line num in coconut source)
        assert (strict_proves)(TE(x, ~R(x)), TE(y, R(y) >> (R(j) & R(k))))  #318 (line num in coconut source)
        assert (strict_proves)(P(c), TE(x, P(x)))  #319 (line num in coconut source)
        assert (strict_proves)(P(c), TE(x, top))  #320 (line num in coconut source)
        assert (strict_proves)(P(c) & ~P(c), TE(x, top))  #321 (line num in coconut source)
        assert (strict_proves)(P(c) | ~P(c), TE(x, top))  #322 (line num in coconut source)

# invalid theorems
        assert not (strict_proves)(FA(x, R(x)) >> FA(y, S(y)), FA(z, R(z) >> S(z)))  #325 (line num in coconut source)
        assert not (strict_proves)(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))  #326 (line num in coconut source)
        assert not (strict_proves)(TE(x, R(x)), FA(y, R(y)))  #327 (line num in coconut source)

# non-empty universe theorems
        assert not (strict_proves)(top, TE(x, top))  #330 (line num in coconut source)
        assert not (strict_proves)(top, TE(x, D(x) >> FA(y, D(y))))  #331 (line num in coconut source)
        assert not (strict_proves)((R(j), FA(x, R(x) >> S(x))), S(j))  #332 (line num in coconut source)
        assert not (strict_proves)(FA(x, R(x)) >> FA(y, S(y)), TE(x, FA(y, ~R(x) | S(y))))  #333 (line num in coconut source)
        assert not (strict_proves)(FA(x, R(x)), TE(y, R(y)))  #334 (line num in coconut source)
        assert not (strict_proves)((T(i), FA(x, T(x) >> T(s(x)))), T(s(i)))  #335 (line num in coconut source)
        assert not (strict_proves)(top, TE(x, R(x) >> (R(j) & R(k))))  #336 (line num in coconut source)
        assert not (strict_proves)((FA(x, ~F(x)), FA(x, F(x))), bot)  #337 (line num in coconut source)

# equality theorems
        assert (strict_proves)(top, Eq(a, a))  #340 (line num in coconut source)
        assert (strict_proves)(Eq(a, b) & Eq(b, c), Eq(a, c))  #341 (line num in coconut source)
        assert (strict_proves)(Eq(a, b) & Eq(b, c), Eq(c, a))  #342 (line num in coconut source)
        assert (strict_proves)(Eq(a, b) & F(a), F(b))  #343 (line num in coconut source)
        assert (strict_proves)((Eq(a, b) | Eq(a, c), F(a)), F(b) | F(c))  #344 (line num in coconut source)
        assert (strict_proves)(FA(x, Eq(a, x)), Eq(a, b))  #345 (line num in coconut source)
        assert (strict_proves)(Eq(a, b), Eq(b, a))  #346 (line num in coconut source)
        assert (strict_proves)(Eq(a, b), Eq(f(a), f(b)))  #347 (line num in coconut source)


def test_parser():  #349 (line num in coconut source)
    """Tests math notation parsing."""  #350 (line num in coconut source)
    with StandardMath.use_in(globals()):  #351 (line num in coconut source)
        assert expr(r"A") == A  #352 (line num in coconut source)
        assert expr(r"F(x)") == F(x)  #353 (line num in coconut source)
        assert expr(r"F(f(x))") == F(f(x))  #354 (line num in coconut source)
        assert expr(r"A x. F(x)") == FA(x, F(x))  #355 (line num in coconut source)
        assert expr(r"A x. E y. F(x) \/ G(y)") == FA(x, TE(y, F(x) | G(y)))  #356 (line num in coconut source)
        assert expr(r"F(i) /\ A x. G(x)") == F(i) & FA(x, G(x))  #357 (line num in coconut source)
        assert expr(r"F -> G -> H") == F >> (G >> H)  #358 (line num in coconut source)
        assert expr(r"~F(x)") == ~F(x)  #359 (line num in coconut source)
        assert expr(r"-G(x) /\ F(x)") == ~G(x) & F(x)  #360 (line num in coconut source)
        assert expr(r"A /\ (B \/ C)") == A & (B | C)  #361 (line num in coconut source)
        assert expr(r"a = b") == Eq(a, b)  #362 (line num in coconut source)
        assert expr(r"forall x: A, B(x)") == FA(x, A(x) >> B(x))  #363 (line num in coconut source)
        assert expr(r"exists x: A, B(x)") == TE(x, A(x) & B(x))  #364 (line num in coconut source)
        assert expr(r"Q(x, x', x'')") == Q(x, Const("x'"), Const("x''"))  #365 (line num in coconut source)



def test_sort():  #368 (line num in coconut source)
    """Tests Sorting on predicates."""  #369 (line num in coconut source)
    assert (sorted)([expr("B"), expr("A")]) == [expr("A"), expr("B")]  #370 (line num in coconut source)



def test_regression():  #373 (line num in coconut source)
    """Test hard cases to avoid regressions."""  #374 (line num in coconut source)
    assert (proves)(expr("FA x, ~P(x, x)"), expr("~FA u, FA v, P(g(f(v)), g(u))"))  #375 (line num in coconut source)
    e1 = expr("∀z,∃x, ¬((Q(z)∧Q(x)))")  #376 (line num in coconut source)
    e2 = expr("∃z,∀x, ¬((Q(x)∧Q(z)))")  #377 (line num in coconut source)
    assert not (strict_proves)(e1, e2)  #378 (line num in coconut source)
    assert (strict_proves)(e2, e1)  #379 (line num in coconut source)
    e3 = expr("∃y,∃z,∀x, (Q(x,z)->Q(y,x))")  #380 (line num in coconut source)
    e4 = expr("∀y,∃x, ((R(x,z)∧R(x))->R(y))")  #381 (line num in coconut source)
    assert (strict_proves)(e3, e4)  #382 (line num in coconut source)
    assert not (strict_proves)(e4, e3)  #383 (line num in coconut source)
    assert expr("Q(?x) & P(?y)").find_unification(expr("Q(a) & P(b)")) == {Var("x"): Const("a"), Var("y"): Const("b")}  #384 (line num in coconut source)



if __name__ == "__main__":  #387 (line num in coconut source)
    test_propositional_logic()  #388 (line num in coconut source)
    test_predicate_logic()  #389 (line num in coconut source)
    test_empty_universe()  #390 (line num in coconut source)
    test_parser()  #391 (line num in coconut source)
    test_sort()  #392 (line num in coconut source)
    test_regression()  #393 (line num in coconut source)
    print("<success>")  #394 (line num in coconut source)
