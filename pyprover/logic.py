#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf11b759b

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


# Classes:


class Expr(_coconut.object):  #40 (line num in coconut source)
    """Base class for all formulae."""  #41 (line num in coconut source)
    __slots__ = ()  #42 (line num in coconut source)

    @_coconut_tco  #44 (line num in coconut source)
    def __hash__(self):  #44 (line num in coconut source)
#type: (...) -> int
        return _coconut_tail_call((hash), str(self))  #45 (line num in coconut source)


    def __lt__(self, other):  #47 (line num in coconut source)
#type: (...) -> int
        return str(self) < str(other)  #48 (line num in coconut source)


    def __gt__(self, other):  #50 (line num in coconut source)
#type: (...) -> int
        return str(self) > str(other)  #51 (line num in coconut source)


    def __ge__(self, other):  #53 (line num in coconut source)
#type: (...) -> int
        return str(self) >= str(other)  #54 (line num in coconut source)


    def __le__(self, other):  #56 (line num in coconut source)
#type: (...) -> int
        return str(self) <= str(other)  #57 (line num in coconut source)


    @_coconut_tco  #59 (line num in coconut source)
    def __and__(self, other):  #59 (line num in coconut source)
        if isinstance(other, And):  #60 (line num in coconut source)
            return other & self  #61 (line num in coconut source)
        else:  #62 (line num in coconut source)
            return _coconut_tail_call(And, self, other)  #63 (line num in coconut source)


    @_coconut_tco  #65 (line num in coconut source)
    def __or__(self, other):  #65 (line num in coconut source)
        if isinstance(other, Or):  #66 (line num in coconut source)
            return other | self  #67 (line num in coconut source)
        else:  #68 (line num in coconut source)
            return _coconut_tail_call(Or, self, other)  #69 (line num in coconut source)


    @_coconut_tco  #71 (line num in coconut source)
    def __rshift__(self, other):  #71 (line num in coconut source)
        if isinstance(other, Imp):  #72 (line num in coconut source)
            return other << self  #73 (line num in coconut source)
        else:  #74 (line num in coconut source)
            return _coconut_tail_call(Imp, self, other)  #75 (line num in coconut source)


    def __lshift__(self, other):  #77 (line num in coconut source)
        assert wff(other), other  #78 (line num in coconut source)
        return other >> self  #79 (line num in coconut source)


    @_coconut_tco  #81 (line num in coconut source)
    def __invert__(self):  #81 (line num in coconut source)
        return _coconut_tail_call(Not, self)  #82 (line num in coconut source)


    @_coconut_tco  #84 (line num in coconut source)
    def __xor__(self, other):  #84 (line num in coconut source)
        return _coconut_tail_call(Or, And(self, Not(other)), And(Not(self), other))  #85 (line num in coconut source)


    def __len__(self):  #87 (line num in coconut source)
        return 1  #87 (line num in coconut source)


    def simplify(self, **kwargs):  #89 (line num in coconut source)
        """Simplify the given expression."""  #90 (line num in coconut source)
        return self  #91 (line num in coconut source)


    def substitute(self, subs, **kwargs):  #93 (line num in coconut source)
        """Substitutes a dictionary into the expression."""  #94 (line num in coconut source)
        return self  #95 (line num in coconut source)


    @_coconut_tco  #97 (line num in coconut source)
    def resolve(self, **kwargs):  #97 (line num in coconut source)
        """Performs resolution on the clauses in a CNF expression."""  #98 (line num in coconut source)
        return _coconut_tail_call(self.simplify, dnf=False, **kwargs)  #99 (line num in coconut source)


    @_coconut_tco  #101 (line num in coconut source)
    def find_unification(self, other):  #101 (line num in coconut source)
        """Find a substitution in self that would make self into other."""  #102 (line num in coconut source)
        if isinstance(other, Quantifier):  #103 (line num in coconut source)
            return _coconut_tail_call(other.find_unification, self)  #104 (line num in coconut source)
        elif self == other:  #105 (line num in coconut source)
            return {}  #106 (line num in coconut source)
        else:  #107 (line num in coconut source)
            return None  #108 (line num in coconut source)


    @_coconut_tco  #110 (line num in coconut source)
    def contradicts(self, other, **kwargs):  #110 (line num in coconut source)
        """Assuming self is simplified, determines if it contradicts other."""  #111 (line num in coconut source)
        if isinstance(other, Not):  #112 (line num in coconut source)
            return _coconut_tail_call(other.contradicts, self, **kwargs)  #113 (line num in coconut source)
        else:  #114 (line num in coconut source)
            return self == Not(other).simplify(**kwargs)  #115 (line num in coconut source)


    @_coconut_tco  #117 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #117 (line num in coconut source)
        """Attempt to perform a resolution against other else None."""  #118 (line num in coconut source)
        if isinstance(other, (Not, Or, Eq)):  #119 (line num in coconut source)
            return _coconut_tail_call(other.resolve_against, self, **kwargs)  #120 (line num in coconut source)
        elif (self.find_unification)(Not(other).simplify(**kwargs)) is not None:  #121 (line num in coconut source)
            return bot  #122 (line num in coconut source)
        else:  #123 (line num in coconut source)
            return None  #124 (line num in coconut source)


    def admits_empty_universe(self):  #126 (line num in coconut source)
        """Determines if self allows for the possibility of an empty universe."""  #127 (line num in coconut source)
        return True  #128 (line num in coconut source)



_coconut_call_set_names(Expr)  #131 (line num in coconut source)
class Top(Expr):  #131 (line num in coconut source)
    """True"""  #132 (line num in coconut source)
    __slots__ = ()  #133 (line num in coconut source)

    @_coconut_tco  #135 (line num in coconut source)
    def __eq__(self, other):  #135 (line num in coconut source)
        return _coconut_tail_call(isinstance, other, Top)  #135 (line num in coconut source)


    def __repr__(self):  #137 (line num in coconut source)
        return "top"  #137 (line num in coconut source)


    def __str__(self):  #139 (line num in coconut source)
        return top_sym  #139 (line num in coconut source)


    def __bool__(self):  #141 (line num in coconut source)
        return True  #141 (line num in coconut source)


_coconut_call_set_names(Top)  #143 (line num in coconut source)
top = true = Top()  #143 (line num in coconut source)


class Bot(Expr):  #146 (line num in coconut source)
    """False"""  #147 (line num in coconut source)
    __slots__ = ()  #148 (line num in coconut source)

    @_coconut_tco  #150 (line num in coconut source)
    def __eq__(self, other):  #150 (line num in coconut source)
        return _coconut_tail_call(isinstance, other, Bot)  #150 (line num in coconut source)


    def __repr__(self):  #152 (line num in coconut source)
        return "bot"  #152 (line num in coconut source)


    def __str__(self):  #154 (line num in coconut source)
        return bot_sym  #154 (line num in coconut source)


    def __bool__(self):  #156 (line num in coconut source)
        return False  #156 (line num in coconut source)


    def admits_empty_universe(self):  #158 (line num in coconut source)
        return False  #158 (line num in coconut source)


_coconut_call_set_names(Bot)  #160 (line num in coconut source)
bot = false = Bot()  #160 (line num in coconut source)


