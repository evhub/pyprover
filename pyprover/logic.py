#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x43741860

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
    """Base class for all formulae."""  # line 32
    __slots__ = ()  # line 33
    @_coconut_tco  # line 34
    def __and__(self, other):  # line 34
        if isinstance(other, And):  # line 35
            return other & self  # line 36
        else:  # line 37
            raise _coconut_tail_call(And, self, other)  # line 38
    @_coconut_tco  # line 39
    def __or__(self, other):  # line 39
        if isinstance(other, Or):  # line 40
            return other | self  # line 41
        else:  # line 42
            raise _coconut_tail_call(Or, self, other)  # line 43
    @_coconut_tco  # line 44
    def __rshift__(self, other):  # line 44
        if isinstance(other, Implies):  # line 45
            return other << self  # line 46
        else:  # line 47
            raise _coconut_tail_call(Implies, self, other)  # line 48
    def __lshift__(self, other):  # line 49
        assert wff(other), other  # line 50
        return other >> self  # line 51
    @_coconut_tco  # line 52
    def __invert__(self):  # line 52
        raise _coconut_tail_call(Not, self)  # line 53
    @_coconut_tco  # line 54
    def __xor__(self, other):  # line 54
        raise _coconut_tail_call(Or, And(self, Not(other)), And(Not(self), other))  # line 55
    def __len__(self):  # line 56
        return 1  # line 56
    def __ne__(self, other):  # line 57
        return not self == other  # line 57
    def simplify(self, **kwargs):  # line 58
        """Simplify the given expression."""  # line 59
        return self  # line 60
    def substitute(self, subs):  # line 61
        """Substitutes a dictionary into the expression."""  # line 62
        return self  # line 63
    def resolve(self, **kwargs):  # line 64
        """Performs resolution on the clauses in a CNF expression."""  # line 65
        return self  # line 66
    def find_unification(self, other):  # line 67
        """Find a substitution in self that would make self into other."""  # line 68
        if self == other:  # line 69
            return {}  # line 70
        else:  # line 71
            return None  # line 72
    @_coconut_tco  # line 73
    def contradicts(self, other, **kwargs):  # line 73
        """Assuming self is simplified, determines if it contradicts other."""  # line 74
        if isinstance(other, Not):  # line 75
            raise _coconut_tail_call(other.contradicts, self, **kwargs)  # line 76
        else:  # line 77
            return self == Not(other).simplify(**kwargs)  # line 78
    @_coconut_tco  # line 79
    def resolve_against(self, other, **kwargs):  # line 79
        """Attempt to perform a resolution against other else None."""  # line 80
        if isinstance(other, (Not, Or)):  # line 81
            raise _coconut_tail_call(other.resolve_against, self, **kwargs)  # line 82
        elif (self.find_unification)(Not(other).simplify(**kwargs)) is not None:  # line 83
            return bot  # line 84
        else:  # line 85
            return None  # line 86

class Top(Expr):  # line 88
    """True"""  # line 89
    __slots__ = ()  # line 90
    @_coconut_tco  # line 91
    def __eq__(self, other):  # line 91
        raise _coconut_tail_call(isinstance, other, Top)  # line 91
    def __repr__(self):  # line 92
        return "top"  # line 92
    def __str__(self):  # line 93
        return top_sym  # line 93
    def __bool__(self):  # line 94
        return True  # line 94
top = true = Top()  # line 95

class Bot(Expr):  # line 97
    """False"""  # line 98
    __slots__ = ()  # line 99
    @_coconut_tco  # line 100
    def __eq__(self, other):  # line 100
        raise _coconut_tail_call(isinstance, other, Bot)  # line 100
    def __repr__(self):  # line 101
        return "bot"  # line 101
    def __str__(self):  # line 102
        return bot_sym  # line 102
    def __bool__(self):  # line 103
        return False  # line 103
bot = false = Bot()  # line 104

