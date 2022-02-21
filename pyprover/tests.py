#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x49ab9f7d

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

from pyprover.logic import FA  #3 (line num in coconut source)
from pyprover.logic import TE  #3 (line num in coconut source)
from pyprover.logic import top  #3 (line num in coconut source)
from pyprover.logic import bot  #3 (line num in coconut source)
from pyprover.logic import And  #3 (line num in coconut source)
from pyprover.logic import Or  #3 (line num in coconut source)
from pyprover.logic import Eq  #3 (line num in coconut source)
from pyprover.logic import Const  #3 (line num in coconut source)
from pyprover.tools import proves  #13 (line num in coconut source)
from pyprover.tools import proves_and_proved_by  #13 (line num in coconut source)
from pyprover.tools import simplify  #13 (line num in coconut source)
from pyprover.tools import simplest_form  #13 (line num in coconut source)
from pyprover.tools import substitute  #13 (line num in coconut source)
from pyprover.tools import strict_simplify  #13 (line num in coconut source)
from pyprover.tools import strict_proves  #13 (line num in coconut source)
from pyprover.atoms import LowercasePropositions  #22 (line num in coconut source)
from pyprover.atoms import StandardMath  #22 (line num in coconut source)
from pyprover.parser import expr  #26 (line num in coconut source)


# Tests:

def test_propositional_logic():  #31 (line num in coconut source)
    """Runs propositional logic tests."""  #32 (line num in coconut source)
    with LowercasePropositions.use_in(globals()):  #33 (line num in coconut source)

# constructive theorems
        assert (proves)(e & f, e)  #36 (line num in coconut source)
        assert (proves)(e & f, f)  #37 (line num in coconut source)
        assert (proves)((e >> f, f >> g, e), g)  #38 (line num in coconut source)
        assert (proves)((e >> (f >> g), e >> f, e), g)  #39 (line num in coconut source)
        assert (proves)((e >> f, f >> g), e >> g)  #40 (line num in coconut source)
        assert (proves)(e >> (f >> g), f >> (e >> g))  #41 (line num in coconut source)
        assert (proves)(e >> (f >> g), (e >> f) >> (e >> g))  #42 (line num in coconut source)
        assert (proves)(e, f >> e)  #43 (line num in coconut source)
        assert (proves)(top, e >> (f >> e))  #44 (line num in coconut source)
        assert (proves)(e >> (f & g), (e >> f) & (e >> g))  #45 (line num in coconut source)
        assert (proves)(e >> (f >> g), (e & f) >> g)  #46 (line num in coconut source)
        assert (proves)((e & f) >> g, e >> (f >> g))  #47 (line num in coconut source)
        assert (proves)((e >> f) >> g, (e & f) >> g)  #48 (line num in coconut source)
        assert (proves)(e & (f >> g), (e >> f) >> g)  #49 (line num in coconut source)
        assert (proves)(e, e | f)  #50 (line num in coconut source)
        assert (proves)(f, e | f)  #51 (line num in coconut source)
        assert (proves)(e | f, f | e)  #52 (line num in coconut source)
        assert (proves)(f >> g, (e | f) >> (e | g))  #53 (line num in coconut source)
        assert (proves)(e, e | e)  #54 (line num in coconut source)
        assert (proves)(e, ~~e)  #55 (line num in coconut source)
        assert (proves)(~e, e >> f)  #56 (line num in coconut source)
        assert (proves)(e >> f, ~f >> ~e)  #57 (line num in coconut source)
        assert (proves)(e | f, ~(~e & ~f))  #58 (line num in coconut source)
        assert (proves)(e & f, ~(~e | ~f))  #59 (line num in coconut source)
        assert (proves)(~(e | f), ~e & ~f)  #60 (line num in coconut source)
        assert (proves)(~e & ~f, ~(e | f))  #61 (line num in coconut source)
        assert (proves)(~e | ~f, ~(e & f))  #62 (line num in coconut source)
        assert (proves)(top, ~(e & ~e))  #63 (line num in coconut source)
        assert (proves)(e & ~e, f)  #64 (line num in coconut source)
        assert (proves)(~f, f >> g)  #65 (line num in coconut source)
        assert (proves)((f >> g, ~f >> g), g)  #66 (line num in coconut source)
        assert (proves)(g, f >> g)  #67 (line num in coconut source)
        assert (proves)((f, ~(f & g)), ~g)  #68 (line num in coconut source)
        assert (proves)((p >> r, p >> ~r), ~p)  #69 (line num in coconut source)
        assert (proves)(top, (p >> ~p) >> ~p)  #70 (line num in coconut source)
        assert (proves)(bot, a)  #71 (line num in coconut source)
        assert (proves)(bot, top)  #72 (line num in coconut source)
        assert (proves)(a, top)  #73 (line num in coconut source)

