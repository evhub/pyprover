#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x957160b1

# Compiled with Coconut version 2.0.0-post_dev23 [How Not to Be Seen]

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
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Imports:

from pyprover.constants import top_sym  #3 (line in Coconut source)
from pyprover.constants import bot_sym  #3 (line in Coconut source)
from pyprover.constants import not_sym  #3 (line in Coconut source)
from pyprover.constants import imp_sym  #3 (line in Coconut source)
from pyprover.constants import and_sym  #3 (line in Coconut source)
from pyprover.constants import or_sym  #3 (line in Coconut source)
from pyprover.constants import forall_sym  #3 (line in Coconut source)
from pyprover.constants import exists_sym  #3 (line in Coconut source)
from pyprover.constants import empty_var  #3 (line in Coconut source)
from pyprover.util import unorderd_eq  #14 (line in Coconut source)
from pyprover.util import quote  #14 (line in Coconut source)
from pyprover.util import log_simplification  #14 (line in Coconut source)
from pyprover.util import log_resolution  #14 (line in Coconut source)
from pyprover.util import rem_var  #14 (line in Coconut source)
from pyprover.util import can_sub  #14 (line in Coconut source)
from pyprover.util import do_sub  #14 (line in Coconut source)
from pyprover.util import sub_once  #14 (line in Coconut source)
from pyprover.util import unify_elems  #14 (line in Coconut source)

# Functions:

def wff(expr):  #28 (line in Coconut source)
    """Determines whether expr is a well-formed formula."""  #29 (line in Coconut source)
    return isinstance(expr, Expr) and not isinstance(expr, Term)  #30 (line in Coconut source)



@_coconut_tco  #33 (line in Coconut source)
def isvar(var):  #33 (line in Coconut source)
    """Whether a term is a variable."""  #34 (line in Coconut source)
    return _coconut_tail_call(isinstance, var, (Const, Var))  #35 (line in Coconut source)


# Classes:


class Expr(_coconut.object):  #40 (line in Coconut source)
    """Base class for all formulae."""  #41 (line in Coconut source)
    __slots__ = ()  #42 (line in Coconut source)

    @_coconut_tco  #44 (line in Coconut source)
    def __hash__(self):  #44 (line in Coconut source)
#type: (...) -> int
        return _coconut_tail_call((hash), repr(self))  #45 (line in Coconut source)


    def __lt__(self, other):  #47 (line in Coconut source)
#type: (...) -> int
        return str(self) < str(other)  #48 (line in Coconut source)


    def __gt__(self, other):  #50 (line in Coconut source)
#type: (...) -> int
        return str(self) > str(other)  #51 (line in Coconut source)


    def __ge__(self, other):  #53 (line in Coconut source)
#type: (...) -> int
        return str(self) >= str(other)  #54 (line in Coconut source)


    def __le__(self, other):  #56 (line in Coconut source)
#type: (...) -> int
        return str(self) <= str(other)  #57 (line in Coconut source)


    @_coconut_tco  #59 (line in Coconut source)
    def __and__(self, other):  #59 (line in Coconut source)
        if isinstance(other, And):  #60 (line in Coconut source)
            return other & self  #61 (line in Coconut source)
        else:  #62 (line in Coconut source)
            return _coconut_tail_call(And, self, other)  #63 (line in Coconut source)


    @_coconut_tco  #65 (line in Coconut source)
    def __or__(self, other):  #65 (line in Coconut source)
        if isinstance(other, Or):  #66 (line in Coconut source)
            return other | self  #67 (line in Coconut source)
        else:  #68 (line in Coconut source)
            return _coconut_tail_call(Or, self, other)  #69 (line in Coconut source)


    @_coconut_tco  #71 (line in Coconut source)
    def __rshift__(self, other):  #71 (line in Coconut source)
        if isinstance(other, Imp):  #72 (line in Coconut source)
            return other << self  #73 (line in Coconut source)
        else:  #74 (line in Coconut source)
            return _coconut_tail_call(Imp, self, other)  #75 (line in Coconut source)


    def __lshift__(self, other):  #77 (line in Coconut source)
        assert wff(other), other  #78 (line in Coconut source)
        return other >> self  #79 (line in Coconut source)


    @_coconut_tco  #81 (line in Coconut source)
    def __invert__(self):  #81 (line in Coconut source)
        return _coconut_tail_call(Not, self)  #82 (line in Coconut source)


    @_coconut_tco  #84 (line in Coconut source)
    def __xor__(self, other):  #84 (line in Coconut source)
        return _coconut_tail_call(Or, And(self, Not(other)), And(Not(self), other))  #85 (line in Coconut source)


    def __len__(self):  #87 (line in Coconut source)
        return 1  #87 (line in Coconut source)


    def simplify(self, **kwargs):  #89 (line in Coconut source)
        """Simplify the given expression."""  #90 (line in Coconut source)
        return self  #91 (line in Coconut source)


    def substitute(self, subs, **kwargs):  #93 (line in Coconut source)
        """Substitutes a dictionary into the expression."""  #94 (line in Coconut source)
        return self  #95 (line in Coconut source)


    @_coconut_tco  #97 (line in Coconut source)
    def resolve(self, **kwargs):  #97 (line in Coconut source)
        """Performs resolution on the clauses in a CNF expression."""  #98 (line in Coconut source)
        return _coconut_tail_call(self.simplify, dnf=False, **kwargs)  #99 (line in Coconut source)


    @_coconut_tco  #101 (line in Coconut source)
    def find_unification(self, other, **kwargs):  #101 (line in Coconut source)
        """Find a substitution in self that would make self into other."""  #102 (line in Coconut source)
        if isinstance(other, (Quantifier, Var)):  #103 (line in Coconut source)
            return _coconut_tail_call(other.find_unification, self, **kwargs)  #104 (line in Coconut source)
        elif self == other:  #105 (line in Coconut source)
            return {}  #106 (line in Coconut source)
        else:  #107 (line in Coconut source)
            return None  #108 (line in Coconut source)


    @_coconut_tco  #110 (line in Coconut source)
    def contradicts(self, other, **kwargs):  #110 (line in Coconut source)
        """Assuming self is simplified, determines if it contradicts other."""  #111 (line in Coconut source)
        if isinstance(other, Not):  #112 (line in Coconut source)
            return _coconut_tail_call(other.contradicts, self, **kwargs)  #113 (line in Coconut source)
        else:  #114 (line in Coconut source)
            return self == Not(other).simplify(**kwargs)  #115 (line in Coconut source)


    @_coconut_tco  #117 (line in Coconut source)
    def resolve_against(self, other, **kwargs):  #117 (line in Coconut source)
        """Attempt to perform a resolution against other else None."""  #118 (line in Coconut source)
        if isinstance(other, (Not, Or, Eq)):  #119 (line in Coconut source)
            return _coconut_tail_call(other.resolve_against, self, **kwargs)  #120 (line in Coconut source)
        elif (self.find_unification)(Not(other).simplify(**kwargs), **kwargs) is not None:  #121 (line in Coconut source)
            return bot  #122 (line in Coconut source)
        else:  #123 (line in Coconut source)
            return None  #124 (line in Coconut source)


    def admits_empty_universe(self):  #126 (line in Coconut source)
        """Determines if self allows for the possibility of an empty universe."""  #127 (line in Coconut source)
        return True  #128 (line in Coconut source)



_coconut_call_set_names(Expr)  #131 (line in Coconut source)
class Top(Expr):  #131 (line in Coconut source)
    """True"""  #132 (line in Coconut source)
    __slots__ = ()  #133 (line in Coconut source)
    __hash__ = Expr.__hash__  #134 (line in Coconut source)

    @_coconut_tco  #136 (line in Coconut source)
    def __eq__(self, other):  #136 (line in Coconut source)
        return _coconut_tail_call(isinstance, other, Top)  #136 (line in Coconut source)


    def __repr__(self):  #138 (line in Coconut source)
        return "top"  #138 (line in Coconut source)


    def __str__(self):  #140 (line in Coconut source)
        return top_sym  #140 (line in Coconut source)


    def __bool__(self):  #142 (line in Coconut source)
        return True  #142 (line in Coconut source)


_coconut_call_set_names(Top)  #144 (line in Coconut source)
top = true = Top()  #144 (line in Coconut source)


