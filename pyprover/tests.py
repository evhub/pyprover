#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xda888489

# Compiled with Coconut version 1.2.2-post_dev5 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_tee, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------

# Imports:

from pyprover.logic import FA
from pyprover.logic import TE
from pyprover.logic import top
from pyprover.logic import bot
from pyprover.logic import And
from pyprover.logic import Or
from pyprover.tools import proves
from pyprover.tools import iff
from pyprover.tools import simplify
from pyprover.tools import simplest_form
from pyprover.tools import sub_in
from pyprover.tools import strict_simplify
from pyprover.tools import strict_proves
from pyprover.atoms import LowercasePropositions
from pyprover.atoms import StandardMath
from pyprover.parser import expr

# Tests:

def test_propositional_logic():
    """Runs propositional logic tests."""
    with LowercasePropositions.using(globals()) :

# constructive theorems
        assert (proves)(e & f, e)
        assert (proves)(e & f, f)
        assert (proves)((e >> f, f >> g, e), g)
        assert (proves)((e >> (f >> g), e >> f, e), g)
        assert (proves)((e >> f, f >> g), e >> g)
        assert (proves)(e >> (f >> g), f >> (e >> g))
        assert (proves)(e >> (f >> g), (e >> f) >> (e >> g))
        assert (proves)(e, f >> e)
        assert (proves)(top, e >> (f >> e))
        assert (proves)(e >> (f & g), (e >> f) & (e >> g))
        assert (proves)(e >> (f >> g), (e & f) >> g)
        assert (proves)((e & f) >> g, e >> (f >> g))
        assert (proves)((e >> f) >> g, (e & f) >> g)
        assert (proves)(e & (f >> g), (e >> f) >> g)
        assert (proves)(e, e | f)
        assert (proves)(f, e | f)
        assert (proves)(e | f, f | e)
        assert (proves)(f >> g, (e | f) >> (e | g))
        assert (proves)(e, e | e)
        assert (proves)(e, ~~e)
        assert (proves)(~e, e >> f)
        assert (proves)(e >> f, ~f >> ~e)
        assert (proves)(e | f, ~(~e & ~f))
        assert (proves)(e & f, ~(~e | ~f))
        assert (proves)(~(e | f), ~e & ~f)
        assert (proves)(~e & ~f, ~(e | f))
        assert (proves)(~e | ~f, ~(e & f))
        assert (proves)(top, ~(e & ~e))
        assert (proves)(e & ~e, f)
        assert (proves)(~f, f >> g)
        assert (proves)((f >> g, ~f >> g), g)
        assert (proves)(g, f >> g)
        assert (proves)((f, ~(f & g)), ~g)
        assert (proves)((p >> r, p >> ~r), ~p)
        assert (proves)(top, (p >> ~p) >> ~p)
        assert (proves)(bot, a)
        assert (proves)(bot, top)
        assert (proves)(a, top)

# classical theorems
        assert (proves)(~~e, e)
        assert (proves)(top, e | ~e)
        assert (proves)(top, ((e >> f) >> e) >> e)
        assert (proves)(~f >> ~e, e >> f)
        assert (proves)(~(~e & ~f), e | f)
        assert (proves)(~(~e | ~f), e & f)
        assert (proves)(~(e & f), ~e | ~f)
        assert (proves)(top, (e >> f) | (f >> e))
        assert (proves)(top, (~~a | a) >> a)
        assert (proves)(p >> r, (f >> r) | (p >> g))
        assert (proves)(~(f >> g), f & ~g)
        assert (proves)(top, (~f >> bot) >> f)
        assert (proves)(f >> g, ~f | g)
        assert (proves)(top, r & s | (~r | ~s))
        assert (proves)(f >> g, g | ~f)
        assert (proves)((a & b) >> ~c, ~a | ~b | ~c)
        assert (proves)(f >> (g >> h), ~f | ~g | h)