# classical theorems
        assert (proves)(~~e, e)  #76 (line num in coconut source)
        assert (proves)(top, e | ~e)  #77 (line num in coconut source)
        assert (proves)(top, ((e >> f) >> e) >> e)  #78 (line num in coconut source)
        assert (proves)(~f >> ~e, e >> f)  #79 (line num in coconut source)
        assert (proves)(~(~e & ~f), e | f)  #80 (line num in coconut source)
        assert (proves)(~(~e | ~f), e & f)  #81 (line num in coconut source)
        assert (proves)(~(e & f), ~e | ~f)  #82 (line num in coconut source)
        assert (proves)(top, (e >> f) | (f >> e))  #83 (line num in coconut source)
        assert (proves)(top, (~~a | a) >> a)  #84 (line num in coconut source)
        assert (proves)(p >> r, (f >> r) | (p >> g))  #85 (line num in coconut source)
        assert (proves)(~(f >> g), f & ~g)  #86 (line num in coconut source)
        assert (proves)(top, (~f >> bot) >> f)  #87 (line num in coconut source)
        assert (proves)(f >> g, ~f | g)  #88 (line num in coconut source)
        assert (proves)(top, r & s | (~r | ~s))  #89 (line num in coconut source)
        assert (proves)(f >> g, g | ~f)  #90 (line num in coconut source)
        assert (proves)((a & b) >> ~c, ~a | ~b | ~c)  #91 (line num in coconut source)
        assert (proves)(f >> (g >> h), ~f | ~g | h)  #92 (line num in coconut source)

# other theorems
        assert (proves)(t & (t >> d) | ~t & ~(t >> d), d)  #95 (line num in coconut source)
        assert (proves)((f >> g, c >> d), (f | c) >> (g | d))  #96 (line num in coconut source)
        assert (proves)((f >> g) >> h, f >> (g >> h))  #97 (line num in coconut source)
        assert (proves)(top, p >> (s >> p))  #98 (line num in coconut source)
        assert (proves)(~f | (f >> g), ~f | g)  #99 (line num in coconut source)
        assert (proves)((~f, g >> f), ~g)  #100 (line num in coconut source)
        assert (proves)((p >> s, r >> t, ~s | ~t), ~p | ~r)  #101 (line num in coconut source)
        assert (proves)(top, ~~(f | ~f))  #102 (line num in coconut source)
        assert (proves)(top, ~~(~~f >> f))  #103 (line num in coconut source)
        assert (proves)((p | r, ~p), r)  #104 (line num in coconut source)
        assert (proves)((f | g, ~f), g)  #105 (line num in coconut source)
        assert (proves)((t | ~a, ~a | ~t), ~a)  #106 (line num in coconut source)
        assert (proves)(top, ~~((~f >> bot) >> f))  #107 (line num in coconut source)
        assert (proves)((s & h | ~s & ~h) & ~(s & h) | (s & ~h | ~s & h) & (s & h), ~s & ~h)  #108 (line num in coconut source)
        assert (proves)(~a | ~b | ~c, (a & b) >> ~c)  #109 (line num in coconut source)
        assert (proves)(~p, p >> bot)  #110 (line num in coconut source)
        assert (proves)((a | b, ~a | c), b | c)  #111 (line num in coconut source)
        assert (proves)(top, (f & g) >> g)  #112 (line num in coconut source)
        assert (proves)((p >> s, r >> t, p | r), s | t)  #113 (line num in coconut source)
        assert (proves)(top, ~p >> (p >> s))  #114 (line num in coconut source)
        assert (proves)(f >> g, ((f & g) >> f) | (f >> (f & g)))  #115 (line num in coconut source)
        assert (proves)((f | ~f) >> g, ~~g)  #116 (line num in coconut source)
        assert (proves)(p >> r, p >> (p & r))  #117 (line num in coconut source)
        assert (proves)((s & h | ~s & ~h) & (h | s) | (s & ~h | ~s & h) & ~(h | s), s & h)  #118 (line num in coconut source)
        assert (proves)(~(f >> g), g >> f)  #119 (line num in coconut source)
        assert (proves)((f >> g) & (f >> h), f >> (g & h))  #120 (line num in coconut source)
        assert (proves)((s & h | ~s & ~h) & (~s & ~h) | (s & ~h | ~s & h) & ~(~s & ~h), ~(s & h))  #121 (line num in coconut source)
        assert (proves)(top, (p >> (s >> e)) >> ((p >> s) >> (p >> e)))  #122 (line num in coconut source)
        assert (proves)(top, p >> p)  #123 (line num in coconut source)
        assert (proves)(~f, ~(f & g))  #124 (line num in coconut source)
        assert (proves)(f >> ~f, ~f)  #125 (line num in coconut source)
        assert (proves)(f >> g, ~g >> ~f)  #126 (line num in coconut source)
        assert (f & g) >> f  #127 (line num in coconut source)
        assert (proves)((f >> (t & a | ~t & ~a), t & ~f | ~t & f, g >> (t & ~a | ~t & a), t & g | ~t & ~g), ~a)  #128 (line num in coconut source)
        assert (proves)(t & (~t & ~a) | ~t & ~(~t & ~a), a)  #129 (line num in coconut source)
        assert (proves)(~f | ~g | h, f >> (g >> h))  #130 (line num in coconut source)

