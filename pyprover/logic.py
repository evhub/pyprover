#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x67d32bf0

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

from pyprover.constants import top_sym  #3 (line num in coconut source)
from pyprover.constants import bot_sym  #3 (line num in coconut source)
from pyprover.constants import not_sym  #3 (line num in coconut source)
from pyprover.constants import imp_sym  #3 (line num in coconut source)
from pyprover.constants import and_sym  #3 (line num in coconut source)
from pyprover.constants import or_sym  #3 (line num in coconut source)
from pyprover.constants import forall_sym  #3 (line num in coconut source)
from pyprover.constants import exists_sym  #3 (line num in coconut source)
from pyprover.constants import empty_var  #3 (line num in coconut source)
from pyprover.util import unorderd_eq  #14 (line num in coconut source)
from pyprover.util import quote  #14 (line num in coconut source)
from pyprover.util import log_simplification  #14 (line num in coconut source)
from pyprover.util import log_resolution  #14 (line num in coconut source)
from pyprover.util import rem_var  #14 (line num in coconut source)
from pyprover.util import can_sub  #14 (line num in coconut source)
from pyprover.util import do_sub  #14 (line num in coconut source)
from pyprover.util import merge_dicts  #14 (line num in coconut source)
from pyprover.util import sub_once  #14 (line num in coconut source)

# Functions:

def wff(expr):  #28 (line num in coconut source)
    """Determines whether expr is a well-formed formula."""  #29 (line num in coconut source)
    return isinstance(expr, Expr) and not isinstance(expr, Term)  #30 (line num in coconut source)



@_coconut_tco  #33 (line num in coconut source)
def isvar(var):  #33 (line num in coconut source)
    """Whether a term is a variable."""  #34 (line num in coconut source)
    return _coconut_tail_call(isinstance, var, (Const, Var))  #35 (line num in coconut source)



def unify_elems(a, b, elems_getter, **kwargs):  #38 (line num in coconut source)
    """Find the most general unifier of the elements in a and b."""  #39 (line num in coconut source)
    subs = {}  #40 (line num in coconut source)
    for i, x in enumerate(elems_getter(a)):  #41 (line num in coconut source)
        y = elems_getter(b)[i]  #42 (line num in coconut source)
        unif = x.find_unification(y, **kwargs)  #43 (line num in coconut source)
        if unif is None:  #44 (line num in coconut source)
            return None  #45 (line num in coconut source)
        for var, sub in unif.items():  #46 (line num in coconut source)
            _coconut_match_to_0 = subs  #47 (line num in coconut source)
            _coconut_match_check_0 = False  #47 (line num in coconut source)
            _coconut_match_set_name_prev_sub = _coconut_sentinel  #47 (line num in coconut source)
            if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #47 (line num in coconut source)
                _coconut_match_temp_0 = _coconut_match_to_0.get(var, _coconut_sentinel)  #47 (line num in coconut source)
                if _coconut_match_temp_0 is not _coconut_sentinel:  #47 (line num in coconut source)
                    _coconut_match_set_name_prev_sub = _coconut_match_temp_0  #47 (line num in coconut source)
                    _coconut_match_check_0 = True  #47 (line num in coconut source)
            if _coconut_match_check_0:  #47 (line num in coconut source)
                if _coconut_match_set_name_prev_sub is not _coconut_sentinel:  #47 (line num in coconut source)
                    prev_sub = _coconut_match_set_name_prev_sub  #47 (line num in coconut source)
            if _coconut_match_check_0:  #47 (line num in coconut source)
                mgu = prev_sub.find_unification(sub)  #48 (line num in coconut source)
                if mgu is None:  #49 (line num in coconut source)
                    return None  #50 (line num in coconut source)
                elif mgu:  #51 (line num in coconut source)
                    new_a = a.substitute(mgu, **kwargs)  #52 (line num in coconut source)
                    new_b = b.substitute(mgu, **kwargs)  #53 (line num in coconut source)
                    new_unif = new_a.find_unification(new_b, **kwargs)  #54 (line num in coconut source)
                    if new_unif is None:  #55 (line num in coconut source)
                        return None  #56 (line num in coconut source)
                    mgu.update(new_unif)  #57 (line num in coconut source)
                    return mgu  #58 (line num in coconut source)
            else:  #59 (line num in coconut source)
                subs[var] = sub  #60 (line num in coconut source)
    return subs  #61 (line num in coconut source)


# Classes:


class Expr(_coconut.object):  #66 (line num in coconut source)
    """Base class for all formulae."""  #67 (line num in coconut source)
    __slots__ = ()  #68 (line num in coconut source)

    @_coconut_tco  #70 (line num in coconut source)
    def __hash__(self):  #70 (line num in coconut source)
#type: (...) -> int
        return _coconut_tail_call((hash), str(self))  #71 (line num in coconut source)


    def __lt__(self, other):  #73 (line num in coconut source)
#type: (...) -> int
        return str(self) < str(other)  #74 (line num in coconut source)


    def __gt__(self, other):  #76 (line num in coconut source)
#type: (...) -> int
        return str(self) > str(other)  #77 (line num in coconut source)


    def __ge__(self, other):  #79 (line num in coconut source)
#type: (...) -> int
        return str(self) >= str(other)  #80 (line num in coconut source)


    def __le__(self, other):  #82 (line num in coconut source)
#type: (...) -> int
        return str(self) <= str(other)  #83 (line num in coconut source)


    @_coconut_tco  #85 (line num in coconut source)
    def __and__(self, other):  #85 (line num in coconut source)
        if isinstance(other, And):  #86 (line num in coconut source)
            return other & self  #87 (line num in coconut source)
        else:  #88 (line num in coconut source)
            return _coconut_tail_call(And, self, other)  #89 (line num in coconut source)


    @_coconut_tco  #91 (line num in coconut source)
    def __or__(self, other):  #91 (line num in coconut source)
        if isinstance(other, Or):  #92 (line num in coconut source)
            return other | self  #93 (line num in coconut source)
        else:  #94 (line num in coconut source)
            return _coconut_tail_call(Or, self, other)  #95 (line num in coconut source)


    @_coconut_tco  #97 (line num in coconut source)
    def __rshift__(self, other):  #97 (line num in coconut source)
        if isinstance(other, Imp):  #98 (line num in coconut source)
            return other << self  #99 (line num in coconut source)
        else:  #100 (line num in coconut source)
            return _coconut_tail_call(Imp, self, other)  #101 (line num in coconut source)


    def __lshift__(self, other):  #103 (line num in coconut source)
        assert wff(other), other  #104 (line num in coconut source)
        return other >> self  #105 (line num in coconut source)


    @_coconut_tco  #107 (line num in coconut source)
    def __invert__(self):  #107 (line num in coconut source)
        return _coconut_tail_call(Not, self)  #108 (line num in coconut source)


    @_coconut_tco  #110 (line num in coconut source)
    def __xor__(self, other):  #110 (line num in coconut source)
        return _coconut_tail_call(Or, And(self, Not(other)), And(Not(self), other))  #111 (line num in coconut source)


    def __len__(self):  #113 (line num in coconut source)
        return 1  #113 (line num in coconut source)


    def simplify(self, **kwargs):  #115 (line num in coconut source)
        """Simplify the given expression."""  #116 (line num in coconut source)
        return self  #117 (line num in coconut source)


    def substitute(self, subs, **kwargs):  #119 (line num in coconut source)
        """Substitutes a dictionary into the expression."""  #120 (line num in coconut source)
        return self  #121 (line num in coconut source)


    @_coconut_tco  #123 (line num in coconut source)
    def resolve(self, **kwargs):  #123 (line num in coconut source)
        """Performs resolution on the clauses in a CNF expression."""  #124 (line num in coconut source)
        return _coconut_tail_call(self.simplify, dnf=False, **kwargs)  #125 (line num in coconut source)


    @_coconut_tco  #127 (line num in coconut source)
    def find_unification(self, other, **kwargs):  #127 (line num in coconut source)
        """Find a substitution in self that would make self into other."""  #128 (line num in coconut source)
        if isinstance(other, (Quantifier, Var)):  #129 (line num in coconut source)
            return _coconut_tail_call(other.find_unification, self, **kwargs)  #130 (line num in coconut source)
        elif self == other:  #131 (line num in coconut source)
            return {}  #132 (line num in coconut source)
        else:  #133 (line num in coconut source)
            return None  #134 (line num in coconut source)


    @_coconut_tco  #136 (line num in coconut source)
    def contradicts(self, other, **kwargs):  #136 (line num in coconut source)
        """Assuming self is simplified, determines if it contradicts other."""  #137 (line num in coconut source)
        if isinstance(other, Not):  #138 (line num in coconut source)
            return _coconut_tail_call(other.contradicts, self, **kwargs)  #139 (line num in coconut source)
        else:  #140 (line num in coconut source)
            return self == Not(other).simplify(**kwargs)  #141 (line num in coconut source)


    @_coconut_tco  #143 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #143 (line num in coconut source)
        """Attempt to perform a resolution against other else None."""  #144 (line num in coconut source)
        if isinstance(other, (Not, Or, Eq)):  #145 (line num in coconut source)
            return _coconut_tail_call(other.resolve_against, self, **kwargs)  #146 (line num in coconut source)
        elif (self.find_unification)(Not(other).simplify(**kwargs), **kwargs) is not None:  #147 (line num in coconut source)
            return bot  #148 (line num in coconut source)
        else:  #149 (line num in coconut source)
            return None  #150 (line num in coconut source)


    def admits_empty_universe(self):  #152 (line num in coconut source)
        """Determines if self allows for the possibility of an empty universe."""  #153 (line num in coconut source)
        return True  #154 (line num in coconut source)