class Atom(Expr):  # line 106
    """Base class for all variables."""  # line 107
    __slots__ = ("name",)  # line 108
    def __init__(self, name):  # line 109
        if isinstance(name, Atom):  # line 110
            name = name.name  # line 111
        assert isinstance(name, str), name  # line 112
        self.name = name  # line 113
    def __repr__(self):  # line 114
        return self.__class__.__name__ + '("' + self.name + '")'  # line 115
    def __str__(self):  # line 116
        return self.name  # line 117
    def __eq__(self, other):  # line 118
        return isinstance(other, self.__class__) and self.name == other.name  # line 119
    @_coconut_tco  # line 120
    def __hash__(self):  # line 120
        raise _coconut_tail_call((hash), (self.__class__.__name__, self.name))  # line 121
    def substitute_elements(self, subs):  # line 122
        """Substitute for the elements of the Atom, not the Atom itself."""  # line 123
        return self  # line 124
    @_coconut_tco  # line 125
    def substitute(self, subs):  # line 125
        try:  # line 126
            sub = subs[self]  # line 127
        except KeyError:  # line 128
            raise _coconut_tail_call(self.substitute_elements, subs)  # line 129
        else:  # line 130
            if wff(sub):  # line 131
                return sub  # line 132
            elif sub is True:  # line 133
                return top  # line 134
            elif sub is False:  # line 135
                return bot  # line 136
            else:  # line 137
                raise TypeError("cannot perform substitution " + self + " => " + sub)  # line 138

class Prop(Atom):  # line 140
    """Logical proposition that is either true or false."""  # line 141
    __slots__ = ()  # line 142
    @_coconut_tco  # line 143
    def __call__(self, *args):  # line 143
        raise _coconut_tail_call(Predicate, self.name, *args)  # line 144
Proposition = Prop  # line 145

class FuncAtom(Atom):  # line 147
    """Base class for predicates and functions."""  # line 148
    __slots__ = ("args",)  # line 149
    def __init__(self, name, *args):  # line 150
        super(FuncAtom, self).__init__(name)  # line 151
        for arg in args:  # line 152
            assert isinstance(arg, Term), arg  # line 153
        self.args = args  # line 154
    def __repr__(self):  # line 155
        return self.__class__.__name__ + '("' + self.name + '"' + ", ".join((repr(x) for x in self.args)) + ")"  # line 156
    def __str__(self):  # line 157
        return self.name + "(" + ", ".join((str(x) for x in self.args)) + ")"  # line 158
    def __eq__(self, other):  # line 159
        return isinstance(other, self.__class__) and self.name == other.name and self.args == other.args  # line 160
    @_coconut_tco  # line 161
    def __hash__(self):  # line 161
        raise _coconut_tail_call((hash), (self.__class__.__name__, self.name, self.args))  # line 162
    def find_unification(self, other):  # line 163
        if isinstance(other, self.__class__) and self.name == other.name and len(self.args) == len(other.args):  # line 164
            subs = {}  # line 165
            for i, x in enumerate(self.args):  # line 166
                y = other.args[i]  # line 167
                unif = x.find_unification(y)  # line 168
                if unif is None:  # line 169
                    return None  # line 170
                for name, var in unif.items():  # line 171
                    if name not in subs:  # line 172
                        subs[name] = var  # line 173
                    elif subs[name] != var:  # line 174
                        return None  # line 175
            return subs  # line 176
        else:  # line 177
            return None  # line 178

class Pred(FuncAtom):  # line 180
    """Boolean function of terms."""  # line 181
    __slots__ = ()  # line 182
    @_coconut_tco  # line 183
    def proposition(self):  # line 183
        raise _coconut_tail_call(Proposition, self.name)  # line 184
    @_coconut_tco  # line 185
    def substitute_elements(self, subs):  # line 185
        try:  # line 186
            sub = subs[self.proposition()]  # line 187
        except KeyError:  # line 188
            raise _coconut_tail_call((_coconut.functools.partial(Predicate, self.name)), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.args))  # line 189
        else:  # line 190
            raise _coconut_tail_call(Predicate, sub.name, *self.args)  # line 191
Predicate = Pred  # line 192