# invalid theorems
        assert not (proves)(e >> (f >> g), (e >> f) >> g)  #133 (line num in coconut source)
        assert not (proves)((e & f) >> g, (e >> f) >> g)  #134 (line num in coconut source)
        assert not (proves)((e >> f) >> g, e & (f >> g))  #135 (line num in coconut source)
        assert not (proves)(e, e & f)  #136 (line num in coconut source)
        assert not (proves)(e | f, e & f)  #137 (line num in coconut source)
        assert not (proves)(e | top, e)  #138 (line num in coconut source)
        assert not (proves)(e, e & bot)  #139 (line num in coconut source)
        assert not (proves)(top, bot)  #140 (line num in coconut source)

# other tests
        assert And() == top  #143 (line num in coconut source)
        assert Or() == bot  #144 (line num in coconut source)
        assert (proves)((), top)  #145 (line num in coconut source)
        assert (proves)((a ^ b, a), ~b)  #146 (line num in coconut source)
        assert (proves_and_proved_by)(f >> (g >> h), (f & g) >> h)  #147 (line num in coconut source)
        assert (proves_and_proved_by)(bot, a & ~a)  #148 (line num in coconut source)
        assert (proves_and_proved_by)(top, a | ~a)  #149 (line num in coconut source)
        assert (simplify)(top & bot) == bot  #150 (line num in coconut source)
        assert simplify(a & a, b & b) == (a, b)  #151 (line num in coconut source)
        assert (simplest_form)(a ^ b) == (b | a) & (~a | ~b)  #152 (line num in coconut source)
        assert (simplest_form)((s & h | ~s & ~h) & ~(s & h) | (s & ~h | ~s & h) & (s & h)) == ~s & ~h  #153 (line num in coconut source)
        assert (simplify)((substitute)(a ^ b, {a: True, b: False})) == top  #154 (line num in coconut source)
        assert (simplify)((substitute)(a ^ b, {a: top, b: top})) == bot  #155 (line num in coconut source)
        assert e << f == f >> e  #156 (line num in coconut source)



def test_predicate_logic():  #159 (line num in coconut source)
    """Runs predicate logic tests."""  #160 (line num in coconut source)
    with StandardMath.use_in(globals()):  #161 (line num in coconut source)

# basic tests
        assert (simplify)(FA(x, F)) == F  #164 (line num in coconut source)
        assert (simplify)(TE(x, F)) == F  #165 (line num in coconut source)
        assert (simplify)(FA(x, F(x)) & G) == FA(y, F(y) & G)  #166 (line num in coconut source)
        assert (simplify)(FA(x, F(x)) | G) == FA(y, F(y) | G)  #167 (line num in coconut source)
        assert (simplify)(TE(x, F(x)) & G) == TE(y, F(y) & G)  #168 (line num in coconut source)
        assert (simplify)(TE(x, F(x)) | G) == TE(y, F(y) | G)  #169 (line num in coconut source)
        assert FA(x, F(f(x))) == FA(y, F(f(y)))  #170 (line num in coconut source)
        assert TE(x, F(f(x))) == TE(y, F(f(y)))  #171 (line num in coconut source)
        assert TE(f, F(f(x))) == TE(g, F(g(x)))  #172 (line num in coconut source)

