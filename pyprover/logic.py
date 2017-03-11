#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xcd50336a

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

from pyprover.constants import top_sym
from pyprover.constants import bot_sym
from pyprover.constants import not_sym
from pyprover.constants import imp_sym
from pyprover.constants import and_sym
from pyprover.constants import or_sym
from pyprover.constants import forall_sym
from pyprover.constants import exists_sym
from pyprover.util import unorderd_eq
from pyprover.util import quote
from pyprover.util import log_simplification
from pyprover.util import add_sub

# Functions:

def wff(expr):
    """Determines whether expr is a well-formed formula."""
    return isinstance(expr, Expr) and not isinstance(expr, Term)

@_coconut_tco
def isvar(var):
    """Whether a term is a variable."""
    raise _coconut_tail_call(isinstance, var, (Constant, Variable))

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
        if isinstance(other, Implies):
            return other << self
        else:
            raise _coconut_tail_call(Implies, self, other)
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
    def resolve(self, **kwargs):
        """Performs resolution on the clauses in a CNF expression."""
        return self
    def find_unification(self, other):
        """Find a substitution in self that would make self into other."""
        if self == other:
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
        if isinstance(other, (Not, Or)):
            raise _coconut_tail_call(other.resolve_against, self, **kwargs)
        elif (self.find_unification)(Not(other).simplify(**kwargs)) is not None:
            return bot
        else:
            return None

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
        try:
            sub = subs[self]
        except KeyError:
            raise _coconut_tail_call(self.substitute_elements, subs, **kwargs)
        else:
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
        raise _coconut_tail_call(Predicate, self.name, *args)
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
        return self.__class__.__name__ + '("' + self.name + '"' + ", ".join((repr(x) for x in self.args)) + ")"
    def __str__(self):
        return self.name + "(" + ", ".join((str(x) for x in self.args)) + ")"
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name and self.args == other.args
    @_coconut_tco
    def __hash__(self):
        raise _coconut_tail_call((hash), (self.__class__.__name__, self.name, self.args))
    def find_unification(self, other):
        if isinstance(other, self.__class__) and self.name == other.name and len(self.args) == len(other.args):
            subs = {}
            for i, x in enumerate(self.args):
                y = other.args[i]
                unif = x.find_unification(y)
                if unif is None:
                    return None
                for name, var in unif.items():
                    if name not in subs:
                        subs[name] = var
                    elif subs[name] != var:
                        return None
            return subs
        else:
            return None

class Pred(FuncAtom):
    """Boolean function of terms."""
    __slots__ = ()
    @_coconut_tco
    def proposition(self):
        raise _coconut_tail_call(Proposition, self.name)
    @_coconut_tco
    def substitute_elements(self, subs, **kwargs):
        try:
            sub = subs[self.proposition()]
        except KeyError:
            raise _coconut_tail_call((_coconut.functools.partial(Predicate, self.name)), *(_coconut.functools.partial(map, lambda x: x.substitute(subs, **kwargs)))(self.args))
        else:
            raise _coconut_tail_call(Predicate, sub.name, *self.args)
Predicate = Pred

class Term(Atom):
    """Base class for all terms."""
    __slots__ = ()
    @_coconut_tco
    def variable(self):
        """Convert to a variable."""
        raise _coconut_tail_call(Variable, self.name)
    @_coconut_tco
    def constant(self):
        """Convert to a constant."""
        raise _coconut_tail_call(Constant, self.name)
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
        for var, sub in subs.items():
            if isinstance(var, Term) and self.name == var.name:
                if isvar(self) or self == var:
                    return sub
                else:
                    raise _coconut_tail_call(self.rename, sub.name)
        raise _coconut_tail_call(self.substitute_elements, subs, **kwargs)

class Var(Term):
    """A variable quantified by a ForAll."""
    __slots__ = ()
    def variable(self):
        return self
    @_coconut_tco
    def __call__(self, *args):
        raise _coconut_tail_call(Function, self.name, *args)
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
        raise _coconut_tail_call(Function, self.name, *args)
    def find_unification(self, other):
        if isinstance(other, Variable):
            return {other: self}
        else:
            return super(Constant, self).find_unification(other)
Constant = Const

