#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x61bd1387

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
        if isinstance(other, (Quantifier, Var)):  #103 (line num in coconut source)
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


    def find_unification(self, other):  #238 (line num in coconut source)
        if isinstance(other, self.__class__) and self.name == other.name and len(self.args) == len(other.args):  #239 (line num in coconut source)
            subs = {}  #240 (line num in coconut source)
            for i, x in enumerate(self.args):  #241 (line num in coconut source)
                y = other.args[i]  #242 (line num in coconut source)
                unif = x.find_unification(y)  #243 (line num in coconut source)
                if unif is None:  #244 (line num in coconut source)
                    return None  #245 (line num in coconut source)
                for var, sub in unif.items():  #246 (line num in coconut source)
                    if var not in subs:  #247 (line num in coconut source)
                        subs[var] = sub  #248 (line num in coconut source)
                    elif subs[var] != sub:  #249 (line num in coconut source)
                        return None  #250 (line num in coconut source)
            return subs  #251 (line num in coconut source)
        else:  #252 (line num in coconut source)
            __class__ = FuncAtom  #253 (line num in coconut source)

            return super().find_unification(other)  #253 (line num in coconut source)


    @_coconut_tco  #255 (line num in coconut source)
    def admits_empty_universe(self):  #255 (line num in coconut source)
        return _coconut_tail_call(all, (x.admits_empty_universe() for x in self.args))  #256 (line num in coconut source)



_coconut_call_set_names(FuncAtom)  #259 (line num in coconut source)
class Pred(FuncAtom):  #259 (line num in coconut source)
    """Boolean function of terms."""  #260 (line num in coconut source)
    __slots__ = ()  #261 (line num in coconut source)

    @_coconut_tco  #263 (line num in coconut source)
    def proposition(self):  #263 (line num in coconut source)
        return _coconut_tail_call(Prop, self.name)  #264 (line num in coconut source)


    @_coconut_tco  #266 (line num in coconut source)
    def substitute_elements(self, subs, **kwargs):  #266 (line num in coconut source)
        if not can_sub(kwargs):  #267 (line num in coconut source)
            return self  #268 (line num in coconut source)
        _coconut_match_to_1 = subs  #269 (line num in coconut source)
        _coconut_match_check_1 = False  #269 (line num in coconut source)
        _coconut_match_set_name_sub = _coconut_sentinel  #269 (line num in coconut source)
        if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #269 (line num in coconut source)
            _coconut_match_temp_1 = _coconut_match_to_1.get(self.proposition(), _coconut_sentinel)  #269 (line num in coconut source)
            if _coconut_match_temp_1 is not _coconut_sentinel:  #269 (line num in coconut source)
                _coconut_match_set_name_sub = _coconut_match_temp_1  #269 (line num in coconut source)
                _coconut_match_check_1 = True  #269 (line num in coconut source)
        if _coconut_match_check_1:  #269 (line num in coconut source)
            if _coconut_match_set_name_sub is not _coconut_sentinel:  #269 (line num in coconut source)
                sub = _coconut_match_set_name_sub  #269 (line num in coconut source)
        if _coconut_match_check_1:  #269 (line num in coconut source)
            assert isinstance(sub, Atom), sub  #270 (line num in coconut source)
            do_sub(kwargs)  #271 (line num in coconut source)
            name = sub.name  #272 (line num in coconut source)
        else:  #273 (line num in coconut source)
            name = self.name  #274 (line num in coconut source)
        if can_sub(kwargs):  #275 (line num in coconut source)
            return _coconut_tail_call((Pred), name, *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.args))  #276 (line num in coconut source)
        else:  #277 (line num in coconut source)
            return _coconut_tail_call(Pred, name, *self.args)  #278 (line num in coconut source)


_coconut_call_set_names(Pred)  #280 (line num in coconut source)
Predicate = Pred  #280 (line num in coconut source)


class Term(Atom):  #283 (line num in coconut source)
    """Base class for all terms."""  #284 (line num in coconut source)
    __slots__ = ()  #285 (line num in coconut source)

    @_coconut_tco  #287 (line num in coconut source)
    def variable(self):  #287 (line num in coconut source)
        """Convert to a variable."""  #288 (line num in coconut source)
        return _coconut_tail_call(Var, self.name)  #289 (line num in coconut source)


    @_coconut_tco  #291 (line num in coconut source)
    def constant(self):  #291 (line num in coconut source)
        """Convert to a constant."""  #292 (line num in coconut source)
        return _coconut_tail_call(Const, self.name)  #293 (line num in coconut source)


    @_coconut_tco  #295 (line num in coconut source)
    def rename(self, name):  #295 (line num in coconut source)
        """Create a new term with a different name."""  #296 (line num in coconut source)
        return _coconut_tail_call(self.__class__, name)  #297 (line num in coconut source)


    @_coconut_tco  #299 (line num in coconut source)
    def prime(self):  #299 (line num in coconut source)
        """Rename by adding a prime."""  #300 (line num in coconut source)
        return _coconut_tail_call(self.rename, self.name + "'")  #301 (line num in coconut source)


    @_coconut_tco  #303 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #303 (line num in coconut source)
        if can_sub(kwargs):  #304 (line num in coconut source)
            for var, sub in subs.items():  #305 (line num in coconut source)
                if can_sub(kwargs) and isinstance(var, Term) and self.name == var.name:  #306 (line num in coconut source)
                    do_sub(kwargs)  #307 (line num in coconut source)
                    if isvar(self) or self == var:  #308 (line num in coconut source)
                        return sub  #309 (line num in coconut source)
                    else:  #310 (line num in coconut source)
                        return self.rename(sub.name)  #311 (line num in coconut source)
        if can_sub(kwargs):  #312 (line num in coconut source)
            return _coconut_tail_call(self.substitute_elements, subs, **kwargs)  #313 (line num in coconut source)
        return self  #314 (line num in coconut source)



