#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x12876d81

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

from pyprover.constants import top_sym  # line 2
from pyprover.constants import bot_sym  # line 2
from pyprover.constants import not_sym  # line 2
from pyprover.constants import imp_sym  # line 2
from pyprover.constants import and_sym  # line 2
from pyprover.constants import or_sym  # line 2
from pyprover.constants import forall_sym  # line 2
from pyprover.constants import exists_sym  # line 3
from pyprover.util import unorderd_eq  # line 4
from pyprover.util import quote  # line 4
from pyprover.util import log_simplification  # line 13

# Functions:

def wff(expr):  # line 20
    """Determines whether expr is a well-formed formula."""  # line 22
    return isinstance(expr, Expr) and not isinstance(expr, Term)  # line 23

@_coconut_tco  # line 24
def isvar(var):  # line 24
    """Whether a term is a variable."""  # line 26
    raise _coconut_tail_call(isinstance, var, (Constant, Variable))  # line 27

# Classes:

class Expr(_coconut.object):  # line 31
    __slots__ = ()  # line 32
    @_coconut_tco  # line 33
    def __and__(self, other):  # line 33
        if isinstance(other, And):  # line 34
            return other & self  # line 35
        else:  # line 36
            raise _coconut_tail_call(And, self, other)  # line 37
    @_coconut_tco  # line 38
    def __or__(self, other):  # line 38
        if isinstance(other, Or):  # line 39
            return other | self  # line 40
        else:  # line 41
            raise _coconut_tail_call(Or, self, other)  # line 42
    @_coconut_tco  # line 43
    def __rshift__(self, other):  # line 43
        if isinstance(other, Imp):  # line 44
            return other << self  # line 45
        else:  # line 46
            raise _coconut_tail_call(Imp, self, other)  # line 47
    def __lshift__(self, other):  # line 48
        assert wff(other), other  # line 49
        return other >> self  # line 50
    @_coconut_tco  # line 51
    def __invert__(self):  # line 51
        raise _coconut_tail_call(Not, self)  # line 52
    @_coconut_tco  # line 53
    def __xor__(self, other):  # line 53
        raise _coconut_tail_call(Or, And(self, Not(other)), And(Not(self), other))  # line 54
    def __len__(self):  # line 55
        return 1  # line 55
    def __ne__(self, other):  # line 56
        return not self == other  # line 56
    def simplify(self, **kwargs):  # line 57
        """Simplify the given expression."""  # line 58
        return self  # line 59
    def substitute(self, subs):  # line 60
        """Substitutes a dictionary into the expression."""  # line 61
        return self  # line 62
    def resolve(self, **kwargs):  # line 63
        """Performs resolution on the clauses in a CNF expression."""  # line 64
        return self  # line 65
    def find_unification(self, other):  # line 66
        """Find a substitution in self that would make self into other."""  # line 67
        if self == other:  # line 68
            return {}  # line 69
        else:  # line 70
            return None  # line 71
    @_coconut_tco  # line 72
    def contradicts(self, other, **kwargs):  # line 72
        """Assuming self is simplified, determines if it contradicts other."""  # line 73
        if isinstance(other, Not):  # line 74
            raise _coconut_tail_call(other.contradicts, self, **kwargs)  # line 75
        else:  # line 76
            return self == Not(other).simplify(**kwargs)  # line 77
    @_coconut_tco  # line 78
    def resolve_against(self, other, **kwargs):  # line 78
        """Attempt to perform a resolution against other else None."""  # line 79
        if isinstance(other, (Not, Or)):  # line 80
            raise _coconut_tail_call(other.resolve_against, self, **kwargs)  # line 81
        elif (self.find_unification)(Not(other).simplify(**kwargs)) is not None:  # line 82
            return bot  # line 83
        else:  # line 84
            return None  # line 85

class Top(Expr):  # line 87
    __slots__ = ()  # line 88
    @_coconut_tco  # line 89
    def __eq__(self, other):  # line 89
        raise _coconut_tail_call(isinstance, other, Top)  # line 89
    def __repr__(self):  # line 90
        return "top"  # line 90
    def __str__(self):  # line 91
        return top_sym  # line 91
    def __bool__(self):  # line 92
        return True  # line 92
