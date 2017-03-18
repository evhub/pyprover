#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x3d154e7c

# Compiled with Coconut version 1.2.2-post_dev7 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------

# Imports:

from pyprover.constants import top_sym
from pyprover.constants import bot_sym
from pyprover.constants import not_sym
from pyprover.constants import imp_sym
from pyprover.constants import and_sym
from pyprover.constants import or_sym
from pyprover.constants import forall_sym
from pyprover.constants import exists_sym
from pyprover.constants import empty_var
from pyprover.util import unorderd_eq
from pyprover.util import quote
from pyprover.util import log_simplification
from pyprover.util import rem_var
from pyprover.util import can_sub
from pyprover.util import do_sub
from pyprover.util import merge_dicts
from pyprover.util import sub_once

# Functions:

def wff(expr):
    """Determines whether expr is a well-formed formula."""
    return isinstance(expr, Expr) and not isinstance(expr, Term)

@_coconut_tco
def isvar(var):
    """Whether a term is a variable."""
    raise _coconut_tail_call(isinstance, var, (Const, Var))

# Classes:

class Expr(_coconut.object):
    """Base class for all formulae."""
    __slots__ = ()
    @_coconut_tco
    def __and__(self, other):
        if isinstance(other, And):
            return other & self
        else:
            raise _coconut_tail_call(And, self, other)
    @_coconut_tco
    def __or__(self, other):
        if isinstance(other, Or):
            return other | self
        else:
            raise _coconut_tail_call(Or, self, other)
    @_coconut_tco
    def __rshift__(self, other):
        if isinstance(other, Imp):
            return other << self
        else:
            raise _coconut_tail_call(Imp, self, other)
    def __lshift__(self, other):
        assert wff(other), other
        return other >> self
    @_coconut_tco
    def __invert__(self):
        raise _coconut_tail_call(Not, self)
    @_coconut_tco
    def __xor__(self, other):
        raise _coconut_tail_call(Or, And(self, Not(other)), And(Not(self), other))
    def __len__(self):
        return 1
    def __ne__(self, other):
        return not self == other
    def simplify(self, **kwargs):
        """Simplify the given expression."""
        return self
    def substitute(self, subs, **kwargs):
        """Substitutes a dictionary into the expression."""
        return self
    @_coconut_tco
    def resolve(self, **kwargs):
        """Performs resolution on the clauses in a CNF expression."""
        raise _coconut_tail_call(self.simplify, dnf=False, **kwargs)
    @_coconut_tco
    def find_unification(self, other):
        """Find a substitution in self that would make self into other."""
        if isinstance(other, Quantifier):
            raise _coconut_tail_call(other.find_unification, self)
        elif self == other:
            return {}
        else:
            return None
    @_coconut_tco
    def contradicts(self, other, **kwargs):
        """Assuming self is simplified, determines if it contradicts other."""
        if isinstance(other, Not):
            raise _coconut_tail_call(other.contradicts, self, **kwargs)
        else:
            return self == Not(other).simplify(**kwargs)
    @_coconut_tco
    def resolve_against(self, other, **kwargs):
        """Attempt to perform a resolution against other else None."""
        if isinstance(other, (Not, Or, Eq)):
            raise _coconut_tail_call(other.resolve_against, self, **kwargs)
        elif (self.find_unification)(Not(other).simplify(**kwargs)) is not None:
            return bot
        else:
            return None
    def admits_empty_universe(self):
        """Determines if self allows for the possibility of an empty universe."""
        return True

class Top(Expr):
    """True"""
    __slots__ = ()
    @_coconut_tco
    def __eq__(self, other):
        raise _coconut_tail_call(isinstance, other, Top)
    def __repr__(self):
        return "top"
    def __str__(self):
        return top_sym
    def __bool__(self):
        return True
top = true = Top()

class Bot(Expr):
    """False"""
    __slots__ = ()
    @_coconut_tco
    def __eq__(self, other):
        raise _coconut_tail_call(isinstance, other, Bot)
    def __repr__(self):
        return "bot"
    def __str__(self):
        return bot_sym
    def __bool__(self):
        return False
    def admits_empty_universe(self):
        return False
