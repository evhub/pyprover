#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x44b9d90e

# Compiled with Coconut version 1.2.2-post_dev4 [Colonel]

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

from pyprover.logic import FA  # line 2
from pyprover.logic import TE  # line 2
from pyprover.logic import top  # line 2
from pyprover.logic import bot  # line 2
from pyprover.logic import And  # line 2
from pyprover.logic import Or  # line 3
from pyprover.tools import proves  # line 4
from pyprover.tools import iff  # line 4
from pyprover.tools import simplify  # line 4
from pyprover.tools import simplest_form  # line 4
from pyprover.tools import sub_in  # line 4
from pyprover.tools import strict_simplify  # line 4
from pyprover.tools import strict_proves  # line 11
from pyprover.atoms import LowercasePropositions  # line 12
from pyprover.atoms import StandardMath  # line 20
from pyprover.parser import expr  # line 24

# Tests:

def test_propositional_logic():  # line 28
    """Runs propositional logic tests."""  # line 29
    with LowercasePropositions.using(globals()) :  # line 30

# constructive theorems
        assert (proves)(e & f, e)  # line 33
        assert (proves)(e & f, f)  # line 34
        assert (proves)((e >> f, f >> g, e), g)  # line 35
        assert (proves)((e >> (f >> g), e >> f, e), g)  # line 36
        assert (proves)((e >> f, f >> g), e >> g)  # line 37
        assert (proves)(e >> (f >> g), f >> (e >> g))  # line 38
        assert (proves)(e >> (f >> g), (e >> f) >> (e >> g))  # line 39
        assert (proves)(e, f >> e)  # line 40
        assert (proves)(top, e >> (f >> e))  # line 41
        assert (proves)(e >> (f & g), (e >> f) & (e >> g))  # line 42
        assert (proves)(e >> (f >> g), (e & f) >> g)  # line 43
        assert (proves)((e & f) >> g, e >> (f >> g))  # line 44
        assert (proves)((e >> f) >> g, (e & f) >> g)  # line 45
        assert (proves)(e & (f >> g), (e >> f) >> g)  # line 46
        assert (proves)(e, e | f)  # line 47
        assert (proves)(f, e | f)  # line 48
        assert (proves)(e | f, f | e)  # line 49
        assert (proves)(f >> g, (e | f) >> (e | g))  # line 50
        assert (proves)(e, e | e)  # line 51
        assert (proves)(e, ~~e)  # line 52
        assert (proves)(~e, e >> f)  # line 53
        assert (proves)(e >> f, ~f >> ~e)  # line 54
        assert (proves)(e | f, ~(~e & ~f))  # line 55
        assert (proves)(e & f, ~(~e | ~f))  # line 56
        assert (proves)(~(e | f), ~e & ~f)  # line 57
        assert (proves)(~e & ~f, ~(e | f))  # line 58
        assert (proves)(~e | ~f, ~(e & f))  # line 59
        assert (proves)(top, ~(e & ~e))  # line 60
        assert (proves)(e & ~e, f)  # line 61
        assert (proves)(~f, f >> g)  # line 62
        assert (proves)((f >> g, ~f >> g), g)  # line 63
        assert (proves)(g, f >> g)  # line 64
        assert (proves)((f, ~(f & g)), ~g)  # line 65
        assert (proves)((p >> r, p >> ~r), ~p)  # line 66
        assert (proves)(top, (p >> ~p) >> ~p)  # line 67
        assert (proves)(bot, a)  # line 68
        assert (proves)(bot, top)  # line 69
        assert (proves)(a, top)  # line 70

# classical theorems
        assert (proves)(~~e, e)  # line 73
        assert (proves)(top, e | ~e)  # line 74
        assert (proves)(top, ((e >> f) >> e) >> e)  # line 75
        assert (proves)(~f >> ~e, e >> f)  # line 76
        assert (proves)(~(~e & ~f), e | f)  # line 77
        assert (proves)(~(~e | ~f), e & f)  # line 78
        assert (proves)(~(e & f), ~e | ~f)  # line 79
        assert (proves)(top, (e >> f) | (f >> e))  # line 80
        assert (proves)(top, (~~a | a) >> a)  # line 81
        assert (proves)(p >> r, (f >> r) | (p >> g))  # line 82
        assert (proves)(~(f >> g), f & ~g)  # line 83
        assert (proves)(top, (~f >> bot) >> f)  # line 84
        assert (proves)(f >> g, ~f | g)  # line 85
        assert (proves)(top, r & s | (~r | ~s))  # line 86
        assert (proves)(f >> g, g | ~f)  # line 87
        assert (proves)((a & b) >> ~c, ~a | ~b | ~c)  # line 88
        assert (proves)(f >> (g >> h), ~f | ~g | h)  # line 89

