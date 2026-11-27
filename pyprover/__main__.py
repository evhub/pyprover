#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xde7a1e64

# Compiled with Coconut version 3.2.0-post_dev19
# This file was compiled from __main__.coco by the Coconut compiler; edit that file rather than this one.
# For a guide to writing Coconut, see http://coconut.readthedocs.io/en/develop/llms.txt (or run 'coconut --ai-docs').

"""The pyprover command-line interface."""

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

import sys  #5 (line in Coconut source)
import argparse  #6 (line in Coconut source)

from pyprover.constants import version  #8 (line in Coconut source)
from pyprover.constants import default_timeout  #8 (line in Coconut source)
from pyprover.constants import symbols  #8 (line in Coconut source)
from pyprover.constants import use_ascii  #8 (line in Coconut source)
from pyprover.parser import ParseError  #14 (line in Coconut source)
from pyprover.parser import expr  #14 (line in Coconut source)
from pyprover.prover import prove  #18 (line in Coconut source)
from pyprover.normal import nnf  #19 (line in Coconut source)
from pyprover.normal import prenex  #19 (line in Coconut source)
from pyprover.normal import cnf  #19 (line in Coconut source)
from pyprover.normal import dnf  #19 (line in Coconut source)
from pyprover.normal import simplify  #19 (line in Coconut source)
from pyprover.normal import simplest_form  #19 (line in Coconut source)
from pyprover.normal import skolemize  #19 (line in Coconut source)


# Command line:

transformations = {"simplify": (simplify, "simplify a formula (to prenex form with a DNF matrix)"), "simplest": (simplest_form, "find the smaller of a formula's CNF and DNF"), "nnf": (nnf, "convert a formula to negation normal form"), "prenex": (prenex, "convert a formula to prenex normal form"), "cnf": (cnf, "convert a formula to prenex conjunctive normal form"), "dnf": (dnf, "convert a formula to prenex disjunctive normal form"), "skolemize": (skolemize, "convert a formula to Skolem normal form")}  #32 (line in Coconut source)

examples = r"""examples:
  pyprover prove 'A x. F(x) -> G(x)' 'F(a)' 'G(a)'
  pyprover prove --tree '~(P \/ Q)' '~P /\ ~Q'
  pyprover simplify '(A -> B) /\ A'"""  #45 (line in Coconut source)

def make_parser():  #47 (line in Coconut source)
    parser = argparse.ArgumentParser(prog="pyprover", description="A theorem prover for first-order logic with equality.", epilog=examples, formatter_class=argparse.RawDescriptionHelpFormatter)  #48 (line in Coconut source)
    parser.add_argument("--version", action="version", version="%(prog)s " + version)  #54 (line in Coconut source)
    parser.add_argument("--ascii", action="store_true", help="print formulas using only ASCII characters")  #55 (line in Coconut source)
    commands = parser.add_subparsers(dest="command", required=True)  #56 (line in Coconut source)

    prove_parser = commands.add_parser("prove", help="prove a conclusion from zero or more premises")  #58 (line in Coconut source)
    prove_parser.add_argument("formulas", nargs="+", metavar="formula", help="the premises followed by the conclusion")  #59 (line in Coconut source)
    prove_parser.add_argument("--strict", action="store_true", help="don't assume that something exists")  #60 (line in Coconut source)
    prove_parser.add_argument("--timeout", type=float, default=default_timeout, help="give up after this many seconds (default: {_coconut_format_0})".format(_coconut_format_0=(default_timeout)))  #61 (line in Coconut source)
    style = prove_parser.add_mutually_exclusive_group()  #62 (line in Coconut source)
    style.add_argument("--tree", action="store_true", help="print the proof as a tree")  #63 (line in Coconut source)
    style.add_argument("--dot", action="store_true", help="print the proof as a Graphviz DOT graph")  #64 (line in Coconut source)
    style.add_argument("--quiet", "-q", action="store_true", help="only print the result")  #65 (line in Coconut source)

    for name, (_, help_text) in transformations.items():  #67 (line in Coconut source)
        sub = commands.add_parser(name, help=help_text)  #68 (line in Coconut source)
        sub.add_argument("formula")  #69 (line in Coconut source)
        sub.add_argument("--strict", action="store_true", help="don't assume that something exists")  #70 (line in Coconut source)
    return parser  #71 (line in Coconut source)


def main(args=None) -> int:  #73 (line in Coconut source)
    """Run the pyprover command-line interface."""  #74 (line in Coconut source)
    opts = make_parser().parse_args(args)  #75 (line in Coconut source)
    saved_symbols = symbols.copy()  #76 (line in Coconut source)
    if opts.ascii:  #77 (line in Coconut source)
        use_ascii()  #78 (line in Coconut source)
    try:  #79 (line in Coconut source)
        _coconut_case_match_to_0 = opts.command  #80 (line in Coconut source)
        _coconut_case_match_check_0 = False  #80 (line in Coconut source)
        if _coconut_case_match_to_0 == "prove":  #80 (line in Coconut source)
            _coconut_case_match_check_0 = True  #80 (line in Coconut source)
        if _coconut_case_match_check_0:  #80 (line in Coconut source)
            *premises, conclusion = map(expr, opts.formulas)  #82 (line in Coconut source)
            result = prove(premises, conclusion, nonempty_universe=not opts.strict, timeout=opts.timeout)  #83 (line in Coconut source)
            if opts.quiet:  #84 (line in Coconut source)
                print(result.status)  #85 (line in Coconut source)
            elif opts.dot:  #86 (line in Coconut source)
                print(result.to_dot())  #87 (line in Coconut source)
            elif opts.tree and result.steps:  #88 (line in Coconut source)
                print(result.tree())  #89 (line in Coconut source)
            else:  #90 (line in Coconut source)
                print(result)  #91 (line in Coconut source)
            return {"proved": 0, "disproved": 1}.get(result.status, 2)  #92 (line in Coconut source)
        if not _coconut_case_match_check_0:  #93 (line in Coconut source)
            _coconut_match_set_name_name = _coconut_sentinel  #93 (line in Coconut source)
            _coconut_match_set_name_name = _coconut_case_match_to_0  #93 (line in Coconut source)
            _coconut_case_match_check_0 = True  #93 (line in Coconut source)
            if _coconut_case_match_check_0:  #93 (line in Coconut source)
                if _coconut_match_set_name_name is not _coconut_sentinel:  #93 (line in Coconut source)
                    name = _coconut_match_set_name_name  #93 (line in Coconut source)
            if _coconut_case_match_check_0:  #93 (line in Coconut source)
                kwargs = {} if name in ("nnf", "skolemize") else {"nonempty_universe": not opts.strict}  #94 (line in Coconut source)
                transform, _ = transformations[name]  #95 (line in Coconut source)
                print(transform(expr(opts.formula), **kwargs))  #96 (line in Coconut source)
                return 0  #97 (line in Coconut source)
    except ParseError as err:  #98 (line in Coconut source)
        print("pyprover: error: could not parse formula: " + str(err), file=sys.stderr)  #99 (line in Coconut source)
        return 3  #100 (line in Coconut source)
    finally:  #101 (line in Coconut source)
        symbols.update(saved_symbols)  #102 (line in Coconut source)


if __name__ == "__main__":  #104 (line in Coconut source)
    sys.exit(main())  #105 (line in Coconut source)