class Term(Atom):  # line 194
    """Base class for all terms."""  # line 195
    __slots__ = ()  # line 196
    @_coconut_tco  # line 197
    def variable(self):  # line 197
        """Convert to a variable."""  # line 198
        raise _coconut_tail_call(Variable, self.name)  # line 199
    @_coconut_tco  # line 200
    def constant(self):  # line 200
        """Convert to a constant."""  # line 201
        raise _coconut_tail_call(Constant, self.name)  # line 202
    @_coconut_tco  # line 203
    def rename(self, name):  # line 203
        """Create a new term with a different name."""  # line 204
        raise _coconut_tail_call(self.__class__, name)  # line 205
    @_coconut_tco  # line 206
    def prime(self):  # line 206
        """Rename by adding a prime."""  # line 207
        raise _coconut_tail_call(self.rename, self.name + "'")  # line 208
    @_coconut_tco  # line 209
    def substitute(self, subs):  # line 209
        for var, sub in subs.items():  # line 210
            if isinstance(var, Term) and self.name == var.name:  # line 211
                if isvar(self) or self == var:  # line 212
                    return sub  # line 213
                else:  # line 214
                    raise _coconut_tail_call(self.rename, sub.name)  # line 215
        raise _coconut_tail_call(self.substitute_elements, subs)  # line 216

class Var(Term):  # line 218
    """A variable quantified by a ForAll."""  # line 219
    __slots__ = ()  # line 220
    def variable(self):  # line 221
        return self  # line 221
    @_coconut_tco  # line 222
    def __call__(self, *args):  # line 222
        raise _coconut_tail_call(Function, self.name, *args)  # line 223
    def find_unification(self, other):  # line 224
        if isinstance(other, Term):  # line 225
            return {self: other}  # line 226
        else:  # line 227
            return None  # line 228
Variable = Var  # line 229

class Const(Term):  # line 231
    """A variable quantified by an Exists."""  # line 232
    __slots__ = ()  # line 233
    def constant(self):  # line 234
        return self  # line 234
    @_coconut_tco  # line 235
    def __call__(self, *args):  # line 235
        raise _coconut_tail_call(Function, self.name, *args)  # line 236
    def find_unification(self, other):  # line 237
        if isinstance(other, Variable):  # line 238
            return {other: self}  # line 239
        else:  # line 240
            return super(Constant, self).find_unification(other)  # line 241
Constant = Const  # line 242

class Func(Term, FuncAtom):  # line 244
    """A function on terms."""  # line 245
    __slots__ = ()  # line 246
    @_coconut_tco  # line 247
    def substitute_elements(self, subs):  # line 247
        raise _coconut_tail_call((_coconut.functools.partial(Function, self.name)), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.args))  # line 248
    @_coconut_tco  # line 249
    def rename(self, name):  # line 249
        raise _coconut_tail_call(self.__class__, name, *self.args)  # line 250
    def find_unification(self, other):  # line 251
        if isinstance(other, Variable):  # line 252
            return {other: self}  # line 253
        else:  # line 254
            return super(Function, self).find_unification(other)  # line 255
Function = Func  # line 256

class UnaryOp(Expr):  # line 258
    """Base class for unary operators."""  # line 259
    __slots__ = ("elem",)  # line 260
    def __init__(self, elem):  # line 261
        assert wff(elem), elem  # line 262
        self.elem = elem  # line 263
    def __repr__(self):  # line 264
        return self.__class__.__name__ + "(" + repr(self.elem) + ")"  # line 265
    def __eq__(self, other):  # line 266
        return isinstance(other, self.__class__) and self.elem == other.elem  # line 267
    def __str__(self):  # line 268
        return self.opstr + quote(self.elem)  # line 269
    def __len__(self):  # line 270
        return len(self.elem) + 1  # line 271
    @_coconut_tco  # line 272
    def substitute(self, subs):  # line 272
        raise _coconut_tail_call(self.__class__, self.elem.substitute(subs))  # line 273
    @_coconut_tco  # line 274
    def find_unification(self, other):  # line 274
        if isinstance(other, self.__class__):  # line 275
            raise _coconut_tail_call(self.elem.find_unification, other.elem)  # line 276
        else:  # line 277
            return None  # line 278
    def resolve(self, **kwargs):  # line 279
        return self.__class__(self.elem.resolve(**kwargs)).simplify(**kwargs)  # line 280