top = true = Top()  # line 93

class Bot(Expr):  # line 95
    __slots__ = ()  # line 96
    @_coconut_tco  # line 97
    def __eq__(self, other):  # line 97
        raise _coconut_tail_call(isinstance, other, Bot)  # line 97
    def __repr__(self):  # line 98
        return "bot"  # line 98
    def __str__(self):  # line 99
        return bot_sym  # line 99
    def __bool__(self):  # line 100
        return False  # line 100
bot = false = Bot()  # line 101

class Atom(Expr):  # line 103
    __slots__ = ("name",)  # line 104
    def __init__(self, name):  # line 105
        if isinstance(name, Atom):  # line 106
            name = name.name  # line 107
        assert isinstance(name, str)  # line 108
        self.name = name  # line 109
    def __repr__(self):  # line 110
        return self.__class__.__name__ + '("' + self.name + '")'  # line 111
    def __str__(self):  # line 112
        return self.name  # line 113
    def __eq__(self, other):  # line 114
        return isinstance(other, self.__class__) and self.name == other.name  # line 115
    @_coconut_tco  # line 116
    def __hash__(self):  # line 116
        raise _coconut_tail_call((hash), (self.__class__.__name__, self.name))  # line 117
    def substitute_elements(self, subs):  # line 118
        """Substitute for the elements of the Atom, not the Atom itself."""  # line 119
        return self  # line 120
    @_coconut_tco  # line 121
    def substitute(self, subs):  # line 121
        try:  # line 122
            sub = subs[self]  # line 123
        except KeyError:  # line 124
            raise _coconut_tail_call(self.substitute_elements, subs)  # line 125
        else:  # line 126
            if wff(sub):  # line 127
                return sub  # line 128
            elif sub is True:  # line 129
                return top  # line 130
            elif sub is False:  # line 131
                return bot  # line 132
            else:  # line 133
                raise TypeError("cannot perform substitution " + self + " => " + sub)  # line 134

class Prop(Atom):  # line 136
    __slots__ = ()  # line 137
    @_coconut_tco  # line 138
    def __call__(self, *args):  # line 138
        raise _coconut_tail_call(Predicate, self.name, *args)  # line 139
Proposition = Prop  # line 140

class FuncAtom(Atom):  # line 142
    __slots__ = ("args",)  # line 143
    def __init__(self, name, *args):  # line 144
        super(FuncAtom, self).__init__(name)  # line 145
        for arg in args:  # line 146
            assert isinstance(arg, Term), arg  # line 147
        self.args = args  # line 148
    def __repr__(self):  # line 149
        return self.name + "(" + ", ".join((repr(x) for x in self.args)) + ")"  # line 150
    def __str__(self):  # line 151
        return self.name + "(" + ", ".join((str(x) for x in self.args)) + ")"  # line 152
    def __eq__(self, other):  # line 153
        return isinstance(other, self.__class__) and self.name == other.name and self.args == other.args  # line 154
    @_coconut_tco  # line 155
    def __hash__(self):  # line 155
        raise _coconut_tail_call((hash), (self.__class__.__name__, self.name, self.args))  # line 156
    def find_unification(self, other):  # line 157
        if isinstance(other, self.__class__) and self.name == other.name and len(self.args) == len(other.args):  # line 158
            subs = {}  # line 159
            for i, x in enumerate(self.args):  # line 160
                y = other.args[i]  # line 161
                unif = x.find_unification(y)  # line 162
                if unif is None:  # line 163
                    return None  # line 164
                for name, var in unif.items():  # line 165
                    if name not in subs:  # line 166
                        subs[name] = var  # line 167
                    elif subs[name] != var:  # line 168
                        return None  # line 169
            return subs  # line 170
        else:  # line 171
            return None  # line 172