bot = false = Bot()

class Atom(Expr):
    """Base class for all variables."""
    __slots__ = ("name",)
    def __init__(self, name):
        if isinstance(name, Atom):
            name = name.name
        assert isinstance(name, str), name
        self.name = name
    def __repr__(self):
        return self.__class__.__name__ + '("' + self.name + '")'
    def __str__(self):
        return self.name
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name
    @_coconut_tco
    def __hash__(self):
        raise _coconut_tail_call((hash), (self.__class__.__name__, self.name))
    def substitute_elements(self, subs, **kwargs):
        """Substitute for the elements of the Atom, not the Atom itself."""
        return self
    @_coconut_tco
    def substitute(self, subs, **kwargs):
        if not can_sub(kwargs):
            return self
        try:
            sub = subs[self]
        except KeyError:
            raise _coconut_tail_call(self.substitute_elements, subs, **kwargs)
        else:
            do_sub(kwargs)
            if wff(sub):
                return sub
            elif sub is True:
                return top
            elif sub is False:
                return bot
            else:
                raise TypeError("cannot perform substitution " + self + " => " + sub)

class Prop(Atom):
    """Logical proposition that is either true or false."""
    __slots__ = ()
    @_coconut_tco
    def __call__(self, *args):
        raise _coconut_tail_call(Pred, self.name, *args)
Proposition = Prop

class FuncAtom(Atom):
    """Base class for predicates and functions."""
    __slots__ = ("args",)
    def __init__(self, name, *args):
        super(FuncAtom, self).__init__(name)
        for arg in args:
            assert isinstance(arg, Term), arg
        self.args = args
    def __repr__(self):
        return self.__class__.__name__ + '("' + self.name + '"' + (", " if self.args else "") + ", ".join((repr(x) for x in self.args)) + ")"
    def __str__(self):
        return self.name + "(" + ", ".join((str(x) for x in self.args)) + ")"
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name and self.args == other.args
    @_coconut_tco
    def __hash__(self):
        raise _coconut_tail_call((hash), (self.__class__.__name__, self.name, self.args))
    @_coconut_tco
    def find_unification(self, other):
        if isinstance(other, Quantifier):
            raise _coconut_tail_call(other.find_unification, self)
        elif isinstance(other, self.__class__) and self.name == other.name and len(self.args) == len(other.args):
            subs = {}
            for i, x in enumerate(self.args):
                y = other.args[i]
                unif = x.find_unification(y)
                if unif is None:
                    return None
                for var, sub in unif.items():
                    if var not in subs:
                        subs[var] = sub
                    elif subs[var] != sub:
                        return None
            return subs
        else:
            return None
    @_coconut_tco
    def admits_empty_universe(self):
        raise _coconut_tail_call(all, (x.admits_empty_universe() for x in self.args))

class Pred(FuncAtom):
    """Boolean function of terms."""
    __slots__ = ()
    @_coconut_tco
    def proposition(self):
        raise _coconut_tail_call(Prop, self.name)
    @_coconut_tco
    def substitute_elements(self, subs, **kwargs):
        if not can_sub(kwargs):
            return self
        try:
            sub = subs[self.proposition()]
        except KeyError:
            name = self.name
        else:
            assert isinstance(sub, Atom), sub
            do_sub(kwargs)
            name = sub.name
        if can_sub(kwargs):
            raise _coconut_tail_call((_coconut.functools.partial(Pred, name)), *(_coconut.functools.partial(map, lambda x: x.substitute(subs, **kwargs)))(self.args))
        else:
            raise _coconut_tail_call(Pred, name, *self.args)
Predicate = Pred