# other theorems
        assert (proves)(t & (t >> d) | ~t & ~(t >> d), d)  # line 92
        assert (proves)((f >> g, c >> d), (f | c) >> (g | d))  # line 93
        assert (proves)((f >> g) >> h, f >> (g >> h))  # line 94
        assert (proves)(top, p >> (s >> p))  # line 95
        assert (proves)(~f | (f >> g), ~f | g)  # line 96
        assert (proves)((~f, g >> f), ~g)  # line 97
        assert (proves)((p >> s, r >> t, ~s | ~t), ~p | ~r)  # line 98
        assert (proves)(top, ~~(f | ~f))  # line 99
        assert (proves)(top, ~~(~~f >> f))  # line 100
        assert (proves)((p | r, ~p), r)  # line 101
        assert (proves)((f | g, ~f), g)  # line 102
        assert (proves)((t | ~a, ~a | ~t), ~a)  # line 103
        assert (proves)(top, ~~((~f >> bot) >> f))  # line 104
        assert (proves)((s & h | ~s & ~h) & ~(s & h) | (s & ~h | ~s & h) & (s & h), ~s & ~h)  # line 105
        assert (proves)(~a | ~b | ~c, (a & b) >> ~c)  # line 106
        assert (proves)(~p, p >> bot)  # line 107
        assert (proves)((a | b, ~a | c), b | c)  # line 108
        assert (proves)(top, (f & g) >> g)  # line 109
        assert (proves)((p >> s, r >> t, p | r), s | t)  # line 110
        assert (proves)(top, ~p >> (p >> s))  # line 111
        assert (proves)(f >> g, ((f & g) >> f) | (f >> (f & g)))  # line 112
        assert (proves)((f | ~f) >> g, ~~g)  # line 113
        assert (proves)(p >> r, p >> (p & r))  # line 114
        assert (proves)((s & h | ~s & ~h) & (h | s) | (s & ~h | ~s & h) & ~(h | s), s & h)  # line 115
        assert (proves)(~(f >> g), g >> f)  # line 116
        assert (proves)((f >> g) & (f >> h), f >> (g & h))  # line 117
        assert (proves)((s & h | ~s & ~h) & (~s & ~h) | (s & ~h | ~s & h) & ~(~s & ~h), ~(s & h))  # line 118
        assert (proves)(top, (p >> (s >> e)) >> ((p >> s) >> (p >> e)))  # line 119
        assert (proves)(top, p >> p)  # line 120
        assert (proves)(~f, ~(f & g))  # line 121
        assert (proves)(f >> ~f, ~f)  # line 122
        assert (proves)(f >> g, ~g >> ~f)  # line 123
        assert (f & g) >> f  # line 124
        assert (proves)((f >> (t & a | ~t & ~a), t & ~f | ~t & f, g >> (t & ~a | ~t & a), t & g | ~t & ~g), ~a)  # line 125
        assert (proves)(t & (~t & ~a) | ~t & ~(~t & ~a), a)  # line 126
        assert (proves)(~f | ~g | h, f >> (g >> h))  # line 127

# invalid theorems
        assert not (proves)(e >> (f >> g), (e >> f) >> g)  # line 130
        assert not (proves)((e & f) >> g, (e >> f) >> g)  # line 131
        assert not (proves)((e >> f) >> g, e & (f >> g))  # line 132
        assert not (proves)(e, e & f)  # line 133
        assert not (proves)(e | f, e & f)  # line 134
        assert not (proves)(e | top, e)  # line 135
        assert not (proves)(e, e & bot)  # line 136
        assert not (proves)(top, bot)  # line 137