class Bot(Expr):  #147 (line in Coconut source)
    """False"""  #148 (line in Coconut source)
    __slots__ = ()  #149 (line in Coconut source)
    __hash__ = Expr.__hash__  #150 (line in Coconut source)

    @_coconut_tco  #152 (line in Coconut source)
    def __eq__(self, other):  #152 (line in Coconut source)
        return _coconut_tail_call(isinstance, other, Bot)  #152 (line in Coconut source)


    def __repr__(self):  #154 (line in Coconut source)
        return "bot"  #154 (line in Coconut source)


    def __str__(self):  #156 (line in Coconut source)
        return bot_sym  #156 (line in Coconut source)


    def __bool__(self):  #158 (line in Coconut source)
        return False  #158 (line in Coconut source)


    def admits_empty_universe(self):  #160 (line in Coconut source)
        return False  #160 (line in Coconut source)


_coconut_call_set_names(Bot)  #162 (line in Coconut source)
bot = false = Bot()  #162 (line in Coconut source)


class Atom(Expr):  #165 (line in Coconut source)
    """Base class for all variables."""  #166 (line in Coconut source)
    __slots__ = ("name",)  #167 (line in Coconut source)
    __hash__ = Expr.__hash__  #168 (line in Coconut source)

    def __init__(self, name):  #170 (line in Coconut source)
        if isinstance(name, Atom):  #171 (line in Coconut source)
            name = name.name  #172 (line in Coconut source)
        assert isinstance(name, str), name  #173 (line in Coconut source)
        self.name = name  #174 (line in Coconut source)


    def __repr__(self):  #176 (line in Coconut source)
        return self.__class__.__name__ + '("' + self.name + '")'  #177 (line in Coconut source)


    def __str__(self):  #179 (line in Coconut source)
        return self.name  #180 (line in Coconut source)


    def __eq__(self, other):  #182 (line in Coconut source)
        return isinstance(other, self.__class__) and self.name == other.name  #183 (line in Coconut source)


    def substitute_elements(self, subs, **kwargs):  #185 (line in Coconut source)
        """Substitute for the elements of the Atom, not the Atom itself."""  #186 (line in Coconut source)
        return self  #187 (line in Coconut source)


    @_coconut_tco  #189 (line in Coconut source)
    def substitute(self, subs, **kwargs):  #189 (line in Coconut source)
        if not can_sub(kwargs):  #190 (line in Coconut source)
            return self  #191 (line in Coconut source)
        _coconut_match_to_0 = subs  #192 (line in Coconut source)
        _coconut_match_check_0 = False  #192 (line in Coconut source)
        _coconut_match_set_name_sub = _coconut_sentinel  #192 (line in Coconut source)
        if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #192 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_match_to_0.get(self, _coconut_sentinel)  #192 (line in Coconut source)
            if _coconut_match_temp_0 is not _coconut_sentinel:  #192 (line in Coconut source)
                _coconut_match_set_name_sub = _coconut_match_temp_0  #192 (line in Coconut source)
                _coconut_match_check_0 = True  #192 (line in Coconut source)
        if _coconut_match_check_0:  #192 (line in Coconut source)
            if _coconut_match_set_name_sub is not _coconut_sentinel:  #192 (line in Coconut source)
                sub = _coconut_match_set_name_sub  #192 (line in Coconut source)
        if _coconut_match_check_0:  #192 (line in Coconut source)
            do_sub(kwargs)  #193 (line in Coconut source)
            if wff(sub):  #194 (line in Coconut source)
                return sub  #195 (line in Coconut source)
            elif sub is True:  #196 (line in Coconut source)
                return top  #197 (line in Coconut source)
            elif sub is False:  #198 (line in Coconut source)
                return bot  #199 (line in Coconut source)
            else:  #200 (line in Coconut source)
                raise TypeError("cannot perform substitution " + str(self) + " => " + str(sub))  #201 (line in Coconut source)
        else:  #202 (line in Coconut source)
            return _coconut_tail_call(self.substitute_elements, subs, **kwargs)  #203 (line in Coconut source)



_coconut_call_set_names(Atom)  #206 (line in Coconut source)
class Prop(Atom):  #206 (line in Coconut source)
    """Logical proposition that is either true or false."""  #207 (line in Coconut source)
    __slots__ = ()  #208 (line in Coconut source)
    __hash__ = Expr.__hash__  #209 (line in Coconut source)

    @_coconut_tco  #211 (line in Coconut source)
    def __call__(self, *args):  #211 (line in Coconut source)
        return _coconut_tail_call(Pred, self.name, *args)  #212 (line in Coconut source)


_coconut_call_set_names(Prop)  #214 (line in Coconut source)
Proposition = Prop  #214 (line in Coconut source)


class FuncAtom(Atom):  #217 (line in Coconut source)
    """Base class for predicates and functions."""  #218 (line in Coconut source)
    __slots__ = ("args",)  #219 (line in Coconut source)
    __hash__ = Expr.__hash__  #220 (line in Coconut source)

    def __init__(self, name, *args):  #222 (line in Coconut source)
        __class__ = FuncAtom  #223 (line in Coconut source)

        super().__init__(name)  #223 (line in Coconut source)
        for arg in args:  #224 (line in Coconut source)
            assert isinstance(arg, Term), arg  #225 (line in Coconut source)
        self.args = args  #226 (line in Coconut source)


    def __repr__(self):  #228 (line in Coconut source)
        return self.__class__.__name__ + '("' + self.name + '"' + (", " if self.args else "") + ", ".join((repr(x) for x in self.args)) + ")"  #229 (line in Coconut source)


    def __str__(self):  #231 (line in Coconut source)
        return self.name + "(" + ", ".join((str(x) for x in self.args)) + ")"  #232 (line in Coconut source)


    def __eq__(self, other):  #234 (line in Coconut source)
        return isinstance(other, self.__class__) and self.name == other.name and self.args == other.args  #235 (line in Coconut source)


    @_coconut_tco  #237 (line in Coconut source)
    def find_unification(self, other, **kwargs):  #237 (line in Coconut source)
        if isinstance(other, self.__class__) and self.name == other.name and len(self.args) == len(other.args):  #238 (line in Coconut source)
            return _coconut_tail_call(unify_elems, self, other, elems_getter=_coconut.operator.attrgetter("args"), **kwargs)  #239 (line in Coconut source)
        else:  #240 (line in Coconut source)
            __class__ = FuncAtom  #241 (line in Coconut source)

            return super().find_unification(other, **kwargs)  #241 (line in Coconut source)


    @_coconut_tco  #243 (line in Coconut source)
    def admits_empty_universe(self):  #243 (line in Coconut source)
        return _coconut_tail_call(all, (x.admits_empty_universe() for x in self.args))  #244 (line in Coconut source)



_coconut_call_set_names(FuncAtom)  #247 (line in Coconut source)
class Pred(FuncAtom):  #247 (line in Coconut source)
    """Boolean function of terms."""  #248 (line in Coconut source)
    __slots__ = ()  #249 (line in Coconut source)
    __hash__ = Expr.__hash__  #250 (line in Coconut source)

    @_coconut_tco  #252 (line in Coconut source)
    def proposition(self):  #252 (line in Coconut source)
        return _coconut_tail_call(Prop, self.name)  #253 (line in Coconut source)


    @_coconut_tco  #255 (line in Coconut source)
    def substitute_elements(self, subs, **kwargs):  #255 (line in Coconut source)
        if not can_sub(kwargs):  #256 (line in Coconut source)
            return self  #257 (line in Coconut source)
        _coconut_match_to_1 = subs  #258 (line in Coconut source)
        _coconut_match_check_1 = False  #258 (line in Coconut source)
        _coconut_match_set_name_sub = _coconut_sentinel  #258 (line in Coconut source)
        if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #258 (line in Coconut source)
            _coconut_match_temp_1 = _coconut_match_to_1.get(self.proposition(), _coconut_sentinel)  #258 (line in Coconut source)
            if _coconut_match_temp_1 is not _coconut_sentinel:  #258 (line in Coconut source)
                _coconut_match_set_name_sub = _coconut_match_temp_1  #258 (line in Coconut source)
                _coconut_match_check_1 = True  #258 (line in Coconut source)
        if _coconut_match_check_1:  #258 (line in Coconut source)
            if _coconut_match_set_name_sub is not _coconut_sentinel:  #258 (line in Coconut source)
                sub = _coconut_match_set_name_sub  #258 (line in Coconut source)
        if _coconut_match_check_1:  #258 (line in Coconut source)
            assert isinstance(sub, Atom), sub  #259 (line in Coconut source)
            do_sub(kwargs)  #260 (line in Coconut source)
            name = sub.name  #261 (line in Coconut source)
        else:  #262 (line in Coconut source)
            name = self.name  #263 (line in Coconut source)
        if can_sub(kwargs):  #264 (line in Coconut source)
            return _coconut_tail_call((Pred), name, *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.args))  #265 (line in Coconut source)
        else:  #266 (line in Coconut source)
            return _coconut_tail_call(Pred, name, *self.args)  #267 (line in Coconut source)