class Predicate(FuncAtom):  # line 174
    __slots__ = ()  # line 175
    @_coconut_tco  # line 176
    def proposition(self):  # line 176
        raise _coconut_tail_call(Proposition, self.name)  # line 177
    @_coconut_tco  # line 178
    def substitute_elements(self, subs):  # line 178
        try:  # line 179
            sub = subs[self.proposition()]  # line 180
        except KeyError:  # line 181
            raise _coconut_tail_call((_coconut.functools.partial(Predicate, self.name)), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.args))  # line 182
        else:  # line 183
            raise _coconut_tail_call(Predicate, sub.name, *self.args)  # line 184

class Term(Atom):  # line 186
    __slots__ = ()  # line 187
    @_coconut_tco  # line 188
    def variable(self):  # line 188
        """Convert to a variable."""  # line 189
        raise _coconut_tail_call(Variable, self.name)  # line 190
    @_coconut_tco  # line 191
    def constant(self):  # line 191
        """Convert to a constant."""  # line 192
        raise _coconut_tail_call(Constant, self.name)  # line 193
    @_coconut_tco  # line 194
    def rename(self, name):  # line 194
        """Create a new term with a different name."""  # line 195
        raise _coconut_tail_call(self.__class__, name)  # line 196
    @_coconut_tco  # line 197
    def prime(self):  # line 197
        """Rename by adding a prime."""  # line 198
        raise _coconut_tail_call(self.rename, self.name + "'")  # line 199
    @_coconut_tco  # line 200
    def substitute(self, subs):  # line 200
        for var, sub in subs.items():  # line 201
            if isinstance(var, Term) and self.name == var.name:  # line 202
                if isvar(self) or self == var:  # line 203
                    return sub  # line 204
                else:  # line 205
                    raise _coconut_tail_call(self.rename, sub.name)  # line 206
        raise _coconut_tail_call(self.substitute_elements, subs)  # line 207

class Var(Term):  # line 209
    __slots__ = ()  # line 210
    def variable(self):  # line 211
        return self  # line 211
    @_coconut_tco  # line 212
    def __call__(self, *args):  # line 212
        raise _coconut_tail_call(Function, self.name, *args)  # line 213
    def find_unification(self, other):  # line 214
        if isinstance(other, Term):  # line 215
            return {self: other}  # line 216
        else:  # line 217
            return None  # line 218
Variable = Var  # line 219

class Const(Term):  # line 221
    __slots__ = ()  # line 222
    def constant(self):  # line 223
        return self  # line 223
    @_coconut_tco  # line 224
    def __call__(self, *args):  # line 224
        raise _coconut_tail_call(Function, self.name, *args)  # line 225
    def find_unification(self, other):  # line 226
        if isinstance(other, Variable):  # line 227
            return {other: self}  # line 228
        else:  # line 229
            return super(Constant, self).find_unification(other)  # line 230
Constant = Const  # line 231

class Function(Term, FuncAtom):  # line 233
    __slots__ = ()  # line 234
    @_coconut_tco  # line 235
    def substitute_elements(self, subs):  # line 235
        raise _coconut_tail_call((_coconut.functools.partial(Function, self.name)), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.args))  # line 236
    @_coconut_tco  # line 237
    def rename(self, name):  # line 237
        raise _coconut_tail_call(self.__class__, name, *self.args)  # line 238
    def find_unification(self, other):  # line 239
        if isinstance(other, Variable):  # line 240
            return {other: self}  # line 241
        else:  # line 242
            return super(Function, self).find_unification(other)  # line 243

class UnaryOp(Expr):  # line 245
    __slots__ = ("elem",)  # line 246
    def __init__(self, elem):  # line 247
        assert wff(elem), elem  # line 248
        self.elem = elem  # line 249
    def __repr__(self):  # line 250
        return self.__class__.__name__ + "(" + repr(self.elem) + ")"  # line 251
    def __eq__(self, other):  # line 252
        return isinstance(other, self.__class__) and self.elem == other.elem  # line 253
    def __str__(self):  # line 254
        return self.opstr + quote(self.elem)  # line 255
    def __len__(self):  # line 256
        return len(self.elem) + 1  # line 257
    @_coconut_tco  # line 258
    def substitute(self, subs):  # line 258
        raise _coconut_tail_call(self.__class__, self.elem.substitute(subs))  # line 259
    @_coconut_tco  # line 260
    def find_unification(self, other):  # line 260
        if isinstance(other, self.__class__):  # line 261
            raise _coconut_tail_call(self.elem.find_unification, other.elem)  # line 262
        else:  # line 263
            return None  # line 264
    def resolve(self, **kwargs):  # line 265
        return self.__class__(self.elem.resolve(**kwargs)).simplify(**kwargs)  # line 266