_coconut_call_set_names(Term)  #317 (line num in coconut source)
class Var(Term):  #317 (line num in coconut source)
    """A variable quantified by a ForAll."""  #318 (line num in coconut source)
    __slots__ = ()  #319 (line num in coconut source)

    def __str__(self):  #321 (line num in coconut source)
        __class__ = Var  #322 (line num in coconut source)

        return "?" + super().__str__()  #322 (line num in coconut source)


    def variable(self):  #324 (line num in coconut source)
        return self  #324 (line num in coconut source)


    @_coconut_tco  #326 (line num in coconut source)
    def __call__(self, *args):  #326 (line num in coconut source)
        return _coconut_tail_call(Func, self.name, *args)  #327 (line num in coconut source)


    def is_free_in(self, expr):  #329 (line num in coconut source)
        """Determine if self is free in expr."""  #330 (line num in coconut source)
        return expr == expr.substitute({self: self.prime()})  #331 (line num in coconut source)


    def find_unification(self, other):  #333 (line num in coconut source)
        if isinstance(other, Term):  #334 (line num in coconut source)
            return {self: other}  #335 (line num in coconut source)
        else:  #336 (line num in coconut source)
            return None  #337 (line num in coconut source)


_coconut_call_set_names(Var)  #339 (line num in coconut source)
Variable = Var  #339 (line num in coconut source)


class Const(Term):  #342 (line num in coconut source)
    """A variable quantified by an Exists."""  #343 (line num in coconut source)
    __slots__ = ()  #344 (line num in coconut source)

    def constant(self):  #346 (line num in coconut source)
        return self  #346 (line num in coconut source)


    @_coconut_tco  #348 (line num in coconut source)
    def __call__(self, *args):  #348 (line num in coconut source)
        return _coconut_tail_call(Func, self.name, *args)  #349 (line num in coconut source)


    def admits_empty_universe(self):  #351 (line num in coconut source)
        return False  #351 (line num in coconut source)


_coconut_call_set_names(Const)  #353 (line num in coconut source)
Constant = Const  #353 (line num in coconut source)


class Func(Term, FuncAtom):  #356 (line num in coconut source)
    """A function on terms."""  #357 (line num in coconut source)
    __slots__ = ()  #358 (line num in coconut source)

    @_coconut_tco  #360 (line num in coconut source)
    def substitute_elements(self, subs, **kwargs):  #360 (line num in coconut source)
        return _coconut_tail_call((Func), self.name, *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.args))  #361 (line num in coconut source)


    @_coconut_tco  #363 (line num in coconut source)
    def rename(self, name):  #363 (line num in coconut source)
        return _coconut_tail_call(self.__class__, name, *self.args)  #364 (line num in coconut source)


_coconut_call_set_names(Func)  #366 (line num in coconut source)
Function = Func  #366 (line num in coconut source)


class UnaryOp(Expr):  #369 (line num in coconut source)
    """Base class for unary operators."""  #370 (line num in coconut source)
    __slots__ = ("elem",)  #371 (line num in coconut source)

    def __init__(self, elem):  #373 (line num in coconut source)
        assert wff(elem), elem  #374 (line num in coconut source)
        self.elem = elem  #375 (line num in coconut source)


    def __repr__(self):  #377 (line num in coconut source)
        return self.__class__.__name__ + "(" + repr(self.elem) + ")"  #378 (line num in coconut source)


    def __eq__(self, other):  #380 (line num in coconut source)
        return isinstance(other, self.__class__) and self.elem == other.elem  #381 (line num in coconut source)


    def __str__(self):  #383 (line num in coconut source)
        return self.opstr + quote(self.elem)  #384 (line num in coconut source)


    def __len__(self):  #386 (line num in coconut source)
        return len(self.elem) + 1  #387 (line num in coconut source)


    @_coconut_tco  #389 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #389 (line num in coconut source)
        return _coconut_tail_call(self.__class__, self.elem.substitute(subs, **kwargs))  #390 (line num in coconut source)


    @_coconut_tco  #392 (line num in coconut source)
    def find_unification(self, other):  #392 (line num in coconut source)
        if isinstance(other, self.__class__):  #393 (line num in coconut source)
            return _coconut_tail_call(self.elem.find_unification, other.elem)  #394 (line num in coconut source)
        else:  #395 (line num in coconut source)
            __class__ = UnaryOp  #396 (line num in coconut source)

            return super().find_unification(other)  #396 (line num in coconut source)


    @_coconut_tco  #398 (line num in coconut source)
    def resolve(self, **kwargs):  #398 (line num in coconut source)
        return _coconut_tail_call(self.__class__(self.elem.resolve(**kwargs)).simplify, dnf=False, **kwargs)  #399 (line num in coconut source)



