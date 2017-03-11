#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x7c1e2f52

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

import string

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

from pyprover.constants import all_top_syms
from pyprover.constants import all_bot_syms
from pyprover.constants import all_not_syms
from pyprover.constants import all_imp_syms
from pyprover.constants import all_and_syms
from pyprover.constants import all_or_syms
from pyprover.constants import all_forall_syms
from pyprover.constants import all_exists_syms
from pyprover.logic import top
from pyprover.logic import bot
from pyprover.logic import Proposition
from pyprover.logic import Predicate
from pyprover.logic import Constant
from pyprover.logic import Function
from pyprover.logic import Not
from pyprover.logic import Implies
from pyprover.logic import And
from pyprover.logic import Or
from pyprover.logic import Exists
from pyprover.logic import ForAll

ParserElement.enablePackrat()

# Utilities:

def attach(action, item):
    """Attaches a parse action to an item."""
    return item.copy().addParseAction(action)

@_coconut_tco
def call(action, item):
    """Call an action on the tokens in item."""
    @_coconut_tco
    def parse_action(o, l, tokens):
        raise _coconut_tail_call(action, *tokens)
    raise _coconut_tail_call((_coconut.functools.partial(attach, parse_action)), item)

@_coconut_tco
def fixto(output, item):
    """Forces an item to result in a specific output."""
    raise _coconut_tail_call((_coconut.functools.partial(attach, replaceWith(output))), item)

def tokenlist(sep, item):
    """Creates a list of tokens matching the item."""
    return item + ZeroOrMore(sep + item) + Optional(sep)

def parse(grammar, text):
    """Parses text using grammar."""
    return grammar.parseWithTabs().parseString(text)

# Grammar:

class Grammar(_coconut.object):

    lparen = Literal("(").suppress()
    rparen = Literal(")").suppress()
    comma = Literal(",").suppress()
    dot = Literal(".").suppress()

    commalist = _coconut.functools.partial(tokenlist, comma)

    not_op = oneOf(all_not_syms).suppress()
    imp_op = oneOf(all_imp_syms).suppress()
    and_op = oneOf(all_and_syms).suppress()
    or_op = oneOf(all_or_syms).suppress()
    forall_op = oneOf(all_forall_syms).suppress()
    exists_op = oneOf(all_exists_syms).suppress()

    top_lit = (_coconut.functools.partial(fixto, top))(oneOf(all_top_syms))
    bot_lit = (_coconut.functools.partial(fixto, bot))(oneOf(all_bot_syms))

    lowercase_name = Regex("[a-z0-9_]\w*")
    uppercase_name = Regex("[A-Z]\w*")

    var = (_coconut.functools.partial(call, Constant))(lowercase_name)
    func = Forward()
    term = func | var
    terms = lparen - commalist(term) - rparen
    func <<= (_coconut.functools.partial(call, Function))(lowercase_name + terms)

    prop = (_coconut.functools.partial(call, Proposition))(uppercase_name)
    pred = Forward()
    atom = pred | prop
    pred <<= (_coconut.functools.partial(call, Predicate))(uppercase_name + terms)

    expr = Forward()
    quant = ((_coconut.functools.partial(call, Exists))(exists_op + var - dot - expr)) | ((_coconut.functools.partial(call, ForAll))(forall_op + var - dot - expr))

    base_expr = top_lit | bot_lit | quant | atom | lparen - expr - rparen
    not_expr = quant | ((_coconut.functools.partial(call, Not))(not_op + base_expr)) | base_expr | quant
    and_expr = quant | ((_coconut.functools.partial(call, And))(not_expr + OneOrMore(and_op - not_expr))) | not_expr
    or_expr = quant | ((_coconut.functools.partial(call, Or))(and_expr + OneOrMore(or_op - and_expr))) | and_expr
    expr <<= quant | ((_coconut.functools.partial(call, Implies))(or_expr + OneOrMore(imp_op - or_expr))) | or_expr

    formula = stringStart + expr + stringEnd

for varname, val in vars(Grammar).items():
    if isinstance(val, ParserElement):
        setattr(Grammar, varname, val.setName(varname))

# Endpoint:

def expr(formula):
    """Parses the given formula into an expression."""
    result = Grammar.formula.parseWithTabs().parseString(formula)
    assert len(result) == 1, results
    return result[0]