class Not(UnaryOp):  # line 268
    __slots__ = ()  # line 269
    opstr = not_sym  # line 270
    @property  # line 271
    def neg(self):  # line 271
        return self.elem  # line 272
    @_coconut_tco  # line 273
    def simplify(self, **kwargs):  # line 273
        if top == self.neg:  # line 274
            return bot  # line 275
        elif bot == self.neg:  # line 276
            return top  # line 277
        elif isinstance(self.neg, Not):  # line 278
            raise _coconut_tail_call(self.neg.neg.simplify, **kwargs)  # line 279
        elif isinstance(self.neg, And):  # line 280
            return Or(*map(Not, self.neg.ands)).simplify(**kwargs)  # line 281
        elif isinstance(self.neg, Or):  # line 282
            return And(*map(Not, self.neg.ors)).simplify(**kwargs)  # line 283
        elif isinstance(self.neg, Imp):  # line 284
            ands = self.neg.conds + (Not(self.neg.concl),)  # line 285
            return And(*ands).simplify(**kwargs)  # line 286
        elif isinstance(self.neg, Exists):  # line 287
            raise _coconut_tail_call(ForAll, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  # line 288
        elif isinstance(self.neg, ForAll):  # line 289
            raise _coconut_tail_call(Exists, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  # line 290
        else:  # line 291
            raise _coconut_tail_call(Not, self.neg.simplify(**kwargs))  # line 292
    def contradicts(self, other, **kwargs):  # line 293
        return self.neg == other  # line 294
    @_coconut_tco  # line 295
    def resolve_against(self, other, **kwargs):  # line 295
        if isinstance(other, Or):  # line 296
            raise _coconut_tail_call(other.resolve_against, self, **kwargs)  # line 297
        elif self.neg.find_unification(other) is not None:  # line 298
            return bot  # line 299
        else:  # line 300
            return None  # line 301

class Quantifier(Expr):  # line 303
    __slots__ = ("var", "elem")  # line 304
    def __repr__(self):  # line 305
        return self.__class__.__name__ + "(" + str(self.var) + ", " + repr(self.elem) + ")"  # line 306
    def __str__(self):  # line 307
        return self.opstr + str(self.var) + ". " + quote(self.elem)  # line 308
    def __len__(self):  # line 309
        return len(self.elem) + len(self.var)  # line 310
    @_coconut_tco  # line 311
    def change_var(self, var):  # line 311
        """Create an equivalent expression with a new quantified variable."""  # line 312
        raise _coconut_tail_call(self.__class__, var, self.elem.substitute({self.var: var}))  # line 313
    @_coconut_tco  # line 314
    def change_elem(self, elem):  # line 314
        """Create an equivalent quantifier with a new expression."""  # line 315
        raise _coconut_tail_call(self.__class__, self.var, elem)  # line 316
    def __eq__(self, other):  # line 317
        if isinstance(other, self.__class__):  # line 318
            return self.elem == other.change_var(self.var).elem  # line 319
        else:  # line 320
            return False  # line 321
    @_coconut_tco  # line 322
    def substitute(self, subs):  # line 322
        raise _coconut_tail_call(self.__class__, self.var.substitute(subs).constant(), self.elem.substitute(subs))  # line 323
    @_coconut_tco  # line 324
    def make_free_in(self, other):  # line 324
        """Makes self free in other."""  # line 325
        var = self.var  # line 326
        newvar = var.prime()  # line 327
        while other != other.substitute({var: newvar}):  # line 328
            var, newvar = newvar, newvar.prime()  # line 329
        raise _coconut_tail_call(self.change_var, var)  # line 330
    def find_unification(self, other):  # line 331
        return self.make_free_in(other).elem.find_unification(other)  # line 332
    @_coconut_tco  # line 333
    def resolve_against(self, other, **kwargs):  # line 333
        if isinstance(other, Quantifier):  # line 334
            resolution = (_coconut.functools.partial(self.elem.resolve_against, **kwargs))(Not(other.elem).simplify(**kwargs))  # line 335
            if resolution is None:  # line 336
                return None  # line 337
            elif isinstance(other, ForAll):  # don't pull an Exists out of a ForAll  # line 338
                raise _coconut_tail_call((other.change_elem), (self.change_elem)(resolution))  # line 339
            else:  # line 340
                raise _coconut_tail_call((self.change_elem), (other.change_elem)(resolution))  # line 341
        else:  # line 342
            return super(Quantifier, self).resolve_against(other, **kwargs)  # line 343

class ForAll(Quantifier):  # line 345
    __slots__ = ()  # line 346
    opstr = forall_sym  # line 347
    def __init__(self, var, elem):  # line 348
        assert wff(elem), elem  # line 349
        assert isvar(var), var  # line 350
        self.var = var.variable()  # line 351
        self.elem = elem.substitute({var: self.var.variable()})  # line 352
    def simplify(self, **kwargs):  # line 353
        kwargs["in_forall"] = True  # line 354
        return self.__class__(self.var, self.elem.simplify(**kwargs)).drop_quantifier(**kwargs)  # line 355
    def resolve(self, **kwargs):  # line 356
        kwargs["in_forall"] = True  # line 357
        kwargs["variables"] = kwargs.get("variables", ()) + (self.var,)  # line 358
        return ForAll(self.var, self.elem.resolve(**kwargs)).simplify(dnf=False, **kwargs)  # line 359
    def drop_quantifier(self, nonempty_universe=True, **kwargs):  # line 360
        kwargs["nonempty_universe"] = nonempty_universe  # line 361
        if not nonempty_universe:  # line 362
            elem = self.elem  # line 363
            while isinstance(elem, Exists):  # line 364
                elem = elem.elem  # line 365
            if top == elem:  # line 366
                return elem  # line 367
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):  # line 368
            return self.elem  # line 369
        return self  # line 370
FA = ForAll  # line 371

class Exists(Quantifier):  # line 373
    __slots__ = ()  # line 374
    opstr = exists_sym  # line 375
    def __init__(self, var, elem):  # line 376
        assert wff(elem), elem  # line 377
        assert isvar(var), var  # line 378
        self.var = var.constant()  # line 379
        self.elem = elem.substitute({var: self.var.constant()})  # line 380
    def simplify(self, **kwargs):  # line 381
        kwargs["in_exists"] = True  # line 382
        return self.__class__(self.var, self.elem.simplify(**kwargs)).drop_quantifier(**kwargs)  # line 383
    def resolve(self, **kwargs):  # line 384
        kwargs["in_exists"] = True  # line 385
        variables = kwargs.get("variables")  # line 386
        if variables is None:  # line 387
            skolem_elem = self.elem  # line 388
        else:  # line 389
            skolem_var = Function(self.var.name, *variables)  # line 390
            skolem_elem = self.elem.substitute({self.var: skolem_var})  # line 391
        return Exists(self.var, skolem_elem.resolve(**kwargs)).simplify(dnf=False, **kwargs)  # line 392
    def drop_quantifier(self, nonempty_universe=True, **kwargs):  # line 393
        kwargs["nonempty_universe"] = nonempty_universe  # line 394
        if not nonempty_universe:  # line 395
            elem = self.elem  # line 396
            while isinstance(elem, ForAll):  # line 397
                elem = elem.elem  # line 398
            if bot == elem:  # line 399
                return elem  # line 400
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):  # line 401
            return self.elem  # line 402
        return self  # line 403
