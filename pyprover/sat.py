#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc04fa4d3

# Compiled with Coconut version 3.2.0-post_dev20
# This file was compiled from sat.coco by the Coconut compiler; edit that file rather than this one.
# For a guide to writing Coconut, see http://coconut.readthedocs.io/en/develop/llms.txt (or run 'coconut --ai-docs').

"""A small CDCL SAT solver (conflict-driven clause learning with two watched
literals, VSIDS-style branching, phase saving, and restarts) used for
propositional reasoning and for finite model search."""

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop, annotations
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev20', '310', True)
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

import heapq  #7 (line in Coconut source)
from collections import defaultdict  #8 (line in Coconut source)
from collections import Counter  #8 (line in Coconut source)


# Solver:

def solve_sat(clauses):  #13 (line in Coconut source)
    """Find a satisfying assignment for the given clauses, where each clause
    is an iterable of nonzero ints (negative ints are negated variables).

    Returns a dict mapping each variable to a bool, or None if the clauses
    are unsatisfiable."""  #18 (line in Coconut source)
    return Solver(clauses).solve()  #19 (line in Coconut source)



class Solver():  #22 (line in Coconut source)
    """A CDCL SAT solver. The hot loops are written imperatively (and avoid
    Coconut's enhanced builtins) for speed."""  #24 (line in Coconut source)

    def __init__(self, clauses):  #26 (line in Coconut source)
        self.clauses = []  #27 (line in Coconut source)
        self.watches = defaultdict(list)  #28 (line in Coconut source)
        self.value = {}  # var -> bool  #29 (line in Coconut source)
        self.level = {}  # var -> decision level  #30 (line in Coconut source)
        self.reason = {}  # var -> index of the clause that implied it (or None)  #31 (line in Coconut source)
        self.trail = []  #32 (line in Coconut source)
        self.trail_lim = []  #33 (line in Coconut source)
        self.qhead = 0  #34 (line in Coconut source)
        self.activity = Counter()  #35 (line in Coconut source)
        self.bump_amount = 1.0  #36 (line in Coconut source)
        self.phase = {}  #37 (line in Coconut source)
        self.ok = True  #38 (line in Coconut source)

        units = []  #40 (line in Coconut source)
        for clause in clauses:  #41 (line in Coconut source)
            lits = list(dict.fromkeys(clause))  #42 (line in Coconut source)
            if any((-lit in lits for lit in lits)):  #43 (line in Coconut source)
                continue  #44 (line in Coconut source)
            if not lits:  #45 (line in Coconut source)
                self.ok = False  #46 (line in Coconut source)
                return  #47 (line in Coconut source)
            for lit in lits:  #48 (line in Coconut source)
                self.activity[abs(lit)] += 1  #49 (line in Coconut source)
                self.phase.setdefault(abs(lit), lit > 0)  #50 (line in Coconut source)
            if len(lits) == 1:  #51 (line in Coconut source)
                units.append(lits[0])  #52 (line in Coconut source)
            else:  #53 (line in Coconut source)
                self.add_clause(lits)  #54 (line in Coconut source)
        self.heap = [(-act, var) for var, act in self.activity.items()]  #55 (line in Coconut source)
        heapq.heapify(self.heap)  #56 (line in Coconut source)
        for lit in units:  #57 (line in Coconut source)
            if not self.enqueue(lit, None):  #58 (line in Coconut source)
                self.ok = False  #59 (line in Coconut source)
                return  #60 (line in Coconut source)


    def add_clause(self, lits) -> int:  #62 (line in Coconut source)
        index = len(self.clauses)  #63 (line in Coconut source)
        self.clauses.append(lits)  #64 (line in Coconut source)
        self.watches[lits[0]].append(index)  #65 (line in Coconut source)
        self.watches[lits[1]].append(index)  #66 (line in Coconut source)
        return index  #67 (line in Coconut source)


    def lit_value(self, lit):  #69 (line in Coconut source)
        val = self.value.get(lit if lit > 0 else -lit)  #70 (line in Coconut source)
        if val is None:  #71 (line in Coconut source)
            return None  #72 (line in Coconut source)
        return val if lit > 0 else not val  #73 (line in Coconut source)


    def enqueue(self, lit, reason) -> bool:  #75 (line in Coconut source)
        """Make lit true; return False if it is already false."""  #76 (line in Coconut source)
        val = self.lit_value(lit)  #77 (line in Coconut source)
        if val is not None:  #78 (line in Coconut source)
            return val  #79 (line in Coconut source)
        var = lit if lit > 0 else -lit  #80 (line in Coconut source)
        self.value[var] = lit > 0  #81 (line in Coconut source)
        self.level[var] = len(self.trail_lim)  #82 (line in Coconut source)
        self.reason[var] = reason  #83 (line in Coconut source)
        self.trail.append(lit)  #84 (line in Coconut source)
        return True  #85 (line in Coconut source)


    def propagate(self):  #87 (line in Coconut source)
        """Unit propagate; return the index of a conflicting clause or None."""  #88 (line in Coconut source)
        clauses, watches, lit_value = self.clauses, self.watches, self.lit_value  #89 (line in Coconut source)
        while self.qhead < len(self.trail):  #90 (line in Coconut source)
            false_lit = -self.trail[self.qhead]  #91 (line in Coconut source)
            self.qhead += 1  #92 (line in Coconut source)
            watching = watches[false_lit]  #93 (line in Coconut source)
            kept = []  #94 (line in Coconut source)
            n = 0  #95 (line in Coconut source)
            while n < len(watching):  #96 (line in Coconut source)
                i = watching[n]  #97 (line in Coconut source)
                n += 1  #98 (line in Coconut source)
                lits = clauses[i]  #99 (line in Coconut source)
                if lits[0] == false_lit:  #100 (line in Coconut source)
                    lits[0], lits[1] = lits[1], lits[0]  #101 (line in Coconut source)
                if lit_value(lits[0]) is True:  #102 (line in Coconut source)
                    kept.append(i)  #103 (line in Coconut source)
                    continue  #104 (line in Coconut source)
                k = 2  #105 (line in Coconut source)
                found = False  #106 (line in Coconut source)
                while k < len(lits):  #107 (line in Coconut source)
                    if lit_value(lits[k]) is not False:  #108 (line in Coconut source)
                        lits[1], lits[k] = lits[k], lits[1]  #109 (line in Coconut source)
                        watches[lits[1]].append(i)  #110 (line in Coconut source)
                        found = True  #111 (line in Coconut source)
                        break  #112 (line in Coconut source)
                    k += 1  #113 (line in Coconut source)
                if found:  #114 (line in Coconut source)
                    continue  #115 (line in Coconut source)
                kept.append(i)  #116 (line in Coconut source)
                if not self.enqueue(lits[0], i):  #117 (line in Coconut source)
                    kept.extend(watching[n:])  #118 (line in Coconut source)
                    watches[false_lit] = kept  #119 (line in Coconut source)
                    return i  #120 (line in Coconut source)
            watches[false_lit] = kept  #121 (line in Coconut source)
        return None  #122 (line in Coconut source)


    def bump(self, var):  #124 (line in Coconut source)
        self.activity[var] += self.bump_amount  #125 (line in Coconut source)
        heapq.heappush(self.heap, (-self.activity[var], var))  #126 (line in Coconut source)


    def analyze(self, conflict):  #128 (line in Coconut source)
        """Derive a learned clause by the first unique implication point
        scheme. Returns (learned clause, level to backtrack to)."""  #130 (line in Coconut source)
        current = len(self.trail_lim)  #131 (line in Coconut source)
        learned = [0,]  #132 (line in Coconut source)
        seen = set()  #133 (line in Coconut source)
        counter = 0  #134 (line in Coconut source)
        lit = None  #135 (line in Coconut source)
        index = len(self.trail) - 1  #136 (line in Coconut source)
        clause = self.clauses[conflict]  #137 (line in Coconut source)
        while True:  #138 (line in Coconut source)
            for q in clause:  #139 (line in Coconut source)
                var = q if q > 0 else -q  #140 (line in Coconut source)
                if lit is not None and var == (lit if lit > 0 else -lit):  #141 (line in Coconut source)
                    continue  #142 (line in Coconut source)
                if var not in seen and self.level[var] > 0:  #143 (line in Coconut source)
                    seen.add(var)  #144 (line in Coconut source)
                    self.bump(var)  #145 (line in Coconut source)
                    if self.level[var] == current:  #146 (line in Coconut source)
                        counter += 1  #147 (line in Coconut source)
                    else:  #148 (line in Coconut source)
                        learned.append(q)  #149 (line in Coconut source)
            while abs(self.trail[index]) not in seen:  #150 (line in Coconut source)
                index -= 1  #151 (line in Coconut source)
            lit = self.trail[index]  #152 (line in Coconut source)
            index -= 1  #153 (line in Coconut source)
            seen.discard(abs(lit))  #154 (line in Coconut source)
            counter -= 1  #155 (line in Coconut source)
            if counter == 0:  #156 (line in Coconut source)
                break  #157 (line in Coconut source)
            clause = self.clauses[self.reason[abs(lit)]]  #158 (line in Coconut source)
        learned[0] = -lit  #159 (line in Coconut source)
        if len(learned) == 1:  #160 (line in Coconut source)
            return learned, 0  #161 (line in Coconut source)