_coconut_call_set_names(UnaryOp)  #402 (line num in coconut source)
class Not(UnaryOp):  #402 (line num in coconut source)
    """Logical not."""  #403 (line num in coconut source)
    __slots__ = ()  #404 (line num in coconut source)
    opstr = not_sym  #405 (line num in coconut source)

    @property  #407 (line num in coconut source)
    def neg(self):  #408 (line num in coconut source)
        return self.elem  #408 (line num in coconut source)


    @_coconut_tco  #410 (line num in coconut source)
    def simplify(self, **kwargs):  #410 (line num in coconut source)
        if top == self.neg:  #411 (line num in coconut source)
            return bot  #412 (line num in coconut source)
        elif bot == self.neg:  #413 (line num in coconut source)
            return top  #414 (line num in coconut source)
        elif isinstance(self.neg, Not):  #415 (line num in coconut source)
            return _coconut_tail_call(self.neg.neg.simplify, **kwargs)  #416 (line num in coconut source)
        elif isinstance(self.neg, And):  #417 (line num in coconut source)
            return _coconut_tail_call(Or(*map(Not, self.neg.ands)).simplify, **kwargs)  #418 (line num in coconut source)
        elif isinstance(self.neg, Or):  #419 (line num in coconut source)
            return _coconut_tail_call(And(*map(Not, self.neg.ors)).simplify, **kwargs)  #420 (line num in coconut source)
        elif isinstance(self.neg, Imp):  #421 (line num in coconut source)
            ands = self.neg.conds + (Not(self.neg.concl),)  #422 (line num in coconut source)
            return _coconut_tail_call(And(*ands).simplify, **kwargs)  #423 (line num in coconut source)
        elif isinstance(self.neg, Exists):  #424 (line num in coconut source)
            return _coconut_tail_call(ForAll, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  #425 (line num in coconut source)
        elif isinstance(self.neg, ForAll):  #426 (line num in coconut source)
            return _coconut_tail_call(Exists, self.neg.var, Not(self.neg.elem).simplify(**kwargs))  #427 (line num in coconut source)
        else:  #428 (line num in coconut source)
            return _coconut_tail_call(Not, self.neg.simplify(**kwargs))  #429 (line num in coconut source)


    def contradicts(self, other, **kwargs):  #431 (line num in coconut source)
        return self.neg == other  #432 (line num in coconut source)


    @_coconut_tco  #434 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #434 (line num in coconut source)
        if isinstance(other, (Or, Eq)):  #435 (line num in coconut source)
            return _coconut_tail_call(other.resolve_against, self, **kwargs)  #436 (line num in coconut source)
        elif self.neg.find_unification(other) is not None:  #437 (line num in coconut source)
            return bot  #438 (line num in coconut source)
        else:  #439 (line num in coconut source)
            return None  #440 (line num in coconut source)


    @_coconut_tco  #442 (line num in coconut source)
    def admits_empty_universe(self):  #442 (line num in coconut source)
        if isinstance(self.neg, Atom):  #443 (line num in coconut source)
            return _coconut_tail_call(self.neg.admits_empty_universe)  #444 (line num in coconut source)
        else:  #445 (line num in coconut source)
            return not self.neg.admits_empty_universe()  #446 (line num in coconut source)



_coconut_call_set_names(Not)  #449 (line num in coconut source)
class Quantifier(Expr):  #449 (line num in coconut source)
    """Base class for logical quantifiers."""  #450 (line num in coconut source)
    __slots__ = ("var", "elem")  #451 (line num in coconut source)

    def __repr__(self):  #453 (line num in coconut source)
        return self.__class__.__name__ + '("' + str(self.var) + '", ' + repr(self.elem) + ")"  #454 (line num in coconut source)


    def __str__(self):  #456 (line num in coconut source)
        return self.opstr + " " + str(self.var) + ", " + quote(self.elem, in_quantifier=True)  #457 (line num in coconut source)


    def __len__(self):  #459 (line num in coconut source)
        return len(self.elem) + len(self.var)  #460 (line num in coconut source)


    @_coconut_tco  #462 (line num in coconut source)
    def change_var(self, var):  #462 (line num in coconut source)
        """Create an equivalent expression with a new quantified variable."""  #463 (line num in coconut source)
        return _coconut_tail_call(self.__class__, var, self.elem.substitute({self.var: var}))  #464 (line num in coconut source)


    @_coconut_tco  #466 (line num in coconut source)
    def change_elem(self, elem):  #466 (line num in coconut source)
        """Create an equivalent quantifier with a new expression."""  #467 (line num in coconut source)
        return _coconut_tail_call(self.__class__, self.var, elem)  #468 (line num in coconut source)


    def __eq__(self, other):  #470 (line num in coconut source)
        if isinstance(other, self.__class__):  #471 (line num in coconut source)
            return self.elem == other.change_var(self.var).elem  #472 (line num in coconut source)
        else:  #473 (line num in coconut source)
            return False  #474 (line num in coconut source)


    def inner_kwargs(self, kwargs):  #476 (line num in coconut source)
        inner_kwargs = kwargs.copy()  #477 (line num in coconut source)
        inner_kwargs["in_" + self.__class__.__name__.lower()] = True  #478 (line num in coconut source)
        return inner_kwargs  #479 (line num in coconut source)


    @_coconut_tco  #481 (line num in coconut source)
    def simplify(self, **kwargs):  #481 (line num in coconut source)
        return _coconut_tail_call(self.__class__(self.var, self.elem.simplify(**self.inner_kwargs(kwargs))).drop_quantifier, **kwargs)  #482 (line num in coconut source)


    @_coconut_tco  #484 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #484 (line num in coconut source)
        return _coconut_tail_call((self.change_elem), (self.elem.substitute)((rem_var)(self.var, subs), **kwargs))  #485 (line num in coconut source)


    @_coconut_tco  #487 (line num in coconut source)
    def make_free_in(self, other):  #487 (line num in coconut source)
        """Makes self free in other."""  #488 (line num in coconut source)
        var = self.var  #489 (line num in coconut source)
        newvar = var.prime()  #490 (line num in coconut source)
        while other != other.substitute({var: newvar}):  #491 (line num in coconut source)
            var, newvar = newvar, newvar.prime()  #492 (line num in coconut source)
        return _coconut_tail_call(self.change_var, var)  #493 (line num in coconut source)


    @_coconut_tco  #495 (line num in coconut source)
    def find_unification(self, other):  #495 (line num in coconut source)
        unif = self.elem.find_unification(other)  #496 (line num in coconut source)
        if unif is None:  #497 (line num in coconut source)
            return None  #498 (line num in coconut source)
        else:  #499 (line num in coconut source)
            return _coconut_tail_call((rem_var), self.var, unif)  #500 (line num in coconut source)


    @_coconut_tco  #502 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #502 (line num in coconut source)
        if isinstance(other, Quantifier):  #503 (line num in coconut source)
            resolution = (self.elem.resolve_against)(Not(other.elem).simplify(**kwargs), **kwargs)  #504 (line num in coconut source)
            if resolution is None:  #505 (line num in coconut source)
                return None  #506 (line num in coconut source)
            elif isinstance(other, ForAll):  # don't pull an Exists out of a ForAll  #507 (line num in coconut source)
                return _coconut_tail_call((other.change_elem), (self.change_elem)(resolution))  #508 (line num in coconut source)
            else:  #509 (line num in coconut source)
                return _coconut_tail_call((self.change_elem), (other.change_elem)(resolution))  #510 (line num in coconut source)
        else:  #511 (line num in coconut source)
            __class__ = Quantifier  #512 (line num in coconut source)

            return super().resolve_against(other, **kwargs)  #512 (line num in coconut source)

    @classmethod  #513 (line num in coconut source)

    @_coconut_tco  #515 (line num in coconut source)
    def blank(cls, elem):  #515 (line num in coconut source)
        """Make a quantifier without a variable."""  #516 (line num in coconut source)
        return _coconut_tail_call(cls(empty_var, elem).make_free_in, elem)  #517 (line num in coconut source)



_coconut_call_set_names(Quantifier)  #520 (line num in coconut source)
class ForAll(Quantifier):  #520 (line num in coconut source)
    """Universal quantifier."""  #521 (line num in coconut source)
    __slots__ = ()  #522 (line num in coconut source)
    opstr = forall_sym  #523 (line num in coconut source)

    def __init__(self, var, elem):  #525 (line num in coconut source)
        assert wff(elem), elem  #526 (line num in coconut source)
        if isinstance(var, str):  #527 (line num in coconut source)
            var = Const(var)  #528 (line num in coconut source)
        assert isvar(var), var  #529 (line num in coconut source)
        self.var = var.variable()  #530 (line num in coconut source)
        self.elem = elem.substitute({var: self.var.variable()})  #531 (line num in coconut source)


    @_coconut_tco  #533 (line num in coconut source)
    def resolve(self, **kwargs):  #533 (line num in coconut source)
        inner_kwargs = self.inner_kwargs(kwargs)  #534 (line num in coconut source)
        inner_kwargs["variables"] = kwargs.get("variables", ()) + (self.var,)  #535 (line num in coconut source)
        return _coconut_tail_call(ForAll(self.var, self.elem.resolve(**inner_kwargs)).simplify, dnf=False, **kwargs)  #536 (line num in coconut source)


    def drop_quantifier(self, nonempty_universe=True, in_forall=False, **kwargs):  #538 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["in_forall"] = nonempty_universe, in_forall  #539 (line num in coconut source)
        if not nonempty_universe and not in_forall:  #540 (line num in coconut source)
            elem = self.elem  #541 (line num in coconut source)
            while isinstance(elem, Exists):  #542 (line num in coconut source)
                elem = elem.elem  #543 (line num in coconut source)
            if top == elem:  #544 (line num in coconut source)
                return elem  #545 (line num in coconut source)
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):  #546 (line num in coconut source)
            return self.elem  #547 (line num in coconut source)
        return self  #548 (line num in coconut source)