class Atom(Expr):  #163 (line num in coconut source)
    """Base class for all variables."""  #164 (line num in coconut source)
    __slots__ = ("name",)  #165 (line num in coconut source)

    def __init__(self, name):  #167 (line num in coconut source)
        if isinstance(name, Atom):  #168 (line num in coconut source)
            name = name.name  #169 (line num in coconut source)
        assert isinstance(name, str), name  #170 (line num in coconut source)
        self.name = name  #171 (line num in coconut source)


    def __repr__(self):  #173 (line num in coconut source)
        return self.__class__.__name__ + '("' + self.name + '")'  #174 (line num in coconut source)


    def __str__(self):  #176 (line num in coconut source)
        return self.name  #177 (line num in coconut source)


    def __eq__(self, other):  #179 (line num in coconut source)
        return isinstance(other, self.__class__) and self.name == other.name  #180 (line num in coconut source)


    @_coconut_tco  #182 (line num in coconut source)
    def __hash__(self):  #182 (line num in coconut source)
        return _coconut_tail_call((hash), (self.__class__.__name__, self.name))  #183 (line num in coconut source)


    def substitute_elements(self, subs, **kwargs):  #185 (line num in coconut source)
        """Substitute for the elements of the Atom, not the Atom itself."""  #186 (line num in coconut source)
        return self  #187 (line num in coconut source)


    @_coconut_tco  #189 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #189 (line num in coconut source)
        if not can_sub(kwargs):  #190 (line num in coconut source)
            return self  #191 (line num in coconut source)
        _coconut_match_to_0 = subs  #192 (line num in coconut source)
        _coconut_match_check_0 = False  #192 (line num in coconut source)
        _coconut_match_set_name_sub = _coconut_sentinel  #192 (line num in coconut source)
        if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #192 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_to_0.get(self, _coconut_sentinel)  #192 (line num in coconut source)
            if _coconut_match_temp_0 is not _coconut_sentinel:  #192 (line num in coconut source)
                _coconut_match_set_name_sub = _coconut_match_temp_0  #192 (line num in coconut source)
                _coconut_match_check_0 = True  #192 (line num in coconut source)
        if _coconut_match_check_0:  #192 (line num in coconut source)
            if _coconut_match_set_name_sub is not _coconut_sentinel:  #192 (line num in coconut source)
                sub = _coconut_match_set_name_sub  #192 (line num in coconut source)
        if _coconut_match_check_0:  #192 (line num in coconut source)
            do_sub(kwargs)  #193 (line num in coconut source)
            if wff(sub):  #194 (line num in coconut source)
                return sub  #195 (line num in coconut source)
            elif sub is True:  #196 (line num in coconut source)
                return top  #197 (line num in coconut source)
            elif sub is False:  #198 (line num in coconut source)
                return bot  #199 (line num in coconut source)
            else:  #200 (line num in coconut source)
                raise TypeError("cannot perform substitution " + str(self) + " => " + str(sub))  #201 (line num in coconut source)
        else:  #202 (line num in coconut source)
            return _coconut_tail_call(self.substitute_elements, subs, **kwargs)  #203 (line num in coconut source)



_coconut_call_set_names(Atom)  #206 (line num in coconut source)
class Prop(Atom):  #206 (line num in coconut source)
    """Logical proposition that is either true or false."""  #207 (line num in coconut source)
    __slots__ = ()  #208 (line num in coconut source)

    @_coconut_tco  #210 (line num in coconut source)
    def __call__(self, *args):  #210 (line num in coconut source)
        return _coconut_tail_call(Pred, self.name, *args)  #211 (line num in coconut source)


_coconut_call_set_names(Prop)  #213 (line num in coconut source)
Proposition = Prop  #213 (line num in coconut source)


class FuncAtom(Atom):  #216 (line num in coconut source)
    """Base class for predicates and functions."""  #217 (line num in coconut source)
    __slots__ = ("args",)  #218 (line num in coconut source)

    def __init__(self, name, *args):  #220 (line num in coconut source)
        __class__ = FuncAtom  #221 (line num in coconut source)

        super().__init__(name)  #221 (line num in coconut source)
        for arg in args:  #222 (line num in coconut source)
            assert isinstance(arg, Term), arg  #223 (line num in coconut source)
        self.args = args  #224 (line num in coconut source)


    def __repr__(self):  #226 (line num in coconut source)
        return self.__class__.__name__ + '("' + self.name + '"' + (", " if self.args else "") + ", ".join((repr(x) for x in self.args)) + ")"  #227 (line num in coconut source)


    def __str__(self):  #229 (line num in coconut source)
        return self.name + "(" + ", ".join((str(x) for x in self.args)) + ")"  #230 (line num in coconut source)


    def __eq__(self, other):  #232 (line num in coconut source)
        return isinstance(other, self.__class__) and self.name == other.name and self.args == other.args  #233 (line num in coconut source)


    @_coconut_tco  #235 (line num in coconut source)
    def __hash__(self):  #235 (line num in coconut source)
        return _coconut_tail_call((hash), (self.__class__.__name__, self.name, self.args))  #236 (line num in coconut source)


    @_coconut_tco  #238 (line num in coconut source)
    def find_unification(self, other):  #238 (line num in coconut source)
        if isinstance(other, Quantifier):  #239 (line num in coconut source)
            return _coconut_tail_call(other.find_unification, self)  #240 (line num in coconut source)
        elif isinstance(other, self.__class__) and self.name == other.name and len(self.args) == len(other.args):  #241 (line num in coconut source)
            subs = {}  #242 (line num in coconut source)
            for i, x in enumerate(self.args):  #243 (line num in coconut source)
                y = other.args[i]  #244 (line num in coconut source)
                unif = x.find_unification(y)  #245 (line num in coconut source)
                if unif is None:  #246 (line num in coconut source)
                    return None  #247 (line num in coconut source)
                for var, sub in unif.items():  #248 (line num in coconut source)
                    if var not in subs:  #249 (line num in coconut source)
                        subs[var] = sub  #250 (line num in coconut source)
                    elif subs[var] != sub:  #251 (line num in coconut source)
                        return None  #252 (line num in coconut source)
            return subs  #253 (line num in coconut source)
        else:  #254 (line num in coconut source)
            return None  #255 (line num in coconut source)


    @_coconut_tco  #257 (line num in coconut source)
    def admits_empty_universe(self):  #257 (line num in coconut source)
        return _coconut_tail_call(all, (x.admits_empty_universe() for x in self.args))  #258 (line num in coconut source)



_coconut_call_set_names(FuncAtom)  #261 (line num in coconut source)
class Pred(FuncAtom):  #261 (line num in coconut source)
    """Boolean function of terms."""  #262 (line num in coconut source)
    __slots__ = ()  #263 (line num in coconut source)

    @_coconut_tco  #265 (line num in coconut source)
    def proposition(self):  #265 (line num in coconut source)
        return _coconut_tail_call(Prop, self.name)  #266 (line num in coconut source)


    @_coconut_tco  #268 (line num in coconut source)
    def substitute_elements(self, subs, **kwargs):  #268 (line num in coconut source)
        if not can_sub(kwargs):  #269 (line num in coconut source)
            return self  #270 (line num in coconut source)
        _coconut_match_to_1 = subs  #271 (line num in coconut source)
        _coconut_match_check_1 = False  #271 (line num in coconut source)
        _coconut_match_set_name_sub = _coconut_sentinel  #271 (line num in coconut source)
        if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #271 (line num in coconut source)
            _coconut_match_temp_1 = _coconut_match_to_1.get(self.proposition(), _coconut_sentinel)  #271 (line num in coconut source)
            if _coconut_match_temp_1 is not _coconut_sentinel:  #271 (line num in coconut source)
                _coconut_match_set_name_sub = _coconut_match_temp_1  #271 (line num in coconut source)
                _coconut_match_check_1 = True  #271 (line num in coconut source)
        if _coconut_match_check_1:  #271 (line num in coconut source)
            if _coconut_match_set_name_sub is not _coconut_sentinel:  #271 (line num in coconut source)
                sub = _coconut_match_set_name_sub  #271 (line num in coconut source)
        if _coconut_match_check_1:  #271 (line num in coconut source)
            assert isinstance(sub, Atom), sub  #272 (line num in coconut source)
            do_sub(kwargs)  #273 (line num in coconut source)
            name = sub.name  #274 (line num in coconut source)
        else:  #275 (line num in coconut source)
            name = self.name  #276 (line num in coconut source)
        if can_sub(kwargs):  #277 (line num in coconut source)
            return _coconut_tail_call((Pred), name, *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.args))  #278 (line num in coconut source)
        else:  #279 (line num in coconut source)
            return _coconut_tail_call(Pred, name, *self.args)  #280 (line num in coconut source)