class Term(Atom):
    """Base class for all terms."""
    __slots__ = ()
    @_coconut_tco
    def variable(self):
        """Convert to a variable."""
        raise _coconut_tail_call(Var, self.name)
    @_coconut_tco
    def constant(self):
        """Convert to a constant."""
        raise _coconut_tail_call(Const, self.name)
    @_coconut_tco
    def rename(self, name):
        """Create a new term with a different name."""
        raise _coconut_tail_call(self.__class__, name)
    @_coconut_tco
    def prime(self):
        """Rename by adding a prime."""
        raise _coconut_tail_call(self.rename, self.name + "'")
    @_coconut_tco
    def substitute(self, subs, **kwargs):
        if can_sub(kwargs):
            for var, sub in subs.items():
                if can_sub(kwargs) and isinstance(var, Term) and self.name == var.name:
                    do_sub(kwargs)
                    if isvar(self) or self == var:
                        return sub
                    else:
                        raise _coconut_tail_call(self.rename, sub.name)
        if can_sub(kwargs):
            raise _coconut_tail_call(self.substitute_elements, subs, **kwargs)
        return self

class Var(Term):
    """A variable quantified by a ForAll."""
    __slots__ = ()
    def variable(self):
        return self
    @_coconut_tco
    def __call__(self, *args):
        raise _coconut_tail_call(Func, self.name, *args)
    def find_unification(self, other):
        if isinstance(other, Term):
            return {self: other}
        else:
            return None
Variable = Var

class Const(Term):
    """A variable quantified by an Exists."""
    __slots__ = ()
    def constant(self):
        return self
    @_coconut_tco
    def __call__(self, *args):
        raise _coconut_tail_call(Func, self.name, *args)
    def find_unification(self, other):
        if isinstance(other, Var):
            return {other: self}
        else:
            return super(Const, self).find_unification(other)
    def admits_empty_universe(self):
        return False
Constant = Const

class Func(Term, FuncAtom):
    """A function on terms."""
    __slots__ = ()
    @_coconut_tco
    def substitute_elements(self, subs, **kwargs):
        raise _coconut_tail_call((_coconut.functools.partial(Func, self.name)), *(_coconut.functools.partial(map, lambda x: x.substitute(subs, **kwargs)))(self.args))
    @_coconut_tco
    def rename(self, name):
        raise _coconut_tail_call(self.__class__, name, *self.args)
    def find_unification(self, other):
        if isinstance(other, Var):
            return {other: self}
        else:
            return super(Func, self).find_unification(other)
Function = Func

class UnaryOp(Expr):
    """Base class for unary operators."""
    __slots__ = ("elem",)
    def __init__(self, elem):
        assert wff(elem), elem
        self.elem = elem
    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.elem) + ")"
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.elem == other.elem
    def __str__(self):
        return self.opstr + quote(self.elem)
    def __len__(self):
        return len(self.elem) + 1
    @_coconut_tco
    def substitute(self, subs, **kwargs):
        raise _coconut_tail_call(self.__class__, self.elem.substitute(subs, **kwargs))
    @_coconut_tco
    def find_unification(self, other):
        if isinstance(other, Quantifier):
            raise _coconut_tail_call(other.find_unification, self)
        elif isinstance(other, self.__class__):
            raise _coconut_tail_call(self.elem.find_unification, other.elem)
        else:
            return None
    def resolve(self, **kwargs):
        return self.__class__(self.elem.resolve(**kwargs)).simplify(dnf=False, **kwargs)