_coconut_call_set_names(Expr)  #157 (line num in coconut source)
class Top(Expr):  #157 (line num in coconut source)
    """True"""  #158 (line num in coconut source)
    __slots__ = ()  #159 (line num in coconut source)

    @_coconut_tco  #161 (line num in coconut source)
    def __eq__(self, other):  #161 (line num in coconut source)
        return _coconut_tail_call(isinstance, other, Top)  #161 (line num in coconut source)


    def __repr__(self):  #163 (line num in coconut source)
        return "top"  #163 (line num in coconut source)


    def __str__(self):  #165 (line num in coconut source)
        return top_sym  #165 (line num in coconut source)


    def __bool__(self):  #167 (line num in coconut source)
        return True  #167 (line num in coconut source)


_coconut_call_set_names(Top)  #169 (line num in coconut source)
top = true = Top()  #169 (line num in coconut source)


class Bot(Expr):  #172 (line num in coconut source)
    """False"""  #173 (line num in coconut source)
    __slots__ = ()  #174 (line num in coconut source)

    @_coconut_tco  #176 (line num in coconut source)
    def __eq__(self, other):  #176 (line num in coconut source)
        return _coconut_tail_call(isinstance, other, Bot)  #176 (line num in coconut source)


    def __repr__(self):  #178 (line num in coconut source)
        return "bot"  #178 (line num in coconut source)


    def __str__(self):  #180 (line num in coconut source)
        return bot_sym  #180 (line num in coconut source)


    def __bool__(self):  #182 (line num in coconut source)
        return False  #182 (line num in coconut source)


    def admits_empty_universe(self):  #184 (line num in coconut source)
        return False  #184 (line num in coconut source)


_coconut_call_set_names(Bot)  #186 (line num in coconut source)
bot = false = Bot()  #186 (line num in coconut source)


class Atom(Expr):  #189 (line num in coconut source)
    """Base class for all variables."""  #190 (line num in coconut source)
    __slots__ = ("name",)  #191 (line num in coconut source)

    def __init__(self, name):  #193 (line num in coconut source)
        if isinstance(name, Atom):  #194 (line num in coconut source)
            name = name.name  #195 (line num in coconut source)
        assert isinstance(name, str), name  #196 (line num in coconut source)
        self.name = name  #197 (line num in coconut source)


    def __repr__(self):  #199 (line num in coconut source)
        return self.__class__.__name__ + '("' + self.name + '")'  #200 (line num in coconut source)


    def __str__(self):  #202 (line num in coconut source)
        return self.name  #203 (line num in coconut source)


    def __eq__(self, other):  #205 (line num in coconut source)
        return isinstance(other, self.__class__) and self.name == other.name  #206 (line num in coconut source)


    @_coconut_tco  #208 (line num in coconut source)
    def __hash__(self):  #208 (line num in coconut source)
        return _coconut_tail_call((hash), (self.__class__.__name__, self.name))  #209 (line num in coconut source)


    def substitute_elements(self, subs, **kwargs):  #211 (line num in coconut source)
        """Substitute for the elements of the Atom, not the Atom itself."""  #212 (line num in coconut source)
        return self  #213 (line num in coconut source)


    @_coconut_tco  #215 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #215 (line num in coconut source)
        if not can_sub(kwargs):  #216 (line num in coconut source)
            return self  #217 (line num in coconut source)
        _coconut_match_to_1 = subs  #218 (line num in coconut source)
        _coconut_match_check_1 = False  #218 (line num in coconut source)
        _coconut_match_set_name_sub = _coconut_sentinel  #218 (line num in coconut source)
        if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #218 (line num in coconut source)
            _coconut_match_temp_1 = _coconut_match_to_1.get(self, _coconut_sentinel)  #218 (line num in coconut source)
            if _coconut_match_temp_1 is not _coconut_sentinel:  #218 (line num in coconut source)
                _coconut_match_set_name_sub = _coconut_match_temp_1  #218 (line num in coconut source)
                _coconut_match_check_1 = True  #218 (line num in coconut source)
        if _coconut_match_check_1:  #218 (line num in coconut source)
            if _coconut_match_set_name_sub is not _coconut_sentinel:  #218 (line num in coconut source)
                sub = _coconut_match_set_name_sub  #218 (line num in coconut source)
        if _coconut_match_check_1:  #218 (line num in coconut source)
            do_sub(kwargs)  #219 (line num in coconut source)
            if wff(sub):  #220 (line num in coconut source)
                return sub  #221 (line num in coconut source)
            elif sub is True:  #222 (line num in coconut source)
                return top  #223 (line num in coconut source)
            elif sub is False:  #224 (line num in coconut source)
                return bot  #225 (line num in coconut source)
            else:  #226 (line num in coconut source)
                raise TypeError("cannot perform substitution " + str(self) + " => " + str(sub))  #227 (line num in coconut source)
        else:  #228 (line num in coconut source)
            return _coconut_tail_call(self.substitute_elements, subs, **kwargs)  #229 (line num in coconut source)



_coconut_call_set_names(Atom)  #232 (line num in coconut source)
class Prop(Atom):  #232 (line num in coconut source)
    """Logical proposition that is either true or false."""  #233 (line num in coconut source)
    __slots__ = ()  #234 (line num in coconut source)

    @_coconut_tco  #236 (line num in coconut source)
    def __call__(self, *args):  #236 (line num in coconut source)
        return _coconut_tail_call(Pred, self.name, *args)  #237 (line num in coconut source)


_coconut_call_set_names(Prop)  #239 (line num in coconut source)
Proposition = Prop  #239 (line num in coconut source)


class FuncAtom(Atom):  #242 (line num in coconut source)
    """Base class for predicates and functions."""  #243 (line num in coconut source)
    __slots__ = ("args",)  #244 (line num in coconut source)

    def __init__(self, name, *args):  #246 (line num in coconut source)
        __class__ = FuncAtom  #247 (line num in coconut source)

        super().__init__(name)  #247 (line num in coconut source)
        for arg in args:  #248 (line num in coconut source)
            assert isinstance(arg, Term), arg  #249 (line num in coconut source)
        self.args = args  #250 (line num in coconut source)


    def __repr__(self):  #252 (line num in coconut source)
        return self.__class__.__name__ + '("' + self.name + '"' + (", " if self.args else "") + ", ".join((repr(x) for x in self.args)) + ")"  #253 (line num in coconut source)


    def __str__(self):  #255 (line num in coconut source)
        return self.name + "(" + ", ".join((str(x) for x in self.args)) + ")"  #256 (line num in coconut source)


    def __eq__(self, other):  #258 (line num in coconut source)
        return isinstance(other, self.__class__) and self.name == other.name and self.args == other.args  #259 (line num in coconut source)


    @_coconut_tco  #261 (line num in coconut source)
    def __hash__(self):  #261 (line num in coconut source)
        return _coconut_tail_call((hash), (self.__class__.__name__, self.name, self.args))  #262 (line num in coconut source)


    @_coconut_tco  #264 (line num in coconut source)
    def find_unification(self, other, **kwargs):  #264 (line num in coconut source)
        if isinstance(other, self.__class__) and self.name == other.name and len(self.args) == len(other.args):  #265 (line num in coconut source)
            return _coconut_tail_call(unify_elems, self, other, elems_getter=_coconut.operator.attrgetter("args"), **kwargs)  #266 (line num in coconut source)
        else:  #267 (line num in coconut source)
            __class__ = FuncAtom  #268 (line num in coconut source)

            return super().find_unification(other, **kwargs)  #268 (line num in coconut source)


    @_coconut_tco  #270 (line num in coconut source)
    def admits_empty_universe(self):  #270 (line num in coconut source)
        return _coconut_tail_call(all, (x.admits_empty_universe() for x in self.args))  #271 (line num in coconut source)



