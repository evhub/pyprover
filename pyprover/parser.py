#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x68d6886c

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

from pyparsing import Literal  #3 (line num in coconut source)
from pyparsing import ZeroOrMore  #3 (line num in coconut source)
from pyparsing import OneOrMore  #3 (line num in coconut source)
from pyparsing import Optional  #3 (line num in coconut source)
from pyparsing import oneOf  #3 (line num in coconut source)
from pyparsing import replaceWith  #3 (line num in coconut source)
from pyparsing import Regex  #3 (line num in coconut source)
from pyparsing import Forward  #3 (line num in coconut source)
from pyparsing import ParserElement  #3 (line num in coconut source)
from pyparsing import stringStart  #3 (line num in coconut source)
from pyparsing import stringEnd  #3 (line num in coconut source)

from pyprover.constants import all_top_syms  #17 (line num in coconut source)
from pyprover.constants import all_bot_syms  #17 (line num in coconut source)
from pyprover.constants import all_not_syms  #17 (line num in coconut source)
from pyprover.constants import all_imp_syms  #17 (line num in coconut source)
from pyprover.constants import all_and_syms  #17 (line num in coconut source)
from pyprover.constants import all_or_syms  #17 (line num in coconut source)
from pyprover.constants import all_forall_syms  #17 (line num in coconut source)
from pyprover.constants import all_exists_syms  #17 (line num in coconut source)
from pyprover.logic import top  #27 (line num in coconut source)
from pyprover.logic import bot  #27 (line num in coconut source)
from pyprover.logic import Proposition  #27 (line num in coconut source)
from pyprover.logic import Predicate  #27 (line num in coconut source)
from pyprover.logic import Constant  #27 (line num in coconut source)
from pyprover.logic import Variable  #27 (line num in coconut source)
from pyprover.logic import Function  #27 (line num in coconut source)
from pyprover.logic import Not  #27 (line num in coconut source)
from pyprover.logic import Implies  #27 (line num in coconut source)
from pyprover.logic import And  #27 (line num in coconut source)
from pyprover.logic import Or  #27 (line num in coconut source)
from pyprover.logic import Exists  #27 (line num in coconut source)
from pyprover.logic import ForAll  #27 (line num in coconut source)
from pyprover.logic import Eq  #27 (line num in coconut source)


ParserElement.enablePackrat()  #45 (line num in coconut source)

oneOf = _coconut_forward_compose(list, oneOf)  #47 (line num in coconut source)


# Utilities:

@_coconut_tco  #52 (line num in coconut source)
def attach(action, item):  #52 (line num in coconut source)
    """Attaches a parse action to an item."""  #53 (line num in coconut source)
    return _coconut_tail_call(item.copy().addParseAction, action)  #54 (line num in coconut source)


@_coconut_tco  #56 (line num in coconut source)
def call(action, item):  #56 (line num in coconut source)
    """Call an action on the tokens in item."""  #57 (line num in coconut source)
    @_coconut_tco  #58 (line num in coconut source)
    def parse_action(o, l, tokens):  #58 (line num in coconut source)
        return _coconut_tail_call(action, *tokens)  #59 (line num in coconut source)

    return _coconut_tail_call((attach), parse_action, item)  #60 (line num in coconut source)


@_coconut_tco  #62 (line num in coconut source)
def fixto(output, item):  #62 (line num in coconut source)
    """Forces an item to result in a specific output."""  #63 (line num in coconut source)
    return _coconut_tail_call((attach), replaceWith(output), item)  #64 (line num in coconut source)


def tokenlist(sep, item):  #66 (line num in coconut source)
    """Creates a list of tokens matching the item."""  #67 (line num in coconut source)
    return item + ZeroOrMore(sep + item) + Optional(sep)  #68 (line num in coconut source)


@_coconut_tco  #70 (line num in coconut source)
def parse(grammar, text):  #70 (line num in coconut source)
    """Parses text using grammar."""  #71 (line num in coconut source)
    return _coconut_tail_call(grammar.parseWithTabs().parseString, text)  #72 (line num in coconut source)


# Grammar:


@_coconut_tco  #77 (line num in coconut source)
@_coconut_mark_as_match  #77 (line num in coconut source)
def exists_handle(*_coconut_match_args, **_coconut_match_kwargs):  #77 (line num in coconut source)
    _coconut_match_check_0 = False  #77 (line num in coconut source)
    _coconut_match_set_name_const = _coconut_sentinel  #77 (line num in coconut source)
    _coconut_match_set_name_expr = _coconut_sentinel  #77 (line num in coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #77 (line num in coconut source)
    if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "const" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "expr" in _coconut_match_kwargs)) == 1):  #77 (line num in coconut source)
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("const")  #77 (line num in coconut source)
        _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("expr")  #77 (line num in coconut source)
        _coconut_match_set_name_const = _coconut_match_temp_0  #77 (line num in coconut source)
        _coconut_match_set_name_expr = _coconut_match_temp_1  #77 (line num in coconut source)
        if not _coconut_match_kwargs:  #77 (line num in coconut source)
            _coconut_match_check_0 = True  #77 (line num in coconut source)
    if _coconut_match_check_0:  #77 (line num in coconut source)
        if _coconut_match_set_name_const is not _coconut_sentinel:  #77 (line num in coconut source)
            const = _coconut_match_set_name_const  #77 (line num in coconut source)
        if _coconut_match_set_name_expr is not _coconut_sentinel:  #77 (line num in coconut source)
            expr = _coconut_match_set_name_expr  #77 (line num in coconut source)
    if not _coconut_match_check_0:  #77 (line num in coconut source)
        raise _coconut_FunctionMatchError('match def exists_handle(const, expr) = Exists(const, expr)', _coconut_match_args)  #77 (line num in coconut source)

    return _coconut_tail_call(Exists, const, expr)  #77 (line num in coconut source)


@addpattern(exists_handle)  #79 (line num in coconut source)
@_coconut_tco  #80 (line num in coconut source)
@_coconut_mark_as_match  #80 (line num in coconut source)
def exists_handle(*_coconut_match_args, **_coconut_match_kwargs):  #80 (line num in coconut source)
    _coconut_match_check_1 = False  #80 (line num in coconut source)
    _coconut_match_set_name_const = _coconut_sentinel  #80 (line num in coconut source)
    _coconut_match_set_name_prop = _coconut_sentinel  #80 (line num in coconut source)
    _coconut_match_set_name_expr = _coconut_sentinel  #80 (line num in coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #80 (line num in coconut source)
    if (_coconut.len(_coconut_match_args) <= 3) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "const" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "prop" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "expr" in _coconut_match_kwargs)) == 1):  #80 (line num in coconut source)
        _coconut_match_temp_2 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("const")  #80 (line num in coconut source)
        _coconut_match_temp_3 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("prop")  #80 (line num in coconut source)
        _coconut_match_temp_4 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("expr")  #80 (line num in coconut source)
        _coconut_match_set_name_const = _coconut_match_temp_2  #80 (line num in coconut source)
        _coconut_match_set_name_prop = _coconut_match_temp_3  #80 (line num in coconut source)
        _coconut_match_set_name_expr = _coconut_match_temp_4  #80 (line num in coconut source)
        if not _coconut_match_kwargs:  #80 (line num in coconut source)
            _coconut_match_check_1 = True  #80 (line num in coconut source)
    if _coconut_match_check_1:  #80 (line num in coconut source)
        if _coconut_match_set_name_const is not _coconut_sentinel:  #80 (line num in coconut source)
            const = _coconut_match_set_name_const  #80 (line num in coconut source)
        if _coconut_match_set_name_prop is not _coconut_sentinel:  #80 (line num in coconut source)
            prop = _coconut_match_set_name_prop  #80 (line num in coconut source)
        if _coconut_match_set_name_expr is not _coconut_sentinel:  #80 (line num in coconut source)
            expr = _coconut_match_set_name_expr  #80 (line num in coconut source)
    if not _coconut_match_check_1:  #80 (line num in coconut source)
        raise _coconut_FunctionMatchError('match def exists_handle(const, prop, expr) =', _coconut_match_args)  #80 (line num in coconut source)

    return _coconut_tail_call(Exists, const, prop(const) & expr)  #81 (line num in coconut source)