# other theorems
        assert (proves)(t & (t >> d) | ~t & ~(t >> d), d)
        assert (proves)((f >> g, c >> d), (f | c) >> (g | d))
        assert (proves)((f >> g) >> h, f >> (g >> h))
        assert (proves)(top, p >> (s >> p))
        assert (proves)(~f | (f >> g), ~f | g)
        assert (proves)((~f, g >> f), ~g)
        assert (proves)((p >> s, r >> t, ~s | ~t), ~p | ~r)
        assert (proves)(top, ~~(f | ~f))
        assert (proves)(top, ~~(~~f >> f))
        assert (proves)((p | r, ~p), r)
        assert (proves)((f | g, ~f), g)
        assert (proves)((t | ~a, ~a | ~t), ~a)
        assert (proves)(top, ~~((~f >> bot) >> f))
        assert (proves)((s & h | ~s & ~h) & ~(s & h) | (s & ~h | ~s & h) & (s & h), ~s & ~h)
        assert (proves)(~a | ~b | ~c, (a & b) >> ~c)
        assert (proves)(~p, p >> bot)
        assert (proves)((a | b, ~a | c), b | c)
        assert (proves)(top, (f & g) >> g)
        assert (proves)((p >> s, r >> t, p | r), s | t)
        assert (proves)(top, ~p >> (p >> s))
        assert (proves)(f >> g, ((f & g) >> f) | (f >> (f & g)))
        assert (proves)((f | ~f) >> g, ~~g)
        assert (proves)(p >> r, p >> (p & r))
        assert (proves)((s & h | ~s & ~h) & (h | s) | (s & ~h | ~s & h) & ~(h | s), s & h)
        assert (proves)(~(f >> g), g >> f)
        assert (proves)((f >> g) & (f >> h), f >> (g & h))
        assert (proves)((s & h | ~s & ~h) & (~s & ~h) | (s & ~h | ~s & h) & ~(~s & ~h), ~(s & h))
        assert (proves)(top, (p >> (s >> e)) >> ((p >> s) >> (p >> e)))
        assert (proves)(top, p >> p)
        assert (proves)(~f, ~(f & g))
        assert (proves)(f >> ~f, ~f)
        assert (proves)(f >> g, ~g >> ~f)
        assert (f & g) >> f
        assert (proves)((f >> (t & a | ~t & ~a), t & ~f | ~t & f, g >> (t & ~a | ~t & a), t & g | ~t & ~g), ~a)
        assert (proves)(t & (~t & ~a) | ~t & ~(~t & ~a), a)
        assert (proves)(~f | ~g | h, f >> (g >> h))

# invalid theorems
        assert not (proves)(e >> (f >> g), (e >> f) >> g)
        assert not (proves)((e & f) >> g, (e >> f) >> g)
        assert not (proves)((e >> f) >> g, e & (f >> g))
        assert not (proves)(e, e & f)
        assert not (proves)(e | f, e & f)
        assert not (proves)(e | top, e)
        assert not (proves)(e, e & bot)
        assert not (proves)(top, bot)

# other tests
        assert And() == top
        assert Or() == bot
        assert (proves)((), top)
        assert (proves)((a ^ b, a), ~b)
        assert (iff)(f >> (g >> h), (f & g) >> h)
        assert (iff)(bot, a & ~a)
        assert (iff)(top, a | ~a)
        assert (simplify)(top & bot) == bot
        assert simplify(a & a, b & b) == (a, b)
        assert (simplest_form)(a ^ b) == (b | a) & (~a | ~b)
        assert (simplest_form)((s & h | ~s & ~h) & ~(s & h) | (s & ~h | ~s & h) & (s & h)) == ~s & ~h
        assert (simplify)((sub_in)(a ^ b, {a: True, b: False})) == top
        assert (simplify)((sub_in)(a ^ b, {a: top, b: top})) == bot
        assert e << f == f >> e

def test_predicate_logic():
    """Runs predicate logic tests."""
    with StandardMath.using(globals()) :

# basic tests
        assert (simplify)(FA(x, F)) == F
        assert (simplify)(TE(x, F)) == F
        assert (simplify)(FA(x, F(x)) & G(x)) == FA(y, F(y) & G(x))
        assert (simplify)(FA(x, F(x)) | G(x)) == FA(y, F(y) | G(x))
        assert (simplify)(TE(x, F(x)) & G(x)) == TE(y, F(y) & G(x))
        assert (simplify)(TE(x, F(x)) | G(x)) == TE(y, F(y) | G(x))
        assert FA(x, F(f(x))) == FA(y, F(f(y)))
        assert TE(x, F(f(x))) == TE(y, F(f(y)))
        assert TE(f, F(f(x))) == TE(g, F(g(x)))