class Func(Term, FuncAtom):
    """A function on terms."""
    __slots__ = ()
    @_coconut_tco
    def substitute_elements(self, subs, **kwargs):
        raise _coconut_tail_call((_coconut.functools.partial(Function, self.name)), *(_coconut.functools.partial(map, lambda x: x.substitute(subs, **kwargs)))(self.args))
    @_coconut_tco
    def rename(self, name):
        raise _coconut_tail_call(self.__class__, name, *self.args)
    def find_unification(self, other):
        if isinstance(other, Variable):
            return {other: self}
        else:
            return super(Function, self).find_unification(other)
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
        if isinstance(other, self.__class__):
            raise _coconut_tail_call(self.elem.find_unification, other.elem)
        else:
            return None
    def resolve(self, **kwargs):
        return self.__class__(self.elem.resolve(**kwargs)).simplify(**kwargs)

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
        elif isinstance(self.neg, Implies):
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
        if isinstance(other, Or):
            raise _coconut_tail_call(other.resolve_against, self, **kwargs)
        elif self.neg.find_unification(other) is not None:
            return bot
        else:
            return None

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
    @_coconut_tco
    def substitute(self, subs, **kwargs):
        var = self.var
        newvar = var.prime()
        while var != var.substitute(subs):  # don't pass kwargs here, since this isn't a real sub
            var, newvar = newvar, newvar.prime()
        raise _coconut_tail_call((_coconut.functools.partial(self.__class__, var)), (_coconut.functools.partial(self.elem.substitute, **kwargs))(add_sub(subs, self.var, var)))
    @_coconut_tco
    def make_free_in(self, other):
        """Makes self free in other."""
        var = self.var
        newvar = var.prime()
        while other != other.substitute({var: newvar}):
            var, newvar = newvar, newvar.prime()
        raise _coconut_tail_call(self.change_var, var)
    def find_unification(self, other):
        return self.make_free_in(other).elem.find_unification(other)
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

class ForAll(Quantifier):
    """Universal quantifier."""
    __slots__ = ()
    opstr = forall_sym
    def __init__(self, var, elem):
        assert wff(elem), elem
        if isinstance(var, str):
            var = Constant(var)
        assert isvar(var), var
        self.var = var.variable()
        self.elem = elem.substitute({var: self.var.variable()})
    def simplify(self, **kwargs):
        kwargs["in_forall"] = True
        return self.__class__(self.var, self.elem.simplify(**kwargs)).drop_quantifier(**kwargs)
    def resolve(self, **kwargs):
        kwargs["in_forall"] = True
        kwargs["variables"] = kwargs.get("variables", ()) + (self.var,)
        return ForAll(self.var, self.elem.resolve(**kwargs)).simplify(dnf=False, **kwargs)
    def drop_quantifier(self, nonempty_universe=True, **kwargs):
        kwargs["nonempty_universe"] = nonempty_universe
        if not nonempty_universe:
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
            var = Constant(var)
        assert isvar(var), var
        self.var = var.constant()
        self.elem = elem.substitute({var: self.var.constant()})
    def simplify(self, **kwargs):
        kwargs["in_exists"] = True
        return self.__class__(self.var, self.elem.simplify(**kwargs)).drop_quantifier(**kwargs)
    def resolve(self, **kwargs):
        kwargs["in_exists"] = True
        variables = kwargs.get("variables")
        if variables is None:
            skolem_elem = self.elem
        else:
            skolem_var = Function(self.var.name, *variables)
            skolem_elem = self.elem.substitute({self.var: skolem_var})
        return Exists(self.var, skolem_elem.resolve(**kwargs)).simplify(dnf=False, **kwargs)
    def drop_quantifier(self, nonempty_universe=True, **kwargs):
        kwargs["nonempty_universe"] = nonempty_universe
        if not nonempty_universe:
            elem = self.elem
            while isinstance(elem, ForAll):
                elem = elem.elem
            if bot == elem:
                return elem
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):
            return self.elem
        return self
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
        return self.__class__(*elems).simplify(**kwargs)

class Imp(BinaryOp):
    """Logical implication."""
    __slots__ = ()
    opstr = imp_sym
    @_coconut_tco
    def __rshift__(self, other):
        if isinstance(other, Implies):
            raise _coconut_tail_call(Implies, self, *other.elems)
        else:
            raise _coconut_tail_call(Implies, self, other)
    @_coconut_tco
    def __lshift__(self, other):
        raise _coconut_tail_call((Implies), *(other,) + self.elems)
    @property
    def conds(self):
        return self.elems[:-1]
    @property
    def concl(self):
        return self.elems[-1]
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.concl == other.concl and (unorderd_eq)(self.conds, other.conds)
    def simplify(self, **kwargs):
        ors = tuple(map(Not, self.conds)) + (self.concl,)
        return Or(*ors).simplify(**kwargs)