# other tests
        assert And() == top  # line 140
        assert Or() == bot  # line 141
        assert (proves)((), top)  # line 142
        assert (proves)((a ^ b, a), ~b)  # line 143
        assert (iff)(f >> (g >> h), (f & g) >> h)  # line 144
        assert (iff)(bot, a & ~a)  # line 145
        assert (iff)(top, a | ~a)  # line 146
        assert (simplify)(top & bot) == bot  # line 147
        assert simplify(a & a, b & b) == (a, b)  # line 148
        assert (simplest_form)(a ^ b) == (b | a) & (~a | ~b)  # line 149
        assert (simplest_form)((s & h | ~s & ~h) & ~(s & h) | (s & ~h | ~s & h) & (s & h)) == ~s & ~h  # line 150
        assert (simplify)((sub_in)(a ^ b, {a: True, b: False})) == top  # line 151
        assert (simplify)((sub_in)(a ^ b, {a: top, b: top})) == bot  # line 152
        assert e << f == f >> e  # line 153

def test_predicate_logic():  # line 155
    """Runs predicate logic tests."""  # line 156
    with StandardMath.using(globals()) :  # line 157

# basic tests
        assert (simplify)(FA(x, F)) == F  # line 160
        assert (simplify)(TE(x, F)) == F  # line 161
        assert (simplify)(FA(x, F(x)) & G(x)) == FA(y, F(y) & G(x))  # line 162
        assert (simplify)(FA(x, F(x)) | G(x)) == FA(y, F(y) | G(x))  # line 163
        assert (simplify)(TE(x, F(x)) & G(x)) == TE(y, F(y) & G(x))  # line 164
        assert (simplify)(TE(x, F(x)) | G(x)) == TE(y, F(y) | G(x))  # line 165
        assert FA(x, F(f(x))) == FA(y, F(f(y)))  # line 166
        assert TE(x, F(f(x))) == TE(y, F(f(y)))  # line 167
        assert TE(f, F(f(x))) == TE(g, F(g(x)))  # line 168

# constructive theorems
        assert (proves)(TE(x, bot), bot)  # line 171
        assert (proves)(top, FA(x, top))  # line 172
        assert (proves)(FA(x, R(x) >> S(x)), FA(y, R(y)) >> FA(z, S(z)))  # line 173
        assert (proves)(FA(x, R(x) & S(x)), FA(y, R(y)) & FA(z, S(z)))  # line 174
        assert (proves)((FA(x, R(x) >> S(x)), TE(y, R(y))), TE(z, S(z)))  # line 175
        assert (proves)(TE(x, R(x) & S(x)), TE(y, R(y)) & TE(z, S(z)))  # line 176
        assert (proves)(TE(x, R(x)) | TE(y, S(y)), TE(z, R(z) | S(z)))  # line 177
        assert (proves)(TE(x, R(x) | S(x)), TE(y, R(y)) | TE(z, S(z)))  # line 178
        assert (proves)(FA(x, R(x)), ~TE(y, ~R(y)))  # line 179
        assert (proves)(TE(x, ~R(x)), ~FA(y, R(y)))  # line 180
        assert (proves)(FA(x, ~R(x)), ~TE(y, R(y)))  # line 181
        assert (proves)(~TE(x, R(x)), FA(y, ~R(y)))  # line 182
        assert (proves)(R(j), TE(x, R(x)))  # line 183

# classical theorems
        assert (proves)(~TE(x, ~R(x)), FA(y, R(y)))  # line 186
        assert (proves)(~FA(x, ~R(x)), TE(y, R(y)))  # line 187
        assert (proves)(~FA(x, R(x)), TE(y, ~R(y)))  # line 188
        assert (proves)(FA(x, ~~D(x)), FA(x, D(x)))  # line 189
        assert (proves)(~TE(x, R(x)), FA(y, ~R(y)))  # line 190
        assert (proves)(top, TE(x, D(x)) | FA(x, ~D(x)))  # line 191
        assert (proves)(top, TE(x, ~D(x)) | FA(x, D(x)))  # line 192
        assert (proves)(TE(x, top), TE(x, D(x) >> FA(y, D(y))))  # line 193
        assert (proves)(TE(x, ~~D(x)), TE(x, D(x)))  # line 194
        assert (proves)(FA(x, C(x) | D(x)), FA(x, C(x)) | TE(x, D(x)))  # line 195