# constructive theorems
        assert (proves)(TE(x, bot), bot)
        assert (proves)(top, FA(x, top))
        assert (proves)(FA(x, R(x) >> S(x)), FA(y, R(y)) >> FA(z, S(z)))
        assert (proves)(FA(x, R(x) & S(x)), FA(y, R(y)) & FA(z, S(z)))
        assert (proves)((FA(x, R(x) >> S(x)), TE(y, R(y))), TE(z, S(z)))
        assert (proves)(TE(x, R(x) & S(x)), TE(y, R(y)) & TE(z, S(z)))
        assert (proves)(TE(x, R(x)) | TE(y, S(y)), TE(z, R(z) | S(z)))
        assert (proves)(TE(x, R(x) | S(x)), TE(y, R(y)) | TE(z, S(z)))
        assert (proves)(FA(x, R(x)), ~TE(y, ~R(y)))
        assert (proves)(TE(x, ~R(x)), ~FA(y, R(y)))
        assert (proves)(FA(x, ~R(x)), ~TE(y, R(y)))
        assert (proves)(~TE(x, R(x)), FA(y, ~R(y)))
        assert (proves)(R(j), TE(x, R(x)))

# classical theorems
        assert (proves)(~TE(x, ~R(x)), FA(y, R(y)))
        assert (proves)(~FA(x, ~R(x)), TE(y, R(y)))
        assert (proves)(~FA(x, R(x)), TE(y, ~R(y)))
        assert (proves)(FA(x, ~~D(x)), FA(x, D(x)))
        assert (proves)(~TE(x, R(x)), FA(y, ~R(y)))
        assert (proves)(top, TE(x, D(x)) | FA(x, ~D(x)))
        assert (proves)(top, TE(x, ~D(x)) | FA(x, D(x)))
        assert (proves)(TE(x, top), TE(x, D(x) >> FA(y, D(y))))
        assert (proves)(TE(x, ~~D(x)), TE(x, D(x)))
        assert (proves)(FA(x, C(x) | D(x)), FA(x, C(x)) | TE(x, D(x)))

# other theorems
        assert (proves)(FA(x, H(j) >> T(x)), H(j) >> FA(x, T(x)))
        assert (proves)(TE(x, R(x) >> B(x)), FA(x, R(x)) >> TE(x, B(x)))
        assert (proves)(~FA(x, bot), TE(x, top))
        assert (proves)(FA(x, TE(y, F(y) | G(x))), FA(x, G(x) | TE(x, F(x))))
        assert (proves)((FA(x, FA(y, FA(z, (S(x, y) & S(y, z)) >> S(x, z)))), ~TE(x, S(x, x))), FA(x, FA(y, S(x, y) >> ~S(y, x))))
        assert (proves)(FA(x, G(x)) | FA(x, B(x)), FA(x, G(x) | B(x)))
        assert (proves)(TE(z, FA(k, P(z, k))), FA(y, TE(x, P(x, y))))
        assert (proves)(TE(x, C(x) & B(x)), TE(x, B(x) & C(x)))
        assert (proves)(TE(x, C(x, i) & B(x, j)), TE(x, C(x, i) >> B(x, j)))
        assert (proves)(FA(x, C(x) & B(x)), FA(x, B(x) & C(x)))
        assert (proves)(FA(x, C(x) & B(x)), FA(x, C(x)) & FA(x, B(x)))
        assert (proves)(FA(x, bot), ~TE(x, top))
        assert (proves)((~TE(x, G(x)) | FA(x, F(x)), C(j) >> FA(x, D(x))), FA(y, FA(z, ~G(z) | F(y) & C(j) >> D(y))))
        assert (proves)(FA(x, G(x)) | TE(x, F(x)), FA(x, TE(y, F(y) | G(x))))
        assert (proves)((P | TE(x, W)) >> FA(z, R), FA(z, FA(x, (P | W) >> R)))
        assert (proves)((TE(x, ~F(x)), FA(x, F(x))), bot)
        assert (proves)((FA(x, ~F(x)), FA(x, F(x))), FA(x, bot))
        assert (proves)(TE(x, F(x)) | TE(x, G(x)), TE(x, TE(y, F(x) | G(y))))
        assert (proves)(TE(x, FA(y, P(x, y))), FA(y, TE(x, P(x, y))))
        assert (proves)(TE(x, FA(y, bot)), bot)
        assert (proves)(top, FA(x, TE(y, top)))
        assert (proves)(FA(x, TE(y, F(y)) | G(x)), FA(x, TE(y, F(y) | G(x))))
        assert (proves)(TE(x, FA(y, F(y) & G(x))), TE(x, FA(y, F(y)) & G(x)))
        assert (proves)(TE(x, ~R(x)), TE(y, R(y) >> (R(j) & R(k))))