_coconut_call_set_names(FuncAtom)  #274 (line num in coconut source)
class Pred(FuncAtom):  #274 (line num in coconut source)
    """Boolean function of terms."""  #275 (line num in coconut source)
    __slots__ = ()  #276 (line num in coconut source)

    @_coconut_tco  #278 (line num in coconut source)
    def proposition(self):  #278 (line num in coconut source)
        return _coconut_tail_call(Prop, self.name)  #279 (line num in coconut source)


    @_coconut_tco  #281 (line num in coconut source)
    def substitute_elements(self, subs, **kwargs):  #281 (line num in coconut source)
        if not can_sub(kwargs):  #282 (line num in coconut source)
            return self  #283 (line num in coconut source)
        _coconut_match_to_2 = subs  #284 (line num in coconut source)
        _coconut_match_check_2 = False  #284 (line num in coconut source)
        _coconut_match_set_name_sub = _coconut_sentinel  #284 (line num in coconut source)
        if _coconut.isinstance(_coconut_match_to_2, _coconut.abc.Mapping):  #284 (line num in coconut source)
            _coconut_match_temp_2 = _coconut_match_to_2.get(self.proposition(), _coconut_sentinel)  #284 (line num in coconut source)
            if _coconut_match_temp_2 is not _coconut_sentinel:  #284 (line num in coconut source)
                _coconut_match_set_name_sub = _coconut_match_temp_2  #284 (line num in coconut source)
                _coconut_match_check_2 = True  #284 (line num in coconut source)
        if _coconut_match_check_2:  #284 (line num in coconut source)
            if _coconut_match_set_name_sub is not _coconut_sentinel:  #284 (line num in coconut source)
                sub = _coconut_match_set_name_sub  #284 (line num in coconut source)
        if _coconut_match_check_2:  #284 (line num in coconut source)
            assert isinstance(sub, Atom), sub  #285 (line num in coconut source)
            do_sub(kwargs)  #286 (line num in coconut source)
            name = sub.name  #287 (line num in coconut source)
        else:  #288 (line num in coconut source)
            name = self.name  #289 (line num in coconut source)
        if can_sub(kwargs):  #290 (line num in coconut source)
            return _coconut_tail_call((Pred), name, *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.args))  #291 (line num in coconut source)
        else:  #292 (line num in coconut source)
            return _coconut_tail_call(Pred, name, *self.args)  #293 (line num in coconut source)


_coconut_call_set_names(Pred)  #295 (line num in coconut source)
Predicate = Pred  #295 (line num in coconut source)


class Term(Atom):  #298 (line num in coconut source)
    """Base class for all terms."""  #299 (line num in coconut source)
    __slots__ = ()  #300 (line num in coconut source)

    @_coconut_tco  #302 (line num in coconut source)
    def variable(self):  #302 (line num in coconut source)
        """Convert to a variable."""  #303 (line num in coconut source)
        return _coconut_tail_call(Var, self.name)  #304 (line num in coconut source)


    @_coconut_tco  #306 (line num in coconut source)
    def constant(self):  #306 (line num in coconut source)
        """Convert to a constant."""  #307 (line num in coconut source)
        return _coconut_tail_call(Const, self.name)  #308 (line num in coconut source)


    @_coconut_tco  #310 (line num in coconut source)
    def rename(self, name):  #310 (line num in coconut source)
        """Create a new term with a different name."""  #311 (line num in coconut source)
        return _coconut_tail_call(self.__class__, name)  #312 (line num in coconut source)


    @_coconut_tco  #314 (line num in coconut source)
    def prime(self):  #314 (line num in coconut source)
        """Rename by adding a prime."""  #315 (line num in coconut source)
        return _coconut_tail_call(self.rename, self.name + "'")  #316 (line num in coconut source)


    @_coconut_tco  #318 (line num in coconut source)
    def subscript(self, i):  #318 (line num in coconut source)
        """Rename by adding a subscript."""  #319 (line num in coconut source)
        return _coconut_tail_call(self.rename, self.name + "_" + str(i))  #320 (line num in coconut source)


    @_coconut_tco  #322 (line num in coconut source)
    def skolem(self):  #322 (line num in coconut source)
        """Rename to a Skolem variable."""  #323 (line num in coconut source)
        return _coconut_tail_call(Const, "_" + self.name)  #324 (line num in coconut source)


    def is_free_in(self, expr):  #326 (line num in coconut source)
        """Determine if self is free in expr."""  #327 (line num in coconut source)
        return expr == expr.substitute({self: self.prime()})  #328 (line num in coconut source)


    @_coconut_tco  #330 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #330 (line num in coconut source)
        if can_sub(kwargs):  #331 (line num in coconut source)
            for var, sub in subs.items():  #332 (line num in coconut source)
                if can_sub(kwargs) and isinstance(var, Term) and self.name == var.name:  #333 (line num in coconut source)
                    do_sub(kwargs)  #334 (line num in coconut source)
                    if isvar(self) or self == var:  #335 (line num in coconut source)
                        return sub  #336 (line num in coconut source)
                    else:  #337 (line num in coconut source)
                        return self.rename(sub.name)  #338 (line num in coconut source)
        if can_sub(kwargs):  #339 (line num in coconut source)
            return _coconut_tail_call(self.substitute_elements, subs, **kwargs)  #340 (line num in coconut source)
        return self  #341 (line num in coconut source)



_coconut_call_set_names(Term)  #344 (line num in coconut source)
class Var(Term):  #344 (line num in coconut source)
    """A variable quantified by a ForAll."""  #345 (line num in coconut source)
    __slots__ = ()  #346 (line num in coconut source)

    def __str__(self):  #348 (line num in coconut source)
        __class__ = Var  #349 (line num in coconut source)

        return "?" + super().__str__()  #349 (line num in coconut source)


    def variable(self):  #351 (line num in coconut source)
        return self  #351 (line num in coconut source)


    @_coconut_tco  #353 (line num in coconut source)
    def __call__(self, *args):  #353 (line num in coconut source)
        return _coconut_tail_call(Func, self.name, *args)  #354 (line num in coconut source)


    def find_unification(self, other, occurs_check=True, **kwargs):  #356 (line num in coconut source)
        kwargs["occurs_check"] = occurs_check  #357 (line num in coconut source)
        if isinstance(other, Var):  #358 (line num in coconut source)
            if self.name == other.name:  #359 (line num in coconut source)
                return {}  #360 (line num in coconut source)
            else:  #361 (line num in coconut source)
                return {self: other}  #362 (line num in coconut source)
        elif isinstance(other, Term):  #363 (line num in coconut source)
            if occurs_check and not self.is_free_in(other):  #364 (line num in coconut source)
                return None  #365 (line num in coconut source)
            else:  #366 (line num in coconut source)
                return {self: other}  #367 (line num in coconut source)
        else:  #368 (line num in coconut source)
            return None  #369 (line num in coconut source)


_coconut_call_set_names(Var)  #371 (line num in coconut source)
Variable = Var  #371 (line num in coconut source)


class Const(Term):  #374 (line num in coconut source)
    """A variable quantified by an Exists."""  #375 (line num in coconut source)
    __slots__ = ()  #376 (line num in coconut source)

    def constant(self):  #378 (line num in coconut source)
        return self  #378 (line num in coconut source)


    @_coconut_tco  #380 (line num in coconut source)
    def __call__(self, *args):  #380 (line num in coconut source)
        return _coconut_tail_call(Func, self.name, *args)  #381 (line num in coconut source)


    def admits_empty_universe(self):  #383 (line num in coconut source)
        return False  #383 (line num in coconut source)


_coconut_call_set_names(Const)  #385 (line num in coconut source)
Constant = Const  #385 (line num in coconut source)


