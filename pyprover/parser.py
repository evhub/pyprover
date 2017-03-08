#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xfde97e98

# Compiled with Coconut version 1.2.2-post_dev4 [Colonel]

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

import string  # line 3

from pyparsing import Literal  # line 4
from pyparsing import ZeroOrMore  # line 4
from pyparsing import OneOrMore  # line 4
from pyparsing import Optional  # line 4
from pyparsing import oneOf  # line 4
from pyparsing import replaceWith  # line 4
from pyparsing import Regex  # line 4
from pyparsing import Forward  # line 4
from pyparsing import ParserElement  # line 4
from pyparsing import stringStart  # line 4
from pyparsing import stringEnd  # line 5

from pyprover.constants import all_top_syms  # line 6
from pyprover.constants import all_bot_syms  # line 6
from pyprover.constants import all_not_syms  # line 6
from pyprover.constants import all_imp_syms  # line 6
from pyprover.constants import all_and_syms  # line 6
from pyprover.constants import all_or_syms  # line 6
from pyprover.constants import all_forall_syms  # line 6
from pyprover.constants import all_exists_syms  # line 19
from pyprover.logic import top  # line 20
from pyprover.logic import bot  # line 20
from pyprover.logic import Proposition  # line 20
from pyprover.logic import Predicate  # line 20
from pyprover.logic import Constant  # line 20
from pyprover.logic import Function  # line 20
from pyprover.logic import Not  # line 20
from pyprover.logic import Implies  # line 20
from pyprover.logic import And  # line 20
from pyprover.logic import Or  # line 20
from pyprover.logic import Exists  # line 20
from pyprover.logic import ForAll  # line 29

ParserElement.enablePackrat()  # line 44

# Utilities:

def attach(action, item):  # line 48
    """Attaches a parse action to an item."""  # line 49
    return item.copy().addParseAction(action)  # line 50

@_coconut_tco  # line 51
def call(action, item):  # line 52
    """Call an action on the tokens in item."""  # line 53
    @_coconut_tco  # line 54
    def parse_action(o, l, tokens):  # line 54
        raise _coconut_tail_call(action, *tokens)  # line 55
    raise _coconut_tail_call((_coconut.functools.partial(attach, parse_action)), item)  # line 56

@_coconut_tco  # line 57
def fixto(output, item):  # line 58
    """Forces an item to result in a specific output."""  # line 59
    raise _coconut_tail_call((_coconut.functools.partial(attach, replaceWith(output))), item)  # line 60

def tokenlist(sep, item):  # line 62
    """Creates a list of tokens matching the item."""  # line 63
    return item + ZeroOrMore(sep + item) + Optional(sep)  # line 64

def parse(grammar, text):  # line 66
    """Parses text using grammar."""  # line 67
    return grammar.parseWithTabs().parseString(text)  # line 68

# Grammar:

class Grammar(_coconut.object):  # line 72

    lparen = Literal("(").suppress()  # line 74
    rparen = Literal(")").suppress()  # line 75
    comma = Literal(",").suppress()  # line 76
    dot = Literal(".").suppress()  # line 77

    commalist = _coconut.functools.partial(tokenlist, comma)  # line 79

    not_op = oneOf(all_not_syms).suppress()  # line 81
    imp_op = oneOf(all_imp_syms).suppress()  # line 82
    and_op = oneOf(all_and_syms).suppress()  # line 83
    or_op = oneOf(all_or_syms).suppress()  # line 84
    forall_op = oneOf(all_forall_syms).suppress()  # line 85
    exists_op = oneOf(all_exists_syms).suppress()  # line 86

    top_lit = (_coconut.functools.partial(fixto, top))(oneOf(all_top_syms))  # line 88
    bot_lit = (_coconut.functools.partial(fixto, bot))(oneOf(all_bot_syms))  # line 89

    lowercase_name = Regex("[a-z0-9_]\w*")  # line 91
    uppercase_name = Regex("[A-Z]\w*")  # line 92

    var = (_coconut.functools.partial(call, Constant))(lowercase_name)  # line 94
    func = Forward()  # line 95
    term = func | var  # line 96
    terms = lparen - commalist(term) - rparen  # line 97
    func <<= (_coconut.functools.partial(call, Function))(lowercase_name + terms)  # line 98

    prop = (_coconut.functools.partial(call, Proposition))(uppercase_name)  # line 100
    pred = Forward()  # line 101
    atom = pred | prop  # line 102
    pred <<= (_coconut.functools.partial(call, Predicate))(uppercase_name + terms)  # line 103

    expr = Forward()  # line 105
    quant = ((_coconut.functools.partial(call, Exists))(exists_op + var - dot - expr)) | ((_coconut.functools.partial(call, ForAll))(forall_op + var - dot - expr))  # line 106

    base_expr = top_lit | bot_lit | quant | atom | lparen - expr - rparen  # line 108
    not_expr = quant | ((_coconut.functools.partial(call, Not))(not_op + base_expr)) | base_expr | quant  # line 109
    and_expr = quant | ((_coconut.functools.partial(call, And))(not_expr + OneOrMore(and_op - not_expr))) | not_expr  # line 110
    or_expr = quant | ((_coconut.functools.partial(call, Or))(and_expr + OneOrMore(or_op - and_expr))) | and_expr  # line 111
    expr <<= quant | ((_coconut.functools.partial(call, Implies))(or_expr + OneOrMore(imp_op - or_expr))) | or_expr  # line 112

    formula = stringStart + expr + stringEnd  # line 114

for varname, val in vars(Grammar).items():  # line 116
    if isinstance(val, ParserElement):  # line 117
        setattr(Grammar, varname, val.setName(varname))  # line 118

# Endpoint:

def expr(formula):  # line 121
    """Parses the given formula into an expression."""  # line 123
    result = Grammar.formula.parseWithTabs().parseString(formula)  # line 124
    assert len(result) == 1, results  # line 125
    return result[0]  # line 126