class Not(UnaryOp):  # line 282
    """Logical not."""  # line 283
    __slots__ = ()  # line 284
    opstr = not_sym  # line 285
    @property  # line 286
    def neg(self):  # line 286
        return self.elem  # line 287
    @_coconut_tco  # line 288
    def simplify(self, **kwargs):  # line 288
        if top == self.neg:  # line 289
            return bot  # line 290
        elif bot == self.neg:  # line 291
            return top  # line 292
        elif isinstance(self.neg, Not):  # line 293
            raise _coconut_tail_call(self.neg.neg.simplify, **kwargs)  # line 294
        elif isinstance(self.neg, And):  # line 295
            return Or(*map(Not, self.neg.ands)).simplify(**kwargs)  # line 296
        elif isinstance(self.neg, Or):  # line 297
            return And(*map(Not, self.neg.ors)).simplify(**kwargs)  # line 298
        elif isinstance(self.neg, Implies):  # line 299
            ands = self.neg.conds + (Not(self.neg.concl),)  # line 300
            return And(*ands).simplify(**kwargs)  # line 301
        elif isinstance(self.neg, Exists):  # line 302
            raise _coconut_tail_call(ForAll, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  # line 303
        elif isinstance(self.neg, ForAll):  # line 304
            raise _coconut_tail_call(Exists, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  # line 305
        else:  # line 306
            raise _coconut_tail_call(Not, self.neg.simplify(**kwargs))  # line 307
    def contradicts(self, other, **kwargs):  # line 308
        return self.neg == other  # line 309
    @_coconut_tco  # line 310
    def resolve_against(self, other, **kwargs):  # line 310
        if isinstance(other, Or):  # line 311
            raise _coconut_tail_call(other.resolve_against, self, **kwargs)  # line 312
        elif self.neg.find_unification(other) is not None:  # line 313
            return bot  # line 314
        else:  # line 315
            return None  # line 316

class Quantifier(Expr):  # line 318
    """Base class for logical quantifiers."""  # line 319
    __slots__ = ("var", "elem")  # line 320
    def __repr__(self):  # line 321
        return self.__class__.__name__ + '("' + str(self.var) + '", ' + repr(self.elem) + ")"  # line 322
    def __str__(self):  # line 323
        return self.opstr + str(self.var) + ". " + quote(self.elem, in_quantifier=True)  # line 324
    def __len__(self):  # line 325
        return len(self.elem) + len(self.var)  # line 326
    @_coconut_tco  # line 327
    def change_var(self, var):  # line 327
        """Create an equivalent expression with a new quantified variable."""  # line 328
        raise _coconut_tail_call(self.__class__, var, self.elem.substitute({self.var: var}))  # line 329
    @_coconut_tco  # line 330
    def change_elem(self, elem):  # line 330
        """Create an equivalent quantifier with a new expression."""  # line 331
        raise _coconut_tail_call(self.__class__, self.var, elem)  # line 332
    def __eq__(self, other):  # line 333
        if isinstance(other, self.__class__):  # line 334
            return self.elem == other.change_var(self.var).elem  # line 335
        else:  # line 336
            return False  # line 337
    @_coconut_tco  # line 338
    def substitute(self, subs):  # line 338
        raise _coconut_tail_call(self.__class__, self.var.substitute(subs).constant(), self.elem.substitute(subs))  # line 339
    @_coconut_tco  # line 340
    def make_free_in(self, other):  # line 340
        """Makes self free in other."""  # line 341
        var = self.var  # line 342
        newvar = var.prime()  # line 343
        while other != other.substitute({var: newvar}):  # line 344
            var, newvar = newvar, newvar.prime()  # line 345
        raise _coconut_tail_call(self.change_var, var)  # line 346
    def find_unification(self, other):  # line 347
        return self.make_free_in(other).elem.find_unification(other)  # line 348
    @_coconut_tco  # line 349
    def resolve_against(self, other, **kwargs):  # line 349
        if isinstance(other, Quantifier):  # line 350
            resolution = (_coconut.functools.partial(self.elem.resolve_against, **kwargs))(Not(other.elem).simplify(**kwargs))  # line 351
            if resolution is None:  # line 352
                return None  # line 353
            elif isinstance(other, ForAll):  # don't pull an Exists out of a ForAll  # line 354
                raise _coconut_tail_call((other.change_elem), (self.change_elem)(resolution))  # line 355
            else:  # line 356
                raise _coconut_tail_call((self.change_elem), (other.change_elem)(resolution))  # line 357
        else:  # line 358
            return super(Quantifier, self).resolve_against(other, **kwargs)  # line 359

class ForAll(Quantifier):  # line 361
    """Universal quantifier."""  # line 362
    __slots__ = ()  # line 363
    opstr = forall_sym  # line 364
    def __init__(self, var, elem):  # line 365
        assert wff(elem), elem  # line 366
        if isinstance(var, str):  # line 367
            var = Constant(var)  # line 368
        assert isvar(var), var  # line 369
        self.var = var.variable()  # line 370
        self.elem = elem.substitute({var: self.var.variable()})  # line 371
    def simplify(self, **kwargs):  # line 372
        kwargs["in_forall"] = True  # line 373
        return self.__class__(self.var, self.elem.simplify(**kwargs)).drop_quantifier(**kwargs)  # line 374
    def resolve(self, **kwargs):  # line 375
        kwargs["in_forall"] = True  # line 376
        kwargs["variables"] = kwargs.get("variables", ()) + (self.var,)  # line 377
        return ForAll(self.var, self.elem.resolve(**kwargs)).simplify(dnf=False, **kwargs)  # line 378
    def drop_quantifier(self, nonempty_universe=True, **kwargs):  # line 379
        kwargs["nonempty_universe"] = nonempty_universe  # line 380
        if not nonempty_universe:  # line 381
            elem = self.elem  # line 382
            while isinstance(elem, Exists):  # line 383
                elem = elem.elem  # line 384
            if top == elem:  # line 385
                return elem  # line 386
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):  # line 387
            return self.elem  # line 388
        return self  # line 389
FA = ForAll  # line 390

class Exists(Quantifier):  # line 392
    """Existential quantifier."""  # line 393
    __slots__ = ()  # line 394
    opstr = exists_sym  # line 395
    def __init__(self, var, elem):  # line 396
        assert wff(elem), elem  # line 397
        if isinstance(var, str):  # line 398
            var = Constant(var)  # line 399
        assert isvar(var), var  # line 400
        self.var = var.constant()  # line 401
        self.elem = elem.substitute({var: self.var.constant()})  # line 402
    def simplify(self, **kwargs):  # line 403
        kwargs["in_exists"] = True  # line 404
        return self.__class__(self.var, self.elem.simplify(**kwargs)).drop_quantifier(**kwargs)  # line 405
    def resolve(self, **kwargs):  # line 406
        kwargs["in_exists"] = True  # line 407
        variables = kwargs.get("variables")  # line 408
        if variables is None:  # line 409
            skolem_elem = self.elem  # line 410
        else:  # line 411
            skolem_var = Function(self.var.name, *variables)  # line 412
            skolem_elem = self.elem.substitute({self.var: skolem_var})  # line 413
        return Exists(self.var, skolem_elem.resolve(**kwargs)).simplify(dnf=False, **kwargs)  # line 414
    def drop_quantifier(self, nonempty_universe=True, **kwargs):  # line 415
        kwargs["nonempty_universe"] = nonempty_universe  # line 416
        if not nonempty_universe:  # line 417
            elem = self.elem  # line 418
            while isinstance(elem, ForAll):  # line 419
                elem = elem.elem  # line 420
            if bot == elem:  # line 421
                return elem  # line 422
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):  # line 423
            return self.elem  # line 424
        return self  # line 425