# watch the literal from the highest remaining level second
        best = max(range(1, len(learned)), key=(lambda _=None: self.level[abs(learned[_])]))  #163 (line in Coconut source)
        learned[1], learned[best] = learned[best], learned[1]  #164 (line in Coconut source)
        return learned, self.level[abs(learned[1])]  #165 (line in Coconut source)


    def backtrack(self, level):  #167 (line in Coconut source)
        if len(self.trail_lim) <= level:  #168 (line in Coconut source)
            return  #169 (line in Coconut source)
        start = self.trail_lim[level]  #170 (line in Coconut source)
        for lit in self.trail[start:]:  #171 (line in Coconut source)
            var = abs(lit)  #172 (line in Coconut source)
            self.phase[var] = self.value.pop(var)  #173 (line in Coconut source)
            del self.level[var]  #174 (line in Coconut source)
            del self.reason[var]  #175 (line in Coconut source)
            heapq.heappush(self.heap, (-self.activity[var], var))  #176 (line in Coconut source)
        del self.trail[start:]  #177 (line in Coconut source)
        del self.trail_lim[level:]  #178 (line in Coconut source)
        self.qhead = start  #179 (line in Coconut source)


    def pick_branch(self):  #181 (line in Coconut source)
        while self.heap:  #182 (line in Coconut source)
            _, var = heapq.heappop(self.heap)  #183 (line in Coconut source)
            if var not in self.value:  #184 (line in Coconut source)
                return var  #185 (line in Coconut source)
        return None  #186 (line in Coconut source)


    def solve(self):  #188 (line in Coconut source)
        if not self.ok:  #189 (line in Coconut source)
            return None  #190 (line in Coconut source)
        conflicts = 0  #191 (line in Coconut source)
        restart_limit = 100  #192 (line in Coconut source)
        while True:  #193 (line in Coconut source)
            conflict = self.propagate()  #194 (line in Coconut source)
            if conflict is not None:  #195 (line in Coconut source)
                if not self.trail_lim:  #196 (line in Coconut source)
                    return None  #197 (line in Coconut source)
                conflicts += 1  #198 (line in Coconut source)
                learned, level = self.analyze(conflict)  #199 (line in Coconut source)
                self.backtrack(level)  #200 (line in Coconut source)
                if len(learned) == 1:  #201 (line in Coconut source)
                    self.enqueue(learned[0], None)  #202 (line in Coconut source)
                else:  #203 (line in Coconut source)
                    self.enqueue(learned[0], self.add_clause(learned))  #204 (line in Coconut source)
                self.bump_amount /= 0.95  #205 (line in Coconut source)
                if self.bump_amount > 1e100:  #206 (line in Coconut source)
                    for var in self.activity:  #207 (line in Coconut source)
                        self.activity[var] *= 1e-100  #208 (line in Coconut source)
                    self.bump_amount *= 1e-100  #209 (line in Coconut source)
                    self.heap = [(-act, var) for var, act in self.activity.items()]  #210 (line in Coconut source)
                    heapq.heapify(self.heap)  #211 (line in Coconut source)
                if conflicts >= restart_limit:  #212 (line in Coconut source)
                    conflicts = 0  #213 (line in Coconut source)
                    restart_limit = int(restart_limit * 1.5)  #214 (line in Coconut source)
                    self.backtrack(0)  #215 (line in Coconut source)
            else:  #216 (line in Coconut source)
                var = self.pick_branch()  #217 (line in Coconut source)
                if var is None:  #218 (line in Coconut source)
                    return dict(self.value)  #219 (line in Coconut source)
                self.trail_lim.append(len(self.trail))  #220 (line in Coconut source)
                self.enqueue(var if self.phase.get(var, True) else -var, None)  #221 (line in Coconut source)
