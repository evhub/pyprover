#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x8a660474

# Compiled with Coconut version 1.5.0-post_dev58 [Fish License]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
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
                type(_coconut_v).__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)
# Compiled Coconut: -----------------------------------------------------------

# Imports:

from pyparsing import Literal
from pyparsing import ZeroOrMore
from pyparsing import OneOrMore
from pyparsing import Optional
from pyparsing import oneOf
from pyparsing import replaceWith
from pyparsing import Regex
from pyparsing import Forward
from pyparsing import ParserElement
from pyparsing import stringStart
from pyparsing import stringEnd

from pxprover.constants import all_top_syms
from pxprover.constants import all_bot_syms
from pxprover.constants import all_not_syms
from pxprover.constants import all_imp_syms
from pxprover.constants import all_and_syms
from pxprover.constants import all_or_syms
from pxprover.constants import all_forall_syms
from pxprover.constants import all_exists_syms
from pxprover.logic import top
from pxprover.logic import bot
from pxprover.logic import Proposition
from pxprover.logic import Predicate
from pxprover.logic import Constant
from pxprover.logic import Function
from pxprover.logic import Not
from pxprover.logic import Implies
from pxprover.logic import And
from pxprover.logic import Or
from pxprover.logic import Exists
from pxprover.logic import ForAll
from pxprover.logic import Eq

ParserElement.enablePackrat()

oneOf = _coconut_forward_compose(list, oneOf)

# Utilities:

@_coconut_tco
def attach(action, item):
    """Attaches a parse action to an item."""
    return _coconut_tail_call(item.copy().addParseAction, action)

@_coconut_tco
def call(action, item):
    """Call an action on the tokens in item."""
    @_coconut_tco
    def parse_action(o, l, tokens):
        return _coconut_tail_call(action, *tokens)
    return _coconut_tail_call((attach), parse_action, item)

@_coconut_tco
def fixto(output, item):
    """Forces an item to result in a specific output."""
    return _coconut_tail_call((attach), replaceWith(output), item)

def tokenlist(sep, item):
    """Creates a list of tokens matching the item."""
    return item + ZeroOrMore(sep + item) + Optional(sep)

@_coconut_tco
def parse(grammar, text):
    """Parses text using grammar."""
    return _coconut_tail_call(grammar.parseWithTabs().parseString, text)

# Grammar:

@_coconut_tco
@_coconut_mark_as_match
def exists_handle(*_coconut_match_args, **_coconut_match_kwargs):
    _coconut_match_check_0 = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "const" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "expr" in _coconut_match_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("const")
        _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("expr")
        if not _coconut_match_kwargs:
            const = _coconut_match_temp_0
            expr = _coconut_match_temp_1
            _coconut_match_check_0 = True
    if not _coconut_match_check_0:
        raise _coconut_FunctionMatchError('match def exists_handle(const, expr) = Exists(const, expr)', _coconut_match_args)

    return _coconut_tail_call(Exists, const, expr)

@addpattern(exists_handle)
@_coconut_tco
@_coconut_mark_as_match
def exists_handle(*_coconut_match_args, **_coconut_match_kwargs):
    _coconut_match_check_1 = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_args) <= 3) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "const" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "prop" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "expr" in _coconut_match_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("const")
        _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("prop")
        _coconut_match_temp_2 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("expr")
        if not _coconut_match_kwargs:
            const = _coconut_match_temp_0
            prop = _coconut_match_temp_1
            expr = _coconut_match_temp_2
            _coconut_match_check_1 = True
    if not _coconut_match_check_1:
        raise _coconut_FunctionMatchError('match def exists_handle(const, prop, expr) =', _coconut_match_args)

    return _coconut_tail_call(Exists, const, prop(const) & expr)

@_coconut_tco
@_coconut_mark_as_match
def forall_handle(*_coconut_match_args, **_coconut_match_kwargs):
    _coconut_match_check_2 = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "const" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "expr" in _coconut_match_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("const")
        _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("expr")
        if not _coconut_match_kwargs:
            const = _coconut_match_temp_0
            expr = _coconut_match_temp_1
            _coconut_match_check_2 = True
    if not _coconut_match_check_2:
        raise _coconut_FunctionMatchError('match def forall_handle(const, expr) = ForAll(const, expr)', _coconut_match_args)

    return _coconut_tail_call(ForAll, const, expr)

@addpattern(forall_handle)
@_coconut_tco
@_coconut_mark_as_match
def forall_handle(*_coconut_match_args, **_coconut_match_kwargs):
    _coconut_match_check_3 = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_args) <= 3) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "const" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "prop" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "expr" in _coconut_match_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("const")
        _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("prop")
        _coconut_match_temp_2 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("expr")
        if not _coconut_match_kwargs:
            const = _coconut_match_temp_0
            prop = _coconut_match_temp_1
            expr = _coconut_match_temp_2
            _coconut_match_check_3 = True
    if not _coconut_match_check_3:
        raise _coconut_FunctionMatchError('match def forall_handle(const, prop, expr) =', _coconut_match_args)

    return _coconut_tail_call(ForAll, const, prop(const) >> expr)

class Grammar(_coconut.object):

    lparen = Literal("(").suppress()
    rparen = Literal(")").suppress()
    comma = Literal(",").suppress()
    dot = Literal(".").suppress()
    equals = Literal("=").suppress()
    colon = Literal(":").suppress()

    commalist = _coconut.functools.partial(tokenlist, comma)

    not_op = oneOf(all_not_syms).suppress()
    imp_op = oneOf(all_imp_syms).suppress()
    and_op = oneOf(all_and_syms).suppress()
    or_op = oneOf(all_or_syms).suppress()
    forall_op = oneOf(all_forall_syms).suppress()
    exists_op = oneOf(all_exists_syms).suppress()

    top_lit = (fixto)(top, oneOf(all_top_syms))
    bot_lit = (fixto)(bot, oneOf(all_bot_syms))

    lowercase_name = Regex("[a-z0-9_]\w*")
    uppercase_name = Regex("[A-Z]\w*")

    var = (call)(Constant, lowercase_name)
    func = Forward()
    term = func | var
    terms = lparen - commalist(term) - rparen
    func <<= (call)(Function, lowercase_name + terms)

    prop = (call)(Proposition, uppercase_name)
    pred = (call)(Predicate, uppercase_name + terms)
    equality = (call)(Eq, term + equals + term)
    atom = pred | prop | equality

    expr = Forward()
    quant_sep = dot | comma
    exists = ((call)(exists_handle, exists_op + var + Optional(colon + prop) + quant_sep + expr))
    forall = ((call)(forall_handle, forall_op + var + Optional(colon + prop) + quant_sep + expr))
    quant = exists | forall

    base_expr = top_lit | bot_lit | quant | atom | lparen - expr - rparen
    not_expr = quant | ((call)(Not, not_op + base_expr)) | base_expr | quant
    and_expr = quant | ((call)(And, not_expr + OneOrMore(and_op - not_expr))) | not_expr
    or_expr = quant | ((call)(Or, and_expr + OneOrMore(or_op - and_expr))) | and_expr
    expr <<= quant | ((call)(Implies, or_expr + OneOrMore(imp_op - or_expr))) | or_expr

    formula = stringStart + expr + stringEnd

_coconut_call_set_names(Grammar)
for varname, val in vars(Grammar).items():
    if isinstance(val, ParserElement):
        setattr(Grammar, varname, val.setName(varname))

# Endpoint:

def expr(formula):
    """Parses the given formula into an expression."""
    result = parse(Grammar.formula, formula)
    assert len(result) == 1, results
    return result[0]