TE = Exists  # line 404

class BinaryOp(Expr):  # line 406
    __slots__ = ("elems",)  # line 407
    identity = None  # line 408
    def __new__(cls, *elems):  # line 409
        if not elems:  # line 410
            if cls.identity is None:  # line 411
                raise TypeError(cls.__name__ + " requires at least one argument")  # line 412
            else:  # line 413
                return cls.identity  # line 414
        elif len(elems) == 1:  # line 415
            assert wff(elems[0]), elems[0]  # line 416
            return elems[0]  # sometimes returns an instance of cls  # line 417
        else:  # line 418
            return super(BinaryOp, cls).__new__(cls)  # line 419
    def __init__(self, *elems):  # line 420
        if len(elems) > 1:  # __new__ should handle all other cases  # line 421
            assert len(elems) >= 2, elems  # line 422
            for x in elems:  # line 423
                assert wff(x), x  # line 424
            self.elems = elems  # line 425
    def __repr__(self):  # line 426
        return self.__class__.__name__ + "(" + ", ".join((repr(x) for x in self.elems)) + ")"  # line 427
    @_coconut_tco  # line 428
    def __str__(self):  # line 428
        raise _coconut_tail_call((" " + self.opstr + " ").join, (quote(x) for x in self.elems))  # line 429
    def __len__(self):  # line 430
        return sum(map(len, self.elems)) + 1  # line 431
    @_coconut_tco  # line 432
    def substitute(self, subs):  # line 432
        raise _coconut_tail_call((self.__class__), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.elems))  # line 433
    def resolve(self, **kwargs):  # line 434
        elems = (_coconut.functools.partial(map, lambda x: x.resolve(**kwargs)))(self.elems)  # line 435
        return self.__class__(*elems).simplify(**kwargs)  # line 436