_coconut_call_set_names(Pred)  #282 (line num in coconut source)
Predicate = Pred  #282 (line num in coconut source)


class Term(Atom):  #285 (line num in coconut source)
    """Base class for all terms."""  #286 (line num in coconut source)
    __slots__ = ()  #287 (line num in coconut source)

    @_coconut_tco  #289 (line num in coconut source)
    def variable(self):  #289 (line num in coconut source)
        """Convert to a variable."""  #290 (line num in coconut source)
        return _coconut_tail_call(Var, self.name)  #291 (line num in coconut source)


    @_coconut_tco  #293 (line num in coconut source)
    def constant(self):  #293 (line num in coconut source)
        """Convert to a constant."""  #294 (line num in coconut source)
        return _coconut_tail_call(Const, self.name)  #295 (line num in coconut source)


    @_coconut_tco  #297 (line num in coconut source)
    def rename(self, name):  #297 (line num in coconut source)
        """Create a new term with a different name."""  #298 (line num in coconut source)
        return _coconut_tail_call(self.__class__, name)  #299 (line num in coconut source)


    @_coconut_tco  #301 (line num in coconut source)
    def prime(self):  #301 (line num in coconut source)
        """Rename by adding a prime."""  #302 (line num in coconut source)
        return _coconut_tail_call(self.rename, self.name + "'")  #303 (line num in coconut source)


    @_coconut_tco  #305 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #305 (line num in coconut source)
        if can_sub(kwargs):  #306 (line num in coconut source)
            for var, sub in subs.items():  #307 (line num in coconut source)
                if can_sub(kwargs) and isinstance(var, Term) and self.name == var.name:  #308 (line num in coconut source)
                    do_sub(kwargs)  #309 (line num in coconut source)
                    if isvar(self) or self == var:  #310 (line num in coconut source)
                        return sub  #311 (line num in coconut source)
                    else:  #312 (line num in coconut source)
                        return self.rename(sub.name)  #313 (line num in coconut source)
        if can_sub(kwargs):  #314 (line num in coconut source)
            return _coconut_tail_call(self.substitute_elements, subs, **kwargs)  #315 (line num in coconut source)
        return self  #316 (line num in coconut source)



_coconut_call_set_names(Term)  #319 (line num in coconut source)
class Var(Term):  #319 (line num in coconut source)
    """A variable quantified by a ForAll."""  #320 (line num in coconut source)
    __slots__ = ()  #321 (line num in coconut source)

    def __str__(self):  #323 (line num in coconut source)
        __class__ = Var  #324 (line num in coconut source)

        return "?" + super().__str__()  #324 (line num in coconut source)


    def variable(self):  #326 (line num in coconut source)
        return self  #326 (line num in coconut source)


    @_coconut_tco  #328 (line num in coconut source)
    def __call__(self, *args):  #328 (line num in coconut source)
        return _coconut_tail_call(Func, self.name, *args)  #329 (line num in coconut source)


    def is_free_in(self, expr):  #331 (line num in coconut source)
        """Determine if self is free in expr."""  #332 (line num in coconut source)
        return expr == expr.substitute({self: self.prime()})  #333 (line num in coconut source)


    def find_unification(self, other):  #335 (line num in coconut source)
        if isinstance(other, Term) and self.is_free_in(other):  #336 (line num in coconut source)
            return {self: other}  #337 (line num in coconut source)
        else:  #338 (line num in coconut source)
            return None  #339 (line num in coconut source)


_coconut_call_set_names(Var)  #341 (line num in coconut source)
Variable = Var  #341 (line num in coconut source)


class Const(Term):  #344 (line num in coconut source)
    """A variable quantified by an Exists."""  #345 (line num in coconut source)
    __slots__ = ()  #346 (line num in coconut source)

    def constant(self):  #348 (line num in coconut source)
        return self  #348 (line num in coconut source)


    @_coconut_tco  #350 (line num in coconut source)
    def __call__(self, *args):  #350 (line num in coconut source)
        return _coconut_tail_call(Func, self.name, *args)  #351 (line num in coconut source)


    def find_unification(self, other):  #353 (line num in coconut source)
        if isinstance(other, Var):  #354 (line num in coconut source)
            return {other: self}  #355 (line num in coconut source)
        else:  #356 (line num in coconut source)
            __class__ = Const  #357 (line num in coconut source)

            return super().find_unification(other)  #357 (line num in coconut source)


    def admits_empty_universe(self):  #359 (line num in coconut source)
        return False  #359 (line num in coconut source)


_coconut_call_set_names(Const)  #361 (line num in coconut source)
Constant = Const  #361 (line num in coconut source)


class Func(Term, FuncAtom):  #364 (line num in coconut source)
    """A function on terms."""  #365 (line num in coconut source)
    __slots__ = ()  #366 (line num in coconut source)

    @_coconut_tco  #368 (line num in coconut source)
    def substitute_elements(self, subs, **kwargs):  #368 (line num in coconut source)
        return _coconut_tail_call((Func), self.name, *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.args))  #369 (line num in coconut source)


    @_coconut_tco  #371 (line num in coconut source)
    def rename(self, name):  #371 (line num in coconut source)
        return _coconut_tail_call(self.__class__, name, *self.args)  #372 (line num in coconut source)


    def find_unification(self, other):  #374 (line num in coconut source)
        if isinstance(other, Var):  #375 (line num in coconut source)
            return {other: self}  #376 (line num in coconut source)
        else:  #377 (line num in coconut source)
            __class__ = Func  #378 (line num in coconut source)

            return super().find_unification(other)  #378 (line num in coconut source)


_coconut_call_set_names(Func)  #380 (line num in coconut source)
Function = Func  #380 (line num in coconut source)


class UnaryOp(Expr):  #383 (line num in coconut source)
    """Base class for unary operators."""  #384 (line num in coconut source)
    __slots__ = ("elem",)  #385 (line num in coconut source)

    def __init__(self, elem):  #387 (line num in coconut source)
        assert wff(elem), elem  #388 (line num in coconut source)
        self.elem = elem  #389 (line num in coconut source)


    def __repr__(self):  #391 (line num in coconut source)
        return self.__class__.__name__ + "(" + repr(self.elem) + ")"  #392 (line num in coconut source)


    def __eq__(self, other):  #394 (line num in coconut source)
        return isinstance(other, self.__class__) and self.elem == other.elem  #395 (line num in coconut source)


    def __str__(self):  #397 (line num in coconut source)
        return self.opstr + quote(self.elem)  #398 (line num in coconut source)


    def __len__(self):  #400 (line num in coconut source)
        return len(self.elem) + 1  #401 (line num in coconut source)


    @_coconut_tco  #403 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #403 (line num in coconut source)
        return _coconut_tail_call(self.__class__, self.elem.substitute(subs, **kwargs))  #404 (line num in coconut source)


    @_coconut_tco  #406 (line num in coconut source)
    def find_unification(self, other):  #406 (line num in coconut source)
        if isinstance(other, Quantifier):  #407 (line num in coconut source)
            return _coconut_tail_call(other.find_unification, self)  #408 (line num in coconut source)
        elif isinstance(other, self.__class__):  #409 (line num in coconut source)
            return _coconut_tail_call(self.elem.find_unification, other.elem)  #410 (line num in coconut source)
        else:  #411 (line num in coconut source)
            return None  #412 (line num in coconut source)


    @_coconut_tco  #414 (line num in coconut source)
    def resolve(self, **kwargs):  #414 (line num in coconut source)
        return _coconut_tail_call(self.__class__(self.elem.resolve(**kwargs)).simplify, dnf=False, **kwargs)  #415 (line num in coconut source)