TE = Exists  # line 426

class BinaryOp(Expr):  # line 428
    """Base class for binary operators."""  # line 429
    __slots__ = ("elems",)  # line 430
    identity = None  # line 431
    def __new__(cls, *elems):  # line 432
        if not elems:  # line 433
            if cls.identity is None:  # line 434
                raise TypeError(cls.__name__ + " requires at least one argument")  # line 435
            else:  # line 436
                return cls.identity  # line 437
        elif len(elems) == 1:  # line 438
            assert wff(elems[0]), elems[0]  # line 439
            return elems[0]  # sometimes returns an instance of cls  # line 440
        else:  # line 441
            return super(BinaryOp, cls).__new__(cls)  # line 442
    def __init__(self, *elems):  # line 443
        if len(elems) > 1:  # __new__ should handle all other cases  # line 444
            assert len(elems) >= 2, elems  # line 445
            for x in elems:  # line 446
                assert wff(x), x  # line 447
            self.elems = elems  # line 448
    def __repr__(self):  # line 449
        return self.__class__.__name__ + "(" + ", ".join((repr(x) for x in self.elems)) + ")"  # line 450
    @_coconut_tco  # line 451
    def __str__(self):  # line 451
        raise _coconut_tail_call((" " + self.opstr + " ").join, (quote(x) for x in self.elems))  # line 452
    def __len__(self):  # line 453
        return sum(map(len, self.elems)) + 1  # line 454
    @_coconut_tco  # line 455
    def substitute(self, subs):  # line 455
        raise _coconut_tail_call((self.__class__), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.elems))  # line 456
    def resolve(self, **kwargs):  # line 457
        elems = (_coconut.functools.partial(map, lambda x: x.resolve(**kwargs)))(self.elems)  # line 458
        return self.__class__(*elems).simplify(**kwargs)  # line 459