_coconut_call_set_names(Pred)  #269 (line in Coconut source)
Predicate = Pred  #269 (line in Coconut source)


class Term(Atom):  #272 (line in Coconut source)
    """Base class for all terms."""  #273 (line in Coconut source)
    __slots__ = ()  #274 (line in Coconut source)
    __hash__ = Expr.__hash__  #275 (line in Coconut source)

    @_coconut_tco  #277 (line in Coconut source)
    def variable(self):  #277 (line in Coconut source)
        """Convert to a variable."""  #278 (line in Coconut source)
        return _coconut_tail_call(Var, self.name)  #279 (line in Coconut source)


    @_coconut_tco  #281 (line in Coconut source)
    def constant(self):  #281 (line in Coconut source)
        """Convert to a constant."""  #282 (line in Coconut source)
        return _coconut_tail_call(Const, self.name)  #283 (line in Coconut source)


    @_coconut_tco  #285 (line in Coconut source)
    def rename(self, name):  #285 (line in Coconut source)
        """Create a new term with a different name."""  #286 (line in Coconut source)
        return _coconut_tail_call(self.__class__, name)  #287 (line in Coconut source)


    @_coconut_tco  #289 (line in Coconut source)
    def prime(self):  #289 (line in Coconut source)
        """Rename by adding a prime."""  #290 (line in Coconut source)
        return _coconut_tail_call(self.rename, self.name + "'")  #291 (line in Coconut source)


    @_coconut_tco  #293 (line in Coconut source)
    def subscript(self, i):  #293 (line in Coconut source)
        """Rename by adding a subscript."""  #294 (line in Coconut source)
        return _coconut_tail_call(self.rename, self.name + "_" + str(i))  #295 (line in Coconut source)


    @_coconut_tco  #297 (line in Coconut source)
    def skolem(self):  #297 (line in Coconut source)
        """Rename to a Skolem variable."""  #298 (line in Coconut source)
        return _coconut_tail_call(Const, "_" + self.name)  #299 (line in Coconut source)


    def is_free_in(self, expr):  #301 (line in Coconut source)
        """Determine if self is free in expr."""  #302 (line in Coconut source)
        return expr == expr.substitute({self: self.prime()})  #303 (line in Coconut source)


    @_coconut_tco  #305 (line in Coconut source)
    def substitute(self, subs, **kwargs):  #305 (line in Coconut source)
        if can_sub(kwargs):  #306 (line in Coconut source)
            for var, sub in subs.items():  #307 (line in Coconut source)
                if can_sub(kwargs) and isinstance(var, Term) and self.name == var.name:  #308 (line in Coconut source)
                    do_sub(kwargs)  #309 (line in Coconut source)
                    if isvar(self) or self == var:  #310 (line in Coconut source)
                        return sub  #311 (line in Coconut source)
                    else:  #312 (line in Coconut source)
                        return self.rename(sub.name)  #313 (line in Coconut source)
        if can_sub(kwargs):  #314 (line in Coconut source)
            return _coconut_tail_call(self.substitute_elements, subs, **kwargs)  #315 (line in Coconut source)
        return self  #316 (line in Coconut source)



_coconut_call_set_names(Term)  #319 (line in Coconut source)
class Var(Term):  #319 (line in Coconut source)
    """A variable quantified by a ForAll."""  #320 (line in Coconut source)
    __slots__ = ()  #321 (line in Coconut source)
    __hash__ = Expr.__hash__  #322 (line in Coconut source)

    def __str__(self):  #324 (line in Coconut source)
        __class__ = Var  #325 (line in Coconut source)

        return "?" + super().__str__()  #325 (line in Coconut source)


    def variable(self):  #327 (line in Coconut source)
        return self  #327 (line in Coconut source)


    @_coconut_tco  #329 (line in Coconut source)
    def __call__(self, *args):  #329 (line in Coconut source)
        return _coconut_tail_call(Func, self.name, *args)  #330 (line in Coconut source)


    def find_unification(self, other, occurs_check=True, **kwargs):  #332 (line in Coconut source)
        kwargs["occurs_check"] = occurs_check  #333 (line in Coconut source)
        if isinstance(other, Var):  #334 (line in Coconut source)
            if self.name == other.name:  #335 (line in Coconut source)
                return {}  #336 (line in Coconut source)
            else:  #337 (line in Coconut source)
                return {self: other}  #338 (line in Coconut source)
        elif isinstance(other, Term):  #339 (line in Coconut source)
            if occurs_check and not self.is_free_in(other):  #340 (line in Coconut source)
                return None  #341 (line in Coconut source)
            else:  #342 (line in Coconut source)
                return {self: other}  #343 (line in Coconut source)
        else:  #344 (line in Coconut source)
            return None  #345 (line in Coconut source)


_coconut_call_set_names(Var)  #347 (line in Coconut source)
Variable = Var  #347 (line in Coconut source)


class Const(Term):  #350 (line in Coconut source)
    """A variable quantified by an Exists."""  #351 (line in Coconut source)
    __slots__ = ()  #352 (line in Coconut source)
    __hash__ = Expr.__hash__  #353 (line in Coconut source)

    def constant(self):  #355 (line in Coconut source)
        return self  #355 (line in Coconut source)


    @_coconut_tco  #357 (line in Coconut source)
    def __call__(self, *args):  #357 (line in Coconut source)
        return _coconut_tail_call(Func, self.name, *args)  #358 (line in Coconut source)


    def admits_empty_universe(self):  #360 (line in Coconut source)
        return False  #360 (line in Coconut source)


_coconut_call_set_names(Const)  #362 (line in Coconut source)
Constant = Const  #362 (line in Coconut source)


class Func(Term, FuncAtom):  #365 (line in Coconut source)
    """A function on terms."""  #366 (line in Coconut source)
    __slots__ = ()  #367 (line in Coconut source)
    __hash__ = Expr.__hash__  #368 (line in Coconut source)

    @_coconut_tco  #370 (line in Coconut source)
    def substitute_elements(self, subs, **kwargs):  #370 (line in Coconut source)
        return _coconut_tail_call((Func), self.name, *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.args))  #371 (line in Coconut source)


    @_coconut_tco  #373 (line in Coconut source)
    def rename(self, name):  #373 (line in Coconut source)
        return _coconut_tail_call(self.__class__, name, *self.args)  #374 (line in Coconut source)


_coconut_call_set_names(Func)  #376 (line in Coconut source)
Function = Func  #376 (line in Coconut source)


class UnaryOp(Expr):  #379 (line in Coconut source)
    """Base class for unary operators."""  #380 (line in Coconut source)
    __slots__ = ("elem",)  #381 (line in Coconut source)
    __hash__ = Expr.__hash__  #382 (line in Coconut source)

    def __init__(self, elem):  #384 (line in Coconut source)
        assert wff(elem), elem  #385 (line in Coconut source)
        self.elem = elem  #386 (line in Coconut source)


    def __repr__(self):  #388 (line in Coconut source)
        return self.__class__.__name__ + "(" + repr(self.elem) + ")"  #389 (line in Coconut source)


    def __eq__(self, other):  #391 (line in Coconut source)
        return isinstance(other, self.__class__) and self.elem == other.elem  #392 (line in Coconut source)


    def __str__(self):  #394 (line in Coconut source)
        return self.opstr + quote(self.elem)  #395 (line in Coconut source)


    def __len__(self):  #397 (line in Coconut source)
        return len(self.elem) + 1  #398 (line in Coconut source)


    @_coconut_tco  #400 (line in Coconut source)
    def substitute(self, subs, **kwargs):  #400 (line in Coconut source)
        return _coconut_tail_call(self.__class__, self.elem.substitute(subs, **kwargs))  #401 (line in Coconut source)


    @_coconut_tco  #403 (line in Coconut source)
    def find_unification(self, other, **kwargs):  #403 (line in Coconut source)
        if isinstance(other, self.__class__):  #404 (line in Coconut source)
            return _coconut_tail_call(self.elem.find_unification, other.elem, **kwargs)  #405 (line in Coconut source)
        else:  #406 (line in Coconut source)
            __class__ = UnaryOp  #407 (line in Coconut source)

            return super().find_unification(other, **kwargs)  #407 (line in Coconut source)


    @_coconut_tco  #409 (line in Coconut source)
    def resolve(self, **kwargs):  #409 (line in Coconut source)
        return _coconut_tail_call(self.__class__(self.elem.resolve(**kwargs)).simplify, dnf=False, **kwargs)  #410 (line in Coconut source)