_coconut_call_set_names(UnaryOp)  #418 (line num in coconut source)
class Not(UnaryOp):  #418 (line num in coconut source)
    """Logical not."""  #419 (line num in coconut source)
    __slots__ = ()  #420 (line num in coconut source)
    opstr = not_sym  #421 (line num in coconut source)

    @property  #423 (line num in coconut source)
    def neg(self):  #424 (line num in coconut source)
        return self.elem  #424 (line num in coconut source)


    @_coconut_tco  #426 (line num in coconut source)
    def simplify(self, **kwargs):  #426 (line num in coconut source)
        if top == self.neg:  #427 (line num in coconut source)
            return bot  #428 (line num in coconut source)
        elif bot == self.neg:  #429 (line num in coconut source)
            return top  #430 (line num in coconut source)
        elif isinstance(self.neg, Not):  #431 (line num in coconut source)
            return _coconut_tail_call(self.neg.neg.simplify, **kwargs)  #432 (line num in coconut source)
        elif isinstance(self.neg, And):  #433 (line num in coconut source)
            return _coconut_tail_call(Or(*map(Not, self.neg.ands)).simplify, **kwargs)  #434 (line num in coconut source)
        elif isinstance(self.neg, Or):  #435 (line num in coconut source)
            return _coconut_tail_call(And(*map(Not, self.neg.ors)).simplify, **kwargs)  #436 (line num in coconut source)
        elif isinstance(self.neg, Imp):  #437 (line num in coconut source)
            ands = self.neg.conds + (Not(self.neg.concl),)  #438 (line num in coconut source)
            return _coconut_tail_call(And(*ands).simplify, **kwargs)  #439 (line num in coconut source)
        elif isinstance(self.neg, Exists):  #440 (line num in coconut source)
            return _coconut_tail_call(ForAll, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  #441 (line num in coconut source)
        elif isinstance(self.neg, ForAll):  #442 (line num in coconut source)
            return _coconut_tail_call(Exists, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  #443 (line num in coconut source)
        else:  #444 (line num in coconut source)
            return _coconut_tail_call(Not, self.neg.simplify(**kwargs))  #445 (line num in coconut source)


    def contradicts(self, other, **kwargs):  #447 (line num in coconut source)
        return self.neg == other  #448 (line num in coconut source)


    @_coconut_tco  #450 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #450 (line num in coconut source)
        if isinstance(other, (Or, Eq)):  #451 (line num in coconut source)
            return _coconut_tail_call(other.resolve_against, self, **kwargs)  #452 (line num in coconut source)
        elif self.neg.find_unification(other) is not None:  #453 (line num in coconut source)
            return bot  #454 (line num in coconut source)
        else:  #455 (line num in coconut source)
            return None  #456 (line num in coconut source)


    @_coconut_tco  #458 (line num in coconut source)
    def admits_empty_universe(self):  #458 (line num in coconut source)
        if isinstance(self.neg, Atom):  #459 (line num in coconut source)
            return _coconut_tail_call(self.neg.admits_empty_universe)  #460 (line num in coconut source)
        else:  #461 (line num in coconut source)
            return not self.neg.admits_empty_universe()  #462 (line num in coconut source)



_coconut_call_set_names(Not)  #465 (line num in coconut source)
class Quantifier(Expr):  #465 (line num in coconut source)
    """Base class for logical quantifiers."""  #466 (line num in coconut source)
    __slots__ = ("var", "elem")  #467 (line num in coconut source)

    def __repr__(self):  #469 (line num in coconut source)
        return self.__class__.__name__ + '("' + str(self.var) + '", ' + repr(self.elem) + ")"  #470 (line num in coconut source)


    def __str__(self):  #472 (line num in coconut source)
        return self.opstr + " " + str(self.var) + ", " + quote(self.elem, in_quantifier=True)  #473 (line num in coconut source)


    def __len__(self):  #475 (line num in coconut source)
        return len(self.elem) + len(self.var)  #476 (line num in coconut source)


    @_coconut_tco  #478 (line num in coconut source)
    def change_var(self, var):  #478 (line num in coconut source)
        """Create an equivalent expression with a new quantified variable."""  #479 (line num in coconut source)
        return _coconut_tail_call(self.__class__, var, self.elem.substitute({self.var: var}))  #480 (line num in coconut source)


    @_coconut_tco  #482 (line num in coconut source)
    def change_elem(self, elem):  #482 (line num in coconut source)
        """Create an equivalent quantifier with a new expression."""  #483 (line num in coconut source)
        return _coconut_tail_call(self.__class__, self.var, elem)  #484 (line num in coconut source)


    def __eq__(self, other):  #486 (line num in coconut source)
        if isinstance(other, self.__class__):  #487 (line num in coconut source)
            return self.elem == other.change_var(self.var).elem  #488 (line num in coconut source)
        else:  #489 (line num in coconut source)
            return False  #490 (line num in coconut source)


    def inner_kwargs(self, kwargs):  #492 (line num in coconut source)
        inner_kwargs = kwargs.copy()  #493 (line num in coconut source)
        inner_kwargs["in_" + self.__class__.__name__.lower()] = True  #494 (line num in coconut source)
        return inner_kwargs  #495 (line num in coconut source)


    @_coconut_tco  #497 (line num in coconut source)
    def simplify(self, **kwargs):  #497 (line num in coconut source)
        return _coconut_tail_call(self.__class__(self.var, self.elem.simplify(**self.inner_kwargs(kwargs))).drop_quantifier, **kwargs)  #498 (line num in coconut source)


    @_coconut_tco  #500 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #500 (line num in coconut source)
        return _coconut_tail_call((self.change_elem), (self.elem.substitute)((rem_var)(self.var, subs), **kwargs))  #501 (line num in coconut source)


    @_coconut_tco  #503 (line num in coconut source)
    def make_free_in(self, other):  #503 (line num in coconut source)
        """Makes self free in other."""  #504 (line num in coconut source)
        var = self.var  #505 (line num in coconut source)
        newvar = var.prime()  #506 (line num in coconut source)
        while other != other.substitute({var: newvar}):  #507 (line num in coconut source)
            var, newvar = newvar, newvar.prime()  #508 (line num in coconut source)
        return _coconut_tail_call(self.change_var, var)  #509 (line num in coconut source)


    @_coconut_tco  #511 (line num in coconut source)
    def find_unification(self, other):  #511 (line num in coconut source)
        unif = self.elem.find_unification(other)  #512 (line num in coconut source)
        if unif is None:  #513 (line num in coconut source)
            return None  #514 (line num in coconut source)
        else:  #515 (line num in coconut source)
            return _coconut_tail_call((rem_var), self.var, unif)  #516 (line num in coconut source)


    @_coconut_tco  #518 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #518 (line num in coconut source)
        if isinstance(other, Quantifier):  #519 (line num in coconut source)
            resolution = (self.elem.resolve_against)(Not(other.elem).simplify(**kwargs), **kwargs)  #520 (line num in coconut source)
            if resolution is None:  #521 (line num in coconut source)
                return None  #522 (line num in coconut source)
            elif isinstance(other, ForAll):  # don't pull an Exists out of a ForAll  #523 (line num in coconut source)
                return _coconut_tail_call((other.change_elem), (self.change_elem)(resolution))  #524 (line num in coconut source)
            else:  #525 (line num in coconut source)
                return _coconut_tail_call((self.change_elem), (other.change_elem)(resolution))  #526 (line num in coconut source)
        else:  #527 (line num in coconut source)
            __class__ = Quantifier  #528 (line num in coconut source)

            return super().resolve_against(other, **kwargs)  #528 (line num in coconut source)

    @classmethod  #529 (line num in coconut source)

    @_coconut_tco  #531 (line num in coconut source)
    def blank(cls, elem):  #531 (line num in coconut source)
        """Make a quantifier without a variable."""  #532 (line num in coconut source)
        return _coconut_tail_call(cls(empty_var, elem).make_free_in, elem)  #533 (line num in coconut source)



_coconut_call_set_names(Quantifier)  #536 (line num in coconut source)
class ForAll(Quantifier):  #536 (line num in coconut source)
    """Universal quantifier."""  #537 (line num in coconut source)
    __slots__ = ()  #538 (line num in coconut source)
    opstr = forall_sym  #539 (line num in coconut source)

    def __init__(self, var, elem):  #541 (line num in coconut source)
        assert wff(elem), elem  #542 (line num in coconut source)
        if isinstance(var, str):  #543 (line num in coconut source)
            var = Const(var)  #544 (line num in coconut source)
        assert isvar(var), var  #545 (line num in coconut source)
        self.var = var.variable()  #546 (line num in coconut source)
        self.elem = elem.substitute({var: self.var.variable()})  #547 (line num in coconut source)


    @_coconut_tco  #549 (line num in coconut source)
    def resolve(self, **kwargs):  #549 (line num in coconut source)
        inner_kwargs = self.inner_kwargs(kwargs)  #550 (line num in coconut source)
        inner_kwargs["variables"] = kwargs.get("variables", ()) + (self.var,)  #551 (line num in coconut source)
        return _coconut_tail_call(ForAll(self.var, self.elem.resolve(**inner_kwargs)).simplify, dnf=False, **kwargs)  #552 (line num in coconut source)


    def drop_quantifier(self, nonempty_universe=True, in_forall=False, **kwargs):  #554 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["in_forall"] = nonempty_universe, in_forall  #555 (line num in coconut source)
        if not nonempty_universe and not in_forall:  #556 (line num in coconut source)
            elem = self.elem  #557 (line num in coconut source)
            while isinstance(elem, Exists):  #558 (line num in coconut source)
                elem = elem.elem  #559 (line num in coconut source)
            if top == elem:  #560 (line num in coconut source)
                return elem  #561 (line num in coconut source)
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):  #562 (line num in coconut source)
            return self.elem  #563 (line num in coconut source)
        return self  #564 (line num in coconut source)


_coconut_call_set_names(ForAll)  #566 (line num in coconut source)
FA = ForAll  #566 (line num in coconut source)


class Exists(Quantifier):  #569 (line num in coconut source)
    """Existential quantifier."""  #570 (line num in coconut source)
    __slots__ = ()  #571 (line num in coconut source)
    opstr = exists_sym  #572 (line num in coconut source)

    def __init__(self, var, elem):  #574 (line num in coconut source)
        assert wff(elem), elem  #575 (line num in coconut source)
        if isinstance(var, str):  #576 (line num in coconut source)
            var = Const(var)  #577 (line num in coconut source)
        assert isvar(var), var  #578 (line num in coconut source)
        self.var = var.constant()  #579 (line num in coconut source)
        self.elem = elem.substitute({var: self.var.constant()})  #580 (line num in coconut source)


    @_coconut_tco  #582 (line num in coconut source)
    def resolve(self, **kwargs):  #582 (line num in coconut source)
        inner_kwargs = self.inner_kwargs(kwargs)  #583 (line num in coconut source)
        variables = inner_kwargs.get("variables")  #584 (line num in coconut source)
        if variables is None:  #585 (line num in coconut source)
            skolem_elem = self.elem  #586 (line num in coconut source)
        else:  #587 (line num in coconut source)
            skolem_var = Func(self.var.name, *variables)  #588 (line num in coconut source)
            skolem_elem = self.elem.substitute({self.var: skolem_var})  #589 (line num in coconut source)
        return _coconut_tail_call(Exists(self.var, skolem_elem.resolve(**inner_kwargs)).simplify, dnf=False, **kwargs)  #590 (line num in coconut source)


    def drop_quantifier(self, nonempty_universe=True, in_exists=False, **kwargs):  #592 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["in_exists"] = nonempty_universe, in_exists  #593 (line num in coconut source)
        if not nonempty_universe and not in_exists:  #594 (line num in coconut source)
            elem = self.elem  #595 (line num in coconut source)
            while isinstance(elem, ForAll):  #596 (line num in coconut source)
                elem = elem.elem  #597 (line num in coconut source)
            if bot == elem:  #598 (line num in coconut source)
                return elem  #599 (line num in coconut source)
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):  #600 (line num in coconut source)
            return self.elem  #601 (line num in coconut source)
        return self  #602 (line num in coconut source)


    def admits_empty_universe(self):  #604 (line num in coconut source)
        return False  #604 (line num in coconut source)