class Imp(BinaryOp):  # line 461
    """Logical implication."""  # line 462
    __slots__ = ()  # line 463
    opstr = imp_sym  # line 464
    @_coconut_tco  # line 465
    def __rshift__(self, other):  # line 465
        if isinstance(other, Implies):  # line 466
            raise _coconut_tail_call(Implies, self, *other.elems)  # line 467
        else:  # line 468
            raise _coconut_tail_call(Implies, self, other)  # line 469
    @_coconut_tco  # line 470
    def __lshift__(self, other):  # line 470
        raise _coconut_tail_call((Implies), *(other,) + self.elems)  # line 471
    @property  # line 472
    def conds(self):  # line 472
        return self.elems[:-1]  # line 473
    @property  # line 474
    def concl(self):  # line 474
        return self.elems[-1]  # line 475
    def __eq__(self, other):  # line 476
        return isinstance(other, self.__class__) and self.concl == other.concl and (unorderd_eq)(self.conds, other.conds)  # line 477
    def simplify(self, **kwargs):  # line 478
        ors = tuple(map(Not, self.conds)) + (self.concl,)  # line 479
        return Or(*ors).simplify(**kwargs)  # line 480
Implies = Imp  # line 481

class BoolOp(BinaryOp):  # line 483
    """Base class for Or and And."""  # line 484
    __slots__ = ()  # line 485
    def __eq__(self, other):  # line 486
        return isinstance(other, self.__class__) and (unorderd_eq)(self.elems, other.elems)  # line 487
    @_coconut_tco  # line 488
    def merge(self):  # line 488
        """Merges nested copies of a boolean operator."""  # line 489
        elems = []  # line 490
        for x in self.elems:  # line 491
            if isinstance(x, self.__class__):  # line 492
                elems.extend(x.merge().elems)  # line 493
            else:  # line 494
                elems.append(x)  # line 495
        raise _coconut_tail_call(self.__class__, *elems)  # line 496
    @_coconut_tco  # line 497
    def dedupe(self):  # line 497
        """Removes duplicate elements from a boolean operator."""  # line 498
        elems = []  # line 499
        for x in self.elems:  # line 500
            if x not in elems:  # line 501
                elems.append(x)  # line 502
        raise _coconut_tail_call(self.__class__, *elems)  # line 503
    @_coconut_tco  # line 504
    def clean(self):  # line 504
        """Removes copies of the identity."""  # line 505
        raise _coconut_tail_call((self.__class__), *(_coconut.functools.partial(filter, _coconut.functools.partial(_coconut.operator.ne, self.identity)))(self.elems))  # line 506
    def prenex(self, **kwargs):  # line 507
        """Pulls quantifiers out."""  # line 508
        for i, x in enumerate(self.elems):  # line 509
            if isinstance(x, Quantifier) and self.can_prenex(x, **kwargs):  # line 510
                elems = self.elems[:i] + self.elems[i + 1:]  # line 511
                free_x = x.make_free_in(self.__class__(*elems))  # line 512
                elems += (free_x.elem,)  # line 513
                return free_x.change_elem(self.__class__(*elems)).simplify(**kwargs)  # line 514
        return self  # line 515