class Not(UnaryOp):
    """Logical not."""
    __slots__ = ()
    opstr = not_sym
    @property
    def neg(self):
        return self.elem
    @_coconut_tco
    def simplify(self, **kwargs):
        if top == self.neg:
            return bot
        elif bot == self.neg:
            return top
        elif isinstance(self.neg, Not):
            raise _coconut_tail_call(self.neg.neg.simplify, **kwargs)
        elif isinstance(self.neg, And):
            return Or(*map(Not, self.neg.ands)).simplify(**kwargs)
        elif isinstance(self.neg, Or):
            return And(*map(Not, self.neg.ors)).simplify(**kwargs)
        elif isinstance(self.neg, Imp):
            ands = self.neg.conds + (Not(self.neg.concl),)
            return And(*ands).simplify(**kwargs)
        elif isinstance(self.neg, Exists):
            raise _coconut_tail_call(ForAll, self.neg.var, Not(self.neg.elem).simplify(**kwargs))
        elif isinstance(self.neg, ForAll):
            raise _coconut_tail_call(Exists, self.neg.var, Not(self.neg.elem).simplify(**kwargs))
        else:
            raise _coconut_tail_call(Not, self.neg.simplify(**kwargs))
    def contradicts(self, other, **kwargs):
        return self.neg == other
    @_coconut_tco
    def resolve_against(self, other, **kwargs):
        if isinstance(other, (Or, Eq)):
            raise _coconut_tail_call(other.resolve_against, self, **kwargs)
        elif self.neg.find_unification(other) is not None:
            return bot
        else:
            return None
    @_coconut_tco
    def admits_empty_universe(self):
        if isinstance(self.neg, Atom):
            raise _coconut_tail_call(self.neg.admits_empty_universe)
        else:
            return not self.neg.admits_empty_universe()

class Quantifier(Expr):
    """Base class for logical quantifiers."""
    __slots__ = ("var", "elem")
    def __repr__(self):
        return self.__class__.__name__ + '("' + str(self.var) + '", ' + repr(self.elem) + ")"
    def __str__(self):
        return self.opstr + str(self.var) + ". " + quote(self.elem, in_quantifier=True)
    def __len__(self):
        return len(self.elem) + len(self.var)
    @_coconut_tco
    def change_var(self, var):
        """Create an equivalent expression with a new quantified variable."""
        raise _coconut_tail_call(self.__class__, var, self.elem.substitute({self.var: var}))
    @_coconut_tco
    def change_elem(self, elem):
        """Create an equivalent quantifier with a new expression."""
        raise _coconut_tail_call(self.__class__, self.var, elem)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.elem == other.change_var(self.var).elem
        else:
            return False
    def inner_kwargs(self, kwargs):
        inner_kwargs = kwargs.copy()
        inner_kwargs["in_" + self.__class__.__name__.lower()] = True
        return inner_kwargs
    def simplify(self, **kwargs):
        return self.__class__(self.var, self.elem.simplify(**self.inner_kwargs(kwargs))).drop_quantifier(**kwargs)
    @_coconut_tco
    def substitute(self, subs, **kwargs):
        raise _coconut_tail_call((self.change_elem), (_coconut.functools.partial(self.elem.substitute, **kwargs))((_coconut.functools.partial(rem_var, self.var))(subs)))
    @_coconut_tco
    def make_free_in(self, other):
        """Makes self free in other."""
        var = self.var
        newvar = var.prime()
        while other != other.substitute({var: newvar}):
            var, newvar = newvar, newvar.prime()
        raise _coconut_tail_call(self.change_var, var)
    @_coconut_tco
    def find_unification(self, other):
        unif = self.elem.find_unification(other)
        if unif is None:
            return None
        else:
            raise _coconut_tail_call((_coconut.functools.partial(rem_var, self.var)), unif)
    @_coconut_tco
    def resolve_against(self, other, **kwargs):
        if isinstance(other, Quantifier):
            resolution = (_coconut.functools.partial(self.elem.resolve_against, **kwargs))(Not(other.elem).simplify(**kwargs))
            if resolution is None:
                return None
            elif isinstance(other, ForAll):  # don't pull an Exists out of a ForAll
                raise _coconut_tail_call((other.change_elem), (self.change_elem)(resolution))
            else:
                raise _coconut_tail_call((self.change_elem), (other.change_elem)(resolution))
        else:
            return super(Quantifier, self).resolve_against(other, **kwargs)
    @classmethod
    def blank(cls, elem=top):
        """Make a quantifier without a variable (or optionally elem)."""
        return cls(empty_var, elem).make_free_in(elem)