_coconut_call_set_names(Exists)  #606 (line num in coconut source)
TE = Exists  #606 (line num in coconut source)


class BinaryOp(Expr):  #609 (line num in coconut source)
    """Base class for binary operators."""  #610 (line num in coconut source)
    __slots__ = ("elems",)  #611 (line num in coconut source)
    identity = None  #612 (line num in coconut source)

    def __new__(cls, *elems):  #614 (line num in coconut source)
        if not elems:  #615 (line num in coconut source)
            if cls.identity is None:  #616 (line num in coconut source)
                raise TypeError(cls.__name__ + " requires at least one argument")  #617 (line num in coconut source)
            else:  #618 (line num in coconut source)
                return cls.identity  #619 (line num in coconut source)
        elif len(elems) == 1:  #620 (line num in coconut source)
            assert wff(elems[0]), elems[0]  #621 (line num in coconut source)
            return elems[0]  # sometimes returns an instance of cls  #622 (line num in coconut source)
        else:  #623 (line num in coconut source)
            __class__ = BinaryOp  #624 (line num in coconut source)

            return super().__new__(cls)  #624 (line num in coconut source)


    def __init__(self, *elems):  #626 (line num in coconut source)
        if len(elems) > 1:  # __new__ should handle all other cases  #627 (line num in coconut source)
            assert len(elems) >= 2, elems  #628 (line num in coconut source)
            for x in elems:  #629 (line num in coconut source)
                assert wff(x), x  #630 (line num in coconut source)
            self.elems = elems  #631 (line num in coconut source)


    def __repr__(self):  #633 (line num in coconut source)
        return self.__class__.__name__ + "(" + ", ".join((repr(x) for x in self.elems)) + ")"  #634 (line num in coconut source)


    @_coconut_tco  #636 (line num in coconut source)
    def __str__(self):  #636 (line num in coconut source)
        return _coconut_tail_call((" " + self.opstr + " ").join, (quote(x) for x in self.elems))  #637 (line num in coconut source)


    def __len__(self):  #639 (line num in coconut source)
        return sum(map(len, self.elems)) + 1  #640 (line num in coconut source)


    @_coconut_tco  #642 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #642 (line num in coconut source)
        return _coconut_tail_call((self.__class__), *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.elems))  #643 (line num in coconut source)


    @_coconut_tco  #645 (line num in coconut source)
    def resolve(self, **kwargs):  #645 (line num in coconut source)
        elems = (map)(_coconut.operator.methodcaller("resolve", **kwargs), self.elems)  #646 (line num in coconut source)
        return _coconut_tail_call(self.__class__(*elems).simplify, dnf=False, **kwargs)  #647 (line num in coconut source)