class Or(BoolOp):  # line 517
    """Logical disjunction."""  # line 518
    __slots__ = ()  # line 519
    opstr = or_sym  # line 520
    identity = bot  # line 521
    @_coconut_tco  # line 522
    def __or__(self, other):  # line 522
        raise _coconut_tail_call((Or), *self.elems + (other,))  # line 523
    @property  # line 524
    def ors(self):  # line 524
        return self.elems  # line 525
    def distribute(self, **kwargs):  # line 526
        """If this Or contains an And, distribute into it."""  # line 527
        for i, x in enumerate(self.ors):  # line 528
            if isinstance(x, And):  # line 529
                ands = ((Or)(*(y,) + self.ors[:i] + self.ors[i + 1:]) for y in x.ands)  # line 530
                return And(*ands).simplify(**kwargs)  # line 531
        return self  # line 532
    def simplify(self, dnf=False, **kwargs):  # line 533
        kwargs["dnf"] = dnf  # line 534
        ors = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))(self.merge().ors)  # line 535
        out = Or(*ors).clean()  # line 536
        if isinstance(out, Or) and not dnf:  # line 537
            out = out.distribute(**kwargs)  # line 538
        if isinstance(out, Or):  # line 539
            out = out.merge().dedupe()  # line 540
        if isinstance(out, Or) and out.tautology(**kwargs):  # line 541
            out = top  # line 542
        if isinstance(out, Or):  # line 543
            out = out.prenex(**kwargs)  # line 544
        log_simplification(self, out, **kwargs)  # line 545
        return out  # line 546
    def tautology(self, **kwargs):  # line 547
        """Determines if the Or is a blatant tautology."""  # line 548
        for i, x in enumerate(self.ors):  # line 549
            if top == x:  # line 550
                return True  # line 551
            for y in self.ors[i + 1:]:  # line 552
                if x.contradicts(y, **kwargs):  # line 553
                    return True  # line 554
        return False  # line 555
    def can_prenex(self, other, nonempty_universe=True, in_forall=False, **kwargs):  # line 556
        kwargs["nonempty_universe"], kwargs["in_forall"] = nonempty_universe, in_forall  # line 557
        return (nonempty_universe or in_forall or not isinstance(other, Exists) or all((isinstance(x, Exists) for x in self.elems)))  # line 558
    @_coconut_tco  # line 559
    def resolve_against(self, other, **kwargs):  # line 562
        if isinstance(other, Or):  # line 563
            not_other_ors = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))((_coconut.functools.partial(map, Not))(other.ors))  # line 564
            for i, x in enumerate(self.ors):  # line 565
                for j, y in enumerate(not_other_ors):  # line 566
                    subs = x.find_unification(y)  # line 567
                    if subs is not None:  # line 568
                        raise _coconut_tail_call((Or), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.ors[:i] + self.ors[i + 1:] + other.ors[:j] + other.ors[j + 1:]))  # line 569
        else:  # line 570
            not_other = Not(other).simplify(**kwargs)  # line 571
            for i, x in enumerate(self.ors):  # line 572
                subs = x.find_unification(not_other)  # line 573
                if subs is not None:  # line 574
                    raise _coconut_tail_call((Or), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.ors[:i] + self.ors[i + 1:]))  # line 575
        return None  # line 576

