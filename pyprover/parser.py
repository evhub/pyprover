#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x8462840b

# Compiled with Coconut version 3.2.0-post_dev19
# This file was compiled from parser.coco by the Coconut compiler; edit that file rather than this one.
# For a guide to writing Coconut, see http://coconut.readthedocs.io/en/develop/llms.txt (or run 'coconut --ai-docs').

"""A parser for formulas written in standard mathematical notation."""

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop, annotations
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev19', '39', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get('__coconut__')
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules['_coconut_cached__coconut__'] = _coconut_cached__coconut__
        del _coconut_sys.modules['__coconut__']
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and _coconut_os.path.exists(_coconut_os.path.join(_coconut_file_dir, "__init__.py")):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == '__coconut__':  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == '__coconut__':  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning, _coconut_lazy_module, _coconut_lazy_get, _coconut_type, _coconut_assert_msg
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and '__coconut_cache__' in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != '__coconut_cache__':
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------



# Imports:

import re  #5 (line in Coconut source)

from pyprover.constants import all_top_syms  #7 (line in Coconut source)
from pyprover.constants import all_bot_syms  #7 (line in Coconut source)
from pyprover.constants import all_not_syms  #7 (line in Coconut source)
from pyprover.constants import all_imp_syms  #7 (line in Coconut source)
from pyprover.constants import all_iff_syms  #7 (line in Coconut source)
from pyprover.constants import all_and_syms  #7 (line in Coconut source)
from pyprover.constants import all_or_syms  #7 (line in Coconut source)
from pyprover.constants import all_eq_syms  #7 (line in Coconut source)
from pyprover.constants import all_neq_syms  #7 (line in Coconut source)
from pyprover.constants import all_forall_syms  #7 (line in Coconut source)
from pyprover.constants import all_exists_syms  #7 (line in Coconut source)
from pyprover.logic import top  #20 (line in Coconut source)
from pyprover.logic import bot  #20 (line in Coconut source)
from pyprover.logic import Prop  #20 (line in Coconut source)
from pyprover.logic import Pred  #20 (line in Coconut source)
from pyprover.logic import Eq  #20 (line in Coconut source)
from pyprover.logic import Not  #20 (line in Coconut source)
from pyprover.logic import And  #20 (line in Coconut source)
from pyprover.logic import Or  #20 (line in Coconut source)
from pyprover.logic import Imp  #20 (line in Coconut source)
from pyprover.logic import Iff  #20 (line in Coconut source)
from pyprover.logic import ForAll  #20 (line in Coconut source)
from pyprover.logic import Exists  #20 (line in Coconut source)
from pyprover.logic import Const  #20 (line in Coconut source)
from pyprover.logic import Var  #20 (line in Coconut source)
from pyprover.logic import Func  #20 (line in Coconut source)


# Tokens:

class ParseError(ValueError):  #41 (line in Coconut source)
    """Raised when a formula can't be parsed."""  #42 (line in Coconut source)

class Token(_coconut.typing.NamedTuple("Token", [("kind", 'str'), ("text", 'str'), ("pos", 'int')])):  #44 (line in Coconut source)
    __slots__ = ()  #44 (line in Coconut source)
    _coconut_is_data = True  #44 (line in Coconut source)
    __match_args__ = ('kind', 'text', 'pos')  #44 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #44 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #44 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #44 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #44 (line in Coconut source)
    def __eq__(self, other):  #44 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #44 (line in Coconut source)
    def __hash__(self):  #44 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #44 (line in Coconut source)


punctuation = "(", ")", ",", ".", ":", "?"  #46 (line in Coconut source)

# every symbol that isn't a word, longest first so that e.g. "->" beats "-"
operator_syms = (sorted)((filter)(lambda s: not re.fullmatch(r"\w+", s), (all_top_syms + all_bot_syms + all_not_syms + all_imp_syms + all_iff_syms + all_and_syms + all_or_syms + all_eq_syms + all_neq_syms + punctuation + ("∀", "∃"))), key=len, reverse=True)  #49 (line in Coconut source)

word_ops = {sym: kind for kind, syms in [("top", all_top_syms), ("bot", all_bot_syms), ("not", all_not_syms), ("imp", all_imp_syms), ("iff", all_iff_syms), ("and", all_and_syms), ("or", all_or_syms)] for sym in syms if re.fullmatch(r"\w+", sym)}  #55 (line in Coconut source)

sym_kinds = {sym: kind for kind, syms in [("top", all_top_syms), ("bot", all_bot_syms), ("not", all_not_syms), ("imp", all_imp_syms), ("iff", all_iff_syms), ("and", all_and_syms), ("or", all_or_syms), ("eq", all_eq_syms), ("neq", all_neq_syms), ("forall", ("∀",)), ("exists", ("∃",))] for sym in syms} | {p: p for p in punctuation}  #70 (line in Coconut source)

token_regex = re.compile(r"\s*(?:(?P<op>" + "|".join(map(re.escape, operator_syms)) + r")|(?P<name>\w+'*))")  #88 (line in Coconut source)

def tokenize(text) -> list:  #92 (line in Coconut source)
    """Split text into tokens."""  #93 (line in Coconut source)
    tokens = []  #94 (line in Coconut source)
    pos = 0  #95 (line in Coconut source)
    text = text.rstrip()  #96 (line in Coconut source)
    while pos < len(text):  #97 (line in Coconut source)
        match_ = token_regex.match(text, pos)  #98 (line in Coconut source)
        if not match_:  #99 (line in Coconut source)
            raise ParseError(error_message(text, pos + len(text[pos:]) - len(text[pos:].lstrip()), "unexpected character"))  #100 (line in Coconut source)
        start = match_.start(match_.lastgroup)  #101 (line in Coconut source)
        if match_.lastgroup == "op":  #102 (line in Coconut source)
            tokens.append(Token(sym_kinds[match_.group("op")], match_.group("op"), start))  #103 (line in Coconut source)
        else:  #104 (line in Coconut source)
            name = match_.group("name")  #105 (line in Coconut source)
            tokens.append(Token(word_ops.get(name, "name"), name, start))  #106 (line in Coconut source)
        pos = match_.end()  #107 (line in Coconut source)
    return tokens  #108 (line in Coconut source)