class ForAll(Quantifier):
    """Universal quantifier."""
    __slots__ = ()
    opstr = forall_sym
    def __init__(self, var, elem):
        assert wff(elem), elem
        if isinstance(var, str):
            var = Const(var)
        assert isvar(var), var
        self.var = var.variable()
        self.elem = elem.substitute({var: self.var.variable()})
    def resolve(self, **kwargs):
        inner_kwargs = self.inner_kwargs(kwargs)
        inner_kwargs["variables"] = kwargs.get("variables", ()) + (self.var,)
        return ForAll(self.var, self.elem.resolve(**inner_kwargs)).simplify(dnf=False, **kwargs)
    def drop_quantifier(self, nonempty_universe=True, in_forall=False, **kwargs):
        kwargs["nonempty_universe"], kwargs["in_forall"] = nonempty_universe, in_forall
        if not nonempty_universe and not in_forall:
            elem = self.elem
            while isinstance(elem, Exists):
                elem = elem.elem
            if top == elem:
                return elem
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):
            return self.elem
        return self
FA = ForAll

class Exists(Quantifier):
    """Existential quantifier."""
    __slots__ = ()
    opstr = exists_sym
    def __init__(self, var, elem):
        assert wff(elem), elem
        if isinstance(var, str):
            var = Const(var)
        assert isvar(var), var
        self.var = var.constant()
        self.elem = elem.substitute({var: self.var.constant()})
    def resolve(self, **kwargs):
        inner_kwargs = self.inner_kwargs(kwargs)
        variables = inner_kwargs.get("variables")
        if variables is None:
            skolem_elem = self.elem
        else:
            skolem_var = Func(self.var.name, *variables)
            skolem_elem = self.elem.substitute({self.var: skolem_var})
        return Exists(self.var, skolem_elem.resolve(**inner_kwargs)).simplify(dnf=False, **kwargs)
    def drop_quantifier(self, nonempty_universe=True, in_exists=False, **kwargs):
        kwargs["nonempty_universe"], kwargs["in_exists"] = nonempty_universe, in_exists
        if not nonempty_universe and not in_exists:
            elem = self.elem
            while isinstance(elem, ForAll):
                elem = elem.elem
            if bot == elem:
                return elem
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):
            return self.elem
        return self
    def admits_empty_universe(self):
        return False
TE = Exists

class BinaryOp(Expr):
    """Base class for binary operators."""
    __slots__ = ("elems",)
    identity = None
    def __new__(cls, *elems):
        if not elems:
            if cls.identity is None:
                raise TypeError(cls.__name__ + " requires at least one argument")
            else:
                return cls.identity
        elif len(elems) == 1:
            assert wff(elems[0]), elems[0]
            return elems[0]  # sometimes returns an instance of cls
        else:
            return super(BinaryOp, cls).__new__(cls)
    def __init__(self, *elems):
        if len(elems) > 1:  # __new__ should handle all other cases
            assert len(elems) >= 2, elems
            for x in elems:
                assert wff(x), x
            self.elems = elems
    def __repr__(self):
        return self.__class__.__name__ + "(" + ", ".join((repr(x) for x in self.elems)) + ")"
    @_coconut_tco
    def __str__(self):
        raise _coconut_tail_call((" " + self.opstr + " ").join, (quote(x) for x in self.elems))
    def __len__(self):
        return sum(map(len, self.elems)) + 1
    @_coconut_tco
    def substitute(self, subs, **kwargs):
        raise _coconut_tail_call((self.__class__), *(_coconut.functools.partial(map, lambda x: x.substitute(subs, **kwargs)))(self.elems))
    def resolve(self, **kwargs):
        elems = (_coconut.functools.partial(map, lambda x: x.resolve(**kwargs)))(self.elems)
        return self.__class__(*elems).simplify(dnf=False, **kwargs)