class And(BoolOp):  # line 578
    """Logical conjunction."""  # line 579
    __slots__ = ()  # line 580
    opstr = and_sym  # line 581
    identity = top  # line 582
    @_coconut_tco  # line 583
    def __and__(self, other):  # line 583
        raise _coconut_tail_call((And), *self.elems + (other,))  # line 584
    @property  # line 585
    def ands(self):  # line 585
        return self.elems  # line 586
    def distribute(self, **kwargs):  # line 587
        """If this And contains an Or, distribute into it."""  # line 588
        for i, x in enumerate(self.ands):  # line 589
            if isinstance(x, Or):  # line 590
                ors = ((And)(*(y,) + self.ands[:i] + self.ands[i + 1:]) for y in x.ors)  # line 591
                return Or(*ors).simplify(**kwargs)  # line 592
        return self  # line 593
    def simplify(self, dnf=False, **kwargs):  # line 594
        kwargs["dnf"] = dnf  # line 595
        ands = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))(self.merge().ands)  # line 596
        out = And(*ands).clean()  # line 597
        if isinstance(out, And) and dnf:  # line 598
            out = out.distribute(**kwargs)  # line 599
        if isinstance(out, And):  # line 600
            out = out.merge().dedupe()  # line 601
        if isinstance(out, And) and out.contradiction(**kwargs):  # line 602
            out = bot  # line 603
        if isinstance(out, And):  # line 604
            out = out.prenex(**kwargs)  # line 605
        log_simplification(self, out, **kwargs)  # line 606
        return out  # line 607
    def contradiction(self, **kwargs):  # line 608
        """Determines if the And is a blatant contradiction."""  # line 609
        for i, x in enumerate(self.ands):  # line 610
            if bot == x:  # line 611
                return True  # line 612
            for y in self.ands[i + 1:]:  # line 613
                if x.contradicts(y, **kwargs):  # line 614
                    return True  # line 615
        return False  # line 616
    def can_prenex(self, other, nonempty_universe=True, in_exists=False, **kwargs):  # line 617
        kwargs["nonempty_universe"], kwargs["in_exists"] = nonempty_universe, in_exists  # line 618
        return (nonempty_universe or in_exists or not isinstance(other, ForAll) or all((isinstance(x, ForAll) for x in self.elems)))  # line 619
    @_coconut_tco  # line 620
    def resolve(self, debug=False, **kwargs):  # line 623
        """Performs all possible resolutions within the And."""  # line 624
        kwargs["debug"] = debug  # line 625
        resolved = super(And, self).resolve(**kwargs)  # line 626
        if not isinstance(resolved, And):  # line 627
            log_simplification(self, resolved, **kwargs)  # line 628
            return resolved  # line 629
        clauses = (list)(resolved.ands)  # line 630
        quantifiers = []  # line 631
        prev_clause_len = 1  # line 632
        while prev_clause_len < len(clauses):  # line 633
            prev_clause_len = len(clauses)  # line 634
# reversed ensures conclusions get tested first
            for i in (reversed)(range(1, len(clauses))):  # line 636
                x = clauses[i]  # line 637
                for y in clauses[:i + 1]:  # allow resolution of a clause against itself  # line 638
                    resolution = x.resolve_against(y)  # line 639
                    if resolution is not None:  # line 640
                        resolution = resolution.simplify(dnf=False, **kwargs)  # line 641
                        if debug:  # line 642
                            print(x, "+", y, "=>", resolution)  # line 643
                        new_quantifiers = []  # line 644
                        while isinstance(resolution, Quantifier) and self.can_prenex(resolution, **kwargs):  # line 645
                            (new_quantifiers.append)(resolution.change_elem)  # line 646
                            resolution = resolution.elem  # line 647
                        if isinstance(resolution, And):  # line 648
                            new_clauses = resolution.ands  # line 649
                        else:  # line 650
                            new_clauses = (resolution,)  # line 651
                        if bot in new_clauses:  # line 652
                            quantifiers.extend(new_quantifiers)  # line 653
                            clauses = [bot]  # line 654
                            break  # line 655
                        novel = False  # line 656
                        for new_clause in new_clauses:  # line 657
                            if new_clause != top and new_clause not in clauses:  # line 658
                                clauses.append(new_clause)  # line 659
                                novel = True  # line 660
                        if novel:  # line 661
                            quantifiers.extend(new_quantifiers)  # line 662
                if bot in clauses:  # line 663
                    break  # line 664
        resolved = reduce(_coconut_pipe, [And(*clauses)] + quantifiers)  # line 665
        log_simplification(self, resolved, **kwargs)  # line 666
        raise _coconut_tail_call(resolved.simplify, dnf=False, **kwargs)  # line 667