class Func(Term, FuncAtom):  #388 (line num in coconut source)
    """A function on terms."""  #389 (line num in coconut source)
    __slots__ = ()  #390 (line num in coconut source)

    @_coconut_tco  #392 (line num in coconut source)
    def substitute_elements(self, subs, **kwargs):  #392 (line num in coconut source)
        return _coconut_tail_call((Func), self.name, *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.args))  #393 (line num in coconut source)


    @_coconut_tco  #395 (line num in coconut source)
    def rename(self, name):  #395 (line num in coconut source)
        return _coconut_tail_call(self.__class__, name, *self.args)  #396 (line num in coconut source)


_coconut_call_set_names(Func)  #398 (line num in coconut source)
Function = Func  #398 (line num in coconut source)


class UnaryOp(Expr):  #401 (line num in coconut source)
    """Base class for unary operators."""  #402 (line num in coconut source)
    __slots__ = ("elem",)  #403 (line num in coconut source)

    def __init__(self, elem):  #405 (line num in coconut source)
        assert wff(elem), elem  #406 (line num in coconut source)
        self.elem = elem  #407 (line num in coconut source)


    def __repr__(self):  #409 (line num in coconut source)
        return self.__class__.__name__ + "(" + repr(self.elem) + ")"  #410 (line num in coconut source)


    def __eq__(self, other):  #412 (line num in coconut source)
        return isinstance(other, self.__class__) and self.elem == other.elem  #413 (line num in coconut source)


    def __str__(self):  #415 (line num in coconut source)
        return self.opstr + quote(self.elem)  #416 (line num in coconut source)


    def __len__(self):  #418 (line num in coconut source)
        return len(self.elem) + 1  #419 (line num in coconut source)


    @_coconut_tco  #421 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #421 (line num in coconut source)
        return _coconut_tail_call(self.__class__, self.elem.substitute(subs, **kwargs))  #422 (line num in coconut source)


    @_coconut_tco  #424 (line num in coconut source)
    def find_unification(self, other, **kwargs):  #424 (line num in coconut source)
        if isinstance(other, self.__class__):  #425 (line num in coconut source)
            return _coconut_tail_call(self.elem.find_unification, other.elem, **kwargs)  #426 (line num in coconut source)
        else:  #427 (line num in coconut source)
            __class__ = UnaryOp  #428 (line num in coconut source)

            return super().find_unification(other, **kwargs)  #428 (line num in coconut source)


    @_coconut_tco  #430 (line num in coconut source)
    def resolve(self, **kwargs):  #430 (line num in coconut source)
        return _coconut_tail_call(self.__class__(self.elem.resolve(**kwargs)).simplify, dnf=False, **kwargs)  #431 (line num in coconut source)