class Imp(BinaryOp):
    """Logical implication."""
    __slots__ = ()
    opstr = imp_sym
    @_coconut_tco
    def __rshift__(self, other):
        if isinstance(other, Imp):
            raise _coconut_tail_call(Imp, self, *other.elems)
        else:
            raise _coconut_tail_call(Imp, self, other)
    @_coconut_tco
    def __lshift__(self, other):
        raise _coconut_tail_call((Imp), *(other,) + self.elems)
    @property
    def conds(self):
        return self.elems[:-1]
    @property
    def concl(self):
        return self.elems[-1]
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.concl == other.concl and (unorderd_eq)(self.conds, other.conds)
    @_coconut_tco
    def to_or(self):
        ors = tuple(map(Not, self.conds)) + (self.concl,)
        raise _coconut_tail_call(Or, *ors)
    def simplify(self, **kwargs):
        return self.to_or().simplify(**kwargs)
    def admits_empty_universe(self):
        return self.to_or().admits_empty_universe()
Implies = Imp

class BoolOp(BinaryOp):
    """Base class for Or and And."""
    __slots__ = ()
    def __eq__(self, other):
        return isinstance(other, self.__class__) and (unorderd_eq)(self.elems, other.elems)
    def simplify(self, **kwargs):
        elems = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))(self.merge().elems)
        out = self.__class__(*elems).clean()
        if isinstance(out, self.__class__):
            out = out.distribute(**kwargs)
        if isinstance(out, self.__class__):
            out = out.merge().dedupe()
        if isinstance(out, self.__class__):
            out = out.inner_simplify(**kwargs)
        if isinstance(out, self.__class__):
            out = out.prenex(**kwargs)
        log_simplification(self, out, **kwargs)
        return out
    @_coconut_tco
    def merge(self):
        """Merges nested copies of a boolean operator."""
        elems = []
        for x in self.elems:
            if isinstance(x, self.__class__):
                elems.extend(x.merge().elems)
            else:
                elems.append(x)
        raise _coconut_tail_call(self.__class__, *elems)
    @_coconut_tco
    def dedupe(self):
        """Removes duplicate elements from a boolean operator."""
        elems = []
        for x in self.elems:
            if x not in elems:
                elems.append(x)
        raise _coconut_tail_call(self.__class__, *elems)
    @_coconut_tco
    def clean(self):
        """Removes copies of the identity."""
        raise _coconut_tail_call((self.__class__), *(_coconut.functools.partial(filter, _coconut.functools.partial(_coconut.operator.ne, self.identity)))(self.elems))
    def prenex(self, **kwargs):
        """Pulls quantifiers out."""
        for i, x in enumerate(self.elems):
            if isinstance(x, Quantifier) and self.can_prenex(x, **kwargs):
                elems = self.elems[:i] + self.elems[i + 1:]
                free_x = x.make_free_in(self.__class__(*elems))
                elems += (free_x.elem,)
                return free_x.change_elem(self.__class__(*elems)).simplify(**kwargs)
        return self