_coconut_call_set_names(ForAll)  #550 (line num in coconut source)
FA = ForAll  #550 (line num in coconut source)


class Exists(Quantifier):  #553 (line num in coconut source)
    """Existential quantifier."""  #554 (line num in coconut source)
    __slots__ = ()  #555 (line num in coconut source)
    opstr = exists_sym  #556 (line num in coconut source)

    def __init__(self, var, elem):  #558 (line num in coconut source)
        assert wff(elem), elem  #559 (line num in coconut source)
        if isinstance(var, str):  #560 (line num in coconut source)
            var = Const(var)  #561 (line num in coconut source)
        assert isvar(var), var  #562 (line num in coconut source)
        self.var = var.constant()  #563 (line num in coconut source)
        self.elem = elem.substitute({var: self.var.constant()})  #564 (line num in coconut source)


    @_coconut_tco  #566 (line num in coconut source)
    def resolve(self, **kwargs):  #566 (line num in coconut source)
        inner_kwargs = self.inner_kwargs(kwargs)  #567 (line num in coconut source)
        skolem_args = inner_kwargs.get("variables")  #568 (line num in coconut source)
        if skolem_args is None:  #569 (line num in coconut source)
            skolem_elem = self.elem  #570 (line num in coconut source)
        else:  #571 (line num in coconut source)
            skolem_var = Func(self.var.name, *skolem_args)  #572 (line num in coconut source)
            skolem_elem = self.elem.substitute({self.var: skolem_var})  #573 (line num in coconut source)
        return _coconut_tail_call(Exists(self.var, skolem_elem.resolve(**inner_kwargs)).simplify, dnf=False, **kwargs)  #574 (line num in coconut source)


    def drop_quantifier(self, nonempty_universe=True, in_exists=False, **kwargs):  #576 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["in_exists"] = nonempty_universe, in_exists  #577 (line num in coconut source)
        if not nonempty_universe and not in_exists:  #578 (line num in coconut source)
            elem = self.elem  #579 (line num in coconut source)
            while isinstance(elem, ForAll):  #580 (line num in coconut source)
                elem = elem.elem  #581 (line num in coconut source)
            if bot == elem:  #582 (line num in coconut source)
                return elem  #583 (line num in coconut source)
        elif self.elem == self.elem.substitute({self.var: self.var.prime()}):  #584 (line num in coconut source)
            return self.elem  #585 (line num in coconut source)
        return self  #586 (line num in coconut source)


    def admits_empty_universe(self):  #588 (line num in coconut source)
        return False  #588 (line num in coconut source)


_coconut_call_set_names(Exists)  #590 (line num in coconut source)
TE = Exists  #590 (line num in coconut source)