# constructive theorems
        assert (proves)(TE(x, bot), bot)  #175 (line num in coconut source)
        assert (proves)(top, FA(x, top))  #176 (line num in coconut source)
        assert (proves)(FA(x, R(x) >> S(x)), FA(y, R(y)) >> FA(z, S(z)))  #177 (line num in coconut source)
        assert (proves)(FA(x, R(x) & S(x)), FA(y, R(y)) & FA(z, S(z)))  #178 (line num in coconut source)
        assert (proves)((FA(x, R(x) >> S(x)), TE(y, R(y))), TE(z, S(z)))  #179 (line num in coconut source)
        assert (proves)(TE(x, R(x) & S(x)), TE(y, R(y)) & TE(z, S(z)))  #180 (line num in coconut source)
        assert (proves)(TE(x, R(x)) | TE(y, S(y)), TE(z, R(z) | S(z)))  #181 (line num in coconut source)
        assert (proves)(TE(x, R(x) | S(x)), TE(y, R(y)) | TE(z, S(z)))  #182 (line num in coconut source)
        assert (proves)(FA(x, R(x)), ~TE(y, ~R(y)))  #183 (line num in coconut source)
        assert (proves)(TE(x, ~R(x)), ~FA(y, R(y)))  #184 (line num in coconut source)
        assert (proves)(FA(x, ~R(x)), ~TE(y, R(y)))  #185 (line num in coconut source)
        assert (proves)(~TE(x, R(x)), FA(y, ~R(y)))  #186 (line num in coconut source)
        assert (proves)(R(j), TE(x, R(x)))  #187 (line num in coconut source)

# classical theorems
        assert (proves)(~TE(x, ~R(x)), FA(y, R(y)))  #190 (line num in coconut source)
        assert (proves)(~FA(x, ~R(x)), TE(y, R(y)))  #191 (line num in coconut source)
        assert (proves)(~FA(x, R(x)), TE(y, ~R(y)))  #192 (line num in coconut source)
        assert (proves)(FA(x, ~~D(x)), FA(x, D(x)))  #193 (line num in coconut source)
        assert (proves)(~TE(x, R(x)), FA(y, ~R(y)))  #194 (line num in coconut source)
        assert (proves)(top, TE(x, D(x)) | FA(x, ~D(x)))  #195 (line num in coconut source)
        assert (proves)(top, TE(x, ~D(x)) | FA(x, D(x)))  #196 (line num in coconut source)
        assert (proves)(top, TE(x, D(x) >> FA(y, D(y))))  #197 (line num in coconut source)
        assert (proves)(TE(x, ~~D(x)), TE(x, D(x)))  #198 (line num in coconut source)
        assert (proves)(FA(x, C(x) | D(x)), FA(x, C(x)) | TE(x, D(x)))  #199 (line num in coconut source)