class Or(BoolOp):
    """Logical disjunction."""
    __slots__ = ()
    opstr = or_sym
    identity = bot
    @_coconut_tco
    def __or__(self, other):
        raise _coconut_tail_call((Or), *self.elems + (other,))
    @property
    def ors(self):
        return self.elems
    def distribute(self, dnf=False, **kwargs):
        """If this Or contains an And, distribute into it."""
        kwargs["dnf"] = dnf
        if not dnf:
            for i, x in enumerate(self.ors):
                if isinstance(x, And):
                    ands = ((Or)(*(y,) + self.ors[:i] + self.ors[i + 1:]) for y in x.ands)
                    return And(*ands).simplify(**kwargs)
        return self
    def inner_simplify(self, **kwargs):
        if self.tautology(**kwargs):
            return top
        else:
            return self
    def tautology(self, **kwargs):
        """Determines if the Or is a blatant tautology."""
        for i, x in enumerate(self.ors):
            if top == x:
                return True
            for y in self.ors[i + 1:]:
                if x.contradicts(y, **kwargs):
                    return True
        return False
    def can_prenex(self, other, nonempty_universe=True, in_forall=False, **kwargs):
        kwargs["nonempty_universe"], kwargs["in_forall"] = nonempty_universe, in_forall
        return (nonempty_universe or in_forall or not isinstance(other, Exists) or all((isinstance(x, Exists) for x in self.elems)))
    @_coconut_tco
    def resolve_against(self, other, **kwargs):
        if isinstance(other, Eq):
            raise _coconut_tail_call(other.resolve_against, self)
        elif isinstance(other, Or):
            not_other_ors = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))((_coconut.functools.partial(map, Not))(other.ors))
            for i, x in enumerate(self.ors):
                if isinstance(x, Eq):
                    resolved_other = (x.paramodulant)(other)
                    raise _coconut_tail_call((Or), *self.ors[:i] + self.ors[i + 1:] + resolved_other.ors)
                for j, y in enumerate(not_other_ors):
                    if isinstance(other.ors[j], Eq):
                        y = other.ors[j]
                        resolved_self = (y.paramodulant)(self)
                        raise _coconut_tail_call((Or), *other.ors[:j] + other.ors[j + 1:] + resolved_self.ors)
                    subs = x.find_unification(y)
                    if subs is not None:
                        raise _coconut_tail_call((Or), *(_coconut.functools.partial(map, lambda x: x.substitute(subs, **kwargs)))(self.ors[:i] + self.ors[i + 1:] + other.ors[:j] + other.ors[j + 1:]))
        else:
            not_other = Not(other).simplify(**kwargs)
            for i, x in enumerate(self.ors):
                if isinstance(x, Eq):
                    raise _coconut_tail_call((x.paramodulant), (Or)(*self.ors[:i] + self.ors[i + 1:]))
                subs = x.find_unification(not_other)
                if subs is not None:
                    raise _coconut_tail_call((Or), *(_coconut.functools.partial(map, lambda x: x.substitute(subs, **kwargs)))(self.ors[:i] + self.ors[i + 1:]))
        return None
    @_coconut_tco
    def admits_empty_universe(self):
        raise _coconut_tail_call(any, (x.admits_empty_universe() for x in self.elems))

class And(BoolOp):
    """Logical conjunction."""
    __slots__ = ()
    opstr = and_sym
    identity = top
    @_coconut_tco
    def __and__(self, other):
        raise _coconut_tail_call((And), *self.elems + (other,))
    @property
    def ands(self):
        return self.elems
    def distribute(self, dnf=False, **kwargs):
        """If this And contains an Or, distribute into it."""
        kwargs["dnf"] = dnf
        if dnf:
            for i, x in enumerate(self.ands):
                if isinstance(x, Or):
                    ors = ((And)(*(y,) + self.ands[:i] + self.ands[i + 1:]) for y in x.ors)
                    return Or(*ors).simplify(**kwargs)
        return self
    def inner_simplify(self, **kwargs):
        if self.contradiction(**kwargs):
            return bot
        else:
            return self
    def contradiction(self, **kwargs):
        """Determines if the And is a blatant contradiction."""
        for i, x in enumerate(self.ands):
            if bot == x:
                return True
            for y in self.ands[i + 1:]:
                if x.contradicts(y, **kwargs):
                    return True
        return False
    def can_prenex(self, other, nonempty_universe=True, in_exists=False, **kwargs):
        kwargs["nonempty_universe"], kwargs["in_exists"] = nonempty_universe, in_exists
        return (nonempty_universe or in_exists or not isinstance(other, ForAll) or all((isinstance(x, ForAll) for x in self.elems)))
    @_coconut_tco
    def resolve(self, nonempty_universe=True, debug=False, **kwargs):
        """Performs all possible resolutions within the And."""
        kwargs["nonempty_universe"], kwargs["debug"] = nonempty_universe, debug
        resolved = super(And, self).resolve(**kwargs)
        if not isinstance(resolved, And):
            log_simplification(self, resolved, **kwargs)
            return resolved
        clauses = (list)(resolved.ands)
        quantifiers = []
        if not nonempty_universe and not self.admits_empty_universe():
            blank = Exists.blank()
            (quantifiers.append)(blank.change_elem)
            kwargs = (blank.inner_kwargs)(kwargs)
        prev_clause_len = 1
        while prev_clause_len < len(clauses):
            prev_clause_len = len(clauses)