class BinaryOp(Expr):  #593 (line num in coconut source)
    """Base class for binary operators."""  #594 (line num in coconut source)
    __slots__ = ("elems",)  #595 (line num in coconut source)
    identity = None  #596 (line num in coconut source)

    def __new__(cls, *elems):  #598 (line num in coconut source)
        if not elems:  #599 (line num in coconut source)
            if cls.identity is None:  #600 (line num in coconut source)
                raise TypeError(cls.__name__ + " requires at least one argument")  #601 (line num in coconut source)
            else:  #602 (line num in coconut source)
                return cls.identity  #603 (line num in coconut source)
        elif len(elems) == 1:  #604 (line num in coconut source)
            assert wff(elems[0]), elems[0]  #605 (line num in coconut source)
            return elems[0]  # sometimes returns an instance of cls  #606 (line num in coconut source)
        else:  #607 (line num in coconut source)
            __class__ = BinaryOp  #608 (line num in coconut source)

            return super().__new__(cls)  #608 (line num in coconut source)


    def __init__(self, *elems):  #610 (line num in coconut source)
        if len(elems) > 1:  # __new__ should handle all other cases  #611 (line num in coconut source)
            assert len(elems) >= 2, elems  #612 (line num in coconut source)
            for x in elems:  #613 (line num in coconut source)
                assert wff(x), x  #614 (line num in coconut source)
            self.elems = elems  #615 (line num in coconut source)


    def __repr__(self):  #617 (line num in coconut source)
        return self.__class__.__name__ + "(" + ", ".join((repr(x) for x in self.elems)) + ")"  #618 (line num in coconut source)


    @_coconut_tco  #620 (line num in coconut source)
    def __str__(self):  #620 (line num in coconut source)
        return _coconut_tail_call((" " + self.opstr + " ").join, (quote(x) for x in self.elems))  #621 (line num in coconut source)


    def __len__(self):  #623 (line num in coconut source)
        return sum(map(len, self.elems)) + 1  #624 (line num in coconut source)


    @_coconut_tco  #626 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #626 (line num in coconut source)
        return _coconut_tail_call((self.__class__), *(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.elems))  #627 (line num in coconut source)


    @_coconut_tco  #629 (line num in coconut source)
    def resolve(self, **kwargs):  #629 (line num in coconut source)
        elems = (map)(_coconut.operator.methodcaller("resolve", **kwargs), self.elems)  #630 (line num in coconut source)
        return _coconut_tail_call(self.__class__(*elems).simplify, dnf=False, **kwargs)  #631 (line num in coconut source)



_coconut_call_set_names(BinaryOp)  #634 (line num in coconut source)
class Imp(BinaryOp):  #634 (line num in coconut source)
    """Logical implication."""  #635 (line num in coconut source)
    __slots__ = ()  #636 (line num in coconut source)
    opstr = imp_sym  #637 (line num in coconut source)

    @_coconut_tco  #639 (line num in coconut source)
    def __rshift__(self, other):  #639 (line num in coconut source)
        if isinstance(other, Imp):  #640 (line num in coconut source)
            return _coconut_tail_call(Imp, self, *other.elems)  #641 (line num in coconut source)
        else:  #642 (line num in coconut source)
            return _coconut_tail_call(Imp, self, other)  #643 (line num in coconut source)


    @_coconut_tco  #645 (line num in coconut source)
    def __lshift__(self, other):  #645 (line num in coconut source)
        return _coconut_tail_call((Imp), *(other,) + self.elems)  #646 (line num in coconut source)


    @property  #648 (line num in coconut source)
    def conds(self):  #649 (line num in coconut source)
        return self.elems[:-1]  #649 (line num in coconut source)


    @property  #651 (line num in coconut source)
    def concl(self):  #652 (line num in coconut source)
        return self.elems[-1]  #652 (line num in coconut source)


    def __eq__(self, other):  #654 (line num in coconut source)
        return isinstance(other, self.__class__) and self.concl == other.concl and (unorderd_eq)(self.conds, other.conds)  #655 (line num in coconut source)


    @_coconut_tco  #657 (line num in coconut source)
    def to_or(self):  #657 (line num in coconut source)
        ors = tuple(map(Not, self.conds)) + (self.concl,)  #658 (line num in coconut source)
        return _coconut_tail_call(Or, *ors)  #659 (line num in coconut source)


    @_coconut_tco  #661 (line num in coconut source)
    def simplify(self, **kwargs):  #661 (line num in coconut source)
        return _coconut_tail_call(self.to_or().simplify, **kwargs)  #662 (line num in coconut source)


    @_coconut_tco  #664 (line num in coconut source)
    def admits_empty_universe(self):  #664 (line num in coconut source)
        return _coconut_tail_call(self.to_or().admits_empty_universe)  #665 (line num in coconut source)


_coconut_call_set_names(Imp)  #667 (line num in coconut source)
Implies = Imp  #667 (line num in coconut source)


class BoolOp(BinaryOp):  #670 (line num in coconut source)
    """Base class for Or and And."""  #671 (line num in coconut source)
    __slots__ = ()  #672 (line num in coconut source)

    def __eq__(self, other):  #674 (line num in coconut source)
        return isinstance(other, self.__class__) and (unorderd_eq)(self.elems, other.elems)  #675 (line num in coconut source)


    def simplify(self, **kwargs):  #677 (line num in coconut source)
        elems = (map)(_coconut.operator.methodcaller("simplify", **kwargs), self.merge().elems)  #678 (line num in coconut source)
        out = self.__class__(*elems).clean()  #679 (line num in coconut source)
        if isinstance(out, self.__class__):  #680 (line num in coconut source)
            out = out.distribute(**kwargs)  #681 (line num in coconut source)
        if isinstance(out, self.__class__):  #682 (line num in coconut source)
            out = out.merge().dedupe()  #683 (line num in coconut source)
        if isinstance(out, self.__class__):  #684 (line num in coconut source)
            out = out.inner_simplify(**kwargs)  #685 (line num in coconut source)
        if isinstance(out, self.__class__):  #686 (line num in coconut source)
            out = out.prenex(**kwargs)  #687 (line num in coconut source)
        log_simplification(self, out, **kwargs)  #688 (line num in coconut source)
        return out  #689 (line num in coconut source)


    @_coconut_tco  #691 (line num in coconut source)
    def merge(self):  #691 (line num in coconut source)
        """Merges nested copies of a boolean operator."""  #692 (line num in coconut source)
        elems = []  #693 (line num in coconut source)
        for x in self.elems:  #694 (line num in coconut source)
            if isinstance(x, self.__class__):  #695 (line num in coconut source)
                elems.extend(x.merge().elems)  #696 (line num in coconut source)
            else:  #697 (line num in coconut source)
                elems.append(x)  #698 (line num in coconut source)
        return _coconut_tail_call(self.__class__, *elems)  #699 (line num in coconut source)


    @_coconut_tco  #701 (line num in coconut source)
    def dedupe(self):  #701 (line num in coconut source)
        """Removes duplicate elements from a boolean operator."""  #702 (line num in coconut source)
        elems = []  #703 (line num in coconut source)
        for x in self.elems:  #704 (line num in coconut source)
            if x not in elems:  #705 (line num in coconut source)
                elems.append(x)  #706 (line num in coconut source)
        return _coconut_tail_call(self.__class__, *elems)  #707 (line num in coconut source)


    @_coconut_tco  #709 (line num in coconut source)
    def clean(self):  #709 (line num in coconut source)
        """Removes copies of the identity."""  #710 (line num in coconut source)
        return _coconut_tail_call((self.__class__), *(filter)(_coconut.functools.partial((_coconut.operator.ne), self.identity), self.elems))  #711 (line num in coconut source)


    def prenex(self, **kwargs):  #713 (line num in coconut source)
        """Pulls quantifiers out."""  #714 (line num in coconut source)
        for i, x in enumerate(self.elems):  #715 (line num in coconut source)
            if isinstance(x, Quantifier) and self.can_prenex(x, **kwargs):  #716 (line num in coconut source)
                elems = self.elems[:i] + self.elems[i + 1:]  #717 (line num in coconut source)
                free_x = x.make_free_in(self.__class__(*elems))  #718 (line num in coconut source)
                elems += (free_x.elem,)  #719 (line num in coconut source)
                return free_x.change_elem(self.__class__(*elems)).simplify(**kwargs)  #720 (line num in coconut source)
        return self  #721 (line num in coconut source)