@_coconut_tco  #83 (line num in coconut source)
@_coconut_mark_as_match  #83 (line num in coconut source)
def forall_handle(*_coconut_match_args, **_coconut_match_kwargs):  #83 (line num in coconut source)
    _coconut_match_check_2 = False  #83 (line num in coconut source)
    _coconut_match_set_name_const = _coconut_sentinel  #83 (line num in coconut source)
    _coconut_match_set_name_expr = _coconut_sentinel  #83 (line num in coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #83 (line num in coconut source)
    if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "const" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "expr" in _coconut_match_kwargs)) == 1):  #83 (line num in coconut source)
        _coconut_match_temp_5 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("const")  #83 (line num in coconut source)
        _coconut_match_temp_6 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("expr")  #83 (line num in coconut source)
        _coconut_match_set_name_const = _coconut_match_temp_5  #83 (line num in coconut source)
        _coconut_match_set_name_expr = _coconut_match_temp_6  #83 (line num in coconut source)
        if not _coconut_match_kwargs:  #83 (line num in coconut source)
            _coconut_match_check_2 = True  #83 (line num in coconut source)
    if _coconut_match_check_2:  #83 (line num in coconut source)
        if _coconut_match_set_name_const is not _coconut_sentinel:  #83 (line num in coconut source)
            const = _coconut_match_set_name_const  #83 (line num in coconut source)
        if _coconut_match_set_name_expr is not _coconut_sentinel:  #83 (line num in coconut source)
            expr = _coconut_match_set_name_expr  #83 (line num in coconut source)
    if not _coconut_match_check_2:  #83 (line num in coconut source)
        raise _coconut_FunctionMatchError('match def forall_handle(const, expr) = ForAll(const, expr)', _coconut_match_args)  #83 (line num in coconut source)

    return _coconut_tail_call(ForAll, const, expr)  #83 (line num in coconut source)


@addpattern(forall_handle)  #85 (line num in coconut source)
@_coconut_tco  #86 (line num in coconut source)
@_coconut_mark_as_match  #86 (line num in coconut source)
def forall_handle(*_coconut_match_args, **_coconut_match_kwargs):  #86 (line num in coconut source)
    _coconut_match_check_3 = False  #86 (line num in coconut source)
    _coconut_match_set_name_const = _coconut_sentinel  #86 (line num in coconut source)
    _coconut_match_set_name_prop = _coconut_sentinel  #86 (line num in coconut source)
    _coconut_match_set_name_expr = _coconut_sentinel  #86 (line num in coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #86 (line num in coconut source)
    if (_coconut.len(_coconut_match_args) <= 3) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "const" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "prop" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "expr" in _coconut_match_kwargs)) == 1):  #86 (line num in coconut source)
        _coconut_match_temp_7 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("const")  #86 (line num in coconut source)
        _coconut_match_temp_8 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("prop")  #86 (line num in coconut source)
        _coconut_match_temp_9 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("expr")  #86 (line num in coconut source)
        _coconut_match_set_name_const = _coconut_match_temp_7  #86 (line num in coconut source)
        _coconut_match_set_name_prop = _coconut_match_temp_8  #86 (line num in coconut source)
        _coconut_match_set_name_expr = _coconut_match_temp_9  #86 (line num in coconut source)
        if not _coconut_match_kwargs:  #86 (line num in coconut source)
            _coconut_match_check_3 = True  #86 (line num in coconut source)
    if _coconut_match_check_3:  #86 (line num in coconut source)
        if _coconut_match_set_name_const is not _coconut_sentinel:  #86 (line num in coconut source)
            const = _coconut_match_set_name_const  #86 (line num in coconut source)
        if _coconut_match_set_name_prop is not _coconut_sentinel:  #86 (line num in coconut source)
            prop = _coconut_match_set_name_prop  #86 (line num in coconut source)
        if _coconut_match_set_name_expr is not _coconut_sentinel:  #86 (line num in coconut source)
            expr = _coconut_match_set_name_expr  #86 (line num in coconut source)
    if not _coconut_match_check_3:  #86 (line num in coconut source)
        raise _coconut_FunctionMatchError('match def forall_handle(const, prop, expr) =', _coconut_match_args)  #86 (line num in coconut source)

    return _coconut_tail_call(ForAll, const, prop(const) >> expr)  #87 (line num in coconut source)