class Imp(BinaryOp):  # line 438
    __slots__ = ()  # line 439
    opstr = imp_sym  # line 440
    @_coconut_tco  # line 441
    def __rshift__(self, other):  # line 441
        if isinstance(other, Imp):  # line 442
            raise _coconut_tail_call(Imp, self, *other.elems)  # line 443
        else:  # line 444
            raise _coconut_tail_call(Imp, self, other)  # line 445
    @_coconut_tco  # line 446
    def __lshift__(self, other):  # line 446
        raise _coconut_tail_call((Imp), *(other,) + self.elems)  # line 447
    @property  # line 448
    def conds(self):  # line 448
        return self.elems[:-1]  # line 449
    @property  # line 450
    def concl(self):  # line 450
        return self.elems[-1]  # line 451
    def __eq__(self, other):  # line 452
        return isinstance(other, self.__class__) and self.concl == other.concl and (unorderd_eq)(self.conds, other.conds)  # line 453
    def simplify(self, **kwargs):  # line 454
        ors = tuple(map(Not, self.conds)) + (self.concl,)  # line 455
        return Or(*ors).simplify(**kwargs)  # line 456

class BoolOp(BinaryOp):  # line 458
    __slots__ = ()  # line 459
    def __eq__(self, other):  # line 460
        return isinstance(other, self.__class__) and (unorderd_eq)(self.elems, other.elems)  # line 461
    @_coconut_tco  # line 462
    def merge(self):  # line 462
        """Merges nested copies of a boolean operator."""  # line 463
        elems = []  # line 464
        for x in self.elems:  # line 465
            if isinstance(x, self.__class__):  # line 466
                elems.extend(x.merge().elems)  # line 467
            else:  # line 468
                elems.append(x)  # line 469
        raise _coconut_tail_call(self.__class__, *elems)  # line 470
    @_coconut_tco  # line 471
    def dedupe(self):  # line 471
        """Removes duplicate elements from a boolean operator."""  # line 472
        elems = []  # line 473
        for x in self.elems:  # line 474
            if x not in elems:  # line 475
                elems.append(x)  # line 476
        raise _coconut_tail_call(self.__class__, *elems)  # line 477
    @_coconut_tco  # line 478
    def clean(self):  # line 478
        """Removes copies of the identity."""  # line 479
        raise _coconut_tail_call((self.__class__), *(_coconut.functools.partial(filter, _coconut.functools.partial(_coconut.operator.ne, self.identity)))(self.elems))  # line 480
    def prenex(self, **kwargs):  # line 481
        """Pulls quantifiers out."""  # line 482
        for i, x in enumerate(self.elems):  # line 483
            if isinstance(x, Quantifier) and self.can_prenex(x, **kwargs):  # line 484
                elems = self.elems[:i] + self.elems[i + 1:]  # line 485
                free_x = x.make_free_in(self.__class__(*elems))  # line 486
                elems += (free_x.elem,)  # line 487
                return free_x.change_elem(self.__class__(*elems)).simplify(**kwargs)  # line 488
        return self  # line 489