_coconut_call_set_names(BoolOp)  #724 (line num in coconut source)
class Or(BoolOp):  #724 (line num in coconut source)
    """Logical disjunction."""  #725 (line num in coconut source)
    __slots__ = ()  #726 (line num in coconut source)
    opstr = or_sym  #727 (line num in coconut source)
    identity = bot  #728 (line num in coconut source)

    @_coconut_tco  #730 (line num in coconut source)
    def __or__(self, other):  #730 (line num in coconut source)
        return _coconut_tail_call((Or), *self.elems + (other,))  #731 (line num in coconut source)


    @property  #733 (line num in coconut source)
    def ors(self):  #734 (line num in coconut source)
        return self.elems  #734 (line num in coconut source)


    def distribute(self, dnf=False, **kwargs):  #736 (line num in coconut source)
        """If this Or contains an And, distribute into it."""  #737 (line num in coconut source)
        kwargs["dnf"] = dnf  #738 (line num in coconut source)
        if not dnf:  #739 (line num in coconut source)
            for i, x in enumerate(self.ors):  #740 (line num in coconut source)
                if isinstance(x, And):  #741 (line num in coconut source)
                    ands = ((Or)(*(y,) + self.ors[:i] + self.ors[i + 1:]) for y in x.ands)  #742 (line num in coconut source)
                    return And(*ands).simplify(**kwargs)  #743 (line num in coconut source)
        return self  #744 (line num in coconut source)


    def inner_simplify(self, nonempty_universe=True, **kwargs):  #746 (line num in coconut source)
        """Determines if the Or is a blatant tautology."""  #747 (line num in coconut source)
        kwargs["nonempty_universe"] = nonempty_universe  #748 (line num in coconut source)
        for i, x in enumerate(self.ors):  #749 (line num in coconut source)
            if top == x:  #750 (line num in coconut source)
                return x  #751 (line num in coconut source)
            for y in self.ors[i + 1:]:  #752 (line num in coconut source)
                if x.contradicts(y, **kwargs):  #753 (line num in coconut source)
                    if not nonempty_universe and not self.admits_empty_universe():  #754 (line num in coconut source)
                        return Exists.blank(top)  #755 (line num in coconut source)
                    else:  #756 (line num in coconut source)
                        return top  #757 (line num in coconut source)
        return self  #758 (line num in coconut source)


    def can_prenex(self, other, nonempty_universe=True, in_forall=False, **kwargs):  #760 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["in_forall"] = nonempty_universe, in_forall  #761 (line num in coconut source)
        return (nonempty_universe or in_forall or not isinstance(other, Exists) or not self.admits_empty_universe())  #762 (line num in coconut source)


    @_coconut_tco  #767 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #767 (line num in coconut source)
        if isinstance(other, Eq):  #768 (line num in coconut source)
            return _coconut_tail_call(other.resolve_against, self)  #769 (line num in coconut source)
        elif isinstance(other, Or):  #770 (line num in coconut source)
            not_other_ors = (map)(_coconut.operator.methodcaller("simplify", **kwargs), (map)(Not, other.ors))  #771 (line num in coconut source)
            for i, x in enumerate(self.ors):  #772 (line num in coconut source)
                if isinstance(x, Eq):  #773 (line num in coconut source)
                    resolved_other = (x.paramodulant)(other)  #774 (line num in coconut source)
                    return (Or)(*self.ors[:i] + self.ors[i + 1:] + resolved_other.ors)  #775 (line num in coconut source)
                for j, y in enumerate(not_other_ors):  #776 (line num in coconut source)
                    if isinstance(other.ors[j], Eq):  #777 (line num in coconut source)
                        y = other.ors[j]  #778 (line num in coconut source)
                        resolved_self = (y.paramodulant)(self)  #779 (line num in coconut source)
                        return (Or)(*other.ors[:j] + other.ors[j + 1:] + resolved_self.ors)  #780 (line num in coconut source)
                    subs = x.find_unification(y)  #781 (line num in coconut source)
                    if subs is not None:  #782 (line num in coconut source)
                        return (Or)(*(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.ors[:i] + self.ors[i + 1:] + other.ors[:j] + other.ors[j + 1:]))  #783 (line num in coconut source)
        else:  #784 (line num in coconut source)
            not_other = Not(other).simplify(**kwargs)  #785 (line num in coconut source)
            for i, x in enumerate(self.ors):  #786 (line num in coconut source)
                if isinstance(x, Eq):  #787 (line num in coconut source)
                    return (x.paramodulant)((Or)(*self.ors[:i] + self.ors[i + 1:]))  #788 (line num in coconut source)
                subs = x.find_unification(not_other)  #789 (line num in coconut source)
                if subs is not None:  #790 (line num in coconut source)
                    return (Or)(*(map)(_coconut.operator.methodcaller("substitute", subs, **kwargs), self.ors[:i] + self.ors[i + 1:]))  #791 (line num in coconut source)
        return None  #792 (line num in coconut source)


    @_coconut_tco  #794 (line num in coconut source)
    def admits_empty_universe(self):  #794 (line num in coconut source)
        return _coconut_tail_call(any, (x.admits_empty_universe() for x in self.elems))  #795 (line num in coconut source)