def error_message(text, pos, msg) -> str:  #110 (line in Coconut source)
    return "{_coconut_format_0} at position {_coconut_format_1}:\n  {_coconut_format_2}\n  {_coconut_format_3}^".format(_coconut_format_0=(msg), _coconut_format_1=(pos), _coconut_format_2=(text), _coconut_format_3=(' ' * pos))  #111 (line in Coconut source)


# Parser:


forall_words = {s for s in all_forall_syms if re.fullmatch(r"\w+", s)}  #116 (line in Coconut source)
exists_words = {s for s in all_exists_syms if re.fullmatch(r"\w+", s)}  #117 (line in Coconut source)

def is_upper(name):  #119 (line in Coconut source)
    return name[0].isupper()  #119 (line in Coconut source)


class Parser():  #121 (line in Coconut source)
    """A recursive descent parser for formulas. Precedence, from loosest to
    tightest: quantifiers (which extend as far right as possible), ↔, →
    (right associative), ∨, ∧, ¬, then atoms."""  #124 (line in Coconut source)

    def __init__(self, text):  #126 (line in Coconut source)
        self.text = text  #127 (line in Coconut source)
        self.tokens = tokenize(text)  #128 (line in Coconut source)
        self.index = 0  #129 (line in Coconut source)


    def peek(self, offset=0):  #131 (line in Coconut source)
        i = self.index + offset  #132 (line in Coconut source)
        return self.tokens[i] if i < len(self.tokens) else Token("end", "", len(self.text))  #133 (line in Coconut source)


    def advance(self):  #135 (line in Coconut source)
        token = self.peek()  #136 (line in Coconut source)
        self.index += 1  #137 (line in Coconut source)
        return token  #138 (line in Coconut source)


    def error(self, msg, token=None):  #140 (line in Coconut source)
        token = (self.peek() if token is None else token)  #141 (line in Coconut source)
        found = repr(token.text) if token.kind != "end" else "end of input"  #142 (line in Coconut source)
        raise ParseError(error_message(self.text, token.pos, "{_coconut_format_0} (found {_coconut_format_1})".format(_coconut_format_0=(msg), _coconut_format_1=(found))))  #143 (line in Coconut source)


    def expect(self, *kinds):  #145 (line in Coconut source)
        if self.peek().kind not in kinds:  #146 (line in Coconut source)
            self.error("expected " + " or ".join(map(repr, kinds)))  #147 (line in Coconut source)
        return self.advance()  #148 (line in Coconut source)


    def parse(self):  #150 (line in Coconut source)
        result = self.formula()  #151 (line in Coconut source)
        if self.peek().kind != "end":  #152 (line in Coconut source)
            self.error("unexpected token")  #153 (line in Coconut source)
        return result  #154 (line in Coconut source)


    def quantifier_kind(self):  #156 (line in Coconut source)
        """If a quantifier starts here, return ForAll or Exists, else None."""  #157 (line in Coconut source)
        token = self.peek()  #158 (line in Coconut source)
        _coconut_case_match_to_0 = token  #159 (line in Coconut source)
        _coconut_case_match_check_0 = False  #159 (line in Coconut source)
        _coconut_match_temp_0 = _coconut.getattr(Token, "_coconut_is_data", False) or _coconut.isinstance(Token, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Token)  # type: ignore  #159 (line in Coconut source)
        _coconut_case_match_check_0 = True  #159 (line in Coconut source)
        if _coconut_case_match_check_0:  #159 (line in Coconut source)
            _coconut_case_match_check_0 = False  #159 (line in Coconut source)
            if not _coconut_case_match_check_0:  #159 (line in Coconut source)
                if (_coconut_match_temp_0) and (_coconut.isinstance(_coconut_case_match_to_0, Token)) and (_coconut.len(_coconut_case_match_to_0) >= 3) and (_coconut_case_match_to_0[0] == "forall"):  #159 (line in Coconut source)
                    _coconut_match_temp_1 = _coconut.len(_coconut_case_match_to_0) <= _coconut.max(3, _coconut.len(_coconut_case_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {}) and _coconut_case_match_to_0[i] == _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(3, _coconut.len(_coconut_case_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0, "__match_args__") else _coconut.len(_coconut_case_match_to_0) == 3  # type: ignore  #159 (line in Coconut source)
                    if _coconut_match_temp_1:  #159 (line in Coconut source)
                        _coconut_case_match_check_0 = True  #159 (line in Coconut source)

            if not _coconut_case_match_check_0:  #159 (line in Coconut source)
                if (not _coconut_match_temp_0) and (_coconut.isinstance(_coconut_case_match_to_0, Token)):  #159 (line in Coconut source)
                    _coconut_case_match_check_0 = True  #159 (line in Coconut source)
                if _coconut_case_match_check_0:  #159 (line in Coconut source)
                    _coconut_case_match_check_0 = False  #159 (line in Coconut source)
                    if not _coconut_case_match_check_0:  #159 (line in Coconut source)
                        if _coconut_type(_coconut_case_match_to_0) in _coconut_self_match_types:  #159 (line in Coconut source)
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports 1)")  #159 (line in Coconut source)
                            _coconut_case_match_check_0 = True  #159 (line in Coconut source)

                    if not _coconut_case_match_check_0:  #159 (line in Coconut source)
                        if not _coconut_type(_coconut_case_match_to_0) in _coconut_self_match_types:  #159 (line in Coconut source)
                            _coconut_match_temp_2 = _coconut.getattr(Token, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #159 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #159 (line in Coconut source)
                                raise _coconut.TypeError("Token.__match_args__ must be a tuple")  #159 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_2) < 3:  #159 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #159 (line in Coconut source)
                            _coconut_match_temp_3 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_2[0], _coconut_sentinel)  #159 (line in Coconut source)
                            _coconut_match_temp_4 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_2[1], _coconut_sentinel)  #159 (line in Coconut source)
                            _coconut_match_temp_5 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_2[2], _coconut_sentinel)  #159 (line in Coconut source)
                            if (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "forall") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_5 is not _coconut_sentinel):  #159 (line in Coconut source)
                                _coconut_case_match_check_0 = True  #159 (line in Coconut source)




        if _coconut_case_match_check_0:  #159 (line in Coconut source)
            return ForAll  #161 (line in Coconut source)
        if not _coconut_case_match_check_0:  #162 (line in Coconut source)
            _coconut_match_temp_6 = _coconut.getattr(Token, "_coconut_is_data", False) or _coconut.isinstance(Token, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Token)  # type: ignore  #162 (line in Coconut source)
            _coconut_case_match_check_0 = True  #162 (line in Coconut source)
            if _coconut_case_match_check_0:  #162 (line in Coconut source)
                _coconut_case_match_check_0 = False  #162 (line in Coconut source)
                if not _coconut_case_match_check_0:  #162 (line in Coconut source)
                    if (_coconut_match_temp_6) and (_coconut.isinstance(_coconut_case_match_to_0, Token)) and (_coconut.len(_coconut_case_match_to_0) >= 3) and (_coconut_case_match_to_0[0] == "exists"):  #162 (line in Coconut source)
                        _coconut_match_temp_7 = _coconut.len(_coconut_case_match_to_0) <= _coconut.max(3, _coconut.len(_coconut_case_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {}) and _coconut_case_match_to_0[i] == _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(3, _coconut.len(_coconut_case_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0, "__match_args__") else _coconut.len(_coconut_case_match_to_0) == 3  # type: ignore  #162 (line in Coconut source)
                        if _coconut_match_temp_7:  #162 (line in Coconut source)
                            _coconut_case_match_check_0 = True  #162 (line in Coconut source)

                if not _coconut_case_match_check_0:  #162 (line in Coconut source)
                    if (not _coconut_match_temp_6) and (_coconut.isinstance(_coconut_case_match_to_0, Token)):  #162 (line in Coconut source)
                        _coconut_case_match_check_0 = True  #162 (line in Coconut source)
                    if _coconut_case_match_check_0:  #162 (line in Coconut source)
                        _coconut_case_match_check_0 = False  #162 (line in Coconut source)
                        if not _coconut_case_match_check_0:  #162 (line in Coconut source)
                            if _coconut_type(_coconut_case_match_to_0) in _coconut_self_match_types:  #162 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports 1)")  #162 (line in Coconut source)
                                _coconut_case_match_check_0 = True  #162 (line in Coconut source)

                        if not _coconut_case_match_check_0:  #162 (line in Coconut source)
                            if not _coconut_type(_coconut_case_match_to_0) in _coconut_self_match_types:  #162 (line in Coconut source)
                                _coconut_match_temp_8 = _coconut.getattr(Token, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #162 (line in Coconut source)
                                if not _coconut.isinstance(_coconut_match_temp_8, _coconut.tuple):  #162 (line in Coconut source)
                                    raise _coconut.TypeError("Token.__match_args__ must be a tuple")  #162 (line in Coconut source)
                                if _coconut.len(_coconut_match_temp_8) < 3:  #162 (line in Coconut source)
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports %s)" % (_coconut.len(_coconut_match_temp_8),))  #162 (line in Coconut source)
                                _coconut_match_temp_9 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_8[0], _coconut_sentinel)  #162 (line in Coconut source)
                                _coconut_match_temp_10 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_8[1], _coconut_sentinel)  #162 (line in Coconut source)
                                _coconut_match_temp_11 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_8[2], _coconut_sentinel)  #162 (line in Coconut source)
                                if (_coconut_match_temp_9 is not _coconut_sentinel) and (_coconut_match_temp_9 == "exists") and (_coconut_match_temp_10 is not _coconut_sentinel) and (_coconut_match_temp_11 is not _coconut_sentinel):  #162 (line in Coconut source)
                                    _coconut_case_match_check_0 = True  #162 (line in Coconut source)




            if _coconut_case_match_check_0:  #162 (line in Coconut source)
                return Exists  #163 (line in Coconut source)
        if not _coconut_case_match_check_0:  #164 (line in Coconut source)
            _coconut_match_temp_12 = _coconut.getattr(Token, "_coconut_is_data", False) or _coconut.isinstance(Token, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Token)  # type: ignore  #164 (line in Coconut source)
            _coconut_case_match_check_0 = True  #164 (line in Coconut source)
            if _coconut_case_match_check_0:  #164 (line in Coconut source)
                _coconut_case_match_check_0 = False  #164 (line in Coconut source)
                if not _coconut_case_match_check_0:  #164 (line in Coconut source)
                    _coconut_match_set_name_word = _coconut_sentinel  #164 (line in Coconut source)
                    if (_coconut_match_temp_12) and (_coconut.isinstance(_coconut_case_match_to_0, Token)) and (_coconut.len(_coconut_case_match_to_0) >= 3) and (_coconut_case_match_to_0[0] == "name"):  #164 (line in Coconut source)
                        _coconut_match_set_name_word = _coconut_case_match_to_0[1]  #164 (line in Coconut source)
                        _coconut_match_temp_13 = _coconut.len(_coconut_case_match_to_0) <= _coconut.max(3, _coconut.len(_coconut_case_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {}) and _coconut_case_match_to_0[i] == _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(3, _coconut.len(_coconut_case_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0, "__match_args__") else _coconut.len(_coconut_case_match_to_0) == 3  # type: ignore  #164 (line in Coconut source)
                        if _coconut_match_temp_13:  #164 (line in Coconut source)
                            _coconut_case_match_check_0 = True  #164 (line in Coconut source)
                    if _coconut_case_match_check_0:  #164 (line in Coconut source)
                        if _coconut_match_set_name_word is not _coconut_sentinel:  #164 (line in Coconut source)
                            word = _coconut_match_set_name_word  #164 (line in Coconut source)

                if not _coconut_case_match_check_0:  #164 (line in Coconut source)
                    if (not _coconut_match_temp_12) and (_coconut.isinstance(_coconut_case_match_to_0, Token)):  #164 (line in Coconut source)
                        _coconut_case_match_check_0 = True  #164 (line in Coconut source)
                    if _coconut_case_match_check_0:  #164 (line in Coconut source)
                        _coconut_case_match_check_0 = False  #164 (line in Coconut source)
                        if not _coconut_case_match_check_0:  #164 (line in Coconut source)
                            if _coconut_type(_coconut_case_match_to_0) in _coconut_self_match_types:  #164 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports 1)")  #164 (line in Coconut source)
                                _coconut_case_match_check_0 = True  #164 (line in Coconut source)

                        if not _coconut_case_match_check_0:  #164 (line in Coconut source)
                            _coconut_match_set_name_word = _coconut_sentinel  #164 (line in Coconut source)
                            if not _coconut_type(_coconut_case_match_to_0) in _coconut_self_match_types:  #164 (line in Coconut source)
                                _coconut_match_temp_14 = _coconut.getattr(Token, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #164 (line in Coconut source)
                                if not _coconut.isinstance(_coconut_match_temp_14, _coconut.tuple):  #164 (line in Coconut source)
                                    raise _coconut.TypeError("Token.__match_args__ must be a tuple")  #164 (line in Coconut source)
                                if _coconut.len(_coconut_match_temp_14) < 3:  #164 (line in Coconut source)
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports %s)" % (_coconut.len(_coconut_match_temp_14),))  #164 (line in Coconut source)
                                _coconut_match_temp_15 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_14[0], _coconut_sentinel)  #164 (line in Coconut source)
                                _coconut_match_temp_16 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_14[1], _coconut_sentinel)  #164 (line in Coconut source)
                                _coconut_match_temp_17 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_14[2], _coconut_sentinel)  #164 (line in Coconut source)
                                if (_coconut_match_temp_15 is not _coconut_sentinel) and (_coconut_match_temp_15 == "name") and (_coconut_match_temp_16 is not _coconut_sentinel) and (_coconut_match_temp_17 is not _coconut_sentinel):  #164 (line in Coconut source)
                                    _coconut_match_set_name_word = _coconut_match_temp_16  #164 (line in Coconut source)
                                    _coconut_case_match_check_0 = True  #164 (line in Coconut source)
                            if _coconut_case_match_check_0:  #164 (line in Coconut source)
                                if _coconut_match_set_name_word is not _coconut_sentinel:  #164 (line in Coconut source)
                                    word = _coconut_match_set_name_word  #164 (line in Coconut source)




            if _coconut_case_match_check_0 and not (self.peek(1).kind == "name" and not is_upper(self.peek(1).text)):  #164 (line in Coconut source)
                _coconut_case_match_check_0 = False  #164 (line in Coconut source)
            if _coconut_case_match_check_0:  #164 (line in Coconut source)
                if word in forall_words:  #165 (line in Coconut source)
                    return ForAll  #166 (line in Coconut source)
                if word in exists_words:  #167 (line in Coconut source)
                    return Exists  #168 (line in Coconut source)
        return None  #169 (line in Coconut source)


    def operand(self, level):  #171 (line in Coconut source)
        """Parse a quantifier (which extends as far as possible) or else level."""  #172 (line in Coconut source)
        return self.quantifier() if self.quantifier_kind() else level()  #173 (line in Coconut source)


    def formula(self):  #175 (line in Coconut source)
        left = self.operand(self.implication)  #176 (line in Coconut source)
        if self.peek().kind == "iff":  #177 (line in Coconut source)
            self.advance()  #178 (line in Coconut source)
            return Iff(left, self.formula())  #179 (line in Coconut source)
        return left  #180 (line in Coconut source)


    def implication(self):  #182 (line in Coconut source)
        left = self.disjunction()  #183 (line in Coconut source)
        if self.peek().kind == "imp":  #184 (line in Coconut source)
            self.advance()  #185 (line in Coconut source)
            return Imp(left, self.operand(self.implication))  #186 (line in Coconut source)
        return left  #187 (line in Coconut source)


    def disjunction(self):  #189 (line in Coconut source)
        elems = [self.conjunction(),]  #190 (line in Coconut source)
        while self.peek().kind == "or":  #191 (line in Coconut source)
            self.advance()  #192 (line in Coconut source)
            elems.append(self.operand(self.conjunction))  #193 (line in Coconut source)
        return Or(*elems)  #194 (line in Coconut source)


    def conjunction(self):  #196 (line in Coconut source)
        elems = [self.negation(),]  #197 (line in Coconut source)
        while self.peek().kind == "and":  #198 (line in Coconut source)
            self.advance()  #199 (line in Coconut source)
            elems.append(self.operand(self.negation))  #200 (line in Coconut source)
        return And(*elems)  #201 (line in Coconut source)


    def negation(self):  #203 (line in Coconut source)
        if self.peek().kind == "not":  #204 (line in Coconut source)
            self.advance()  #205 (line in Coconut source)
            return Not(self.operand(self.negation))  #206 (line in Coconut source)
        return self.primary()  #207 (line in Coconut source)


    def primary(self):  #209 (line in Coconut source)
        token = self.peek()  #210 (line in Coconut source)
        _coconut_case_match_to_1 = token.kind  #211 (line in Coconut source)
        _coconut_case_match_check_1 = False  #211 (line in Coconut source)
        if _coconut_case_match_to_1 == "top":  #211 (line in Coconut source)
            _coconut_case_match_check_1 = True  #211 (line in Coconut source)
        if _coconut_case_match_check_1:  #211 (line in Coconut source)
            self.advance()  #213 (line in Coconut source)
            return top  #214 (line in Coconut source)
        if not _coconut_case_match_check_1:  #215 (line in Coconut source)
            if _coconut_case_match_to_1 == "bot":  #215 (line in Coconut source)
                _coconut_case_match_check_1 = True  #215 (line in Coconut source)
            if _coconut_case_match_check_1:  #215 (line in Coconut source)
                self.advance()  #216 (line in Coconut source)
                return bot  #217 (line in Coconut source)
        if not _coconut_case_match_check_1:  #218 (line in Coconut source)
            if _coconut_case_match_to_1 == "(":  #218 (line in Coconut source)
                _coconut_case_match_check_1 = True  #218 (line in Coconut source)
            if _coconut_case_match_check_1:  #218 (line in Coconut source)
                self.advance()  #219 (line in Coconut source)
                result = self.formula()  #220 (line in Coconut source)
                self.expect(")")  #221 (line in Coconut source)
                return result  #222 (line in Coconut source)
        if self.quantifier_kind():  #223 (line in Coconut source)
            return self.quantifier()  #224 (line in Coconut source)
        _coconut_case_match_to_2 = token  #225 (line in Coconut source)
        _coconut_case_match_check_2 = False  #225 (line in Coconut source)
        _coconut_match_temp_18 = _coconut.getattr(Token, "_coconut_is_data", False) or _coconut.isinstance(Token, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Token)  # type: ignore  #225 (line in Coconut source)
        _coconut_case_match_check_2 = True  #225 (line in Coconut source)
        if _coconut_case_match_check_2:  #225 (line in Coconut source)
            _coconut_case_match_check_2 = False  #225 (line in Coconut source)
            if not _coconut_case_match_check_2:  #225 (line in Coconut source)
                _coconut_match_set_name_name = _coconut_sentinel  #225 (line in Coconut source)
                if (_coconut_match_temp_18) and (_coconut.isinstance(_coconut_case_match_to_2, Token)) and (_coconut.len(_coconut_case_match_to_2) >= 3) and (_coconut_case_match_to_2[0] == "name"):  #225 (line in Coconut source)
                    _coconut_match_set_name_name = _coconut_case_match_to_2[1]  #225 (line in Coconut source)
                    _coconut_match_temp_19 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(3, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(3, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 3  # type: ignore  #225 (line in Coconut source)
                    if _coconut_match_temp_19:  #225 (line in Coconut source)
                        _coconut_case_match_check_2 = True  #225 (line in Coconut source)
                if _coconut_case_match_check_2:  #225 (line in Coconut source)
                    if _coconut_match_set_name_name is not _coconut_sentinel:  #225 (line in Coconut source)
                        name = _coconut_match_set_name_name  #225 (line in Coconut source)

            if not _coconut_case_match_check_2:  #225 (line in Coconut source)
                if (not _coconut_match_temp_18) and (_coconut.isinstance(_coconut_case_match_to_2, Token)):  #225 (line in Coconut source)
                    _coconut_case_match_check_2 = True  #225 (line in Coconut source)
                if _coconut_case_match_check_2:  #225 (line in Coconut source)
                    _coconut_case_match_check_2 = False  #225 (line in Coconut source)
                    if not _coconut_case_match_check_2:  #225 (line in Coconut source)
                        if _coconut_type(_coconut_case_match_to_2) in _coconut_self_match_types:  #225 (line in Coconut source)
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports 1)")  #225 (line in Coconut source)
                            _coconut_case_match_check_2 = True  #225 (line in Coconut source)

                    if not _coconut_case_match_check_2:  #225 (line in Coconut source)
                        _coconut_match_set_name_name = _coconut_sentinel  #225 (line in Coconut source)
                        if not _coconut_type(_coconut_case_match_to_2) in _coconut_self_match_types:  #225 (line in Coconut source)
                            _coconut_match_temp_20 = _coconut.getattr(Token, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #225 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_20, _coconut.tuple):  #225 (line in Coconut source)
                                raise _coconut.TypeError("Token.__match_args__ must be a tuple")  #225 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_20) < 3:  #225 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports %s)" % (_coconut.len(_coconut_match_temp_20),))  #225 (line in Coconut source)
                            _coconut_match_temp_21 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_20[0], _coconut_sentinel)  #225 (line in Coconut source)
                            _coconut_match_temp_22 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_20[1], _coconut_sentinel)  #225 (line in Coconut source)
                            _coconut_match_temp_23 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_20[2], _coconut_sentinel)  #225 (line in Coconut source)
                            if (_coconut_match_temp_21 is not _coconut_sentinel) and (_coconut_match_temp_21 == "name") and (_coconut_match_temp_22 is not _coconut_sentinel) and (_coconut_match_temp_23 is not _coconut_sentinel):  #225 (line in Coconut source)
                                _coconut_match_set_name_name = _coconut_match_temp_22  #225 (line in Coconut source)
                                _coconut_case_match_check_2 = True  #225 (line in Coconut source)
                        if _coconut_case_match_check_2:  #225 (line in Coconut source)
                            if _coconut_match_set_name_name is not _coconut_sentinel:  #225 (line in Coconut source)
                                name = _coconut_match_set_name_name  #225 (line in Coconut source)




        if _coconut_case_match_check_2 and not (is_upper(name)):  #225 (line in Coconut source)
            _coconut_case_match_check_2 = False  #225 (line in Coconut source)
        if _coconut_case_match_check_2:  #225 (line in Coconut source)
            self.advance()  #227 (line in Coconut source)
            if self.peek().kind == "(":  #228 (line in Coconut source)
                return Pred(name, *self.arguments())  #229 (line in Coconut source)
            return Prop(name)  #230 (line in Coconut source)
        if not _coconut_case_match_check_2:  #231 (line in Coconut source)
            _coconut_case_match_check_2 = True  #231 (line in Coconut source)
            if _coconut_case_match_check_2:  #231 (line in Coconut source)
                _coconut_case_match_check_2 = False  #231 (line in Coconut source)
                if not _coconut_case_match_check_2:  #231 (line in Coconut source)
                    _coconut_match_temp_24 = _coconut.getattr(Token, "_coconut_is_data", False) or _coconut.isinstance(Token, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Token)  # type: ignore  #231 (line in Coconut source)
                    _coconut_case_match_check_2 = True  #231 (line in Coconut source)
                    if _coconut_case_match_check_2:  #231 (line in Coconut source)
                        _coconut_case_match_check_2 = False  #231 (line in Coconut source)
                        if not _coconut_case_match_check_2:  #231 (line in Coconut source)
                            if (_coconut_match_temp_24) and (_coconut.isinstance(_coconut_case_match_to_2, Token)) and (_coconut.len(_coconut_case_match_to_2) >= 3) and (_coconut_case_match_to_2[0] == "name"):  #231 (line in Coconut source)
                                _coconut_match_temp_25 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(3, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(3, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 3  # type: ignore  #231 (line in Coconut source)
                                if _coconut_match_temp_25:  #231 (line in Coconut source)
                                    _coconut_case_match_check_2 = True  #231 (line in Coconut source)

                        if not _coconut_case_match_check_2:  #231 (line in Coconut source)
                            if (not _coconut_match_temp_24) and (_coconut.isinstance(_coconut_case_match_to_2, Token)):  #231 (line in Coconut source)
                                _coconut_case_match_check_2 = True  #231 (line in Coconut source)
                            if _coconut_case_match_check_2:  #231 (line in Coconut source)
                                _coconut_case_match_check_2 = False  #231 (line in Coconut source)
                                if not _coconut_case_match_check_2:  #231 (line in Coconut source)
                                    if _coconut_type(_coconut_case_match_to_2) in _coconut_self_match_types:  #231 (line in Coconut source)
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports 1)")  #231 (line in Coconut source)
                                        _coconut_case_match_check_2 = True  #231 (line in Coconut source)

                                if not _coconut_case_match_check_2:  #231 (line in Coconut source)
                                    if not _coconut_type(_coconut_case_match_to_2) in _coconut_self_match_types:  #231 (line in Coconut source)
                                        _coconut_match_temp_26 = _coconut.getattr(Token, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #231 (line in Coconut source)
                                        if not _coconut.isinstance(_coconut_match_temp_26, _coconut.tuple):  #231 (line in Coconut source)
                                            raise _coconut.TypeError("Token.__match_args__ must be a tuple")  #231 (line in Coconut source)
                                        if _coconut.len(_coconut_match_temp_26) < 3:  #231 (line in Coconut source)
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports %s)" % (_coconut.len(_coconut_match_temp_26),))  #231 (line in Coconut source)
                                        _coconut_match_temp_27 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_26[0], _coconut_sentinel)  #231 (line in Coconut source)
                                        _coconut_match_temp_28 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_26[1], _coconut_sentinel)  #231 (line in Coconut source)
                                        _coconut_match_temp_29 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_26[2], _coconut_sentinel)  #231 (line in Coconut source)
                                        if (_coconut_match_temp_27 is not _coconut_sentinel) and (_coconut_match_temp_27 == "name") and (_coconut_match_temp_28 is not _coconut_sentinel) and (_coconut_match_temp_29 is not _coconut_sentinel):  #231 (line in Coconut source)
                                            _coconut_case_match_check_2 = True  #231 (line in Coconut source)





                if not _coconut_case_match_check_2:  #231 (line in Coconut source)
                    _coconut_match_temp_30 = _coconut.getattr(Token, "_coconut_is_data", False) or _coconut.isinstance(Token, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Token)  # type: ignore  #231 (line in Coconut source)
                    _coconut_case_match_check_2 = True  #231 (line in Coconut source)
                    if _coconut_case_match_check_2:  #231 (line in Coconut source)
                        _coconut_case_match_check_2 = False  #231 (line in Coconut source)
                        if not _coconut_case_match_check_2:  #231 (line in Coconut source)
                            if (_coconut_match_temp_30) and (_coconut.isinstance(_coconut_case_match_to_2, Token)) and (_coconut.len(_coconut_case_match_to_2) >= 3) and (_coconut_case_match_to_2[0] == "?"):  #231 (line in Coconut source)
                                _coconut_match_temp_31 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(3, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(3, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 3  # type: ignore  #231 (line in Coconut source)
                                if _coconut_match_temp_31:  #231 (line in Coconut source)
                                    _coconut_case_match_check_2 = True  #231 (line in Coconut source)

                        if not _coconut_case_match_check_2:  #231 (line in Coconut source)
                            if (not _coconut_match_temp_30) and (_coconut.isinstance(_coconut_case_match_to_2, Token)):  #231 (line in Coconut source)
                                _coconut_case_match_check_2 = True  #231 (line in Coconut source)
                            if _coconut_case_match_check_2:  #231 (line in Coconut source)
                                _coconut_case_match_check_2 = False  #231 (line in Coconut source)
                                if not _coconut_case_match_check_2:  #231 (line in Coconut source)
                                    if _coconut_type(_coconut_case_match_to_2) in _coconut_self_match_types:  #231 (line in Coconut source)
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports 1)")  #231 (line in Coconut source)
                                        _coconut_case_match_check_2 = True  #231 (line in Coconut source)

                                if not _coconut_case_match_check_2:  #231 (line in Coconut source)
                                    if not _coconut_type(_coconut_case_match_to_2) in _coconut_self_match_types:  #231 (line in Coconut source)
                                        _coconut_match_temp_32 = _coconut.getattr(Token, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #231 (line in Coconut source)
                                        if not _coconut.isinstance(_coconut_match_temp_32, _coconut.tuple):  #231 (line in Coconut source)
                                            raise _coconut.TypeError("Token.__match_args__ must be a tuple")  #231 (line in Coconut source)
                                        if _coconut.len(_coconut_match_temp_32) < 3:  #231 (line in Coconut source)
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports %s)" % (_coconut.len(_coconut_match_temp_32),))  #231 (line in Coconut source)
                                        _coconut_match_temp_33 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_32[0], _coconut_sentinel)  #231 (line in Coconut source)
                                        _coconut_match_temp_34 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_32[1], _coconut_sentinel)  #231 (line in Coconut source)
                                        _coconut_match_temp_35 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_32[2], _coconut_sentinel)  #231 (line in Coconut source)
                                        if (_coconut_match_temp_33 is not _coconut_sentinel) and (_coconut_match_temp_33 == "?") and (_coconut_match_temp_34 is not _coconut_sentinel) and (_coconut_match_temp_35 is not _coconut_sentinel):  #231 (line in Coconut source)
                                            _coconut_case_match_check_2 = True  #231 (line in Coconut source)






            if _coconut_case_match_check_2:  #231 (line in Coconut source)
                left = self.term()  #232 (line in Coconut source)
                op = self.expect("eq", "neq")  #233 (line in Coconut source)
                right = self.term()  #234 (line in Coconut source)
                return Eq(left, right) if op.kind == "eq" else Not(Eq(left, right))  #235 (line in Coconut source)
        self.error("expected a formula")  #236 (line in Coconut source)


    def arguments(self) -> list:  #238 (line in Coconut source)
        self.expect("(")  #239 (line in Coconut source)
        args = [self.term(),]  #240 (line in Coconut source)
        while self.peek().kind == ",":  #241 (line in Coconut source)
            self.advance()  #242 (line in Coconut source)
            args.append(self.term())  #243 (line in Coconut source)
        self.expect(")")  #244 (line in Coconut source)
        return args  #245 (line in Coconut source)


    def term(self):  #247 (line in Coconut source)
        token = self.peek()  #248 (line in Coconut source)
        _coconut_case_match_to_3 = token  #249 (line in Coconut source)
        _coconut_case_match_check_3 = False  #249 (line in Coconut source)
        _coconut_match_temp_36 = _coconut.getattr(Token, "_coconut_is_data", False) or _coconut.isinstance(Token, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Token)  # type: ignore  #249 (line in Coconut source)
        _coconut_case_match_check_3 = True  #249 (line in Coconut source)
        if _coconut_case_match_check_3:  #249 (line in Coconut source)
            _coconut_case_match_check_3 = False  #249 (line in Coconut source)
            if not _coconut_case_match_check_3:  #249 (line in Coconut source)
                if (_coconut_match_temp_36) and (_coconut.isinstance(_coconut_case_match_to_3, Token)) and (_coconut.len(_coconut_case_match_to_3) >= 3) and (_coconut_case_match_to_3[0] == "?"):  #249 (line in Coconut source)
                    _coconut_match_temp_37 = _coconut.len(_coconut_case_match_to_3) <= _coconut.max(3, _coconut.len(_coconut_case_match_to_3.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {}) and _coconut_case_match_to_3[i] == _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {})[i] for i in _coconut.range(3, _coconut.len(_coconut_case_match_to_3.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_3, "__match_args__") else _coconut.len(_coconut_case_match_to_3) == 3  # type: ignore  #249 (line in Coconut source)
                    if _coconut_match_temp_37:  #249 (line in Coconut source)
                        _coconut_case_match_check_3 = True  #249 (line in Coconut source)

            if not _coconut_case_match_check_3:  #249 (line in Coconut source)
                if (not _coconut_match_temp_36) and (_coconut.isinstance(_coconut_case_match_to_3, Token)):  #249 (line in Coconut source)
                    _coconut_case_match_check_3 = True  #249 (line in Coconut source)
                if _coconut_case_match_check_3:  #249 (line in Coconut source)
                    _coconut_case_match_check_3 = False  #249 (line in Coconut source)
                    if not _coconut_case_match_check_3:  #249 (line in Coconut source)
                        if _coconut_type(_coconut_case_match_to_3) in _coconut_self_match_types:  #249 (line in Coconut source)
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports 1)")  #249 (line in Coconut source)
                            _coconut_case_match_check_3 = True  #249 (line in Coconut source)

                    if not _coconut_case_match_check_3:  #249 (line in Coconut source)
                        if not _coconut_type(_coconut_case_match_to_3) in _coconut_self_match_types:  #249 (line in Coconut source)
                            _coconut_match_temp_38 = _coconut.getattr(Token, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #249 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_38, _coconut.tuple):  #249 (line in Coconut source)
                                raise _coconut.TypeError("Token.__match_args__ must be a tuple")  #249 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_38) < 3:  #249 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports %s)" % (_coconut.len(_coconut_match_temp_38),))  #249 (line in Coconut source)
                            _coconut_match_temp_39 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_38[0], _coconut_sentinel)  #249 (line in Coconut source)
                            _coconut_match_temp_40 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_38[1], _coconut_sentinel)  #249 (line in Coconut source)
                            _coconut_match_temp_41 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_38[2], _coconut_sentinel)  #249 (line in Coconut source)
                            if (_coconut_match_temp_39 is not _coconut_sentinel) and (_coconut_match_temp_39 == "?") and (_coconut_match_temp_40 is not _coconut_sentinel) and (_coconut_match_temp_41 is not _coconut_sentinel):  #249 (line in Coconut source)
                                _coconut_case_match_check_3 = True  #249 (line in Coconut source)




        if _coconut_case_match_check_3:  #249 (line in Coconut source)
            self.advance()  #251 (line in Coconut source)
            return Var(self.lowercase_name())  #252 (line in Coconut source)
        if not _coconut_case_match_check_3:  #253 (line in Coconut source)
            _coconut_match_temp_42 = _coconut.getattr(Token, "_coconut_is_data", False) or _coconut.isinstance(Token, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Token)  # type: ignore  #253 (line in Coconut source)
            _coconut_case_match_check_3 = True  #253 (line in Coconut source)
            if _coconut_case_match_check_3:  #253 (line in Coconut source)
                _coconut_case_match_check_3 = False  #253 (line in Coconut source)
                if not _coconut_case_match_check_3:  #253 (line in Coconut source)
                    _coconut_match_set_name_name = _coconut_sentinel  #253 (line in Coconut source)
                    if (_coconut_match_temp_42) and (_coconut.isinstance(_coconut_case_match_to_3, Token)) and (_coconut.len(_coconut_case_match_to_3) >= 3) and (_coconut_case_match_to_3[0] == "name"):  #253 (line in Coconut source)
                        _coconut_match_set_name_name = _coconut_case_match_to_3[1]  #253 (line in Coconut source)
                        _coconut_match_temp_43 = _coconut.len(_coconut_case_match_to_3) <= _coconut.max(3, _coconut.len(_coconut_case_match_to_3.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {}) and _coconut_case_match_to_3[i] == _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {})[i] for i in _coconut.range(3, _coconut.len(_coconut_case_match_to_3.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_3, "__match_args__") else _coconut.len(_coconut_case_match_to_3) == 3  # type: ignore  #253 (line in Coconut source)
                        if _coconut_match_temp_43:  #253 (line in Coconut source)
                            _coconut_case_match_check_3 = True  #253 (line in Coconut source)
                    if _coconut_case_match_check_3:  #253 (line in Coconut source)
                        if _coconut_match_set_name_name is not _coconut_sentinel:  #253 (line in Coconut source)
                            name = _coconut_match_set_name_name  #253 (line in Coconut source)

                if not _coconut_case_match_check_3:  #253 (line in Coconut source)
                    if (not _coconut_match_temp_42) and (_coconut.isinstance(_coconut_case_match_to_3, Token)):  #253 (line in Coconut source)
                        _coconut_case_match_check_3 = True  #253 (line in Coconut source)
                    if _coconut_case_match_check_3:  #253 (line in Coconut source)
                        _coconut_case_match_check_3 = False  #253 (line in Coconut source)
                        if not _coconut_case_match_check_3:  #253 (line in Coconut source)
                            if _coconut_type(_coconut_case_match_to_3) in _coconut_self_match_types:  #253 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports 1)")  #253 (line in Coconut source)
                                _coconut_case_match_check_3 = True  #253 (line in Coconut source)

                        if not _coconut_case_match_check_3:  #253 (line in Coconut source)
                            _coconut_match_set_name_name = _coconut_sentinel  #253 (line in Coconut source)
                            if not _coconut_type(_coconut_case_match_to_3) in _coconut_self_match_types:  #253 (line in Coconut source)
                                _coconut_match_temp_44 = _coconut.getattr(Token, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #253 (line in Coconut source)
                                if not _coconut.isinstance(_coconut_match_temp_44, _coconut.tuple):  #253 (line in Coconut source)
                                    raise _coconut.TypeError("Token.__match_args__ must be a tuple")  #253 (line in Coconut source)
                                if _coconut.len(_coconut_match_temp_44) < 3:  #253 (line in Coconut source)
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 3; 'Token' only supports %s)" % (_coconut.len(_coconut_match_temp_44),))  #253 (line in Coconut source)
                                _coconut_match_temp_45 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_44[0], _coconut_sentinel)  #253 (line in Coconut source)
                                _coconut_match_temp_46 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_44[1], _coconut_sentinel)  #253 (line in Coconut source)
                                _coconut_match_temp_47 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_44[2], _coconut_sentinel)  #253 (line in Coconut source)
                                if (_coconut_match_temp_45 is not _coconut_sentinel) and (_coconut_match_temp_45 == "name") and (_coconut_match_temp_46 is not _coconut_sentinel) and (_coconut_match_temp_47 is not _coconut_sentinel):  #253 (line in Coconut source)
                                    _coconut_match_set_name_name = _coconut_match_temp_46  #253 (line in Coconut source)
                                    _coconut_case_match_check_3 = True  #253 (line in Coconut source)
                            if _coconut_case_match_check_3:  #253 (line in Coconut source)
                                if _coconut_match_set_name_name is not _coconut_sentinel:  #253 (line in Coconut source)
                                    name = _coconut_match_set_name_name  #253 (line in Coconut source)




            if _coconut_case_match_check_3 and not (not is_upper(name)):  #253 (line in Coconut source)
                _coconut_case_match_check_3 = False  #253 (line in Coconut source)
            if _coconut_case_match_check_3:  #253 (line in Coconut source)
                self.advance()  #254 (line in Coconut source)
                if self.peek().kind == "(":  #255 (line in Coconut source)
                    return Func(name, *self.arguments())  #256 (line in Coconut source)
                return Const(name)  #257 (line in Coconut source)
        self.error("expected a term (terms must start with a lowercase letter, digit, or underscore)")  #258 (line in Coconut source)


    def lowercase_name(self):  #260 (line in Coconut source)
        token = self.expect("name")  #261 (line in Coconut source)
        if is_upper(token.text):  #262 (line in Coconut source)
            self.error("expected a lowercase variable name", token)  #263 (line in Coconut source)
        return token.text  #264 (line in Coconut source)


    def quantifier(self):  #266 (line in Coconut source)
        quant = self.quantifier_kind()  #267 (line in Coconut source)
        self.advance()  #268 (line in Coconut source)
        variables = [self.lowercase_name(),]  #269 (line in Coconut source)
        while self.peek().kind == "name" and not is_upper(self.peek().text):  #270 (line in Coconut source)
            variables.append(self.lowercase_name())  #271 (line in Coconut source)
        restriction = None  #272 (line in Coconut source)
        if self.peek().kind == ":":  #273 (line in Coconut source)
            self.advance()  #274 (line in Coconut source)
            token = self.expect("name")  #275 (line in Coconut source)
            if not is_upper(token.text):  #276 (line in Coconut source)
                self.error("expected a proposition name", token)  #277 (line in Coconut source)
            restriction = Prop(token.text)  #278 (line in Coconut source)
        self.expect(".", ",")  #279 (line in Coconut source)
        body = self.formula()  #280 (line in Coconut source)
        for name in reversed(variables):  #281 (line in Coconut source)
            var = Const(name)  #282 (line in Coconut source)
            if restriction is not None:  #283 (line in Coconut source)
                body = Imp(restriction(var), body) if quant is ForAll else And(restriction(var), body)  #284 (line in Coconut source)
            body = quant(var, body)  #285 (line in Coconut source)
        return body  #286 (line in Coconut source)


# Endpoint:


def expr(formula: str):  #291 (line in Coconut source)
    """Parse a formula written in standard mathematical notation, such as
    "∀x, F(x) → G(x)" or "A x. F(x) -> G(x)". Propositions and predicates
    must start with an uppercase letter; constants, variables, and functions
    must start with a lowercase letter (or a digit or underscore)."""  #295 (line in Coconut source)
    if not isinstance(formula, str):  #296 (line in Coconut source)
        raise TypeError("expr expects a string but got {_coconut_format_0!r}".format(_coconut_format_0=(formula)))  #297 (line in Coconut source)
    return Parser(formula).parse()  #298 (line in Coconut source)


parse = expr  #300 (line in Coconut source)