_coconut_call_set_names(BinaryOp)  #650 (line num in coconut source)
class Imp(BinaryOp):  #650 (line num in coconut source)
    """Logical implication."""  #651 (line num in coconut source)
    __slots__ = ()  #652 (line num in coconut source)
    opstr = imp_sym  #653 (line num in coconut source)

    @_coconut_tco  #655 (line num in coconut source)
    def __rshift__(self, other):  #655 (line num in coconut source)
        if isinstance(other, Imp):  #656 (line num in coconut source)
            return _coconut_tail_call(Imp, self, *other.elems)  #657 (line num in coconut source)
        else:  #658 (line num in coconut source)
            return _coconut_tail_call(Imp, self, other)  #659 (line num in coconut source)


    @_coconut_tco  #661 (line num in coconut source)
    def __lshift__(self, other):  #661 (line num in coconut source)
        return _coconut_tail_call((Imp), *(other,) + self.elems)  #662 (line num in coconut source)


    @property  #664 (line num in coconut source)
    def conds(self):  #665 (line num in coconut source)
        return self.elems[:-1]  #665 (line num in coconut source)


    @property  #667 (line num in coconut source)
    def concl(self):  #668 (line num in coconut source)
        return self.elems[-1]  #668 (line num in coconut source)


    def __eq__(self, other):  #670 (line num in coconut source)
        return isinstance(other, self.__class__) and self.concl == other.concl and (unorderd_eq)(self.conds, other.conds)  #671 (line num in coconut source)


    @_coconut_tco  #673 (line num in coconut source)
    def to_or(self):  #673 (line num in coconut source)
        ors = tuple(map(Not, self.conds)) + (self.concl,)  #674 (line num in coconut source)
        return _coconut_tail_call(Or, *ors)  #675 (line num in coconut source)


    @_coconut_tco  #677 (line num in coconut source)
    def simplify(self, **kwargs):  #677 (line num in coconut source)
        return _coconut_tail_call(self.to_or().simplify, **kwargs)  #678 (line num in coconut source)


    @_coconut_tco  #680 (line num in coconut source)
    def admits_empty_universe(self):  #680 (line num in coconut source)
        return _coconut_tail_call(self.to_or().admits_empty_universe)  #681 (line num in coconut source)


_coconut_call_set_names(Imp)  #683 (line num in coconut source)
Implies = Imp  #683 (line num in coconut source)


class BoolOp(BinaryOp):  #686 (line num in coconut source)
    """Base class for Or and And."""  #687 (line num in coconut source)
    __slots__ = ()  #688 (line num in coconut source)

    def __eq__(self, other):  #690 (line num in coconut source)
        return isinstance(other, self.__class__) and (unorderd_eq)(self.elems, other.elems)  #691 (line num in coconut source)


    def simplify(self, **kwargs):  #693 (line num in coconut source)
        elems = (map)(_coconut.operator.methodcaller("simplify", **kwargs), self.merge().elems)  #694 (line num in coconut source)
        out = self.__class__(*elems).clean()  #695 (line num in coconut source)
        if isinstance(out, self.__class__):  #696 (line num in coconut source)
            out = out.distribute(**kwargs)  #697 (line num in coconut source)
        if isinstance(out, self.__class__):  #698 (line num in coconut source)
            out = out.merge().dedupe()  #699 (line num in coconut source)
        if isinstance(out, self.__class__):  #700 (line num in coconut source)
            out = out.inner_simplify(**kwargs)  #701 (line num in coconut source)
        if isinstance(out, self.__class__):  #702 (line num in coconut source)
            out = out.prenex(**kwargs)  #703 (line num in coconut source)
        log_simplification(self, out, **kwargs)  #704 (line num in coconut source)
        return out  #705 (line num in coconut source)


    @_coconut_tco  #707 (line num in coconut source)
    def merge(self):  #707 (line num in coconut source)
        """Merges nested copies of a boolean operator."""  #708 (line num in coconut source)
        elems = []  #709 (line num in coconut source)
        for x in self.elems:  #710 (line num in coconut source)
            if isinstance(x, self.__class__):  #711 (line num in coconut source)
                elems.extend(x.merge().elems)  #712 (line num in coconut source)
            else:  #713 (line num in coconut source)
                elems.append(x)  #714 (line num in coconut source)
        return _coconut_tail_call(self.__class__, *elems)  #715 (line num in coconut source)


    @_coconut_tco  #717 (line num in coconut source)
    def dedupe(self):  #717 (line num in coconut source)
        """Removes duplicate elements from a boolean operator."""  #718 (line num in coconut source)
        elems = []  #719 (line num in coconut source)
        for x in self.elems:  #720 (line num in coconut source)
            if x not in elems:  #721 (line num in coconut source)
                elems.append(x)  #722 (line num in coconut source)
        return _coconut_tail_call(self.__class__, *elems)  #723 (line num in coconut source)


    @_coconut_tco  #725 (line num in coconut source)
    def clean(self):  #725 (line num in coconut source)
        """Removes copies of the identity."""  #726 (line num in coconut source)
        return _coconut_tail_call((self.__class__), *(filter)(_coconut.functools.partial((_coconut.operator.ne), self.identity), self.elems))  #727 (line num in coconut source)


    def prenex(self, **kwargs):  #729 (line num in coconut source)
        """Pulls quantifiers out."""  #730 (line num in coconut source)
        for i, x in enumerate(self.elems):  #731 (line num in coconut source)
            if isinstance(x, Quantifier) and self.can_prenex(x, **kwargs):  #732 (line num in coconut source)
                elems = self.elems[:i] + self.elems[i + 1:]  #733 (line num in coconut source)
                free_x = x.make_free_in(self.__class__(*elems))  #734 (line num in coconut source)
                elems += (free_x.elem,)  #735 (line num in coconut source)
                return free_x.change_elem(self.__class__(*elems)).simplify(**kwargs)  #736 (line num in coconut source)
        return self  #737 (line num in coconut source)