# other theorems
        assert (proves)(FA(x, H(j) >> T(x)), H(j) >> FA(x, T(x)))  #202 (line num in coconut source)
        assert (proves)(TE(x, R(x) >> B(x)), FA(x, R(x)) >> TE(x, B(x)))  #203 (line num in coconut source)
        assert (proves)(~FA(x, bot), TE(x, top))  #204 (line num in coconut source)
        assert (proves)(FA(x, TE(y, F(y) | G(x))), FA(x, G(x) | TE(x, F(x))))  #205 (line num in coconut source)
        assert (proves)((FA(x, FA(y, FA(z, (S(x, y) & S(y, z)) >> S(x, z)))), ~TE(x, S(x, x))), FA(x, FA(y, S(x, y) >> ~S(y, x))))  #206 (line num in coconut source)
        assert (proves)(FA(x, G(x)) | FA(x, B(x)), FA(x, G(x) | B(x)))  #207 (line num in coconut source)
        assert (proves)(TE(z, FA(k, P(z, k))), FA(y, TE(x, P(x, y))))  #208 (line num in coconut source)
        assert (proves)(TE(x, C(x) & B(x)), TE(x, B(x) & C(x)))  #209 (line num in coconut source)
        assert (proves)(TE(x, C(x, i) & B(x, j)), TE(x, C(x, i) >> B(x, j)))  #210 (line num in coconut source)
        assert (proves)(FA(x, C(x) & B(x)), FA(x, B(x) & C(x)))  #211 (line num in coconut source)
        assert (proves)(FA(x, C(x) & B(x)), FA(x, C(x)) & FA(x, B(x)))  #212 (line num in coconut source)
        assert (proves)(FA(x, bot), ~TE(x, top))  #213 (line num in coconut source)
        assert (proves)((~TE(x, G(x)) | FA(x, F(x)), C(j) >> FA(x, D(x))), FA(y, FA(z, ~G(z) | F(y) & C(j) >> D(y))))  #214 (line num in coconut source)
        assert (proves)(FA(x, G(x)) | TE(x, F(x)), FA(x, TE(y, F(y) | G(x))))  #215 (line num in coconut source)
        assert (proves)((P | TE(x, W)) >> FA(z, R), FA(z, FA(x, (P | W) >> R)))  #216 (line num in coconut source)
        assert (proves)((TE(x, ~F(x)), FA(x, F(x))), bot)  #217 (line num in coconut source)
        assert (proves)((FA(x, ~F(x)), FA(x, F(x))), FA(x, bot))  #218 (line num in coconut source)
        assert (proves)(TE(x, F(x)) | TE(x, G(x)), TE(x, TE(y, F(x) | G(y))))  #219 (line num in coconut source)
        assert (proves)(TE(x, FA(y, P(x, y))), FA(y, TE(x, P(x, y))))  #220 (line num in coconut source)
        assert (proves)(TE(x, FA(y, bot)), bot)  #221 (line num in coconut source)
        assert (proves)(top, FA(x, TE(y, top)))  #222 (line num in coconut source)
        assert (proves)(FA(x, TE(y, F(y)) | G(x)), FA(x, TE(y, F(y) | G(x))))  #223 (line num in coconut source)
        assert (proves)(TE(x, FA(y, F(y) & G(x))), TE(x, FA(y, F(y)) & G(x)))  #224 (line num in coconut source)
        assert (proves)(TE(x, ~R(x)), TE(y, R(y) >> (R(j) & R(k))))  #225 (line num in coconut source)
        assert (proves)(P(c), TE(x, P(x)))  #226 (line num in coconut source)
        assert (proves)(P(c), TE(x, top))  #227 (line num in coconut source)
        assert (proves)(P(c) & ~P(c), TE(x, top))  #228 (line num in coconut source)
        assert (proves)(P(c) | ~P(c), TE(x, top))  #229 (line num in coconut source)

# invalid theorems
        assert not (proves)(FA(x, R(x)) >> FA(y, S(y)), FA(z, R(z) >> S(z)))  #232 (line num in coconut source)
        assert not (proves)(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))  #233 (line num in coconut source)
        assert not (proves)(TE(x, R(x)), FA(y, R(y)))  #234 (line num in coconut source)

# non-empty universe theorems
        assert (proves)(top, TE(x, top))  #237 (line num in coconut source)
        assert (proves)(top, TE(x, D(x) >> FA(y, D(y))))  #238 (line num in coconut source)
        assert (proves)((R(j), FA(x, R(x) >> S(x))), S(j))  #239 (line num in coconut source)
        assert (proves)(FA(x, R(x)) >> FA(y, S(y)), TE(x, FA(y, ~R(x) | S(y))))  #240 (line num in coconut source)
        assert (proves)(FA(x, R(x)), TE(y, R(y)))  #241 (line num in coconut source)
        assert (proves)((T(i), FA(x, T(x) >> T(s(x)))), T(s(i)))  #242 (line num in coconut source)
        assert (proves)(top, TE(x, R(x) >> (R(j) & R(k))))  #243 (line num in coconut source)
        assert (proves)((FA(x, ~F(x)), FA(x, F(x))), bot)  #244 (line num in coconut source)

# equality theorems
        assert (proves)(top, Eq(a, a))  #247 (line num in coconut source)
        assert (proves)(Eq(a, b) & Eq(b, c), Eq(a, c))  #248 (line num in coconut source)
        assert (proves)(Eq(a, b) & Eq(b, c), Eq(c, a))  #249 (line num in coconut source)
        assert (proves)(Eq(a, b) & F(a), F(b))  #250 (line num in coconut source)
        assert (proves)((Eq(a, b) | Eq(a, c), F(a)), F(b) | F(c))  #251 (line num in coconut source)
        assert (proves)(FA(x, Eq(a, x)), Eq(a, b))  #252 (line num in coconut source)
        assert (proves)(Eq(a, b), Eq(b, a))  #253 (line num in coconut source)
        assert (proves)(Eq(a, b), Eq(f(a), f(b)))  #254 (line num in coconut source)


def test_empty_universe():  #256 (line num in coconut source)
    """Runs predicate logic tests in a potentially empty universe."""  #257 (line num in coconut source)
    with StandardMath.use_in(globals()):  #258 (line num in coconut source)