class Or(BoolOp):  # line 491
    __slots__ = ()  # line 492
    opstr = or_sym  # line 493
    identity = bot  # line 494
    @_coconut_tco  # line 495
    def __or__(self, other):  # line 495
        raise _coconut_tail_call((Or), *self.elems + (other,))  # line 496
    @property  # line 497
    def ors(self):  # line 497
        return self.elems  # line 498
    def distribute(self, **kwargs):  # line 499
        """If this Or contains an And, distribute into it."""  # line 500
        for i, x in enumerate(self.ors):  # line 501
            if isinstance(x, And):  # line 502
                ands = ((Or)(*(y,) + self.ors[:i] + self.ors[i + 1:]) for y in x.ands)  # line 503
                return And(*ands).simplify(**kwargs)  # line 504
        return self  # line 505
    def simplify(self, dnf=False, **kwargs):  # line 506
        kwargs["dnf"] = dnf  # line 507
        ors = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))(self.merge().ors)  # line 508
        out = Or(*ors).clean()  # line 509
        if isinstance(out, Or) and not dnf:  # line 510
            out = out.distribute(**kwargs)  # line 511
        if isinstance(out, Or):  # line 512
            out = out.merge().dedupe()  # line 513
        if isinstance(out, Or) and out.tautology(**kwargs):  # line 514
            out = top  # line 515
        if isinstance(out, Or):  # line 516
            out = out.prenex(**kwargs)  # line 517
        log_simplification(self, out, **kwargs)  # line 518
        return out  # line 519
    def tautology(self, **kwargs):  # line 520
        """Determines if the Or is a blatant tautology."""  # line 521
        for i, x in enumerate(self.ors):  # line 522
            if top == x:  # line 523
                return True  # line 524
            for y in self.ors[i + 1:]:  # line 525
                if x.contradicts(y, **kwargs):  # line 526
                    return True  # line 527
        return False  # line 528
    def can_prenex(self, other, nonempty_universe=True, in_forall=False, **kwargs):  # line 529
        kwargs["nonempty_universe"], kwargs["in_forall"] = nonempty_universe, in_forall  # line 530
        return (nonempty_universe or in_forall or not isinstance(other, Exists) or all((isinstance(x, Exists) for x in self.elems)))  # line 531
    @_coconut_tco  # line 532
    def resolve_against(self, other, **kwargs):  # line 535
        if isinstance(other, Or):  # line 536
            not_other_ors = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))((_coconut.functools.partial(map, Not))(other.ors))  # line 537
            for i, x in enumerate(self.ors):  # line 538
                for j, y in enumerate(not_other_ors):  # line 539
                    subs = x.find_unification(y)  # line 540
                    if subs is not None:  # line 541
                        raise _coconut_tail_call((Or), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.ors[:i] + self.ors[i + 1:] + other.ors[:j] + other.ors[j + 1:]))  # line 542
        else:  # line 543
            not_other = Not(other).simplify(**kwargs)  # line 544
            for i, x in enumerate(self.ors):  # line 545
                subs = x.find_unification(not_other)  # line 546
                if subs is not None:  # line 547
                    raise _coconut_tail_call((Or), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.ors[:i] + self.ors[i + 1:]))  # line 548
        return None  # line 549