# other theorems
        assert (proves)(FA(x, H(j) >> T(x)), H(j) >> FA(x, T(x)))  # line 198
        assert (proves)(TE(x, R(x) >> B(x)), FA(x, R(x)) >> TE(x, B(x)))  # line 199
        assert (proves)(~FA(x, bot), TE(x, top))  # line 200
        assert (proves)(FA(x, TE(y, F(y) | G(x))), FA(x, G(x) | TE(x, F(x))))  # line 201
        assert (proves)((FA(x, FA(y, FA(z, (S(x, y) & S(y, z)) >> S(x, z)))), ~TE(x, S(x, x))), FA(x, FA(y, S(x, y) >> ~S(y, x))))  # line 202
        assert (proves)(FA(x, G(x)) | FA(x, B(x)), FA(x, G(x) | B(x)))  # line 203
        assert (proves)(TE(z, FA(k, P(z, k))), FA(y, TE(x, P(x, y))))  # line 204
        assert (proves)(TE(x, C(x) & B(x)), TE(x, B(x) & C(x)))  # line 205
        assert (proves)(TE(x, C(x, i) & B(x, j)), TE(x, C(x, i) >> B(x, j)))  # line 206
        assert (proves)(FA(x, C(x) & B(x)), FA(x, B(x) & C(x)))  # line 207
        assert (proves)(FA(x, C(x) & B(x)), FA(x, C(x)) & FA(x, B(x)))  # line 208
        assert (proves)(FA(x, bot), ~TE(x, top))  # line 209
        assert (proves)((~TE(x, G(x)) | FA(x, F(x)), C(j) >> FA(x, D(x))), FA(y, FA(z, ~G(z) | F(y) & C(j) >> D(y))))  # line 210
        assert (proves)(FA(x, G(x)) | TE(x, F(x)), FA(x, TE(y, F(y) | G(x))))  # line 211
        assert (proves)((P | TE(x, W)) >> FA(z, R), FA(z, FA(x, (P | W) >> R)))  # line 212
        assert (proves)((TE(x, ~F(x)), FA(x, F(x))), bot)  # line 213
        assert (proves)((FA(x, ~F(x)), FA(x, F(x))), FA(x, bot))  # line 214
        assert (proves)(TE(x, F(x)) | TE(x, G(x)), TE(x, TE(y, F(x) | G(y))))  # line 215
        assert (proves)(TE(x, FA(y, P(x, y))), FA(y, TE(x, P(x, y))))  # line 216
        assert (proves)(TE(x, FA(y, bot)), bot)  # line 217
        assert (proves)(top, FA(x, TE(y, top)))  # line 218
        assert (proves)(FA(x, TE(y, F(y)) | G(x)), FA(x, TE(y, F(y) | G(x))))  # line 219
        assert (proves)(TE(x, FA(y, F(y) & G(x))), TE(x, FA(y, F(y)) & G(x)))  # line 220
        assert (proves)(TE(x, ~R(x)), TE(y, R(y) >> (R(j) & R(k))))  # line 221

# invalid theorems
        assert not (proves)(FA(x, R(x)) >> FA(y, S(y)), FA(z, R(z) >> S(z)))  # line 224
        assert not (proves)(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))  # line 225
        assert not (proves)(TE(x, R(x)), FA(y, R(y)))  # line 226

# non-empty universe theorems
        assert (proves)(top, TE(x, top))  # line 229
        assert (proves)(top, TE(x, D(x) >> FA(y, D(y))))  # line 230
        assert (proves)((R(j), FA(x, R(x) >> S(x))), S(j))  # line 231
        assert (proves)(FA(x, R(x)) >> FA(y, S(y)), TE(x, FA(y, ~R(x) | S(y))))  # line 232
        assert (proves)(FA(x, R(x)), TE(y, R(y)))  # line 233
        assert (proves)((T(i), FA(x, T(x) >> T(s(x)))), T(s(i)))  # line 234
        assert (proves)(top, TE(x, R(x) >> (R(j) & R(k))))  # line 235
        assert (proves)((FA(x, ~F(x)), FA(x, F(x))), bot)  # line 236

def test_empty_universe():  # line 238
    """Runs predicate logic tests in a potentially empty universe."""  # line 239
    with StandardMath.using(globals()) :  # line 240