# basic tests
        assert (strict_simplify)(FA(x, F)) != F  #261 (line num in coconut source)
        assert (strict_simplify)(TE(x, F)) != F  #262 (line num in coconut source)
        assert (strict_simplify)(FA(x, F(x)) & G) != FA(y, F(y) & G)  #263 (line num in coconut source)
        assert (strict_simplify)(FA(x, F(x)) | G) == FA(y, F(y) | G)  #264 (line num in coconut source)
        assert (strict_simplify)(TE(x, F(x)) & G) == TE(y, F(y) & G)  #265 (line num in coconut source)
        assert (strict_simplify)(TE(x, F(x)) | G) != TE(y, F(y) | G)  #266 (line num in coconut source)

# constructive theorems
        assert (strict_proves)(TE(x, bot), bot)  #269 (line num in coconut source)
        assert (strict_proves)(top, FA(x, top))  #270 (line num in coconut source)
        assert (strict_proves)(FA(x, R(x) >> S(x)), FA(y, R(y)) >> FA(z, S(z)))  #271 (line num in coconut source)
        assert (strict_proves)(FA(x, R(x) & S(x)), FA(y, R(y)) & FA(z, S(z)))  #272 (line num in coconut source)
        assert (strict_proves)((FA(x, R(x) >> S(x)), TE(y, R(y))), TE(z, S(z)))  #273 (line num in coconut source)
        assert (strict_proves)(TE(x, R(x) & S(x)), TE(y, R(y)) & TE(z, S(z)))  #274 (line num in coconut source)
        assert (strict_proves)(TE(x, R(x)) | TE(y, S(y)), TE(z, R(z) | S(z)))  #275 (line num in coconut source)
        assert (strict_proves)(TE(x, R(x) | S(x)), TE(y, R(y)) | TE(z, S(z)))  #276 (line num in coconut source)
        assert (strict_proves)(FA(x, R(x)), ~TE(y, ~R(y)))  #277 (line num in coconut source)
        assert (strict_proves)(TE(x, ~R(x)), ~FA(y, R(y)))  #278 (line num in coconut source)
        assert (strict_proves)(FA(x, ~R(x)), ~TE(y, R(y)))  #279 (line num in coconut source)
        assert (strict_proves)(~TE(x, R(x)), FA(y, ~R(y)))  #280 (line num in coconut source)
        assert (strict_proves)(R(j), TE(x, R(x)))  #281 (line num in coconut source)

# classical theorems
        assert (strict_proves)(~TE(x, ~R(x)), FA(y, R(y)))  #284 (line num in coconut source)
        assert (strict_proves)(~FA(x, ~R(x)), TE(y, R(y)))  #285 (line num in coconut source)
        assert (strict_proves)(~FA(x, R(x)), TE(y, ~R(y)))  #286 (line num in coconut source)
        assert (strict_proves)(FA(x, ~~D(x)), FA(x, D(x)))  #287 (line num in coconut source)
        assert (strict_proves)(~TE(x, R(x)), FA(y, ~R(y)))  #288 (line num in coconut source)
        assert (strict_proves)(top, TE(x, D(x)) | FA(x, ~D(x)))  #289 (line num in coconut source)
        assert (strict_proves)(top, TE(x, ~D(x)) | FA(x, D(x)))  #290 (line num in coconut source)
        assert (strict_proves)(TE(x, top), TE(x, D(x) >> FA(y, D(y))))  #291 (line num in coconut source)
        assert (strict_proves)(TE(x, ~~D(x)), TE(x, D(x)))  #292 (line num in coconut source)
        assert (strict_proves)(FA(x, C(x) | D(x)), FA(x, C(x)) | TE(x, D(x)))  #293 (line num in coconut source)

