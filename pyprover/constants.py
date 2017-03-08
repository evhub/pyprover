#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xbc169ce2

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

import sys  # line 3

# Utilities:

def first_encodeable(symbols):  # line 7
    for sym in symbols:  # line 8
        try:  # line 9
            if hasattr(sys.stdout, "encoding") and sys.stdout.encoding is not None:  # line 10
                sym.encode(sys.stdout.encoding)  # line 11
            else:  # line 12
                sym.encode()  # line 13
        except UnicodeEncodeError:  # line 14
            pass  # line 15
        else:  # line 16
            return sym  # line 17
    raise ValueError("No encodeable symbol in " + repr(symbols))  # line 18

# Installation:

version = "0.3.0"  # line 22
requirements = []  # line 23
classifiers = ["Development Status :: 3 - Alpha", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries :: Python Modules", "Operating System :: OS Independent",]  # line 24

# Symbols:

all_top_syms = "\u22a4", "\u252c", "-T-", "top", "true"  # line 33
top_sym = (first_encodeable)(all_top_syms)  # line 34

all_bot_syms = "\u22a5", "\u2534", "_|_", "bot", "false"  # line 36
bot_sym = (first_encodeable)(all_bot_syms)  # line 37

all_not_syms = "\xac", "~", "-"  # line 39
not_sym = (first_encodeable)(all_not_syms)  # line 40

all_imp_syms = "\u2192", "->"  # line 42
imp_sym = (first_encodeable)(all_imp_syms)  # line 43

all_and_syms = "\u2227", "/\\", "&"  # line 45
and_sym = (first_encodeable)(all_and_syms)  # line 46

all_or_syms = "\u2228", "\\/", "|"  # line 48
or_sym = (first_encodeable)(all_or_syms)  # line 49

all_forall_syms = "\u2200", "A:", "FA ", "A ", "FA:"  # line 51
forall_sym = (first_encodeable)(all_forall_syms)  # line 52

all_exists_syms = "\u2203", "E:", "TE ", "E ", "TE:"  # line 54
exists_sym = (first_encodeable)(all_exists_syms)  # line 55