Implies = Imp

class BoolOp(BinaryOp):
    """Base class for Or and And."""
    __slots__ = ()
    def __eq__(self, other):
        return isinstance(other, self.__class__) and (unorderd_eq)(self.elems, other.elems)
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
    def distribute(self, **kwargs):
        """If this Or contains an And, distribute into it."""
        for i, x in enumerate(self.ors):
            if isinstance(x, And):
                ands = ((Or)(*(y,) + self.ors[:i] + self.ors[i + 1:]) for y in x.ands)
                return And(*ands).simplify(**kwargs)
        return self
    def simplify(self, dnf=False, **kwargs):
        kwargs["dnf"] = dnf
        ors = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))(self.merge().ors)
        out = Or(*ors).clean()
        if isinstance(out, Or) and not dnf:
            out = out.distribute(**kwargs)
        if isinstance(out, Or):
            out = out.merge().dedupe()
        if isinstance(out, Or) and out.tautology(**kwargs):
            out = top
        if isinstance(out, Or):
            out = out.prenex(**kwargs)
        log_simplification(self, out, **kwargs)
        return out
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
        if isinstance(other, Or):
            not_other_ors = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))((_coconut.functools.partial(map, Not))(other.ors))
            for i, x in enumerate(self.ors):
                for j, y in enumerate(not_other_ors):
                    subs = x.find_unification(y)
                    if subs is not None:
                        raise _coconut_tail_call((Or), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.ors[:i] + self.ors[i + 1:] + other.ors[:j] + other.ors[j + 1:]))
        else:
            not_other = Not(other).simplify(**kwargs)
            for i, x in enumerate(self.ors):
                subs = x.find_unification(not_other)
                if subs is not None:
                    raise _coconut_tail_call((Or), *(_coconut.functools.partial(map, _coconut.operator.methodcaller("substitute", subs)))(self.ors[:i] + self.ors[i + 1:]))
        return None

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
    def distribute(self, **kwargs):
        """If this And contains an Or, distribute into it."""
        for i, x in enumerate(self.ands):
            if isinstance(x, Or):
                ors = ((And)(*(y,) + self.ands[:i] + self.ands[i + 1:]) for y in x.ors)
                return Or(*ors).simplify(**kwargs)
        return self
    def simplify(self, dnf=False, **kwargs):
        kwargs["dnf"] = dnf
        ands = (_coconut.functools.partial(map, lambda x: x.simplify(**kwargs)))(self.merge().ands)
        out = And(*ands).clean()
        if isinstance(out, And) and dnf:
            out = out.distribute(**kwargs)
        if isinstance(out, And):
            out = out.merge().dedupe()
        if isinstance(out, And) and out.contradiction(**kwargs):
            out = bot
        if isinstance(out, And):
            out = out.prenex(**kwargs)
        log_simplification(self, out, **kwargs)
        return out
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
    def resolve(self, debug=False, **kwargs):
        """Performs all possible resolutions within the And."""
        kwargs["debug"] = debug
        resolved = super(And, self).resolve(**kwargs)
        if not isinstance(resolved, And):
            log_simplification(self, resolved, **kwargs)
            return resolved
        clauses = (list)(resolved.ands)
        quantifiers = []
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
                        while isinstance(resolution, Quantifier) and self.can_prenex(resolution, **kwargs):
                            (new_quantifiers.append)(resolution.change_elem)
                            resolution = resolution.elem
                        if isinstance(resolution, And):
                            new_clauses = resolution.ands
                        else:
                            new_clauses = (resolution,)
                        if bot in new_clauses:
                            quantifiers.extend(new_quantifiers)
                            clauses = [bot]
                            break
                        novel = False
                        for new_clause in new_clauses:
                            if new_clause != top and new_clause not in clauses:
                                clauses.append(new_clause)
                                novel = True
                        if novel:
                            quantifiers.extend(new_quantifiers)
                if bot in clauses:
                    break
        resolved = reduce(_coconut_pipe, [And(*clauses)] + quantifiers)
        log_simplification(self, resolved, **kwargs)
        raise _coconut_tail_call(resolved.simplify, dnf=False, **kwargs)
