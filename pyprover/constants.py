#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc50420ba

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

import sys

# Utilities:

def first_encodeable(symbols):
    for sym in symbols:
        try:
            if hasattr(sys.stdout, "encoding") and sys.stdout.encoding is not None:
                sym.encode(sys.stdout.encoding)
            else:
                sym.encode()
        except UnicodeEncodeError:
            pass
        else:
            return sym
    raise ValueError("No encodeable symbol in " + repr(symbols))

# Installation:

version = "0.3.1"
requirements = []
classifiers = ["Development Status :: 3 - Alpha", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries :: Python Modules", "Operating System :: OS Independent",]

# Symbols:

all_top_syms = "\u22a4", "\u252c", "top", "true"
top_sym = (first_encodeable)(all_top_syms)

all_bot_syms = "\u22a5", "\u2534", "bot", "_|_", "false"
bot_sym = (first_encodeable)(all_bot_syms)

all_not_syms = "\xac", "~", "-"
not_sym = (first_encodeable)(all_not_syms)

all_imp_syms = "\u2192", "->"
imp_sym = (first_encodeable)(all_imp_syms)

all_and_syms = "\u2227", "/\\", "&"
and_sym = (first_encodeable)(all_and_syms)

all_or_syms = "\u2228", "\\/", "|"
or_sym = (first_encodeable)(all_or_syms)

all_forall_syms = "\u2200", "A ", "A:", "FA ", "FA:"
forall_sym = (first_encodeable)(all_forall_syms)

all_exists_syms = "\u2203", "E ", "E:", "TE ", "TE:"
exists_sym = (first_encodeable)(all_exists_syms)