# invalid theorems
        assert not (proves)(FA(x, R(x)) >> FA(y, S(y)), FA(z, R(z) >> S(z)))
        assert not (proves)(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))
        assert not (proves)(TE(x, R(x)), FA(y, R(y)))

# non-empty universe theorems
        assert (proves)(top, TE(x, top))
        assert (proves)(top, TE(x, D(x) >> FA(y, D(y))))
        assert (proves)((R(j), FA(x, R(x) >> S(x))), S(j))
        assert (proves)(FA(x, R(x)) >> FA(y, S(y)), TE(x, FA(y, ~R(x) | S(y))))
        assert (proves)(FA(x, R(x)), TE(y, R(y)))
        assert (proves)((T(i), FA(x, T(x) >> T(s(x)))), T(s(i)))
        assert (proves)(top, TE(x, R(x) >> (R(j) & R(k))))
        assert (proves)((FA(x, ~F(x)), FA(x, F(x))), bot)

def test_empty_universe():
    """Runs predicate logic tests in a potentially empty universe."""
    with StandardMath.using(globals()) :

# basic tests
        assert (strict_simplify)(FA(x, F)) != F
        assert (strict_simplify)(TE(x, F)) != F
        assert (strict_simplify)(FA(x, F(x)) & G(x)) != FA(y, F(y) & G(x))
        assert (strict_simplify)(FA(x, F(x)) | G(x)) == FA(y, F(y) | G(x))
        assert (strict_simplify)(TE(x, F(x)) & G(x)) == TE(y, F(y) & G(x))
        assert (strict_simplify)(TE(x, F(x)) | G(x)) != TE(y, F(y) | G(x))

# constructive theorems
        assert (strict_proves)(TE(x, bot), bot)
        assert (strict_proves)(top, FA(x, top))
        assert (strict_proves)(FA(x, R(x) >> S(x)), FA(y, R(y)) >> FA(z, S(z)))
        assert (strict_proves)(FA(x, R(x) & S(x)), FA(y, R(y)) & FA(z, S(z)))
        assert (strict_proves)((FA(x, R(x) >> S(x)), TE(y, R(y))), TE(z, S(z)))
        assert (strict_proves)(TE(x, R(x) & S(x)), TE(y, R(y)) & TE(z, S(z)))
        assert (strict_proves)(TE(x, R(x)) | TE(y, S(y)), TE(z, R(z) | S(z)))
        assert (strict_proves)(TE(x, R(x) | S(x)), TE(y, R(y)) | TE(z, S(z)))
        assert (strict_proves)(FA(x, R(x)), ~TE(y, ~R(y)))
        assert (strict_proves)(TE(x, ~R(x)), ~FA(y, R(y)))
        assert (strict_proves)(FA(x, ~R(x)), ~TE(y, R(y)))
        assert (strict_proves)(~TE(x, R(x)), FA(y, ~R(y)))
        assert (strict_proves)(R(j), TE(x, R(x)))

# classical theorems
        assert (strict_proves)(~TE(x, ~R(x)), FA(y, R(y)))
        assert (strict_proves)(~FA(x, ~R(x)), TE(y, R(y)))
        assert (strict_proves)(~FA(x, R(x)), TE(y, ~R(y)))
        assert (strict_proves)(FA(x, ~~D(x)), FA(x, D(x)))
        assert (strict_proves)(~TE(x, R(x)), FA(y, ~R(y)))
        assert (strict_proves)(top, TE(x, D(x)) | FA(x, ~D(x)))
        assert (strict_proves)(top, TE(x, ~D(x)) | FA(x, D(x)))
        assert (strict_proves)(TE(x, top), TE(x, D(x) >> FA(y, D(y))))
        assert (strict_proves)(TE(x, ~~D(x)), TE(x, D(x)))
        assert (strict_proves)(FA(x, C(x) | D(x)), FA(x, C(x)) | TE(x, D(x)))