# basic tests
        assert (strict_simplify)(FA(x, F)) != F  # line 243
        assert (strict_simplify)(TE(x, F)) != F  # line 244
        assert (strict_simplify)(FA(x, F(x)) & G(x)) != FA(y, F(y) & G(x))  # line 245
        assert (strict_simplify)(FA(x, F(x)) | G(x)) == FA(y, F(y) | G(x))  # line 246
        assert (strict_simplify)(TE(x, F(x)) & G(x)) == TE(y, F(y) & G(x))  # line 247
        assert (strict_simplify)(TE(x, F(x)) | G(x)) != TE(y, F(y) | G(x))  # line 248

# constructive theorems
        assert (strict_proves)(TE(x, bot), bot)  # line 251
        assert (strict_proves)(top, FA(x, top))  # line 252
        assert (strict_proves)(FA(x, R(x) >> S(x)), FA(y, R(y)) >> FA(z, S(z)))  # line 253
        assert (strict_proves)(FA(x, R(x) & S(x)), FA(y, R(y)) & FA(z, S(z)))  # line 254
        assert (strict_proves)((FA(x, R(x) >> S(x)), TE(y, R(y))), TE(z, S(z)))  # line 255
        assert (strict_proves)(TE(x, R(x) & S(x)), TE(y, R(y)) & TE(z, S(z)))  # line 256
        assert (strict_proves)(TE(x, R(x)) | TE(y, S(y)), TE(z, R(z) | S(z)))  # line 257
        assert (strict_proves)(TE(x, R(x) | S(x)), TE(y, R(y)) | TE(z, S(z)))  # line 258
        assert (strict_proves)(FA(x, R(x)), ~TE(y, ~R(y)))  # line 259
        assert (strict_proves)(TE(x, ~R(x)), ~FA(y, R(y)))  # line 260
        assert (strict_proves)(FA(x, ~R(x)), ~TE(y, R(y)))  # line 261
        assert (strict_proves)(~TE(x, R(x)), FA(y, ~R(y)))  # line 262
        assert (strict_proves)(R(j), TE(x, R(x)))  # line 263

# classical theorems
        assert (strict_proves)(~TE(x, ~R(x)), FA(y, R(y)))  # line 266
        assert (strict_proves)(~FA(x, ~R(x)), TE(y, R(y)))  # line 267
        assert (strict_proves)(~FA(x, R(x)), TE(y, ~R(y)))  # line 268
        assert (strict_proves)(FA(x, ~~D(x)), FA(x, D(x)))  # line 269
        assert (strict_proves)(~TE(x, R(x)), FA(y, ~R(y)))  # line 270
        assert (strict_proves)(top, TE(x, D(x)) | FA(x, ~D(x)))  # line 271
        assert (strict_proves)(top, TE(x, ~D(x)) | FA(x, D(x)))  # line 272
        assert (strict_proves)(TE(x, top), TE(x, D(x) >> FA(y, D(y))))  # line 273
        assert (strict_proves)(TE(x, ~~D(x)), TE(x, D(x)))  # line 274
        assert (strict_proves)(FA(x, C(x) | D(x)), FA(x, C(x)) | TE(x, D(x)))  # line 275