_coconut_call_set_names(UnaryOp)  #434 (line num in coconut source)
class Not(UnaryOp):  #434 (line num in coconut source)
    """Logical not."""  #435 (line num in coconut source)
    __slots__ = ()  #436 (line num in coconut source)
    opstr = not_sym  #437 (line num in coconut source)

    @property  #439 (line num in coconut source)
    def neg(self):  #440 (line num in coconut source)
        return self.elem  #440 (line num in coconut source)


    @_coconut_tco  #442 (line num in coconut source)
    def simplify(self, **kwargs):  #442 (line num in coconut source)
        if self.neg == top:  #443 (line num in coconut source)
            return bot  #444 (line num in coconut source)
        elif self.neg == bot:  #445 (line num in coconut source)
            return top  #446 (line num in coconut source)
        elif isinstance(self.neg, Not):  #447 (line num in coconut source)
            return _coconut_tail_call(self.neg.neg.simplify, **kwargs)  #448 (line num in coconut source)
        elif isinstance(self.neg, And):  #449 (line num in coconut source)
            return _coconut_tail_call(Or(*map(Not, self.neg.ands)).simplify, **kwargs)  #450 (line num in coconut source)
        elif isinstance(self.neg, Or):  #451 (line num in coconut source)
            return _coconut_tail_call(And(*map(Not, self.neg.ors)).simplify, **kwargs)  #452 (line num in coconut source)
        elif isinstance(self.neg, Imp):  #453 (line num in coconut source)
            ands = self.neg.conds + (Not(self.neg.concl),)  #454 (line num in coconut source)
            return _coconut_tail_call(And(*ands).simplify, **kwargs)  #455 (line num in coconut source)
        elif isinstance(self.neg, Exists):  #456 (line num in coconut source)
            return _coconut_tail_call(ForAll, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  #457 (line num in coconut source)
        elif isinstance(self.neg, ForAll):  #458 (line num in coconut source)
            return _coconut_tail_call(Exists, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  #459 (line num in coconut source)
        else:  #460 (line num in coconut source)
            return _coconut_tail_call(Not, self.neg.simplify(**kwargs))  #461 (line num in coconut source)


    def contradicts(self, other, **kwargs):  #463 (line num in coconut source)
        return self.neg == other  #464 (line num in coconut source)


    @_coconut_tco  #466 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #466 (line num in coconut source)
        if isinstance(other, (Or, Eq)):  #467 (line num in coconut source)
            return _coconut_tail_call(other.resolve_against, self, **kwargs)  #468 (line num in coconut source)
        elif self.neg.find_unification(other, **kwargs) is not None:  #469 (line num in coconut source)
            return bot  #470 (line num in coconut source)
        else:  #471 (line num in coconut source)
            return None  #472 (line num in coconut source)


    @_coconut_tco  #474 (line num in coconut source)
    def admits_empty_universe(self):  #474 (line num in coconut source)
        if isinstance(self.neg, Atom):  #475 (line num in coconut source)
            return _coconut_tail_call(self.neg.admits_empty_universe)  #476 (line num in coconut source)
        else:  #477 (line num in coconut source)
            return not self.neg.admits_empty_universe()  #478 (line num in coconut source)



_coconut_call_set_names(Not)  #481 (line num in coconut source)
class Quantifier(Expr):  #481 (line num in coconut source)
    """Base class for logical quantifiers."""  #482 (line num in coconut source)
    __slots__ = ("var", "elem")  #483 (line num in coconut source)

    def __repr__(self):  #485 (line num in coconut source)
        return self.__class__.__name__ + '("' + str(self.var) + '", ' + repr(self.elem) + ")"  #486 (line num in coconut source)


    def __str__(self):  #488 (line num in coconut source)
        return self.opstr + " " + str(self.var) + ", " + quote(self.elem, in_quantifier=True)  #489 (line num in coconut source)


    def __len__(self):  #491 (line num in coconut source)
        return len(self.elem) + len(self.var)  #492 (line num in coconut source)


    @_coconut_tco  #494 (line num in coconut source)
    def change_var(self, var):  #494 (line num in coconut source)
        """Create an equivalent expression with a new quantified variable."""  #495 (line num in coconut source)
        return _coconut_tail_call(self.__class__, var, self.elem.substitute({self.var: var}))  #496 (line num in coconut source)


    @_coconut_tco  #498 (line num in coconut source)
    def change_elem(self, elem):  #498 (line num in coconut source)
        """Create an equivalent quantifier with a new expression."""  #499 (line num in coconut source)
        return _coconut_tail_call(self.__class__, self.var, elem)  #500 (line num in coconut source)


    def __eq__(self, other):  #502 (line num in coconut source)
        if isinstance(other, self.__class__):  #503 (line num in coconut source)
            return self.elem == other.change_var(self.var).elem  #504 (line num in coconut source)
        else:  #505 (line num in coconut source)
            return False  #506 (line num in coconut source)


    def inner_kwargs(self, kwargs):  #508 (line num in coconut source)
        inner_kwargs = kwargs.copy()  #509 (line num in coconut source)
        inner_kwargs["in_" + self.__class__.__name__.lower()] = True  #510 (line num in coconut source)
        return inner_kwargs  #511 (line num in coconut source)


    @_coconut_tco  #513 (line num in coconut source)
    def resolve(self, **kwargs):  #513 (line num in coconut source)
        return _coconut_tail_call(self.__class__(self.var, self.elem.resolve(**self.inner_kwargs(kwargs))).simplify, dnf=False, **kwargs)  #514 (line num in coconut source)


    @_coconut_tco  #516 (line num in coconut source)
    def simplify(self, **kwargs):  #516 (line num in coconut source)
        return _coconut_tail_call(self.__class__(self.var, self.elem.simplify(**self.inner_kwargs(kwargs))).drop_quantifier, **kwargs)  #517 (line num in coconut source)


    @_coconut_tco  #519 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #519 (line num in coconut source)
        return _coconut_tail_call((self.change_elem), (self.elem.substitute)((rem_var)(self.var, subs), **kwargs))  #520 (line num in coconut source)


    @_coconut_tco  #522 (line num in coconut source)
    def make_free_in(self, other):  #522 (line num in coconut source)
        """Makes self free in other."""  #523 (line num in coconut source)
        var = self.var  #524 (line num in coconut source)
        while not var.is_free_in(other):  #525 (line num in coconut source)
            var = var.prime()  #526 (line num in coconut source)
        return _coconut_tail_call(self.change_var, var)  #527 (line num in coconut source)


    @_coconut_tco  #529 (line num in coconut source)
    def find_unification(self, other, **kwargs):  #529 (line num in coconut source)
        unif = self.elem.find_unification(other, **kwargs)  #530 (line num in coconut source)
        if unif is None:  #531 (line num in coconut source)
            return None  #532 (line num in coconut source)
        else:  #533 (line num in coconut source)
            return _coconut_tail_call((rem_var), self.var, unif)  #534 (line num in coconut source)


    @_coconut_tco  #536 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #536 (line num in coconut source)
        if isinstance(other, Quantifier):  #537 (line num in coconut source)
            resolution = (self.elem.resolve_against)(Not(other.elem).simplify(**kwargs), **kwargs)  #538 (line num in coconut source)
            if resolution is None:  #539 (line num in coconut source)
                return None  #540 (line num in coconut source)
            elif isinstance(other, ForAll):  # don't pull an Exists out of a ForAll  #541 (line num in coconut source)
                return _coconut_tail_call((other.change_elem), (self.change_elem)(resolution))  #542 (line num in coconut source)
            else:  #543 (line num in coconut source)
                return _coconut_tail_call((self.change_elem), (other.change_elem)(resolution))  #544 (line num in coconut source)
        else:  #545 (line num in coconut source)
            __class__ = Quantifier  #546 (line num in coconut source)

            return super().resolve_against(other, **kwargs)  #546 (line num in coconut source)

    @classmethod  #547 (line num in coconut source)

    @_coconut_tco  #549 (line num in coconut source)
    def blank(cls, elem):  #549 (line num in coconut source)
        """Make a quantifier without a variable."""  #550 (line num in coconut source)
        return _coconut_tail_call(cls(empty_var, elem).make_free_in, elem)  #551 (line num in coconut source)



_coconut_call_set_names(Quantifier)  #554 (line num in coconut source)
class ForAll(Quantifier):  #554 (line num in coconut source)
    """Universal quantifier."""  #555 (line num in coconut source)
    __slots__ = ()  #556 (line num in coconut source)
    opstr = forall_sym  #557 (line num in coconut source)

    def __init__(self, var, elem):  #559 (line num in coconut source)
        assert wff(elem), elem  #560 (line num in coconut source)
        if isinstance(var, str):  #561 (line num in coconut source)
            var = Const(var)  #562 (line num in coconut source)
        assert isvar(var), var  #563 (line num in coconut source)
        self.var = var.variable()  #564 (line num in coconut source)
        self.elem = elem.substitute({var: self.var.variable()})  #565 (line num in coconut source)


    def inner_kwargs(self, kwargs):  #567 (line num in coconut source)
        __class__ = ForAll  #568 (line num in coconut source)

        inner_kwargs = super().inner_kwargs(kwargs)  #568 (line num in coconut source)
        inner_kwargs["variables"] = inner_kwargs.get("variables", ()) + (self.var,)  #569 (line num in coconut source)
        return inner_kwargs  #570 (line num in coconut source)


    def drop_quantifier(self, nonempty_universe=True, in_forall=False, **kwargs):  #572 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["in_forall"] = nonempty_universe, in_forall  #573 (line num in coconut source)
        if not nonempty_universe and not in_forall:  #574 (line num in coconut source)
            elem = self.elem  #575 (line num in coconut source)
            while isinstance(elem, Exists):  #576 (line num in coconut source)
                elem = elem.elem  #577 (line num in coconut source)
            if top == elem:  #578 (line num in coconut source)
                return elem  #579 (line num in coconut source)
        elif self.var.is_free_in(self.elem):  #580 (line num in coconut source)
            return self.elem  #581 (line num in coconut source)
        return self  #582 (line num in coconut source)


_coconut_call_set_names(ForAll)  #584 (line num in coconut source)
FA = ForAll  #584 (line num in coconut source)


class Exists(Quantifier):  #587 (line num in coconut source)
    """Existential quantifier."""  #588 (line num in coconut source)
    __slots__ = ()  #589 (line num in coconut source)
    opstr = exists_sym  #590 (line num in coconut source)

    def __init__(self, var, elem):  #592 (line num in coconut source)
        assert wff(elem), elem  #593 (line num in coconut source)
        if isinstance(var, str):  #594 (line num in coconut source)
            var = Const(var)  #595 (line num in coconut source)
        assert isvar(var), var  #596 (line num in coconut source)
        self.var = var.constant()  #597 (line num in coconut source)
        self.elem = elem.substitute({var: self.var.constant()})  #598 (line num in coconut source)


    @_coconut_tco  #600 (line num in coconut source)
    def resolve(self, **kwargs):  #600 (line num in coconut source)
        skolem_args = kwargs.get("variables")  #601 (line num in coconut source)
        if skolem_args is None:  #602 (line num in coconut source)
            skolem_var = self.var.skolem()  #603 (line num in coconut source)
            while not skolem_var.is_free_in(self.elem):  #604 (line num in coconut source)
                skolem_var = skolem_var.prime()  #605 (line num in coconut source)
        else:  #606 (line num in coconut source)
            skolem_var = Func(self.var.skolem(), *skolem_args)  #607 (line num in coconut source)
        skolem_elem = self.elem.substitute({self.var: skolem_var})  #608 (line num in coconut source)
        return _coconut_tail_call(Exists(self.var, skolem_elem.resolve(**self.inner_kwargs(kwargs))).simplify, dnf=False, **kwargs)  #609 (line num in coconut source)


    def inner_kwargs(self, kwargs):  #611 (line num in coconut source)
        __class__ = Exists  #612 (line num in coconut source)

        inner_kwargs = super().inner_kwargs(kwargs)  #612 (line num in coconut source)
        inner_kwargs["nonempty_universe"] = True  #613 (line num in coconut source)
        return inner_kwargs  #614 (line num in coconut source)


    def drop_quantifier(self, nonempty_universe=True, in_exists=False, **kwargs):  #616 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["in_exists"] = nonempty_universe, in_exists  #617 (line num in coconut source)
        if not nonempty_universe and not in_exists:  #618 (line num in coconut source)
            elem = self.elem  #619 (line num in coconut source)
            while isinstance(elem, ForAll):  #620 (line num in coconut source)
                elem = elem.elem  #621 (line num in coconut source)
            if bot == elem:  #622 (line num in coconut source)
                return elem  #623 (line num in coconut source)
        elif self.var.is_free_in(self.elem):  #624 (line num in coconut source)
            return self.elem  #625 (line num in coconut source)
        return self  #626 (line num in coconut source)


    def admits_empty_universe(self):  #628 (line num in coconut source)
        return False  #628 (line num in coconut source)


_coconut_call_set_names(Exists)  #630 (line num in coconut source)
TE = Exists  #630 (line num in coconut source)


class BinaryOp(Expr):  #633 (line num in coconut source)
    """Base class for binary operators."""  #634 (line num in coconut source)
    __slots__ = ("elems",)  #635 (line num in coconut source)
    identity = None  #636 (line num in coconut source)

    def __new__(cls, *elems):  #638 (line num in coconut source)
        if not elems:  #639 (line num in coconut source)
            if cls.identity is None:  #640 (line num in coconut source)
                raise TypeError(cls.__name__ + " requires at least one argument")  #641 (line num in coconut source)
            else:  #642 (line num in coconut source)
                return cls.identity  #643 (line num in coconut source)
        elif len(elems) == 1:  #644 (line num in coconut source)
            assert wff(elems[0]), elems[0]  #645 (line num in coconut source)
            return elems[0]  # sometimes returns an instance of cls  #646 (line num in coconut source)
        else:  #647 (line num in coconut source)
            __class__ = BinaryOp  #648 (line num in coconut source)

            return super().__new__(cls)  #648 (line num in coconut source)


    def __init__(self, *elems):  #650 (line num in coconut source)
        if len(elems) > 1:  # __new__ should handle all other cases  #651 (line num in coconut source)
            assert len(elems) >= 2, elems  #652 (line num in coconut source)
            for x in elems:  #653 (line num in coconut source)
                assert wff(x), x  #654 (line num in coconut source)
            self.elems = elems  #655 (line num in coconut source)


    def __repr__(self):  #657 (line num in coconut source)
        return self.__class__.__name__ + "(" + ", ".join((repr(x) for x in self.elems)) + ")"  #658 (line num in coconut source)


    @_coconut_tco  #660 (line num in coconut source)
    def __str__(self):  #660 (line num in coconut source)
        return _coconut_tail_call((" " + self.opstr + " ").join, (quote(x) for x in self.elems))  #661 (line num in coconut source)


    def __len__(self):  #663 (line num in coconut source)
        return sum(map(len, self.elems)) + 1  #664 (line num in coconut source)


    @_coconut_tco  #666 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #666 (line num in coconut source)
        return _coconut_tail_call((self.__class__), *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.elems))  #667 (line num in coconut source)


    @_coconut_tco  #669 (line num in coconut source)
    def resolve(self, **kwargs):  #669 (line num in coconut source)
        elems = (map)(_coconut.operator.methodcaller("resolve", **kwargs), self.elems)  #670 (line num in coconut source)
        return _coconut_tail_call(self.__class__(*elems).simplify, dnf=False, **kwargs)  #671 (line num in coconut source)


    @_coconut_tco  #673 (line num in coconut source)
    def find_unification(self, other, **kwargs):  #673 (line num in coconut source)
        if isinstance(other, self.__class__) and len(self.elems) == len(other.elems):  #674 (line num in coconut source)
            return _coconut_tail_call(unify_elems, self, other, elems_getter=_coconut.operator.attrgetter("elems"), **kwargs)  #675 (line num in coconut source)
        else:  #676 (line num in coconut source)
            __class__ = BinaryOp  #677 (line num in coconut source)

            return super().find_unification(other, **kwargs)  #677 (line num in coconut source)



_coconut_call_set_names(BinaryOp)  #680 (line num in coconut source)
class Imp(BinaryOp):  #680 (line num in coconut source)
    """Logical implication."""  #681 (line num in coconut source)
    __slots__ = ()  #682 (line num in coconut source)
    opstr = imp_sym  #683 (line num in coconut source)

    @_coconut_tco  #685 (line num in coconut source)
    def __rshift__(self, other):  #685 (line num in coconut source)
        if isinstance(other, Imp):  #686 (line num in coconut source)
            return _coconut_tail_call(Imp, self, *other.elems)  #687 (line num in coconut source)
        else:  #688 (line num in coconut source)
            return _coconut_tail_call(Imp, self, other)  #689 (line num in coconut source)


    @_coconut_tco  #691 (line num in coconut source)
    def __lshift__(self, other):  #691 (line num in coconut source)
        return _coconut_tail_call((Imp), *(other,) + self.elems)  #692 (line num in coconut source)


    @property  #694 (line num in coconut source)
    def conds(self):  #695 (line num in coconut source)
        return self.elems[:-1]  #695 (line num in coconut source)


    @property  #697 (line num in coconut source)
    def concl(self):  #698 (line num in coconut source)
        return self.elems[-1]  #698 (line num in coconut source)


    def __eq__(self, other):  #700 (line num in coconut source)
        return isinstance(other, self.__class__) and self.concl == other.concl and (unorderd_eq)(self.conds, other.conds)  #701 (line num in coconut source)


    @_coconut_tco  #703 (line num in coconut source)
    def to_or(self):  #703 (line num in coconut source)
        ors = tuple(map(Not, self.conds)) + (self.concl,)  #704 (line num in coconut source)
        return _coconut_tail_call(Or, *ors)  #705 (line num in coconut source)


    @_coconut_tco  #707 (line num in coconut source)
    def simplify(self, **kwargs):  #707 (line num in coconut source)
        return _coconut_tail_call(self.to_or().simplify, **kwargs)  #708 (line num in coconut source)


    @_coconut_tco  #710 (line num in coconut source)
    def admits_empty_universe(self):  #710 (line num in coconut source)
        return _coconut_tail_call(self.to_or().admits_empty_universe)  #711 (line num in coconut source)


_coconut_call_set_names(Imp)  #713 (line num in coconut source)
Implies = Imp  #713 (line num in coconut source)


class BoolOp(BinaryOp):  #716 (line num in coconut source)
    """Base class for Or and And."""  #717 (line num in coconut source)
    __slots__ = ()  #718 (line num in coconut source)

    def __eq__(self, other):  #720 (line num in coconut source)
        return isinstance(other, self.__class__) and (unorderd_eq)(self.elems, other.elems)  #721 (line num in coconut source)


    def simplify(self, **kwargs):  #723 (line num in coconut source)
        elems = (map)(_coconut.operator.methodcaller("simplify", **kwargs), self.merge().elems)  #724 (line num in coconut source)
        out = self.__class__(*elems).clean()  #725 (line num in coconut source)
        if isinstance(out, self.__class__):  #726 (line num in coconut source)
            out = out.distribute(**kwargs)  #727 (line num in coconut source)
        if isinstance(out, self.__class__):  #728 (line num in coconut source)
            out = out.merge().dedupe()  #729 (line num in coconut source)
        if isinstance(out, self.__class__):  #730 (line num in coconut source)
            out = out.inner_simplify(**kwargs)  #731 (line num in coconut source)
        if isinstance(out, self.__class__):  #732 (line num in coconut source)
            out = out.prenex(**kwargs)  #733 (line num in coconut source)
        log_simplification(self, out, **kwargs)  #734 (line num in coconut source)
        return out  #735 (line num in coconut source)


    @_coconut_tco  #737 (line num in coconut source)
    def merge(self):  #737 (line num in coconut source)
        """Merges nested copies of a boolean operator."""  #738 (line num in coconut source)
        elems = []  #739 (line num in coconut source)
        for x in self.elems:  #740 (line num in coconut source)
            if isinstance(x, self.__class__):  #741 (line num in coconut source)
                elems.extend(x.merge().elems)  #742 (line num in coconut source)
            else:  #743 (line num in coconut source)
                elems.append(x)  #744 (line num in coconut source)
        return _coconut_tail_call(self.__class__, *elems)  #745 (line num in coconut source)


    @_coconut_tco  #747 (line num in coconut source)
    def dedupe(self):  #747 (line num in coconut source)
        """Removes duplicate elements from a boolean operator."""  #748 (line num in coconut source)
        elems = []  #749 (line num in coconut source)
        for x in self.elems:  #750 (line num in coconut source)
            if x not in elems:  #751 (line num in coconut source)
                elems.append(x)  #752 (line num in coconut source)
        return _coconut_tail_call(self.__class__, *elems)  #753 (line num in coconut source)


    @_coconut_tco  #755 (line num in coconut source)
    def clean(self):  #755 (line num in coconut source)
        """Removes copies of the identity."""  #756 (line num in coconut source)
        return _coconut_tail_call((self.__class__), *(filter)(_coconut.functools.partial((_coconut.operator.ne), self.identity), self.elems))  #757 (line num in coconut source)


    def prenex(self, **kwargs):  #759 (line num in coconut source)
        """Pulls quantifiers out."""  #760 (line num in coconut source)
        for i, x in enumerate(self.elems):  #761 (line num in coconut source)
            if isinstance(x, Quantifier) and self.can_prenex(x, **kwargs):  #762 (line num in coconut source)
                elems = self.elems[:i] + self.elems[i + 1:]  #763 (line num in coconut source)
                free_x = x.make_free_in(self.__class__(*elems))  #764 (line num in coconut source)
                elems += (free_x.elem,)  #765 (line num in coconut source)
                return free_x.change_elem(self.__class__(*elems)).simplify(**kwargs)  #766 (line num in coconut source)
        return self  #767 (line num in coconut source)



_coconut_call_set_names(BoolOp)  #770 (line num in coconut source)
class Or(BoolOp):  #770 (line num in coconut source)
    """Logical disjunction."""  #771 (line num in coconut source)
    __slots__ = ()  #772 (line num in coconut source)
    opstr = or_sym  #773 (line num in coconut source)
    identity = bot  #774 (line num in coconut source)

    @_coconut_tco  #776 (line num in coconut source)
    def __or__(self, other):  #776 (line num in coconut source)
        return _coconut_tail_call((Or), *self.elems + (other,))  #777 (line num in coconut source)


    @property  #779 (line num in coconut source)
    def ors(self):  #780 (line num in coconut source)
        return self.elems  #780 (line num in coconut source)


    def distribute(self, dnf=False, **kwargs):  #782 (line num in coconut source)
        """If this Or contains an And, distribute into it."""  #783 (line num in coconut source)
        kwargs["dnf"] = dnf  #784 (line num in coconut source)
        if not dnf:  #785 (line num in coconut source)
            for i, x in enumerate(self.ors):  #786 (line num in coconut source)
                if isinstance(x, And):  #787 (line num in coconut source)
                    ands = ((Or)(*(y,) + self.ors[:i] + self.ors[i + 1:]) for y in x.ands)  #788 (line num in coconut source)
                    return And(*ands).simplify(**kwargs)  #789 (line num in coconut source)
        return self  #790 (line num in coconut source)


    def inner_simplify(self, nonempty_universe=True, **kwargs):  #792 (line num in coconut source)
        """Determines if the Or is a blatant tautology."""  #793 (line num in coconut source)
        kwargs["nonempty_universe"] = nonempty_universe  #794 (line num in coconut source)
        for i, x in enumerate(self.ors):  #795 (line num in coconut source)
            if top == x:  #796 (line num in coconut source)
                return x  #797 (line num in coconut source)
            for y in self.ors[i + 1:]:  #798 (line num in coconut source)
                if x.contradicts(y, **kwargs):  #799 (line num in coconut source)
                    if not nonempty_universe and not self.admits_empty_universe():  #800 (line num in coconut source)
                        return Exists.blank(top)  #801 (line num in coconut source)
                    else:  #802 (line num in coconut source)
                        return top  #803 (line num in coconut source)
        return self  #804 (line num in coconut source)


    def can_prenex(self, other, nonempty_universe=True, in_forall=False, prenex_foralls=False, prenex_exists=True, **_):  #806 (line num in coconut source)
        if not prenex_foralls and isinstance(other, ForAll):  #807 (line num in coconut source)
            return False  #808 (line num in coconut source)
        if not prenex_exists and isinstance(other, Exists):  #809 (line num in coconut source)
            return False  #810 (line num in coconut source)
        return (nonempty_universe or in_forall or not isinstance(other, Exists) or not self.admits_empty_universe())  #811 (line num in coconut source)


    @_coconut_tco  #816 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #816 (line num in coconut source)
        if isinstance(other, Eq):  #817 (line num in coconut source)
            return _coconut_tail_call(other.resolve_against, self)  #818 (line num in coconut source)
        elif isinstance(other, Or):  #819 (line num in coconut source)
            not_other_ors = (map)(_coconut.operator.methodcaller("simplify", **kwargs), (map)(Not, other.ors))  #820 (line num in coconut source)
            for i, x in enumerate(self.ors):  #821 (line num in coconut source)
                if isinstance(x, Eq):  #822 (line num in coconut source)
                    resolved_other = (x.paramodulant)(other)  #823 (line num in coconut source)
                    return (Or)(*self.ors[:i] + self.ors[i + 1:] + resolved_other.ors)  #824 (line num in coconut source)
                for j, y in enumerate(not_other_ors):  #825 (line num in coconut source)
                    if isinstance(other.ors[j], Eq):  #826 (line num in coconut source)
                        y = other.ors[j]  #827 (line num in coconut source)
                        resolved_self = (y.paramodulant)(self)  #828 (line num in coconut source)
                        return (Or)(*other.ors[:j] + other.ors[j + 1:] + resolved_self.ors)  #829 (line num in coconut source)
                    subs = x.find_unification(y, **kwargs)  #830 (line num in coconut source)
                    if subs is not None:  #831 (line num in coconut source)
                        return (Or)(*(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.ors[:i] + self.ors[i + 1:] + other.ors[:j] + other.ors[j + 1:]))  #832 (line num in coconut source)
        else:  #833 (line num in coconut source)
            not_other = Not(other).simplify(**kwargs)  #834 (line num in coconut source)
            for i, x in enumerate(self.ors):  #835 (line num in coconut source)
                if isinstance(x, Eq):  #836 (line num in coconut source)
                    return (x.paramodulant)((Or)(*self.ors[:i] + self.ors[i + 1:]))  #837 (line num in coconut source)
                subs = x.find_unification(not_other, **kwargs)  #838 (line num in coconut source)
                if subs is not None:  #839 (line num in coconut source)
                    return (Or)(*(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.ors[:i] + self.ors[i + 1:]))  #840 (line num in coconut source)
        return None  #841 (line num in coconut source)


    @_coconut_tco  #843 (line num in coconut source)
    def admits_empty_universe(self):  #843 (line num in coconut source)
        return _coconut_tail_call(any, (x.admits_empty_universe() for x in self.elems))  #844 (line num in coconut source)



_coconut_call_set_names(Or)  #847 (line num in coconut source)
class And(BoolOp):  #847 (line num in coconut source)
    """Logical conjunction."""  #848 (line num in coconut source)
    __slots__ = ()  #849 (line num in coconut source)
    opstr = and_sym  #850 (line num in coconut source)
    identity = top  #851 (line num in coconut source)

    @_coconut_tco  #853 (line num in coconut source)
    def __and__(self, other):  #853 (line num in coconut source)
        return _coconut_tail_call((And), *self.elems + (other,))  #854 (line num in coconut source)


    @property  #856 (line num in coconut source)
    def ands(self):  #857 (line num in coconut source)
        return self.elems  #857 (line num in coconut source)


    def distribute(self, dnf=False, **kwargs):  #859 (line num in coconut source)
        """If this And contains an Or, distribute into it."""  #860 (line num in coconut source)
        kwargs["dnf"] = dnf  #861 (line num in coconut source)
        if dnf:  #862 (line num in coconut source)
            for i, x in enumerate(self.ands):  #863 (line num in coconut source)
                if isinstance(x, Or):  #864 (line num in coconut source)
                    ors = ((And)(*(y,) + self.ands[:i] + self.ands[i + 1:]) for y in x.ors)  #865 (line num in coconut source)
                    return Or(*ors).simplify(**kwargs)  #866 (line num in coconut source)
        return self  #867 (line num in coconut source)


    def inner_simplify(self, nonempty_universe=True, **kwargs):  #869 (line num in coconut source)
        """Determines if the And is a blatant contradiction."""  #870 (line num in coconut source)
        kwargs["nonempty_universe"] = nonempty_universe  #871 (line num in coconut source)
        for i, x in enumerate(self.ands):  #872 (line num in coconut source)
            if bot == x:  #873 (line num in coconut source)
                return x  #874 (line num in coconut source)
            for y in self.ands[i + 1:]:  #875 (line num in coconut source)
                if x.contradicts(y, **kwargs):  #876 (line num in coconut source)
                    if not nonempty_universe and self.admits_empty_universe():  #877 (line num in coconut source)
                        return ForAll.blank(bot)  #878 (line num in coconut source)
                    else:  #879 (line num in coconut source)
                        return bot  #880 (line num in coconut source)
        return self  #881 (line num in coconut source)


    def can_prenex(self, other, nonempty_universe=True, in_exists=False, prenex_foralls=False, prenex_exists=True, **_):  #883 (line num in coconut source)
        if not prenex_foralls and isinstance(other, ForAll):  #884 (line num in coconut source)
            return False  #885 (line num in coconut source)
        if not prenex_exists and isinstance(other, Exists):  #886 (line num in coconut source)
            return False  #887 (line num in coconut source)
        return (nonempty_universe or in_exists or not isinstance(other, ForAll) or all((isinstance(x, ForAll) for x in self.elems)))  #888 (line num in coconut source)


    @_coconut_tco  #893 (line num in coconut source)
    def resolve(self, nonempty_universe=True, just_skolemize=False, debug=False, **kwargs):  #893 (line num in coconut source)
        """Performs all possible resolutions within the And."""  #894 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["just_skolemize"], kwargs["debug"] = nonempty_universe, just_skolemize, debug  #895 (line num in coconut source)

# skolemize
        __class__ = And  #898 (line num in coconut source)

        resolved = super().resolve(**kwargs)  #898 (line num in coconut source)
        log_simplification(self, resolved, **kwargs)  #899 (line num in coconut source)
        if not isinstance(resolved, And) or just_skolemize:  #900 (line num in coconut source)
            return resolved  #901 (line num in coconut source)
        self = resolved  #902 (line num in coconut source)

# if we don't admit a nonempty universe, enforce that
        quantifiers = []  #905 (line num in coconut source)
        if not nonempty_universe and not self.admits_empty_universe():  #906 (line num in coconut source)
            blank = Exists.blank(top)  #907 (line num in coconut source)
            (quantifiers.append)(blank.change_elem)  #908 (line num in coconut source)
            kwargs = (blank.inner_kwargs)(kwargs)  #909 (line num in coconut source)

# push foralls into clauses
        clauses = []  #912 (line num in coconut source)
        final_subs = {}  #913 (line num in coconut source)
        for i, clause in enumerate(self.ands):  #914 (line num in coconut source)
            clause_subs = dict(((v), (v.subscript(i))) for v in kwargs.get("variables", ()))  #915 (line num in coconut source)
            (clauses.append)(clause.substitute(clause_subs, **kwargs))  #916 (line num in coconut source)
            final_subs.update(dict(((v.subscript(i)), (v)) for v in kwargs.get("variables", ())))  #917 (line num in coconut source)
        kwargs["variables"] = (tuple)(final_subs.keys())  #918 (line num in coconut source)
        log_simplification(self, And(*clauses), **kwargs)  #919 (line num in coconut source)

# main resolution loop
        prev_clause_len = 1  #922 (line num in coconut source)
        while prev_clause_len < len(clauses):  #923 (line num in coconut source)
            prev_clause_len = len(clauses)  #924 (line num in coconut source)
# reversed ensures conclusions get tested first
            for i in (reversed)(range(1, len(clauses))):  #926 (line num in coconut source)
                x = clauses[i]  #927 (line num in coconut source)
                for y in clauses[:i + 1]:  # allow resolution of a clause against itself  #928 (line num in coconut source)
                    resolution = x.resolve_against(y)  #929 (line num in coconut source)
                    if resolution is not None:  #930 (line num in coconut source)
                        resolution = resolution.simplify(dnf=False, **kwargs)  #931 (line num in coconut source)
                        log_resolution(x, y, resolution, **kwargs)  #932 (line num in coconut source)
                        new_quantifiers = []  #933 (line num in coconut source)
                        inner_kwargs = kwargs  #934 (line num in coconut source)
                        while isinstance(resolution, Quantifier) and self.can_prenex(resolution, **kwargs):  #935 (line num in coconut source)
                            (new_quantifiers.append)(resolution.change_elem)  #936 (line num in coconut source)
                            inner_kwargs = (resolution.inner_kwargs)(inner_kwargs)  #937 (line num in coconut source)
                            resolution = resolution.elem  #938 (line num in coconut source)
                        if isinstance(resolution, And):  #939 (line num in coconut source)
                            new_clauses = resolution.ands  #940 (line num in coconut source)
                        else:  #941 (line num in coconut source)
                            new_clauses = (resolution,)  #942 (line num in coconut source)
                        novel = False  #943 (line num in coconut source)
                        for new_clause in new_clauses:  #944 (line num in coconut source)
                            if new_clause == bot:  #945 (line num in coconut source)
                                clauses = [bot,]  #946 (line num in coconut source)
                                novel = True  #947 (line num in coconut source)
                                break  #948 (line num in coconut source)
                            elif new_clause != top and new_clause not in clauses:  #949 (line num in coconut source)
                                clauses.append(new_clause)  #950 (line num in coconut source)
                                novel = True  #951 (line num in coconut source)
                        if novel:  #952 (line num in coconut source)
                            quantifiers.extend(new_quantifiers)  #953 (line num in coconut source)
                            kwargs = inner_kwargs  #954 (line num in coconut source)
                            if clauses == [bot,]:  #955 (line num in coconut source)
                                break  #956 (line num in coconut source)
                if clauses == [bot,]:  #957 (line num in coconut source)
                    break  #958 (line num in coconut source)

# combine resolved clauses
        resolved = ((reduce)(_coconut_pipe, [And(*clauses),] + quantifiers)).substitute(final_subs, **kwargs)  #961 (line num in coconut source)
        log_simplification(self, resolved, **kwargs)  #962 (line num in coconut source)
        self = resolved  #963 (line num in coconut source)

        return _coconut_tail_call(self.simplify, dnf=False, **kwargs)  #965 (line num in coconut source)


    @_coconut_tco  #967 (line num in coconut source)
    def admits_empty_universe(self):  #967 (line num in coconut source)
        return _coconut_tail_call(all, (x.admits_empty_universe() for x in self.elems))  #968 (line num in coconut source)



_coconut_call_set_names(And)  #971 (line num in coconut source)
class Eq(Expr):  #971 (line num in coconut source)
    """Equality operator."""  #972 (line num in coconut source)
    __slots__ = ("a", "b")  #973 (line num in coconut source)

    def __init__(self, a, b):  #975 (line num in coconut source)
        assert isinstance(a, Term), a  #976 (line num in coconut source)
        assert isinstance(b, Term), b  #977 (line num in coconut source)
        self.a, self.b = a, b  #978 (line num in coconut source)


    def __repr__(self):  #980 (line num in coconut source)
        return "Eq(" + repr(self.a) + ", " + repr(self.b) + ")"  #981 (line num in coconut source)


    def __str__(self):  #983 (line num in coconut source)
        return str(self.a) + "=" + str(self.b)  #984 (line num in coconut source)


    def __eq__(self, other):  #986 (line num in coconut source)
        return isinstance(other, Eq) and (self.a == other.a and self.b == other.b or self.a == other.b and self.b == other.a)  #987 (line num in coconut source)


    def simplify(self, **kwargs):  #989 (line num in coconut source)
        if self.a == self.b:  #990 (line num in coconut source)
            return top  #991 (line num in coconut source)
        else:  #992 (line num in coconut source)
            return self  #993 (line num in coconut source)


    @_coconut_tco  #995 (line num in coconut source)
    def swap(self):  #995 (line num in coconut source)
        """Swaps the order of equality."""  #996 (line num in coconut source)
        return _coconut_tail_call(Eq, self.b, self.a)  #997 (line num in coconut source)


    def find_unification(self, other, **kwargs):  #999 (line num in coconut source)
        if isinstance(other, Eq):  #1000 (line num in coconut source)
            a_a = self.a.find_unification(other.a, **kwargs)  #1001 (line num in coconut source)
            b_b = self.b.find_unification(other.b, **kwargs)  #1002 (line num in coconut source)
            if a_a is not None and b_b is not None:  #1003 (line num in coconut source)
                subs = merge_dicts(a_a, b_b)  #1004 (line num in coconut source)
                if subs is not None:  #1005 (line num in coconut source)
                    return subs  #1006 (line num in coconut source)
            a_b = self.a.find_unification(other.a, **kwargs)  #1007 (line num in coconut source)
            b_a = self.b.find_unification(other.b, **kwargs)  #1008 (line num in coconut source)
            if a_b is not None and b_a is not None:  #1009 (line num in coconut source)
                subs = merge_dicts(a_b, b_a)  #1010 (line num in coconut source)
                if subs is not None:  #1011 (line num in coconut source)
                    return subs  #1012 (line num in coconut source)
        else:  #1013 (line num in coconut source)
            __class__ = Eq  #1014 (line num in coconut source)

            return super().find_unification(other, **kwargs)  #1014 (line num in coconut source)


    @_coconut_tco  #1016 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #1016 (line num in coconut source)
        return _coconut_tail_call(Eq, self.a.substitute(subs, **kwargs), self.b.substitute(subs, **kwargs))  #1017 (line num in coconut source)


    @_coconut_tco  #1019 (line num in coconut source)
    def paramodulant(self, other):  #1019 (line num in coconut source)
        """Create a paramodulant of other."""  #1020 (line num in coconut source)
        return _coconut_tail_call((sub_once), other, {self.a: self.b, self.b: self.a})  #1021 (line num in coconut source)


    @_coconut_tco  #1023 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #1023 (line num in coconut source)
        if isinstance(other, Not) and self.find_unification(other.neg, **kwargs) is not None:  #1024 (line num in coconut source)
            return bot  #1025 (line num in coconut source)
        else:  #1026 (line num in coconut source)
            return _coconut_tail_call(self.paramodulant, other)  #1027 (line num in coconut source)


    def admits_empty_universe(self):  #1029 (line num in coconut source)
        return self.a.admits_empty_universe() and self.b.admits_empty_universe()  #1030 (line num in coconut source)


_coconut_call_set_names(Eq)  #1032 (line num in coconut source)
Equals = Eq  #1032 (line num in coconut source)