# other theorems
        assert (strict_proves)(FA(x, H(j) >> T(x)), H(j) >> FA(x, T(x)))
        assert (strict_proves)(TE(x, R(x) >> B(x)), FA(x, R(x)) >> TE(x, B(x)))
        assert (strict_proves)(~FA(x, bot), TE(x, top))
        assert (strict_proves)(FA(x, TE(y, F(y) | G(x))), FA(x, G(x) | TE(x, F(x))))
        assert (strict_proves)((FA(x, FA(y, FA(z, (S(x, y) & S(y, z)) >> S(x, z)))), ~TE(x, S(x, x))), FA(x, FA(y, S(x, y) >> ~S(y, x))))
        assert (strict_proves)(FA(x, G(x)) | FA(x, B(x)), FA(x, G(x) | B(x)))
        assert (strict_proves)(TE(z, FA(k, P(z, k))), FA(y, TE(x, P(x, y))))
        assert (strict_proves)(TE(x, C(x) & B(x)), TE(x, B(x) & C(x)))
        assert (strict_proves)(TE(x, C(x, i) & B(x, j)), TE(x, C(x, i) >> B(x, j)))
        assert (strict_proves)(FA(x, C(x) & B(x)), FA(x, B(x) & C(x)))
        assert (strict_proves)(FA(x, C(x) & B(x)), FA(x, C(x)) & FA(x, B(x)))
        assert (strict_proves)(FA(x, bot), ~TE(x, top))
        assert (strict_proves)((~TE(x, G(x)) | FA(x, F(x)), C(j) >> FA(x, D(x))), FA(y, FA(z, ~G(z) | F(y) & C(j) >> D(y))))
        assert (strict_proves)(FA(x, G(x)) | TE(x, F(x)), FA(x, TE(y, F(y) | G(x))))
        assert (strict_proves)((P | TE(x, W)) >> FA(z, R), FA(z, FA(x, (P | W) >> R)))
        assert (proves)(TE(x, F(x)) | TE(x, G(x)), TE(x, TE(y, F(x) | G(y))))
        assert (proves)(TE(x, FA(y, P(x, y))), FA(y, TE(x, P(x, y))))
        assert (proves)(TE(x, FA(y, bot)), bot)
        assert (proves)(top, FA(x, TE(y, top)))
        assert (proves)(FA(x, TE(y, F(y)) | G(x)), FA(x, TE(y, F(y) | G(x))))
        assert (proves)(TE(x, FA(y, F(y) & G(x))), TE(x, FA(y, F(y)) & G(x)))
        assert (strict_proves)(TE(x, ~R(x)), TE(y, R(y) >> (R(j) & R(k))))

# invalid theorems
        assert not (strict_proves)(FA(x, R(x)) >> FA(y, S(y)), FA(z, R(z) >> S(z)))
        assert not (strict_proves)(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))
        assert not (strict_proves)(TE(x, R(x)), FA(y, R(y)))

# non-empty universe theorems
        assert not (strict_proves)(top, TE(x, top))
        assert not (strict_proves)(top, TE(x, D(x) >> FA(y, D(y))))
        assert not (strict_proves)((R(j), FA(x, R(x) >> S(x))), S(j))
        assert not (strict_proves)(FA(x, R(x)) >> FA(y, S(y)), TE(x, FA(y, ~R(x) | S(y))))
        assert not (strict_proves)(FA(x, R(x)), TE(y, R(y)))
        assert not (strict_proves)((T(i), FA(x, T(x) >> T(s(x)))), T(s(i)))
        assert not (strict_proves)(top, TE(x, R(x) >> (R(j) & R(k))))
        assert not (strict_proves)((FA(x, ~F(x)), FA(x, F(x))), bot)

def test_parser():
    """Tests math notation parsing."""
    with StandardMath.using(globals()) :
        assert expr("A") == A
        assert expr("F(x)") == F(x)
        assert expr("F(f(x))") == F(f(x))
        assert expr("A x. F(x)") == FA(x, F(x))
        assert expr(r"A x. E y. F(x) \/ G(y)") == FA(x, TE(y, F(x) | G(y)))
        assert expr(r"F(i) /\ A x. G(x)") == F(i) & FA(x, G(x))
        assert expr("F -> G -> H") == F >> (G >> H)
        assert expr("~F(x)") == ~F(x)
        assert expr(r"-G(x) /\ F(x)") == ~G(x) & F(x)
        assert expr(r"A /\ (B \/ C)") == A & (B | C)

if __name__ == "__main__":
    test_propositional_logic()
    test_predicate_logic()
    test_empty_universe()
    test_parser()
    print("<success>")