class And(BoolOp):  # line 551
    __slots__ = ()  # line 552
    opstr = and_sym  # line 553
    identity = top  # line 554
    @_coconut_tco  # line 555
    def __and__(self, other):  # line 555
        raise _coconut_tail_call((And), *self.elems + (other,))  # line 556
    @property  # line 557
    def ands(self):  # line 557
        return self.elems  # line 558
    def distribute(self, **kwargs):  # line 559
        """If this And contains an Or, distribute into it."""  # line 560
        for i, x in enumerate(self.ands):  # line 561
            if isinstance(x, Or):  # line 562
                ors = ((And)(*(y,) + self.ands[:i] + self.ands[i + 1:]) for y in x.ors)  # line 563
                return Or(*ors).simplify(**kwargs)  # line 564
        return self  # line 565
    def simplify(self, dnf=False, **kwargs):  # line 566
        kwargs["dnf"] = dnf  # line 567
        ands = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))(self.merge().ands)  # line 568
        out = And(*ands).clean()  # line 569
        if isinstance(out, And) and dnf:  # line 570
            out = out.distribute(**kwargs)  # line 571
        if isinstance(out, And):  # line 572
            out = out.merge().dedupe()  # line 573
        if isinstance(out, And) and out.contradiction(**kwargs):  # line 574
            out = bot  # line 575
        if isinstance(out, And):  # line 576
            out = out.prenex(**kwargs)  # line 577
        log_simplification(self, out, **kwargs)  # line 578
        return out  # line 579
    def contradiction(self, **kwargs):  # line 580
        """Determines if the And is a blatant contradiction."""  # line 581
        for i, x in enumerate(self.ands):  # line 582
            if bot == x:  # line 583
                return True  # line 584
            for y in self.ands[i + 1:]:  # line 585
                if x.contradicts(y, **kwargs):  # line 586
                    return True  # line 587
        return False  # line 588
    def can_prenex(self, other, nonempty_universe=True, in_exists=False, **kwargs):  # line 589
        kwargs["nonempty_universe"], kwargs["in_exists"] = nonempty_universe, in_exists  # line 590
        return (nonempty_universe or in_exists or not isinstance(other, ForAll) or all((isinstance(x, ForAll) for x in self.elems)))  # line 591
    @_coconut_tco  # line 592
    def resolve(self, debug=False, **kwargs):  # line 595
        """Performs all possible resolutions within the And."""  # line 596
        kwargs["debug"] = debug  # line 597
        resolved = super(And, self).resolve(**kwargs)  # line 598
        if not isinstance(resolved, And):  # line 599
            log_simplification(self, resolved, **kwargs)  # line 600
            return resolved  # line 601
        clauses = (list)(resolved.ands)  # line 602
        quantifiers = []  # line 603
        prev_clause_len = 1  # line 604
        while prev_clause_len < len(clauses):  # line 605
            prev_clause_len = len(clauses)  # line 606
# reversed ensures conclusions get tested first
            for i in (reversed)(range(1, len(clauses))):  # line 608
                x = clauses[i]  # line 609
                for y in clauses[:i + 1]:  # allow resolution of a clause against itself  # line 610
                    resolution = x.resolve_against(y)  # line 611
                    if resolution is not None:  # line 612
                        resolution = resolution.simplify(dnf=False, **kwargs)  # line 613
                        if debug:  # line 614
                            print(x, "+", y, "=>", resolution)  # line 615
                        new_quantifiers = []  # line 616
                        while isinstance(resolution, Quantifier) and self.can_prenex(resolution, **kwargs):  # line 617
                            (new_quantifiers.append)(resolution.change_elem)  # line 618
                            resolution = resolution.elem  # line 619
                        if isinstance(resolution, And):  # line 620
                            new_clauses = resolution.ands  # line 621
                        else:  # line 622
                            new_clauses = (resolution,)  # line 623
                        if bot in new_clauses:  # line 624
                            quantifiers.extend(new_quantifiers)  # line 625
                            clauses = [bot]  # line 626
                            break  # line 627
                        novel = False  # line 628
                        for new_clause in new_clauses:  # line 629
                            if new_clause != top and new_clause not in clauses:  # line 630
                                clauses.append(new_clause)  # line 631
                                novel = True  # line 632
                        if novel:  # line 633
                            quantifiers.extend(new_quantifiers)  # line 634
                if clauses == [bot]:  # line 635
                    break  # line 636
        resolved = reduce(_coconut_pipe, [And(*clauses)] + quantifiers)  # line 637
        log_simplification(self, resolved, **kwargs)  # line 638
        raise _coconut_tail_call(resolved.simplify, dnf=False, **kwargs)  # line 639