# other theorems
        assert (strict_proves)(FA(x, H(j) >> T(x)), H(j) >> FA(x, T(x)))  #296 (line num in coconut source)
        assert (strict_proves)(TE(x, R(x) >> B(x)), FA(x, R(x)) >> TE(x, B(x)))  #297 (line num in coconut source)
        assert (strict_proves)(~FA(x, bot), TE(x, top))  #298 (line num in coconut source)
        assert (strict_proves)(FA(x, TE(y, F(y) | G(x))), FA(x, G(x) | TE(x, F(x))))  #299 (line num in coconut source)
        assert (strict_proves)((FA(x, FA(y, FA(z, (S(x, y) & S(y, z)) >> S(x, z)))), ~TE(x, S(x, x))), FA(x, FA(y, S(x, y) >> ~S(y, x))))  #300 (line num in coconut source)
        assert (strict_proves)(FA(x, G(x)) | FA(x, B(x)), FA(x, G(x) | B(x)))  #301 (line num in coconut source)
        assert (strict_proves)(TE(z, FA(k, P(z, k))), FA(y, TE(x, P(x, y))))  #302 (line num in coconut source)
        assert (strict_proves)(TE(x, C(x) & B(x)), TE(x, B(x) & C(x)))  #303 (line num in coconut source)
        assert (strict_proves)(TE(x, C(x, i) & B(x, j)), TE(x, C(x, i) >> B(x, j)))  #304 (line num in coconut source)
        assert (strict_proves)(FA(x, C(x) & B(x)), FA(x, B(x) & C(x)))  #305 (line num in coconut source)
        assert (strict_proves)(FA(x, C(x) & B(x)), FA(x, C(x)) & FA(x, B(x)))  #306 (line num in coconut source)
        assert (strict_proves)(FA(x, bot), ~TE(x, top))  #307 (line num in coconut source)
        assert (strict_proves)((~TE(x, G(x)) | FA(x, F(x)), C(j) >> FA(x, D(x))), FA(y, FA(z, ~G(z) | F(y) & C(j) >> D(y))))  #308 (line num in coconut source)
        assert (strict_proves)(FA(x, G(x)) | TE(x, F(x)), FA(x, TE(y, F(y) | G(x))))  #309 (line num in coconut source)
        assert (strict_proves)((P | TE(x, W)) >> FA(z, R), FA(z, FA(x, (P | W) >> R)))  #310 (line num in coconut source)
        assert (proves)(TE(x, F(x)) | TE(x, G(x)), TE(x, TE(y, F(x) | G(y))))  #311 (line num in coconut source)
        assert (proves)(TE(x, FA(y, P(x, y))), FA(y, TE(x, P(x, y))))  #312 (line num in coconut source)
        assert (proves)(TE(x, FA(y, bot)), bot)  #313 (line num in coconut source)
        assert (proves)(top, FA(x, TE(y, top)))  #314 (line num in coconut source)
        assert (proves)(FA(x, TE(y, F(y)) | G(x)), FA(x, TE(y, F(y) | G(x))))  #315 (line num in coconut source)
        assert (proves)(TE(x, FA(y, F(y) & G(x))), TE(x, FA(y, F(y)) & G(x)))  #316 (line num in coconut source)
        assert (strict_proves)(TE(x, ~R(x)), TE(y, R(y) >> (R(j) & R(k))))  #317 (line num in coconut source)
        assert (strict_proves)(P(c), TE(x, P(x)))  #318 (line num in coconut source)
        assert (strict_proves)(P(c), TE(x, top))  #319 (line num in coconut source)
        assert (strict_proves)(P(c) & ~P(c), TE(x, top))  #320 (line num in coconut source)
        assert (strict_proves)(P(c) | ~P(c), TE(x, top))  #321 (line num in coconut source)

# invalid theorems
        assert not (strict_proves)(FA(x, R(x)) >> FA(y, S(y)), FA(z, R(z) >> S(z)))  #324 (line num in coconut source)
        assert not (strict_proves)(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))  #325 (line num in coconut source)
        assert not (strict_proves)(TE(x, R(x)), FA(y, R(y)))  #326 (line num in coconut source)

# non-empty universe theorems
        assert not (strict_proves)(top, TE(x, top))  #329 (line num in coconut source)
        assert not (strict_proves)(top, TE(x, D(x) >> FA(y, D(y))))  #330 (line num in coconut source)
        assert not (strict_proves)((R(j), FA(x, R(x) >> S(x))), S(j))  #331 (line num in coconut source)
        assert not (strict_proves)(FA(x, R(x)) >> FA(y, S(y)), TE(x, FA(y, ~R(x) | S(y))))  #332 (line num in coconut source)
        assert not (strict_proves)(FA(x, R(x)), TE(y, R(y)))  #333 (line num in coconut source)
        assert not (strict_proves)((T(i), FA(x, T(x) >> T(s(x)))), T(s(i)))  #334 (line num in coconut source)
        assert not (strict_proves)(top, TE(x, R(x) >> (R(j) & R(k))))  #335 (line num in coconut source)
        assert not (strict_proves)((FA(x, ~F(x)), FA(x, F(x))), bot)  #336 (line num in coconut source)