_coconut_call_set_names(Or)  #798 (line num in coconut source)
class And(BoolOp):  #798 (line num in coconut source)
    """Logical conjunction."""  #799 (line num in coconut source)
    __slots__ = ()  #800 (line num in coconut source)
    opstr = and_sym  #801 (line num in coconut source)
    identity = top  #802 (line num in coconut source)

    @_coconut_tco  #804 (line num in coconut source)
    def __and__(self, other):  #804 (line num in coconut source)
        return _coconut_tail_call((And), *self.elems + (other,))  #805 (line num in coconut source)


    @property  #807 (line num in coconut source)
    def ands(self):  #808 (line num in coconut source)
        return self.elems  #808 (line num in coconut source)


    def distribute(self, dnf=False, **kwargs):  #810 (line num in coconut source)
        """If this And contains an Or, distribute into it."""  #811 (line num in coconut source)
        kwargs["dnf"] = dnf  #812 (line num in coconut source)
        if dnf:  #813 (line num in coconut source)
            for i, x in enumerate(self.ands):  #814 (line num in coconut source)
                if isinstance(x, Or):  #815 (line num in coconut source)
                    ors = ((And)(*(y,) + self.ands[:i] + self.ands[i + 1:]) for y in x.ors)  #816 (line num in coconut source)
                    return Or(*ors).simplify(**kwargs)  #817 (line num in coconut source)
        return self  #818 (line num in coconut source)


    def inner_simplify(self, nonempty_universe=True, **kwargs):  #820 (line num in coconut source)
        """Determines if the And is a blatant contradiction."""  #821 (line num in coconut source)
        kwargs["nonempty_universe"] = nonempty_universe  #822 (line num in coconut source)
        for i, x in enumerate(self.ands):  #823 (line num in coconut source)
            if bot == x:  #824 (line num in coconut source)
                return x  #825 (line num in coconut source)
            for y in self.ands[i + 1:]:  #826 (line num in coconut source)
                if x.contradicts(y, **kwargs):  #827 (line num in coconut source)
                    if not nonempty_universe and self.admits_empty_universe():  #828 (line num in coconut source)
                        return ForAll.blank(bot)  #829 (line num in coconut source)
                    else:  #830 (line num in coconut source)
                        return bot  #831 (line num in coconut source)
        return self  #832 (line num in coconut source)


    def can_prenex(self, other, nonempty_universe=True, in_exists=False, **kwargs):  #834 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["in_exists"] = nonempty_universe, in_exists  #835 (line num in coconut source)
        return (nonempty_universe or in_exists or not isinstance(other, ForAll) or all((isinstance(x, ForAll) for x in self.elems)))  #836 (line num in coconut source)


    @_coconut_tco  #841 (line num in coconut source)
    def resolve(self, nonempty_universe=True, just_skolemize=False, debug=False, **kwargs):  #841 (line num in coconut source)
        """Performs all possible resolutions within the And."""  #842 (line num in coconut source)
        kwargs["nonempty_universe"], kwargs["just_skolemize"], kwargs["debug"] = nonempty_universe, just_skolemize, debug  #843 (line num in coconut source)
        __class__ = And  #844 (line num in coconut source)

        resolved = super().resolve(**kwargs)  #844 (line num in coconut source)
        log_simplification(self, resolved, **kwargs)  #845 (line num in coconut source)
        if not isinstance(resolved, And) or just_skolemize:  #846 (line num in coconut source)
            return resolved  #847 (line num in coconut source)
        clauses = (list)(resolved.ands)  #848 (line num in coconut source)
        quantifiers = []  #849 (line num in coconut source)
        if not nonempty_universe and not self.admits_empty_universe():  #850 (line num in coconut source)
            blank = Exists.blank(top)  #851 (line num in coconut source)
            (quantifiers.append)(blank.change_elem)  #852 (line num in coconut source)
            kwargs = (blank.inner_kwargs)(kwargs)  #853 (line num in coconut source)
        prev_clause_len = 1  #854 (line num in coconut source)
        while prev_clause_len < len(clauses):  #855 (line num in coconut source)
            prev_clause_len = len(clauses)  #856 (line num in coconut source)