_coconut_call_set_names(BoolOp)  #740 (line num in coconut source)
class Or(BoolOp):  #740 (line num in coconut source)
    """Logical disjunction."""  #741 (line num in coconut source)
    __slots__ = ()  #742 (line num in coconut source)
    opstr = or_sym  #743 (line num in coconut source)
    identity = bot  #744 (line num in coconut source)

    @_coconut_tco  #746 (line num in coconut source)
    def __or__(self, other):  #746 (line num in coconut source)
        return _coconut_tail_call((Or), *self.elems + (other,))  #747 (line num in coconut source)


    @property  #749 (line num in coconut source)
    def ors(self):  #750 (line num in coconut source)
        return self.elems  #750 (line num in coconut source)


    def distribute(self, dnf=False, **kwargs):  #752 (line num in coconut source)
        """If this Or contains an And, distribute into it."""  #753 (line num in coconut source)
        kwargs["dnf"] = dnf  #754 (line num in coconut source)
        if not dnf:  #755 (line num in coconut source)
            for i, x in enumerate(self.ors):  #756 (line num in coconut source)
                if isinstance(x, And):  #757 (line num in coconut source)
                    ands = ((Or)(*(y,) + self.ors[:i] + self.ors[i + 1:]) for y in x.ands)  #758 (line num in coconut source)
                    return And(*ands).simplify(**kwargs)  #759 (line num in coconut source)
        return self  #760 (line num in coconut source)


    def inner_simplify(self, nonempty_universe=True, **kwargs):  #762 (line num in coconut source)
        """Determines if the Or is a blatant tautology."""  #763 (line num in coconut source)
        kwargs["nonempty_universe"] = nonempty_universe  #764 (line num in coconut source)
        for i, x in enumerate(self.ors):  #765 (line num in coconut source)
            if top == x:  #766 (line num in coconut source)
                return x  #767 (line num in coconut source)
            for y in self.ors[i + 1:]:  #768 (line num in coconut source)
                if x.contradicts(y, **kwargs):  #769 (line num in coconut source)
                    if not nonempty_universe and not self.admits_empty_universe():  #770 (line num in coconut source)
                        return Exists.blank(top)  #771 (line num in coconut source)
                    else:  #772 (line num in coconut source)
                        return top  #773 (line num in coconut source)
        return self  #774 (line num in coconut source)


    def can_prenex(self, other, nonempty_universe=True, in_forall=False, **kwargs):  #776 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["in_forall"] = nonempty_universe, in_forall  #777 (line num in coconut source)
        return (nonempty_universe or in_forall or not isinstance(other, Exists) or not self.admits_empty_universe())  #778 (line num in coconut source)


    @_coconut_tco  #783 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #783 (line num in coconut source)
        if isinstance(other, Eq):  #784 (line num in coconut source)
            return _coconut_tail_call(other.resolve_against, self)  #785 (line num in coconut source)
        elif isinstance(other, Or):  #786 (line num in coconut source)
            not_other_ors = (map)(_coconut.operator.methodcaller("simplify", **kwargs), (map)(Not, other.ors))  #787 (line num in coconut source)
            for i, x in enumerate(self.ors):  #788 (line num in coconut source)
                if isinstance(x, Eq):  #789 (line num in coconut source)
                    resolved_other = (x.paramodulant)(other)  #790 (line num in coconut source)
                    return (Or)(*self.ors[:i] + self.ors[i + 1:] + resolved_other.ors)  #791 (line num in coconut source)
                for j, y in enumerate(not_other_ors):  #792 (line num in coconut source)
                    if isinstance(other.ors[j], Eq):  #793 (line num in coconut source)
                        y = other.ors[j]  #794 (line num in coconut source)
                        resolved_self = (y.paramodulant)(self)  #795 (line num in coconut source)
                        return (Or)(*other.ors[:j] + other.ors[j + 1:] + resolved_self.ors)  #796 (line num in coconut source)
                    subs = x.find_unification(y)  #797 (line num in coconut source)
                    if subs is not None:  #798 (line num in coconut source)
                        return (Or)(*(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.ors[:i] + self.ors[i + 1:] + other.ors[:j] + other.ors[j + 1:]))  #799 (line num in coconut source)
        else:  #800 (line num in coconut source)
            not_other = Not(other).simplify(**kwargs)  #801 (line num in coconut source)
            for i, x in enumerate(self.ors):  #802 (line num in coconut source)
                if isinstance(x, Eq):  #803 (line num in coconut source)
                    return (x.paramodulant)((Or)(*self.ors[:i] + self.ors[i + 1:]))  #804 (line num in coconut source)
                subs = x.find_unification(not_other)  #805 (line num in coconut source)
                if subs is not None:  #806 (line num in coconut source)
                    return (Or)(*(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.ors[:i] + self.ors[i + 1:]))  #807 (line num in coconut source)
        return None  #808 (line num in coconut source)


    @_coconut_tco  #810 (line num in coconut source)
    def admits_empty_universe(self):  #810 (line num in coconut source)
        return _coconut_tail_call(any, (x.admits_empty_universe() for x in self.elems))  #811 (line num in coconut source)



_coconut_call_set_names(Or)  #814 (line num in coconut source)
class And(BoolOp):  #814 (line num in coconut source)
    """Logical conjunction."""  #815 (line num in coconut source)
    __slots__ = ()  #816 (line num in coconut source)
    opstr = and_sym  #817 (line num in coconut source)
    identity = top  #818 (line num in coconut source)

    @_coconut_tco  #820 (line num in coconut source)
    def __and__(self, other):  #820 (line num in coconut source)
        return _coconut_tail_call((And), *self.elems + (other,))  #821 (line num in coconut source)


    @property  #823 (line num in coconut source)
    def ands(self):  #824 (line num in coconut source)
        return self.elems  #824 (line num in coconut source)


    def distribute(self, dnf=False, **kwargs):  #826 (line num in coconut source)
        """If this And contains an Or, distribute into it."""  #827 (line num in coconut source)
        kwargs["dnf"] = dnf  #828 (line num in coconut source)
        if dnf:  #829 (line num in coconut source)
            for i, x in enumerate(self.ands):  #830 (line num in coconut source)
                if isinstance(x, Or):  #831 (line num in coconut source)
                    ors = ((And)(*(y,) + self.ands[:i] + self.ands[i + 1:]) for y in x.ors)  #832 (line num in coconut source)
                    return Or(*ors).simplify(**kwargs)  #833 (line num in coconut source)
        return self  #834 (line num in coconut source)


    def inner_simplify(self, nonempty_universe=True, **kwargs):  #836 (line num in coconut source)
        """Determines if the And is a blatant contradiction."""  #837 (line num in coconut source)
        kwargs["nonempty_universe"] = nonempty_universe  #838 (line num in coconut source)
        for i, x in enumerate(self.ands):  #839 (line num in coconut source)
            if bot == x:  #840 (line num in coconut source)
                return x  #841 (line num in coconut source)
            for y in self.ands[i + 1:]:  #842 (line num in coconut source)
                if x.contradicts(y, **kwargs):  #843 (line num in coconut source)
                    if not nonempty_universe and self.admits_empty_universe():  #844 (line num in coconut source)
                        return ForAll.blank(bot)  #845 (line num in coconut source)
                    else:  #846 (line num in coconut source)
                        return bot  #847 (line num in coconut source)
        return self  #848 (line num in coconut source)


    def can_prenex(self, other, nonempty_universe=True, in_exists=False, **kwargs):  #850 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["in_exists"] = nonempty_universe, in_exists  #851 (line num in coconut source)
        return (nonempty_universe or in_exists or not isinstance(other, ForAll) or all((isinstance(x, ForAll) for x in self.elems)))  #852 (line num in coconut source)


    @_coconut_tco  #857 (line num in coconut source)
    def resolve(self, nonempty_universe=True, debug=False, **kwargs):  #857 (line num in coconut source)
        """Performs all possible resolutions within the And."""  #858 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["debug"] = nonempty_universe, debug  #859 (line num in coconut source)
        __class__ = And  #860 (line num in coconut source)

        resolved = super().resolve(**kwargs)  #860 (line num in coconut source)
        log_simplification(self, resolved, **kwargs)  #861 (line num in coconut source)
        if not isinstance(resolved, And):  #862 (line num in coconut source)
            return resolved  #863 (line num in coconut source)
        clauses = (list)(resolved.ands)  #864 (line num in coconut source)
        quantifiers = []  #865 (line num in coconut source)
        if not nonempty_universe and not self.admits_empty_universe():  #866 (line num in coconut source)
            blank = Exists.blank(top)  #867 (line num in coconut source)
            (quantifiers.append)(blank.change_elem)  #868 (line num in coconut source)
            kwargs = (blank.inner_kwargs)(kwargs)  #869 (line num in coconut source)
        prev_clause_len = 1  #870 (line num in coconut source)
        while prev_clause_len < len(clauses):  #871 (line num in coconut source)
            prev_clause_len = len(clauses)  #872 (line num in coconut source)