_coconut_call_set_names(UnaryOp)  #413 (line in Coconut source)
class Not(UnaryOp):  #413 (line in Coconut source)
    """Logical not."""  #414 (line in Coconut source)
    __slots__ = ()  #415 (line in Coconut source)
    __hash__ = Expr.__hash__  #416 (line in Coconut source)
    opstr = not_sym  #417 (line in Coconut source)

    @property  #419 (line in Coconut source)
    def neg(self):  #420 (line in Coconut source)
        return self.elem  #420 (line in Coconut source)


    @_coconut_tco  #422 (line in Coconut source)
    def simplify(self, **kwargs):  #422 (line in Coconut source)
        if self.neg == top:  #423 (line in Coconut source)
            return bot  #424 (line in Coconut source)
        elif self.neg == bot:  #425 (line in Coconut source)
            return top  #426 (line in Coconut source)
        elif isinstance(self.neg, Not):  #427 (line in Coconut source)
            return _coconut_tail_call(self.neg.neg.simplify, **kwargs)  #428 (line in Coconut source)
        elif isinstance(self.neg, And):  #429 (line in Coconut source)
            return _coconut_tail_call(Or(*map(Not, self.neg.ands)).simplify, **kwargs)  #430 (line in Coconut source)
        elif isinstance(self.neg, Or):  #431 (line in Coconut source)
            return _coconut_tail_call(And(*map(Not, self.neg.ors)).simplify, **kwargs)  #432 (line in Coconut source)
        elif isinstance(self.neg, Imp):  #433 (line in Coconut source)
            ands = self.neg.conds + (Not(self.neg.concl),)  #434 (line in Coconut source)
            return _coconut_tail_call(And(*ands).simplify, **kwargs)  #435 (line in Coconut source)
        elif isinstance(self.neg, Exists):  #436 (line in Coconut source)
            return _coconut_tail_call(ForAll, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  #437 (line in Coconut source)
        elif isinstance(self.neg, ForAll):  #438 (line in Coconut source)
            return _coconut_tail_call(Exists, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  #439 (line in Coconut source)
        else:  #440 (line in Coconut source)
            return _coconut_tail_call(Not, self.neg.simplify(**kwargs))  #441 (line in Coconut source)


    def contradicts(self, other, **kwargs):  #443 (line in Coconut source)
        return self.neg == other  #444 (line in Coconut source)


    @_coconut_tco  #446 (line in Coconut source)
    def resolve_against(self, other, **kwargs):  #446 (line in Coconut source)
        if isinstance(other, (Or, Eq)):  #447 (line in Coconut source)
            return _coconut_tail_call(other.resolve_against, self, **kwargs)  #448 (line in Coconut source)
        elif self.neg.find_unification(other, **kwargs) is not None:  #449 (line in Coconut source)
            return bot  #450 (line in Coconut source)
        else:  #451 (line in Coconut source)
            return None  #452 (line in Coconut source)


    @_coconut_tco  #454 (line in Coconut source)
    def admits_empty_universe(self):  #454 (line in Coconut source)
        if isinstance(self.neg, Atom):  #455 (line in Coconut source)
            return _coconut_tail_call(self.neg.admits_empty_universe)  #456 (line in Coconut source)
        else:  #457 (line in Coconut source)
            return not self.neg.admits_empty_universe()  #458 (line in Coconut source)



_coconut_call_set_names(Not)  #461 (line in Coconut source)
class Quantifier(Expr):  #461 (line in Coconut source)
    """Base class for logical quantifiers."""  #462 (line in Coconut source)
    __slots__ = ("var", "elem")  #463 (line in Coconut source)
    __hash__ = Expr.__hash__  #464 (line in Coconut source)

    def __repr__(self):  #466 (line in Coconut source)
        return self.__class__.__name__ + '("' + str(self.var) + '", ' + repr(self.elem) + ")"  #467 (line in Coconut source)


    def __str__(self):  #469 (line in Coconut source)
        return self.opstr + " " + str(self.var) + ", " + quote(self.elem, in_quantifier=True)  #470 (line in Coconut source)


    def __len__(self):  #472 (line in Coconut source)
        return len(self.elem) + len(self.var)  #473 (line in Coconut source)


    @_coconut_tco  #475 (line in Coconut source)
    def change_var(self, var):  #475 (line in Coconut source)
        """Create an equivalent expression with a new quantified variable."""  #476 (line in Coconut source)
        return _coconut_tail_call(self.__class__, var, self.elem.substitute({self.var: var}))  #477 (line in Coconut source)


    @_coconut_tco  #479 (line in Coconut source)
    def change_elem(self, elem):  #479 (line in Coconut source)
        """Create an equivalent quantifier with a new expression."""  #480 (line in Coconut source)
        return _coconut_tail_call(self.__class__, self.var, elem)  #481 (line in Coconut source)


    def __eq__(self, other):  #483 (line in Coconut source)
        if isinstance(other, self.__class__):  #484 (line in Coconut source)
            return self.elem == other.change_var(self.var).elem  #485 (line in Coconut source)
        else:  #486 (line in Coconut source)
            return False  #487 (line in Coconut source)


    def inner_kwargs(self, kwargs):  #489 (line in Coconut source)
        inner_kwargs = kwargs.copy()  #490 (line in Coconut source)
        inner_kwargs["in_" + self.__class__.__name__.lower()] = True  #491 (line in Coconut source)
        return inner_kwargs  #492 (line in Coconut source)


    @_coconut_tco  #494 (line in Coconut source)
    def resolve(self, **kwargs):  #494 (line in Coconut source)
        return _coconut_tail_call(self.__class__(self.var, self.elem.resolve(**self.inner_kwargs(kwargs))).simplify, dnf=False, **kwargs)  #495 (line in Coconut source)


    @_coconut_tco  #497 (line in Coconut source)
    def simplify(self, **kwargs):  #497 (line in Coconut source)
        return _coconut_tail_call(self.__class__(self.var, self.elem.simplify(**self.inner_kwargs(kwargs))).drop_quantifier, **kwargs)  #498 (line in Coconut source)


    @_coconut_tco  #500 (line in Coconut source)
    def substitute(self, subs, **kwargs):  #500 (line in Coconut source)
        return _coconut_tail_call((self.change_elem), (self.elem.substitute)((rem_var)(self.var, subs), **kwargs))  #501 (line in Coconut source)


    @_coconut_tco  #503 (line in Coconut source)
    def make_free_in(self, other):  #503 (line in Coconut source)
        """Makes self free in other."""  #504 (line in Coconut source)
        var = self.var  #505 (line in Coconut source)
        while not var.is_free_in(other):  #506 (line in Coconut source)
            var = var.prime()  #507 (line in Coconut source)
        return _coconut_tail_call(self.change_var, var)  #508 (line in Coconut source)


    @_coconut_tco  #510 (line in Coconut source)
    def find_unification(self, other, **kwargs):  #510 (line in Coconut source)
        unif = self.elem.find_unification(other, **kwargs)  #511 (line in Coconut source)
        if unif is None:  #512 (line in Coconut source)
            return None  #513 (line in Coconut source)
        else:  #514 (line in Coconut source)
            return _coconut_tail_call((rem_var), self.var, unif)  #515 (line in Coconut source)


    @_coconut_tco  #517 (line in Coconut source)
    def resolve_against(self, other, **kwargs):  #517 (line in Coconut source)
        if isinstance(other, Quantifier):  #518 (line in Coconut source)
            resolution = (self.elem.resolve_against)(Not(other.elem).simplify(**kwargs), **kwargs)  #519 (line in Coconut source)
            if resolution is None:  #520 (line in Coconut source)
                return None  #521 (line in Coconut source)
            elif isinstance(other, ForAll):  # don't pull an Exists out of a ForAll  #522 (line in Coconut source)
                return _coconut_tail_call((other.change_elem), (self.change_elem)(resolution))  #523 (line in Coconut source)
            else:  #524 (line in Coconut source)
                return _coconut_tail_call((self.change_elem), (other.change_elem)(resolution))  #525 (line in Coconut source)
        else:  #526 (line in Coconut source)
            __class__ = Quantifier  #527 (line in Coconut source)

            return super().resolve_against(other, **kwargs)  #527 (line in Coconut source)

    @classmethod  #528 (line in Coconut source)

    @_coconut_tco  #530 (line in Coconut source)
    def blank(cls, elem):  #530 (line in Coconut source)
        """Make a quantifier without a variable."""  #531 (line in Coconut source)
        return _coconut_tail_call(cls(empty_var, elem).make_free_in, elem)  #532 (line in Coconut source)



_coconut_call_set_names(Quantifier)  #535 (line in Coconut source)
class ForAll(Quantifier):  #535 (line in Coconut source)
    """Universal quantifier."""  #536 (line in Coconut source)
    __slots__ = ()  #537 (line in Coconut source)
    __hash__ = Expr.__hash__  #538 (line in Coconut source)
    opstr = forall_sym  #539 (line in Coconut source)

    def __init__(self, var, elem):  #541 (line in Coconut source)
        assert wff(elem), elem  #542 (line in Coconut source)
        if isinstance(var, str):  #543 (line in Coconut source)
            var = Const(var)  #544 (line in Coconut source)
        assert isvar(var), var  #545 (line in Coconut source)
        self.var = var.variable()  #546 (line in Coconut source)
        self.elem = elem.substitute({var: self.var.variable()})  #547 (line in Coconut source)


    def inner_kwargs(self, kwargs):  #549 (line in Coconut source)
        __class__ = ForAll  #550 (line in Coconut source)

        inner_kwargs = super().inner_kwargs(kwargs)  #550 (line in Coconut source)
        inner_kwargs["variables"] = inner_kwargs.get("variables", ()) + (self.var,)  #551 (line in Coconut source)
        return inner_kwargs  #552 (line in Coconut source)


    def drop_quantifier(self, nonempty_universe=True, in_forall=False, **kwargs):  #554 (line in Coconut source)
        kwargs["nonempty_universe"], kwargs["in_forall"] = nonempty_universe, in_forall  #555 (line in Coconut source)
        if not nonempty_universe and not in_forall:  #556 (line in Coconut source)
            elem = self.elem  #557 (line in Coconut source)
            while isinstance(elem, Exists):  #558 (line in Coconut source)
                elem = elem.elem  #559 (line in Coconut source)
            if top == elem:  #560 (line in Coconut source)
                return elem  #561 (line in Coconut source)
        elif self.var.is_free_in(self.elem):  #562 (line in Coconut source)
            return self.elem  #563 (line in Coconut source)
        return self  #564 (line in Coconut source)


_coconut_call_set_names(ForAll)  #566 (line in Coconut source)
FA = ForAll  #566 (line in Coconut source)


class Exists(Quantifier):  #569 (line in Coconut source)
    """Existential quantifier."""  #570 (line in Coconut source)
    __slots__ = ()  #571 (line in Coconut source)
    __hash__ = Expr.__hash__  #572 (line in Coconut source)
    opstr = exists_sym  #573 (line in Coconut source)

    def __init__(self, var, elem):  #575 (line in Coconut source)
        assert wff(elem), elem  #576 (line in Coconut source)
        if isinstance(var, str):  #577 (line in Coconut source)
            var = Const(var)  #578 (line in Coconut source)
        assert isvar(var), var  #579 (line in Coconut source)
        self.var = var.constant()  #580 (line in Coconut source)
        self.elem = elem.substitute({var: self.var.constant()})  #581 (line in Coconut source)


    @_coconut_tco  #583 (line in Coconut source)
    def resolve(self, **kwargs):  #583 (line in Coconut source)
        skolem_args = kwargs.get("variables")  #584 (line in Coconut source)
        if skolem_args is None:  #585 (line in Coconut source)
            skolem_var = self.var.skolem()  #586 (line in Coconut source)
            while not skolem_var.is_free_in(self.elem):  #587 (line in Coconut source)
                skolem_var = skolem_var.prime()  #588 (line in Coconut source)
        else:  #589 (line in Coconut source)
            skolem_var = Func(self.var.skolem(), *skolem_args)  #590 (line in Coconut source)
        skolem_elem = self.elem.substitute({self.var: skolem_var})  #591 (line in Coconut source)
        return _coconut_tail_call(Exists(self.var, skolem_elem.resolve(**self.inner_kwargs(kwargs))).simplify, dnf=False, **kwargs)  #592 (line in Coconut source)


    def inner_kwargs(self, kwargs):  #594 (line in Coconut source)
        __class__ = Exists  #595 (line in Coconut source)

        inner_kwargs = super().inner_kwargs(kwargs)  #595 (line in Coconut source)
        inner_kwargs["nonempty_universe"] = True  #596 (line in Coconut source)
        return inner_kwargs  #597 (line in Coconut source)


    def drop_quantifier(self, nonempty_universe=True, in_exists=False, **kwargs):  #599 (line in Coconut source)
        kwargs["nonempty_universe"], kwargs["in_exists"] = nonempty_universe, in_exists  #600 (line in Coconut source)
        if not nonempty_universe and not in_exists:  #601 (line in Coconut source)
            elem = self.elem  #602 (line in Coconut source)
            while isinstance(elem, ForAll):  #603 (line in Coconut source)
                elem = elem.elem  #604 (line in Coconut source)
            if bot == elem:  #605 (line in Coconut source)
                return elem  #606 (line in Coconut source)
        elif self.var.is_free_in(self.elem):  #607 (line in Coconut source)
            return self.elem  #608 (line in Coconut source)
        return self  #609 (line in Coconut source)


    def admits_empty_universe(self):  #611 (line in Coconut source)
        return False  #611 (line in Coconut source)


_coconut_call_set_names(Exists)  #613 (line in Coconut source)
TE = EX = Exists  #613 (line in Coconut source)


class BinaryOp(Expr):  #616 (line in Coconut source)
    """Base class for binary operators."""  #617 (line in Coconut source)
    __slots__ = ("elems",)  #618 (line in Coconut source)
    __hash__ = Expr.__hash__  #619 (line in Coconut source)
    identity = None  #620 (line in Coconut source)

    def __new__(cls, *elems):  #622 (line in Coconut source)
        if not elems:  #623 (line in Coconut source)
            if cls.identity is None:  #624 (line in Coconut source)
                raise TypeError(cls.__name__ + " requires at least one argument")  #625 (line in Coconut source)
            else:  #626 (line in Coconut source)
                return cls.identity  #627 (line in Coconut source)
        elif len(elems) == 1:  #628 (line in Coconut source)
            assert wff(elems[0]), elems[0]  #629 (line in Coconut source)
            return elems[0]  # sometimes returns an instance of cls  #630 (line in Coconut source)
        else:  #631 (line in Coconut source)
            __class__ = BinaryOp  #632 (line in Coconut source)

            return super().__new__(cls)  #632 (line in Coconut source)


    def __init__(self, *elems):  #634 (line in Coconut source)
        if len(elems) > 1:  # __new__ should handle all other cases  #635 (line in Coconut source)
            assert len(elems) >= 2, elems  #636 (line in Coconut source)
            for x in elems:  #637 (line in Coconut source)
                assert wff(x), x  #638 (line in Coconut source)
            self.elems = elems  #639 (line in Coconut source)


    def __repr__(self):  #641 (line in Coconut source)
        return self.__class__.__name__ + "(" + ", ".join((repr(x) for x in self.elems)) + ")"  #642 (line in Coconut source)


    @_coconut_tco  #644 (line in Coconut source)
    def __str__(self):  #644 (line in Coconut source)
        return _coconut_tail_call((" " + self.opstr + " ").join, (quote(x) for x in self.elems))  #645 (line in Coconut source)


    def __len__(self):  #647 (line in Coconut source)
        return sum(map(len, self.elems)) + 1  #648 (line in Coconut source)


    @_coconut_tco  #650 (line in Coconut source)
    def substitute(self, subs, **kwargs):  #650 (line in Coconut source)
        return _coconut_tail_call((self.__class__), *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.elems))  #651 (line in Coconut source)


    @_coconut_tco  #653 (line in Coconut source)
    def resolve(self, **kwargs):  #653 (line in Coconut source)
        elems = (map)(_coconut.operator.methodcaller("resolve", **kwargs), self.elems)  #654 (line in Coconut source)
        return _coconut_tail_call(self.__class__(*elems).simplify, dnf=False, **kwargs)  #655 (line in Coconut source)


    @_coconut_tco  #657 (line in Coconut source)
    def find_unification(self, other, **kwargs):  #657 (line in Coconut source)
        if isinstance(other, self.__class__) and len(self.elems) == len(other.elems):  #658 (line in Coconut source)
            return _coconut_tail_call(unify_elems, self, other, elems_getter=_coconut.operator.attrgetter("elems"), **kwargs)  #659 (line in Coconut source)
        else:  #660 (line in Coconut source)
            __class__ = BinaryOp  #661 (line in Coconut source)

            return super().find_unification(other, **kwargs)  #661 (line in Coconut source)



_coconut_call_set_names(BinaryOp)  #664 (line in Coconut source)
class Imp(BinaryOp):  #664 (line in Coconut source)
    """Logical implication."""  #665 (line in Coconut source)
    __slots__ = ()  #666 (line in Coconut source)
    __hash__ = Expr.__hash__  #667 (line in Coconut source)
    opstr = imp_sym  #668 (line in Coconut source)

    @_coconut_tco  #670 (line in Coconut source)
    def __rshift__(self, other):  #670 (line in Coconut source)
        if isinstance(other, Imp):  #671 (line in Coconut source)
            return _coconut_tail_call(Imp, self, *other.elems)  #672 (line in Coconut source)
        else:  #673 (line in Coconut source)
            return _coconut_tail_call(Imp, self, other)  #674 (line in Coconut source)


    @_coconut_tco  #676 (line in Coconut source)
    def __lshift__(self, other):  #676 (line in Coconut source)
        return _coconut_tail_call((Imp), *(other,) + self.elems)  #677 (line in Coconut source)


    @property  #679 (line in Coconut source)
    def conds(self):  #680 (line in Coconut source)
        return self.elems[:-1]  #680 (line in Coconut source)


    @property  #682 (line in Coconut source)
    def concl(self):  #683 (line in Coconut source)
        return self.elems[-1]  #683 (line in Coconut source)


    def __eq__(self, other):  #685 (line in Coconut source)
        return isinstance(other, self.__class__) and self.concl == other.concl and (unorderd_eq)(self.conds, other.conds)  #686 (line in Coconut source)


    @_coconut_tco  #688 (line in Coconut source)
    def to_or(self):  #688 (line in Coconut source)
        ors = tuple(map(Not, self.conds)) + (self.concl,)  #689 (line in Coconut source)
        return _coconut_tail_call(Or, *ors)  #690 (line in Coconut source)


    @_coconut_tco  #692 (line in Coconut source)
    def simplify(self, **kwargs):  #692 (line in Coconut source)
        return _coconut_tail_call(self.to_or().simplify, **kwargs)  #693 (line in Coconut source)


    @_coconut_tco  #695 (line in Coconut source)
    def admits_empty_universe(self):  #695 (line in Coconut source)
        return _coconut_tail_call(self.to_or().admits_empty_universe)  #696 (line in Coconut source)


_coconut_call_set_names(Imp)  #698 (line in Coconut source)
Implies = Imp  #698 (line in Coconut source)


class BoolOp(BinaryOp):  #701 (line in Coconut source)
    """Base class for Or and And."""  #702 (line in Coconut source)
    __slots__ = ()  #703 (line in Coconut source)
    __hash__ = Expr.__hash__  #704 (line in Coconut source)

    def __eq__(self, other):  #706 (line in Coconut source)
        return isinstance(other, self.__class__) and (unorderd_eq)(self.elems, other.elems)  #707 (line in Coconut source)


    def simplify(self, **kwargs):  #709 (line in Coconut source)
        elems = (map)(_coconut.operator.methodcaller("simplify", **kwargs), self.merge().elems)  #710 (line in Coconut source)
        out = self.__class__(*elems).clean()  #711 (line in Coconut source)
        if isinstance(out, self.__class__):  #712 (line in Coconut source)
            out = out.distribute(**kwargs)  #713 (line in Coconut source)
        if isinstance(out, self.__class__):  #714 (line in Coconut source)
            out = out.merge().dedupe()  #715 (line in Coconut source)
        if isinstance(out, self.__class__):  #716 (line in Coconut source)
            out = out.inner_simplify(**kwargs)  #717 (line in Coconut source)
        if isinstance(out, self.__class__):  #718 (line in Coconut source)
            out = out.prenex(**kwargs)  #719 (line in Coconut source)
        log_simplification(self, out, **kwargs)  #720 (line in Coconut source)
        return out  #721 (line in Coconut source)


    @_coconut_tco  #723 (line in Coconut source)
    def merge(self):  #723 (line in Coconut source)
        """Merges nested copies of a boolean operator."""  #724 (line in Coconut source)
        elems = []  #725 (line in Coconut source)
        for x in self.elems:  #726 (line in Coconut source)
            if isinstance(x, self.__class__):  #727 (line in Coconut source)
                elems.extend(x.merge().elems)  #728 (line in Coconut source)
            else:  #729 (line in Coconut source)
                elems.append(x)  #730 (line in Coconut source)
        return _coconut_tail_call(self.__class__, *elems)  #731 (line in Coconut source)


    @_coconut_tco  #733 (line in Coconut source)
    def dedupe(self):  #733 (line in Coconut source)
        """Removes duplicate elements from a boolean operator."""  #734 (line in Coconut source)
        elems = []  #735 (line in Coconut source)
        for x in self.elems:  #736 (line in Coconut source)
            if x not in elems:  #737 (line in Coconut source)
                elems.append(x)  #738 (line in Coconut source)
        return _coconut_tail_call(self.__class__, *elems)  #739 (line in Coconut source)


    @_coconut_tco  #741 (line in Coconut source)
    def clean(self):  #741 (line in Coconut source)
        """Removes copies of the identity."""  #742 (line in Coconut source)
        return _coconut_tail_call((self.__class__), *(filter)(_coconut.functools.partial((_coconut.operator.ne), self.identity), self.elems))  #743 (line in Coconut source)


    def prenex(self, **kwargs):  #745 (line in Coconut source)
        """Pulls quantifiers out."""  #746 (line in Coconut source)
        for i, x in enumerate(self.elems):  #747 (line in Coconut source)
            if isinstance(x, Quantifier) and self.can_prenex(x, **kwargs):  #748 (line in Coconut source)
                elems = self.elems[:i] + self.elems[i + 1:]  #749 (line in Coconut source)
                free_x = x.make_free_in(self.__class__(*elems))  #750 (line in Coconut source)
                elems += (free_x.elem,)  #751 (line in Coconut source)
                return free_x.change_elem(self.__class__(*elems)).simplify(**kwargs)  #752 (line in Coconut source)
        return self  #753 (line in Coconut source)



_coconut_call_set_names(BoolOp)  #756 (line in Coconut source)
class Or(BoolOp):  #756 (line in Coconut source)
    """Logical disjunction."""  #757 (line in Coconut source)
    __slots__ = ()  #758 (line in Coconut source)
    __hash__ = Expr.__hash__  #759 (line in Coconut source)
    opstr = or_sym  #760 (line in Coconut source)
    identity = bot  #761 (line in Coconut source)

    @_coconut_tco  #763 (line in Coconut source)
    def __or__(self, other):  #763 (line in Coconut source)
        return _coconut_tail_call((Or), *self.elems + (other,))  #764 (line in Coconut source)


    @property  #766 (line in Coconut source)
    def ors(self):  #767 (line in Coconut source)
        return self.elems  #767 (line in Coconut source)


    def distribute(self, dnf=False, **kwargs):  #769 (line in Coconut source)
        """If this Or contains an And, distribute into it."""  #770 (line in Coconut source)
        kwargs["dnf"] = dnf  #771 (line in Coconut source)
        if not dnf:  #772 (line in Coconut source)
            for i, x in enumerate(self.ors):  #773 (line in Coconut source)
                if isinstance(x, And):  #774 (line in Coconut source)
                    ands = ((Or)(*(y,) + self.ors[:i] + self.ors[i + 1:]) for y in x.ands)  #775 (line in Coconut source)
                    return And(*ands).simplify(**kwargs)  #776 (line in Coconut source)
        return self  #777 (line in Coconut source)


    def inner_simplify(self, nonempty_universe=True, **kwargs):  #779 (line in Coconut source)
        """Determines if the Or is a blatant tautology."""  #780 (line in Coconut source)
        kwargs["nonempty_universe"] = nonempty_universe  #781 (line in Coconut source)
        for i, x in enumerate(self.ors):  #782 (line in Coconut source)
            if top == x:  #783 (line in Coconut source)
                return x  #784 (line in Coconut source)
            for y in self.ors[i + 1:]:  #785 (line in Coconut source)
                if x.contradicts(y, **kwargs):  #786 (line in Coconut source)
                    if not nonempty_universe and not self.admits_empty_universe():  #787 (line in Coconut source)
                        return Exists.blank(top)  #788 (line in Coconut source)
                    else:  #789 (line in Coconut source)
                        return top  #790 (line in Coconut source)
        return self  #791 (line in Coconut source)


    def can_prenex(self, other, nonempty_universe=True, in_forall=False, prenex_foralls=False, prenex_exists=True, **_):  #793 (line in Coconut source)
        if not prenex_foralls and isinstance(other, ForAll):  #794 (line in Coconut source)
            return False  #795 (line in Coconut source)
        if not prenex_exists and isinstance(other, Exists):  #796 (line in Coconut source)
            return False  #797 (line in Coconut source)
        return (nonempty_universe or in_forall or not isinstance(other, Exists) or not self.admits_empty_universe())  #798 (line in Coconut source)


    @_coconut_tco  #803 (line in Coconut source)
    def resolve_against(self, other, **kwargs):  #803 (line in Coconut source)
        if isinstance(other, Eq):  #804 (line in Coconut source)
            return _coconut_tail_call(other.resolve_against, self)  #805 (line in Coconut source)
        elif isinstance(other, Or):  #806 (line in Coconut source)
            not_other_ors = (map)(_coconut.operator.methodcaller("simplify", **kwargs), (map)(Not, other.ors))  #807 (line in Coconut source)
            for i, x in enumerate(self.ors):  #808 (line in Coconut source)
                if isinstance(x, Eq):  #809 (line in Coconut source)
                    resolved_other = (x.paramodulant)(other)  #810 (line in Coconut source)
                    return (Or)(*self.ors[:i] + self.ors[i + 1:] + resolved_other.ors)  #811 (line in Coconut source)
                for j, y in enumerate(not_other_ors):  #812 (line in Coconut source)
                    if isinstance(other.ors[j], Eq):  #813 (line in Coconut source)
                        y = other.ors[j]  #814 (line in Coconut source)
                        resolved_self = (y.paramodulant)(self)  #815 (line in Coconut source)
                        return (Or)(*other.ors[:j] + other.ors[j + 1:] + resolved_self.ors)  #816 (line in Coconut source)
                    subs = x.find_unification(y, **kwargs)  #817 (line in Coconut source)
                    if subs is not None:  #818 (line in Coconut source)
                        return (Or)(*(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.ors[:i] + self.ors[i + 1:] + other.ors[:j] + other.ors[j + 1:]))  #819 (line in Coconut source)
        else:  #820 (line in Coconut source)
            not_other = Not(other).simplify(**kwargs)  #821 (line in Coconut source)
            for i, x in enumerate(self.ors):  #822 (line in Coconut source)
                if isinstance(x, Eq):  #823 (line in Coconut source)
                    return (x.paramodulant)((Or)(*self.ors[:i] + self.ors[i + 1:]))  #824 (line in Coconut source)
                subs = x.find_unification(not_other, **kwargs)  #825 (line in Coconut source)
                if subs is not None:  #826 (line in Coconut source)
                    return (Or)(*(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.ors[:i] + self.ors[i + 1:]))  #827 (line in Coconut source)
        return None  #828 (line in Coconut source)


    @_coconut_tco  #830 (line in Coconut source)
    def admits_empty_universe(self):  #830 (line in Coconut source)
        return _coconut_tail_call(any, (x.admits_empty_universe() for x in self.elems))  #831 (line in Coconut source)



_coconut_call_set_names(Or)  #834 (line in Coconut source)
class And(BoolOp):  #834 (line in Coconut source)
    """Logical conjunction."""  #835 (line in Coconut source)
    __slots__ = ()  #836 (line in Coconut source)
    __hash__ = Expr.__hash__  #837 (line in Coconut source)
    opstr = and_sym  #838 (line in Coconut source)
    identity = top  #839 (line in Coconut source)

    @_coconut_tco  #841 (line in Coconut source)
    def __and__(self, other):  #841 (line in Coconut source)
        return _coconut_tail_call((And), *self.elems + (other,))  #842 (line in Coconut source)


    @property  #844 (line in Coconut source)
    def ands(self):  #845 (line in Coconut source)
        return self.elems  #845 (line in Coconut source)


    def distribute(self, dnf=False, **kwargs):  #847 (line in Coconut source)
        """If this And contains an Or, distribute into it."""  #848 (line in Coconut source)
        kwargs["dnf"] = dnf  #849 (line in Coconut source)
        if dnf:  #850 (line in Coconut source)
            for i, x in enumerate(self.ands):  #851 (line in Coconut source)
                if isinstance(x, Or):  #852 (line in Coconut source)
                    ors = ((And)(*(y,) + self.ands[:i] + self.ands[i + 1:]) for y in x.ors)  #853 (line in Coconut source)
                    return Or(*ors).simplify(**kwargs)  #854 (line in Coconut source)
        return self  #855 (line in Coconut source)


    def inner_simplify(self, nonempty_universe=True, **kwargs):  #857 (line in Coconut source)
        """Determines if the And is a blatant contradiction."""  #858 (line in Coconut source)
        kwargs["nonempty_universe"] = nonempty_universe  #859 (line in Coconut source)
        for i, x in enumerate(self.ands):  #860 (line in Coconut source)
            if bot == x:  #861 (line in Coconut source)
                return x  #862 (line in Coconut source)
            for y in self.ands[i + 1:]:  #863 (line in Coconut source)
                if x.contradicts(y, **kwargs):  #864 (line in Coconut source)
                    if not nonempty_universe and self.admits_empty_universe():  #865 (line in Coconut source)
                        return ForAll.blank(bot)  #866 (line in Coconut source)
                    else:  #867 (line in Coconut source)
                        return bot  #868 (line in Coconut source)
        return self  #869 (line in Coconut source)


    def can_prenex(self, other, nonempty_universe=True, in_exists=False, prenex_foralls=False, prenex_exists=True, **_):  #871 (line in Coconut source)
        if not prenex_foralls and isinstance(other, ForAll):  #872 (line in Coconut source)
            return False  #873 (line in Coconut source)
        if not prenex_exists and isinstance(other, Exists):  #874 (line in Coconut source)
            return False  #875 (line in Coconut source)
        return (nonempty_universe or in_exists or not isinstance(other, ForAll) or all((isinstance(x, ForAll) for x in self.elems)))  #876 (line in Coconut source)


    @_coconut_tco  #881 (line in Coconut source)
    def resolve(self, nonempty_universe=True, just_skolemize=False, debug=False, **kwargs):  #881 (line in Coconut source)
        """Performs all possible resolutions within the And."""  #882 (line in Coconut source)
        kwargs["nonempty_universe"], kwargs["just_skolemize"], kwargs["debug"] = nonempty_universe, just_skolemize, debug  #883 (line in Coconut source)

# skolemize
        __class__ = And  #886 (line in Coconut source)

        resolved = super().resolve(**kwargs)  #886 (line in Coconut source)
        log_simplification(self, resolved, **kwargs)  #887 (line in Coconut source)
        if not isinstance(resolved, And) or just_skolemize:  #888 (line in Coconut source)
            return resolved  #889 (line in Coconut source)
        self = resolved  #890 (line in Coconut source)

# if we don't admit a nonempty universe, enforce that
        quantifiers = []  #893 (line in Coconut source)
        if not nonempty_universe and not self.admits_empty_universe():  #894 (line in Coconut source)
            blank = Exists.blank(top)  #895 (line in Coconut source)
            (quantifiers.append)(blank.change_elem)  #896 (line in Coconut source)
            kwargs = (blank.inner_kwargs)(kwargs)  #897 (line in Coconut source)

# push foralls into clauses
        clauses = []  #900 (line in Coconut source)
        final_subs = {}  #901 (line in Coconut source)
        for i, clause in enumerate(self.ands):  #902 (line in Coconut source)
            clause_subs = dict(((v), (v.subscript(i))) for v in kwargs.get("variables", ()))  #903 (line in Coconut source)
            (clauses.append)(clause.substitute(clause_subs, **kwargs))  #904 (line in Coconut source)
            final_subs.update(dict(((v.subscript(i)), (v)) for v in kwargs.get("variables", ())))  #905 (line in Coconut source)
        kwargs["variables"] = (tuple)(final_subs.keys())  #906 (line in Coconut source)
        log_simplification(self, And(*clauses), **kwargs)  #907 (line in Coconut source)

# main resolution loop
        prev_clause_len = 1  #910 (line in Coconut source)
        while prev_clause_len < len(clauses):  #911 (line in Coconut source)
            prev_clause_len = len(clauses)  #912 (line in Coconut source)
# reversed ensures conclusions get tested first
            for i in (reversed)(range(1, len(clauses))):  #914 (line in Coconut source)
                x = clauses[i]  #915 (line in Coconut source)
                for y in clauses[:i + 1]:  # allow resolution of a clause against itself  #916 (line in Coconut source)
                    resolution = x.resolve_against(y)  #917 (line in Coconut source)
                    if resolution is not None:  #918 (line in Coconut source)
                        resolution = resolution.simplify(dnf=False, **kwargs)  #919 (line in Coconut source)
                        log_resolution(x, y, resolution, **kwargs)  #920 (line in Coconut source)
                        new_quantifiers = []  #921 (line in Coconut source)
                        inner_kwargs = kwargs  #922 (line in Coconut source)
                        while isinstance(resolution, Quantifier) and self.can_prenex(resolution, **kwargs):  #923 (line in Coconut source)
                            (new_quantifiers.append)(resolution.change_elem)  #924 (line in Coconut source)
                            inner_kwargs = (resolution.inner_kwargs)(inner_kwargs)  #925 (line in Coconut source)
                            resolution = resolution.elem  #926 (line in Coconut source)
                        if isinstance(resolution, And):  #927 (line in Coconut source)
                            new_clauses = resolution.ands  #928 (line in Coconut source)
                        else:  #929 (line in Coconut source)
                            new_clauses = (resolution,)  #930 (line in Coconut source)
                        novel = False  #931 (line in Coconut source)
                        for new_clause in new_clauses:  #932 (line in Coconut source)
                            if new_clause == bot:  #933 (line in Coconut source)
                                clauses = [bot,]  #934 (line in Coconut source)
                                novel = True  #935 (line in Coconut source)
                                break  #936 (line in Coconut source)
                            elif new_clause != top and new_clause not in clauses:  #937 (line in Coconut source)
                                clauses.append(new_clause)  #938 (line in Coconut source)
                                novel = True  #939 (line in Coconut source)
                        if novel:  #940 (line in Coconut source)
                            quantifiers.extend(new_quantifiers)  #941 (line in Coconut source)
                            kwargs = inner_kwargs  #942 (line in Coconut source)
                            if clauses == [bot,]:  #943 (line in Coconut source)
                                break  #944 (line in Coconut source)
                if clauses == [bot,]:  #945 (line in Coconut source)
                    break  #946 (line in Coconut source)

# combine resolved clauses
        resolved = ((reduce)(_coconut_pipe, [And(*clauses),] + quantifiers)).substitute(final_subs, **kwargs)  #949 (line in Coconut source)
        log_simplification(self, resolved, **kwargs)  #950 (line in Coconut source)
        self = resolved  #951 (line in Coconut source)

        return _coconut_tail_call(self.simplify, dnf=False, **kwargs)  #953 (line in Coconut source)


    @_coconut_tco  #955 (line in Coconut source)
    def admits_empty_universe(self):  #955 (line in Coconut source)
        return _coconut_tail_call(all, (x.admits_empty_universe() for x in self.elems))  #956 (line in Coconut source)



_coconut_call_set_names(And)  #959 (line in Coconut source)
class Eq(Expr):  #959 (line in Coconut source)
    """Equality operator."""  #960 (line in Coconut source)
    __slots__ = ("a", "b")  #961 (line in Coconut source)
    __hash__ = Expr.__hash__  #962 (line in Coconut source)

    def __init__(self, a, b):  #964 (line in Coconut source)
        assert isinstance(a, Term), a  #965 (line in Coconut source)
        assert isinstance(b, Term), b  #966 (line in Coconut source)
        self.a, self.b = a, b  #967 (line in Coconut source)


    def __repr__(self):  #969 (line in Coconut source)
        return "Eq(" + repr(self.a) + ", " + repr(self.b) + ")"  #970 (line in Coconut source)


    def __str__(self):  #972 (line in Coconut source)
        return str(self.a) + "=" + str(self.b)  #973 (line in Coconut source)


    def __eq__(self, other):  #975 (line in Coconut source)
        return isinstance(other, Eq) and (self.a == other.a and self.b == other.b or self.a == other.b and self.b == other.a)  #976 (line in Coconut source)


    def simplify(self, **kwargs):  #978 (line in Coconut source)
        if self.a == self.b:  #979 (line in Coconut source)
            return top  #980 (line in Coconut source)
        else:  #981 (line in Coconut source)
            return self  #982 (line in Coconut source)


    @_coconut_tco  #984 (line in Coconut source)
    def swap(self):  #984 (line in Coconut source)
        """Swaps the order of equality."""  #985 (line in Coconut source)
        return _coconut_tail_call(Eq, self.b, self.a)  #986 (line in Coconut source)


    def find_unification(self, other, **kwargs):  #988 (line in Coconut source)
        if isinstance(other, Eq):  #989 (line in Coconut source)
            aa_bb_unif = unify_elems(self, other, elems_getter=lift(_coconut_comma_op)(_coconut.operator.attrgetter("a"), _coconut.operator.attrgetter("b")), **kwargs)  #990 (line in Coconut source)
            if aa_bb_unif is not None:  #991 (line in Coconut source)
                return aa_bb_unif  #992 (line in Coconut source)
            ab_ba_unif = unify_elems(self, other.swap(), elems_getter=lift(_coconut_comma_op)(_coconut.operator.attrgetter("a"), _coconut.operator.attrgetter("b")), **kwargs)  #993 (line in Coconut source)
            return ab_ba_unif  #994 (line in Coconut source)
        else:  #995 (line in Coconut source)
            __class__ = Eq  #996 (line in Coconut source)

            return super().find_unification(other, **kwargs)  #996 (line in Coconut source)


    @_coconut_tco  #998 (line in Coconut source)
    def substitute(self, subs, **kwargs):  #998 (line in Coconut source)
        return _coconut_tail_call(Eq, self.a.substitute(subs, **kwargs), self.b.substitute(subs, **kwargs))  #999 (line in Coconut source)


    @_coconut_tco  #1001 (line in Coconut source)
    def paramodulant(self, other):  #1001 (line in Coconut source)
        """Create a paramodulant of other."""  #1002 (line in Coconut source)
        return _coconut_tail_call((sub_once), other, {self.a: self.b, self.b: self.a})  #1003 (line in Coconut source)


    @_coconut_tco  #1005 (line in Coconut source)
    def resolve_against(self, other, **kwargs):  #1005 (line in Coconut source)
        if isinstance(other, Not) and self.find_unification(other.neg, **kwargs) is not None:  #1006 (line in Coconut source)
            return bot  #1007 (line in Coconut source)
        else:  #1008 (line in Coconut source)
            return _coconut_tail_call(self.paramodulant, other)  #1009 (line in Coconut source)


    def admits_empty_universe(self):  #1011 (line in Coconut source)
        return self.a.admits_empty_universe() and self.b.admits_empty_universe()  #1012 (line in Coconut source)


_coconut_call_set_names(Eq)  #1014 (line in Coconut source)
Equals = Eq  #1014 (line in Coconut source)