# reversed ensures conclusions get tested first
            for i in (reversed)(range(1, len(clauses))):  #858 (line num in coconut source)
                x = clauses[i]  #859 (line num in coconut source)
                for y in clauses[:i + 1]:  # allow resolution of a clause against itself  #860 (line num in coconut source)
                    resolution = x.resolve_against(y)  #861 (line num in coconut source)
                    if resolution is not None:  #862 (line num in coconut source)
                        resolution = resolution.simplify(dnf=False, **kwargs)  #863 (line num in coconut source)
                        log_resolution(x, y, resolution, **kwargs)  #864 (line num in coconut source)
                        new_quantifiers = []  #865 (line num in coconut source)
                        inner_kwargs = kwargs  #866 (line num in coconut source)
                        while isinstance(resolution, Quantifier) and self.can_prenex(resolution, **kwargs):  #867 (line num in coconut source)
                            (new_quantifiers.append)(resolution.change_elem)  #868 (line num in coconut source)
                            inner_kwargs = (resolution.inner_kwargs)(inner_kwargs)  #869 (line num in coconut source)
                            resolution = resolution.elem  #870 (line num in coconut source)
                        if isinstance(resolution, And):  #871 (line num in coconut source)
                            new_clauses = resolution.ands  #872 (line num in coconut source)
                        else:  #873 (line num in coconut source)
                            new_clauses = (resolution,)  #874 (line num in coconut source)
                        novel = False  #875 (line num in coconut source)
                        for new_clause in new_clauses:  #876 (line num in coconut source)
                            if new_clause == bot:  #877 (line num in coconut source)
                                clauses = [bot,]  #878 (line num in coconut source)
                                novel = True  #879 (line num in coconut source)
                                break  #880 (line num in coconut source)
                            elif new_clause != top and new_clause not in clauses:  #881 (line num in coconut source)
                                clauses.append(new_clause)  #882 (line num in coconut source)
                                novel = True  #883 (line num in coconut source)
                        if novel:  #884 (line num in coconut source)
                            quantifiers.extend(new_quantifiers)  #885 (line num in coconut source)
                            kwargs = inner_kwargs  #886 (line num in coconut source)
                            if clauses == [bot,]:  #887 (line num in coconut source)
                                break  #888 (line num in coconut source)
                if clauses == [bot,]:  #889 (line num in coconut source)
                    break  #890 (line num in coconut source)
        resolved = (reduce)(_coconut_pipe, [And(*clauses),] + quantifiers)  #891 (line num in coconut source)
        log_simplification(self, resolved, **kwargs)  #892 (line num in coconut source)
        return _coconut_tail_call(resolved.simplify, dnf=False, **kwargs)  #893 (line num in coconut source)


    @_coconut_tco  #895 (line num in coconut source)
    def admits_empty_universe(self):  #895 (line num in coconut source)
        return _coconut_tail_call(all, (x.admits_empty_universe() for x in self.elems))  #896 (line num in coconut source)



_coconut_call_set_names(And)  #899 (line num in coconut source)
class Eq(Expr):  #899 (line num in coconut source)
    """Equality operator."""  #900 (line num in coconut source)
    __slots__ = ("a", "b")  #901 (line num in coconut source)

    def __init__(self, a, b):  #903 (line num in coconut source)
        assert isinstance(a, Term), a  #904 (line num in coconut source)
        assert isinstance(b, Term), b  #905 (line num in coconut source)
        self.a, self.b = a, b  #906 (line num in coconut source)


    def __repr__(self):  #908 (line num in coconut source)
        return "Eq(" + repr(self.a) + ", " + repr(self.b) + ")"  #909 (line num in coconut source)


    def __str__(self):  #911 (line num in coconut source)
        return str(self.a) + "=" + str(self.b)  #912 (line num in coconut source)


    def __eq__(self, other):  #914 (line num in coconut source)
        return isinstance(other, Eq) and (self.a == other.a and self.b == other.b or self.a == other.b and self.b == other.a)  #915 (line num in coconut source)


    def simplify(self, **kwargs):  #917 (line num in coconut source)
        if self.a == self.b:  #918 (line num in coconut source)
            return top  #919 (line num in coconut source)
        else:  #920 (line num in coconut source)
            return self  #921 (line num in coconut source)


    @_coconut_tco  #923 (line num in coconut source)
    def swap(self):  #923 (line num in coconut source)
        """Swaps the order of equality."""  #924 (line num in coconut source)
        return _coconut_tail_call(Eq, self.b, self.a)  #925 (line num in coconut source)


    def find_unification(self, other):  #927 (line num in coconut source)
        if isinstance(other, Eq):  #928 (line num in coconut source)
            a_a = self.a.find_unification(other.a)  #929 (line num in coconut source)
            b_b = self.b.find_unification(other.b)  #930 (line num in coconut source)
            if a_a is not None and b_b is not None:  #931 (line num in coconut source)
                subs = merge_dicts(a_a, b_b)  #932 (line num in coconut source)
                if subs is not None:  #933 (line num in coconut source)
                    return subs  #934 (line num in coconut source)
            a_b = self.a.find_unification(other.a)  #935 (line num in coconut source)
            b_a = self.b.find_unification(other.b)  #936 (line num in coconut source)
            if a_b is not None and b_a is not None:  #937 (line num in coconut source)
                subs = merge_dicts(a_b, b_a)  #938 (line num in coconut source)
                if subs is not None:  #939 (line num in coconut source)
                    return subs  #940 (line num in coconut source)
        else:  #941 (line num in coconut source)
            __class__ = Eq  #942 (line num in coconut source)

            return super().find_unification(other)  #942 (line num in coconut source)


    @_coconut_tco  #944 (line num in coconut source)
    def substitute(self, subs, **kwargs):  #944 (line num in coconut source)
        return _coconut_tail_call(Eq, self.a.substitute(subs, **kwargs), self.b.substitute(subs, **kwargs))  #945 (line num in coconut source)


    @_coconut_tco  #947 (line num in coconut source)
    def paramodulant(self, other):  #947 (line num in coconut source)
        """Create a paramodulant of other."""  #948 (line num in coconut source)
        return _coconut_tail_call((sub_once), other, {self.a: self.b, self.b: self.a})  #949 (line num in coconut source)


    @_coconut_tco  #951 (line num in coconut source)
    def resolve_against(self, other, **kwargs):  #951 (line num in coconut source)
        if isinstance(other, Not) and self.find_unification(other.neg) is not None:  #952 (line num in coconut source)
            return bot  #953 (line num in coconut source)
        else:  #954 (line num in coconut source)
            return _coconut_tail_call(self.paramodulant, other)  #955 (line num in coconut source)


    def admits_empty_universe(self):  #957 (line num in coconut source)
        return self.a.admits_empty_universe() and self.b.admits_empty_universe()  #958 (line num in coconut source)


_coconut_call_set_names(Eq)  #960 (line num in coconut source)
Equals = Eq  #960 (line num in coconut source)