# reversed ensures conclusions get tested first
            for i in (reversed)(range(1, len(clauses))):
                x = clauses[i]
                for y in clauses[:i + 1]:  # allow resolution of a clause against itself
                    resolution = x.resolve_against(y)
                    if resolution is not None:
                        resolution = resolution.simplify(dnf=False, **kwargs)
                        if debug:
                            print(x, "+", y, "=>", resolution)
                        new_quantifiers = []
                        inner_kwargs = kwargs
                        while isinstance(resolution, Quantifier) and self.can_prenex(resolution, **kwargs):
                            (new_quantifiers.append)(resolution.change_elem)
                            inner_kwargs = (resolution.inner_kwargs)(inner_kwargs)
                            resolution = resolution.elem
                        if isinstance(resolution, And):
                            new_clauses = resolution.ands
                        else:
                            new_clauses = (resolution,)
                        novel = False
                        for new_clause in new_clauses:
                            if new_clause == bot:
                                clauses = [bot]
                                novel = True
                                break
                            elif new_clause != top and new_clause not in clauses:
                                clauses.append(new_clause)
                                novel = True
                        if novel:
                            quantifiers.extend(new_quantifiers)
                            kwargs = inner_kwargs
                            if clauses == [bot]:
                                break
                if clauses == [bot]:
                    break
        resolved = reduce(_coconut_pipe, [And(*clauses)] + quantifiers)
        log_simplification(self, resolved, **kwargs)
        raise _coconut_tail_call(resolved.simplify, dnf=False, **kwargs)
    @_coconut_tco
    def admits_empty_universe(self):
        raise _coconut_tail_call(all, (x.admits_empty_universe() for x in self.elems))

class Eq(Expr):
    """Equality operator."""
    __slots__ = ("a", "b")
    def __init__(self, a, b):
        assert isinstance(a, Term), a
        assert isinstance(b, Term), b
        self.a, self.b = a, b
    def __repr__(self):
        return "Eq(" + repr(self.a) + ", " + repr(self.b) + ")"
    def __str__(self):
        return str(self.a) + "=" + str(self.b)
    def __eq__(self, other):
        return isinstance(other, Eq) and (self.a == other.a and self.b == other.b or self.a == other.b and self.b == other.a)
    def simplify(self, **kwargs):
        if self.a == self.b:
            return top
        else:
            return self
    @_coconut_tco
    def swap(self):
        """Swapts the order of equality."""
        raise _coconut_tail_call(Eq, self.b, self.a)
    @_coconut_tco
    def find_unification(self, other):
        if isinstance(other, Quantifier):
            raise _coconut_tail_call(other.find_unification, self)
        elif isinstance(other, Eq):
            a_a = self.a.find_unification(other.a)
            b_b = self.b.find_unification(other.b)
            if a_a is not None and b_b is not None:
                subs = merge_dicts(a_a, b_b)
                if subs is not None:
                    return subs
            a_b = self.a.find_unification(other.a)
            b_a = self.b.find_unification(other.b)
            if a_b is not None and b_a is not None:
                subs = merge_dicts(a_b, b_a)
                if subs is not None:
                    return subs
        else:
            return None
    @_coconut_tco
    def substitute(self, subs, **kwargs):
        raise _coconut_tail_call(Eq, self.a.substitute(subs, **kwargs), self.b.substitute(subs, **kwargs))
    @_coconut_tco
    def paramodulant(self, other):
        """Create a paramodulant of other."""
        raise _coconut_tail_call((sub_once), other, {self.a: self.b, self.b: self.a})
    @_coconut_tco
    def resolve_against(self, other, **kwargs):
        if isinstance(other, Not) and self.find_unification(other.neg) is not None:
            return bot
        else:
            raise _coconut_tail_call(self.paramodulant, other)
    def admits_empty_universe(self):
        return self.a.admits_empty_universe() and self.b.admits_empty_universe()
Equals = Eq