class Grammar(_coconut.object):  #90 (line num in coconut source)

    lparen = Literal("(").suppress()  #92 (line num in coconut source)
    rparen = Literal(")").suppress()  #93 (line num in coconut source)
    comma = Literal(",").suppress()  #94 (line num in coconut source)
    dot = Literal(".").suppress()  #95 (line num in coconut source)
    equals = Literal("=").suppress()  #96 (line num in coconut source)
    colon = Literal(":").suppress()  #97 (line num in coconut source)
    question = Literal("?").suppress()  #98 (line num in coconut source)

    commalist = _coconut.functools.partial(tokenlist, comma)  #100 (line num in coconut source)

    not_op = oneOf(all_not_syms).suppress()  #102 (line num in coconut source)
    imp_op = oneOf(all_imp_syms).suppress()  #103 (line num in coconut source)
    and_op = oneOf(all_and_syms).suppress()  #104 (line num in coconut source)
    or_op = oneOf(all_or_syms).suppress()  #105 (line num in coconut source)
    forall_op = oneOf(all_forall_syms).suppress()  #106 (line num in coconut source)
    exists_op = oneOf(all_exists_syms).suppress()  #107 (line num in coconut source)

    top_lit = (fixto)(top, oneOf(all_top_syms))  #109 (line num in coconut source)
    bot_lit = (fixto)(bot, oneOf(all_bot_syms))  #110 (line num in coconut source)

    lowercase_name = Regex("[a-z0-9_]\w*'*")  #112 (line num in coconut source)
    uppercase_name = Regex("[A-Z]\w*'*")  #113 (line num in coconut source)

    var = (call)(Constant, lowercase_name)  #115 (line num in coconut source)
    any_var = (call)(Variable, question + lowercase_name)  #116 (line num in coconut source)
    func = Forward()  #117 (line num in coconut source)
    term = func | var | any_var  #118 (line num in coconut source)
    terms = lparen - commalist(term) - rparen  #119 (line num in coconut source)
    func <<= (call)(Function, lowercase_name + terms)  #120 (line num in coconut source)

    prop = (call)(Proposition, uppercase_name)  #122 (line num in coconut source)
    pred = (call)(Predicate, uppercase_name + terms)  #123 (line num in coconut source)
    equality = (call)(Eq, term + equals + term)  #124 (line num in coconut source)
    atom = pred | prop | equality  #125 (line num in coconut source)

    expr = Forward()  #127 (line num in coconut source)
    quant_sep = dot | comma  #128 (line num in coconut source)
    exists = ((call)(exists_handle, exists_op + var + Optional(colon + prop) + quant_sep + expr))  #129 (line num in coconut source)
    forall = ((call)(forall_handle, forall_op + var + Optional(colon + prop) + quant_sep + expr))  #133 (line num in coconut source)
    quant = exists | forall  #137 (line num in coconut source)

    base_expr = top_lit | bot_lit | quant | atom | lparen - expr - rparen  #139 (line num in coconut source)
    not_expr = quant | ((call)(Not, not_op + base_expr)) | base_expr | quant  #140 (line num in coconut source)
    and_expr = quant | ((call)(And, not_expr + OneOrMore(and_op - not_expr))) | not_expr  #141 (line num in coconut source)
    or_expr = quant | ((call)(Or, and_expr + OneOrMore(or_op - and_expr))) | and_expr  #142 (line num in coconut source)
    expr <<= quant | ((call)(Implies, or_expr + OneOrMore(imp_op - or_expr))) | or_expr  #143 (line num in coconut source)

    formula = stringStart + expr + stringEnd  #145 (line num in coconut source)

_coconut_call_set_names(Grammar)  #147 (line num in coconut source)
for varname, val in vars(Grammar).items():  #147 (line num in coconut source)
    if isinstance(val, ParserElement):  #148 (line num in coconut source)
        setattr(Grammar, varname, val.setName(varname))  #149 (line num in coconut source)


# Endpoint:

def expr(formula):  #154 (line num in coconut source)
    """Parses the given formula into an expression."""  #155 (line num in coconut source)
    result = parse(Grammar.formula, formula)  #156 (line num in coconut source)
    assert len(result) == 1, results  #157 (line num in coconut source)
    return result[0]  #158 (line num in coconut source)