# equality theorems
        assert (strict_proves)(top, Eq(a, a))  #339 (line num in coconut source)
        assert (strict_proves)(Eq(a, b) & Eq(b, c), Eq(a, c))  #340 (line num in coconut source)
        assert (strict_proves)(Eq(a, b) & Eq(b, c), Eq(c, a))  #341 (line num in coconut source)
        assert (strict_proves)(Eq(a, b) & F(a), F(b))  #342 (line num in coconut source)
        assert (strict_proves)((Eq(a, b) | Eq(a, c), F(a)), F(b) | F(c))  #343 (line num in coconut source)
        assert (strict_proves)(FA(x, Eq(a, x)), Eq(a, b))  #344 (line num in coconut source)
        assert (strict_proves)(Eq(a, b), Eq(b, a))  #345 (line num in coconut source)
        assert (strict_proves)(Eq(a, b), Eq(f(a), f(b)))  #346 (line num in coconut source)


def test_parser():  #348 (line num in coconut source)
    """Tests math notation parsing."""  #349 (line num in coconut source)
    with StandardMath.use_in(globals()):  #350 (line num in coconut source)
        assert expr(r"A") == A  #351 (line num in coconut source)
        assert expr(r"F(x)") == F(x)  #352 (line num in coconut source)
        assert expr(r"F(f(x))") == F(f(x))  #353 (line num in coconut source)
        assert expr(r"A x. F(x)") == FA(x, F(x))  #354 (line num in coconut source)
        assert expr(r"A x. E y. F(x) \/ G(y)") == FA(x, TE(y, F(x) | G(y)))  #355 (line num in coconut source)
        assert expr(r"F(i) /\ A x. G(x)") == F(i) & FA(x, G(x))  #356 (line num in coconut source)
        assert expr(r"F -> G -> H") == F >> (G >> H)  #357 (line num in coconut source)
        assert expr(r"~F(x)") == ~F(x)  #358 (line num in coconut source)
        assert expr(r"-G(x) /\ F(x)") == ~G(x) & F(x)  #359 (line num in coconut source)
        assert expr(r"A /\ (B \/ C)") == A & (B | C)  #360 (line num in coconut source)
        assert expr(r"a = b") == Eq(a, b)  #361 (line num in coconut source)
        assert expr(r"forall x: A, B(x)") == FA(x, A(x) >> B(x))  #362 (line num in coconut source)
        assert expr(r"exists x: A, B(x)") == TE(x, A(x) & B(x))  #363 (line num in coconut source)
        assert expr(r"Q(x, x', x'')") == Q(x, Const("x'"), Const("x''"))  #364 (line num in coconut source)



def test_sort():  #367 (line num in coconut source)
    """Tests Sorting on predicates."""  #368 (line num in coconut source)
    assert (sorted)([expr("B"), expr("A")]) == [expr("A"), expr("B")]  #369 (line num in coconut source)



def test_regression():  #372 (line num in coconut source)
    """Test hard cases to avoid regressions."""  #373 (line num in coconut source)
    assert (proves)(expr("FA x, ~P(x, x)"), expr("~FA u, FA v, P(g(f(v)), g(u))"))  #374 (line num in coconut source)
    e1 = expr("∀z,∃x, ¬((Q(z)∧Q(x)))")  #375 (line num in coconut source)
    e2 = expr("∃z,∀x, ¬((Q(x)∧Q(z)))")  #376 (line num in coconut source)
    assert not (strict_proves)(e1, e2)  #377 (line num in coconut source)
    assert (strict_proves)(e2, e1)  #378 (line num in coconut source)
    e3 = expr("∃y,∃z,∀x, (Q(x,z)->Q(y,x))")  #379 (line num in coconut source)
    e4 = expr("∀y,∃x, ((R(x,z)∧R(x))->R(y))")  #380 (line num in coconut source)
    assert (strict_proves)(e3, e4)  #381 (line num in coconut source)
    assert not (strict_proves)(e4, e3)  #382 (line num in coconut source)



if __name__ == "__main__":  #385 (line num in coconut source)
    test_propositional_logic()  #386 (line num in coconut source)
    test_predicate_logic()  #387 (line num in coconut source)
    test_empty_universe()  #388 (line num in coconut source)
    test_parser()  #389 (line num in coconut source)
    test_sort()  #390 (line num in coconut source)
    test_regression()  #391 (line num in coconut source)
    print("<success>")  #392 (line num in coconut source)