# other theorems
        assert (strict_proves)(FA(x, H(j) >> T(x)), H(j) >> FA(x, T(x)))  # line 278
        assert (strict_proves)(TE(x, R(x) >> B(x)), FA(x, R(x)) >> TE(x, B(x)))  # line 279
        assert (strict_proves)(~FA(x, bot), TE(x, top))  # line 280
        assert (strict_proves)(FA(x, TE(y, F(y) | G(x))), FA(x, G(x) | TE(x, F(x))))  # line 281
        assert (strict_proves)((FA(x, FA(y, FA(z, (S(x, y) & S(y, z)) >> S(x, z)))), ~TE(x, S(x, x))), FA(x, FA(y, S(x, y) >> ~S(y, x))))  # line 282
        assert (strict_proves)(FA(x, G(x)) | FA(x, B(x)), FA(x, G(x) | B(x)))  # line 283
        assert (strict_proves)(TE(z, FA(k, P(z, k))), FA(y, TE(x, P(x, y))))  # line 284
        assert (strict_proves)(TE(x, C(x) & B(x)), TE(x, B(x) & C(x)))  # line 285
        assert (strict_proves)(TE(x, C(x, i) & B(x, j)), TE(x, C(x, i) >> B(x, j)))  # line 286
        assert (strict_proves)(FA(x, C(x) & B(x)), FA(x, B(x) & C(x)))  # line 287
        assert (strict_proves)(FA(x, C(x) & B(x)), FA(x, C(x)) & FA(x, B(x)))  # line 288
        assert (strict_proves)(FA(x, bot), ~TE(x, top))  # line 289
        assert (strict_proves)((~TE(x, G(x)) | FA(x, F(x)), C(j) >> FA(x, D(x))), FA(y, FA(z, ~G(z) | F(y) & C(j) >> D(y))))  # line 290
        assert (strict_proves)(FA(x, G(x)) | TE(x, F(x)), FA(x, TE(y, F(y) | G(x))))  # line 291
        assert (strict_proves)((P | TE(x, W)) >> FA(z, R), FA(z, FA(x, (P | W) >> R)))  # line 292
        assert (proves)(TE(x, F(x)) | TE(x, G(x)), TE(x, TE(y, F(x) | G(y))))  # line 293
        assert (proves)(TE(x, FA(y, P(x, y))), FA(y, TE(x, P(x, y))))  # line 294
        assert (proves)(TE(x, FA(y, bot)), bot)  # line 295
        assert (proves)(top, FA(x, TE(y, top)))  # line 296
        assert (proves)(FA(x, TE(y, F(y)) | G(x)), FA(x, TE(y, F(y) | G(x))))  # line 297
        assert (proves)(TE(x, FA(y, F(y) & G(x))), TE(x, FA(y, F(y)) & G(x)))  # line 298
        assert (strict_proves)(TE(x, ~R(x)), TE(y, R(y) >> (R(j) & R(k))))  # line 299

# invalid theorems
        assert not (strict_proves)(FA(x, R(x)) >> FA(y, S(y)), FA(z, R(z) >> S(z)))  # line 302
        assert not (strict_proves)(TE(x, R(x)) & TE(y, S(y)), TE(z, R(z) & S(z)))  # line 303
        assert not (strict_proves)(TE(x, R(x)), FA(y, R(y)))  # line 304

# non-empty universe theorems
        assert not (strict_proves)(top, TE(x, top))  # line 307
        assert not (strict_proves)(top, TE(x, D(x) >> FA(y, D(y))))  # line 308
        assert not (strict_proves)((R(j), FA(x, R(x) >> S(x))), S(j))  # line 309
        assert not (strict_proves)(FA(x, R(x)) >> FA(y, S(y)), TE(x, FA(y, ~R(x) | S(y))))  # line 310
        assert not (strict_proves)(FA(x, R(x)), TE(y, R(y)))  # line 311
        assert not (strict_proves)((T(i), FA(x, T(x) >> T(s(x)))), T(s(i)))  # line 312
        assert not (strict_proves)(top, TE(x, R(x) >> (R(j) & R(k))))  # line 313
        assert not (strict_proves)((FA(x, ~F(x)), FA(x, F(x))), bot)  # line 314

def test_parser():  # line 316
    """Tests math notation parsing."""  # line 317
    with StandardMath.using(globals()) :  # line 318
        assert expr("A") == A  # line 319
        assert expr("F(x)") == F(x)  # line 320
        assert expr("F(f(x))") == F(f(x))  # line 321
        assert expr("A x. F(x)") == FA(x, F(x))  # line 322
        assert expr(r"A x. E y. F(x) \/ G(y)") == FA(x, TE(y, F(x) | G(y)))  # line 323
        assert expr(r"F(i) /\ A x. G(x)") == F(i) & FA(x, G(x))  # line 324
        assert expr("F -> G -> H") == F >> (G >> H)  # line 325
        assert expr("~F(x)") == ~F(x)  # line 326
        assert expr(r"-G(x) /\ F(x)") == ~G(x) & F(x)  # line 327
        assert expr(r"A /\ (B \/ C)") == A & (B | C)  # line 328

if __name__ == "__main__":  # line 330
    test_propositional_logic()  # line 331
    test_predicate_logic()  # line 332
    test_empty_universe()  # line 333
    test_parser()  # line 334
    print("<success>")  # line 335