# reversed ensures conclusions get tested first
            for i in (reversed)(range(1, len(clauses))):  #874 (line num in coconut source)
                x = clauses[i]  #875 (line num in coconut source)
                for y in clauses[:i + 1]:  # allow resolution of a clause against itself  #876 (line num in coconut source)
                    resolution = x.resolve_against(y)  #877 (line num in coconut source)
                    if resolution is not None:  #878 (line num in coconut source)
                        resolution = resolution.simplify(dnf=False, **kwargs)  #879 (line num in coconut source)
                        log_resolution(x, y, resolution, **kwargs)  #880 (line num in coconut source)
                        new_quantifiers = []  #881 (line num in coconut source)
                        inner_kwargs = kwargs  #882 (line num in coconut source)
                        while isinstance(resolution, Quantifier) and self.can_prenex(resolution, **kwargs):  #883 (line num in coconut source)
                            (new_quantifiers.append)(resolution.change_elem)  #884 (line num in coconut source)
                            inner_kwargs = (resolution.inner_kwargs)(inner_kwargs)  #885 (line num in coconut source)
                            resolution = resolution.elem  #886 (line num in coconut source)
                        if isinstance(resolution, And):  #887 (line num in coconut source)
                            new_clauses = resolution.ands  #888 (line num in coconut source)
                        else:  #889 (line num in coconut source)
                            new_clauses = (resolution,)  #890 (line num in coconut source)
                        novel = False  #891 (line num in coconut source)
                        for new_clause in new_clauses:  #892 (line num in coconut source)
                            if new_clause == bot:  #893 (line num in coconut source)
                                clauses = [bot,]  #894 (line num in coconut source)
                                novel = True  #895 (line num in coconut source)
                                break  #896 (line num in coconut source)
                            elif new_clause != top and new_clause not in clauses:  #897 (line num in coconut source)
                                clauses.append(new_clause)  #898 (line num in coconut source)
                                novel = True  #899 (line num in coconut source)
                        if novel:  #900 (line num in coconut source)
                            quantifiers.extend(new_quantifiers)  #901 (line num in coconut source)
                            kwargs = inner_kwargs  #902 (line num in coconut source)
                            if clauses == [bot,]:  #903 (line num in coconut source)
                                break  #904 (line num in coconut source)
                if clauses == [bot,]:  #905 (line num in coconut source)
                    break  #906 (line num in coconut source)
        resolved = (reduce)(_coconut_pipe, [And(*clauses),] + quantifiers)  #907 (line num in coconut source)
        log_simplification(self, resolved, **kwargs)  #908 (line num in coconut source)
        return _coconut_tail_call(resolved.simplify, dnf=False, **kwargs)  #909 (line num in coconut source)


    @_coconut_tco  #911 (line num in coconut source)
    def admits_empty_universe(self):  #911 (line num in coconut source)
        return _coconut_tail_call(all, (x.admits_empty_universe() for x in self.elems))  #912 (line num in coconut source)



_coconut_call_set_names(And)  #915 (line num in coconut source)
class Eq(Expr):  #915 (line num in coconut source)
    """Equality operator."""  #916 (line num in coconut source)
    __slots__ = ("a", "b")  #917 (line num in coconut source)

    def __init__(self, a, b):  #919 (line num in coconut source)
        assert isinstance(a, Term), a  #920 (line num in coconut source)
        assert isinstance(b, Term), b  #921 (line num in coconut source)
        self.a, self.b = a, b  #922 (line num in coconut source)


    def __repr__(self):  #924 (line num in coconut source)
        return "Eq(" + repr(self.a) + ", " + repr(self.b) + ")"  #925 (line num in coconut source)


    def __str__(self):  #927 (line num in coconut source)
        return str(self.a) + "=" + str(self.b)  #928 (line num in coconut source)


    def __eq__(self, other):  #930 (line num in coconut source)
        return isinstance(other, Eq) and (self.a == other.a and self.b == other.b or self.a == other.b and self.b == other.a)  #931 (line num in coconut source)


    def simplify(self, **kwargs):  #933 (line num in coconut source)
        if self.a == self.b:  #934 (line num in coconut source)
            return top  #935 (line num in coconut source)
        else:  #936 (line num in coconut source)
            return self  #937 (line num in coconut source)


    @_coconut_tco  #939 (line num in coconut source)
    def swap(self):  #939 (line num in coconut source)
        """Swaps the order of equality."""  #940 (line num in coconut source)
        return _coconut_tail_call(Eq, self.b, self.a)  #941 (line num in coconut source)


    @_coconut_tco  #943 (line num in coconut source)
    def find_unification(self, other):  #943 (line num in coconut source)
        if isinstance(other, Quantifier):  #944 (line num in coconut source)
            return _coconut_tail_call(other.find_unification, self)  #945 (line num in coconut source)
        elif isinstance(other, Eq):  #946 (line num in coconut source)
            a_a = self.a.find_unification(other.a)  #947 (line num in coconut source)
            b_b = self.b.find_unification(other.b)  #948 (line num in coconut source)
            if a_a is not None and b_b is not None:  #949 (line num in coconut source)
                subs = merge_dicts(a_a, b_b)  #950 (line num in coconut source)
                if subs is not None:  #951 (line num in coconut source)
                    return subs  #952 (line num in coconut source)
            a_b = self.a.find_unification(other.a)  #953 (line num in coconut source)
            b_a = self.b.find_unification(other.b)  #954 (line num in coconut source)
            if a_b is not None and b_a is not None:  #955 (line num in coconut source)
                subs = merge_dicts(a_b, b_a)  #956 (line num in coconut source)
                if subs is not None:  #957 (line num in coconut source)
                    return subs  #958 (line num in coconut source)
        else:  #959 (line num in coconut source)
            return None  #960 (line num in coconut source)


    @_coconut_tco  #962 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #962 (line num in coconut source)
        return _coconut_tail_call(Eq, self.a.substitute(subs, **kwargs), self.b.substitute(subs, **kwargs))  #963 (line num in coconut source)


    @_coconut_tco  #965 (line num in coconut source)
    def paramodulant(self, other):  #965 (line num in coconut source)
        """Create a paramodulant of other."""  #966 (line num in coconut source)
        return _coconut_tail_call((sub_once), other, {self.a: self.b, self.b: self.a})  #967 (line num in coconut source)


    @_coconut_tco  #969 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #969 (line num in coconut source)
        if isinstance(other, Not) and self.find_unification(other.neg) is not None:  #970 (line num in coconut source)
            return bot  #971 (line num in coconut source)
        else:  #972 (line num in coconut source)
            return _coconut_tail_call(self.paramodulant, other)  #973 (line num in coconut source)


    def admits_empty_universe(self):  #975 (line num in coconut source)
        return self.a.admits_empty_universe() and self.b.admits_empty_universe()  #976 (line num in coconut source)


_coconut_call_set_names(Eq)  #978 (line num in coconut source)
Equals = Eq  #978 (line num in coconut source)
