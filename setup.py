#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x360771f7

# Compiled with Coconut version 1.5.0-post_dev58 [Fish License]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    from __builtin__ import chr, filter, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate, raw_input, xrange
    py_chr, py_hex, py_input, py_int, py_map, py_object, py_oct, py_open, py_print, py_range, py_str, py_zip, py_filter, py_reversed, py_enumerate, py_raw_input, py_xrange, py_repr = chr, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate, raw_input, xrange, repr
    _coconut_py_raw_input, _coconut_py_xrange, _coconut_py_int, _coconut_py_long, _coconut_py_print, _coconut_py_str, _coconut_py_unicode, _coconut_py_repr = raw_input, xrange, int, long, print, str, unicode, repr
    from future_builtins import *
    chr, str = unichr, unicode
    from io import open
    class object(object):
        __slots__ = ()
        def __ne__(self, other):
            eq = self == other
            return _coconut.NotImplemented if eq is _coconut.NotImplemented else not eq
    class int(_coconut_py_int):
        __slots__ = ()
        if hasattr(_coconut_py_int, "__doc__"):
            __doc__ = _coconut_py_int.__doc__
        class __metaclass__(type):
            def __instancecheck__(cls, inst):
                return _coconut.isinstance(inst, (_coconut_py_int, _coconut_py_long))
            def __subclasscheck__(cls, subcls):
                return _coconut.issubclass(subcls, (_coconut_py_int, _coconut_py_long))
    class range(object):
        __slots__ = ("_xrange",)
        if hasattr(_coconut_py_xrange, "__doc__"):
            __doc__ = _coconut_py_xrange.__doc__
        def __init__(self, *args):
            self._xrange = _coconut_py_xrange(*args)
        def __iter__(self):
            return _coconut.iter(self._xrange)
        def __reversed__(self):
            return _coconut.reversed(self._xrange)
        def __len__(self):
            return _coconut.len(self._xrange)
        def __contains__(self, elem):
            return elem in self._xrange
        def __getitem__(self, index):
            if _coconut.isinstance(index, _coconut.slice):
                args = _coconut.slice(*self._args)
                start, stop, step = (args.start if args.start is not None else 0), args.stop, (args.step if args.step is not None else 1)
                if index.start is None:
                    new_start = start if index.step is None or index.step >= 0 else stop - step
                elif index.start >= 0:
                    new_start = start + step * index.start
                    if (step >= 0 and new_start >= stop) or (step < 0 and new_start <= stop):
                        new_start = stop
                else:
                    new_start = stop + step * index.start
                    if (step >= 0 and new_start <= start) or (step < 0 and new_start >= start):
                        new_start = start
                if index.stop is None:
                    new_stop = stop if index.step is None or index.step >= 0 else start - step
                elif index.stop >= 0:
                    new_stop = start + step * index.stop
                    if (step >= 0 and new_stop >= stop) or (step < 0 and new_stop <= stop):
                        new_stop = stop
                else:
                    new_stop = stop + step * index.stop
                    if (step >= 0 and new_stop <= start) or (step < 0 and new_stop >= start):
                        new_stop = start
                new_step = step if index.step is None else step * index.step
                return self.__class__(new_start, new_stop, new_step)
            else:
                return self._xrange[index]
        def count(self, elem):
            """Count the number of times elem appears in the range."""
            return _coconut_py_int(elem in self._xrange)
        def index(self, elem):
            """Find the index of elem in the range."""
            if elem not in self._xrange: raise _coconut.ValueError(_coconut.repr(elem) + " is not in range")
            start, _, step = self._xrange.__reduce_ex__(2)[1]
            return (elem - start) // step
        def __repr__(self):
            return _coconut.repr(self._xrange)[1:]
        @property
        def _args(self):
            return self._xrange.__reduce__()[1]
        def __reduce_ex__(self, protocol):
            return (self.__class__, self._xrange.__reduce_ex__(protocol)[1])
        def __reduce__(self):
            return self.__reduce_ex__(_coconut.pickle.DEFAULT_PROTOCOL)
        def __hash__(self):
            return _coconut.hash(self._args)
        def __copy__(self):
            return self.__class__(*self._args)
        def __eq__(self, other):
            return self.__class__ is other.__class__ and self._args == other._args
    from collections import Sequence as _coconut_Sequence
    _coconut_Sequence.register(range)
    from functools import wraps as _coconut_wraps
    @_coconut_wraps(_coconut_py_print)
    def print(*args, **kwargs):
        file = kwargs.get("file", _coconut_sys.stdout)
        if "flush" in kwargs:
            flush = kwargs["flush"]
            del kwargs["flush"]
        else:
            flush = False
        if _coconut.getattr(file, "encoding", None) is not None:
            _coconut_py_print(*(_coconut_py_unicode(x).encode(file.encoding) for x in args), **kwargs)
        else:
            _coconut_py_print(*args, **kwargs)
        if flush:
            file.flush()
    @_coconut_wraps(_coconut_py_raw_input)
    def input(*args, **kwargs):
        if _coconut.getattr(_coconut_sys.stdout, "encoding", None) is not None:
            return _coconut_py_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
        return _coconut_py_raw_input(*args, **kwargs).decode()
    @_coconut_wraps(_coconut_py_repr)
    def repr(obj):
        import __builtin__
        try:
            __builtin__.repr = _coconut_repr
            if isinstance(obj, _coconut_py_unicode):
                return _coconut_py_unicode(_coconut_py_repr(obj)[1:])
            if isinstance(obj, _coconut_py_str):
                return "b" + _coconut_py_unicode(_coconut_py_repr(obj))
            return _coconut_py_unicode(_coconut_py_repr(obj))
        finally:
            __builtin__.repr = _coconut_py_repr
    ascii = _coconut_repr = repr
    def raw_input(*args):
        """Coconut uses Python 3 'input' instead of Python 2 'raw_input'."""
        raise _coconut.NameError("Coconut uses Python 3 'input' instead of Python 2 'raw_input'")
    def xrange(*args):
        """Coconut uses Python 3 'range' instead of Python 2 'xrange'."""
        raise _coconut.NameError("Coconut uses Python 3 'range' instead of Python 2 'xrange'")
    def _coconut_default_breakpointhook(*args, **kwargs):
        hookname = _coconut.os.getenv("PYTHONBREAKPOINT")
        if hookname != "0":
            if not hookname:
                hookname = "pdb.set_trace"
            modname, dot, funcname = hookname.rpartition(".")
            if not dot:
                modname = "builtins" if _coconut_sys.version_info >= (3,) else "__builtin__"
            if _coconut_sys.version_info >= (2, 7):
                import importlib
                module = importlib.import_module(modname)
            else:
                import imp
                module = imp.load_module(modname, *imp.find_module(modname))
            hook = _coconut.getattr(module, funcname)
            return hook(*args, **kwargs)
    if not hasattr(_coconut_sys, "__breakpointhook__"):
        _coconut_sys.__breakpointhook__ = _coconut_default_breakpointhook
    def breakpoint(*args, **kwargs):
        return _coconut.getattr(_coconut_sys, "breakpointhook", _coconut_default_breakpointhook)(*args, **kwargs)
    if _coconut_sys.version_info < (2, 7):
        import functools as _coconut_functools, copy_reg as _coconut_copy_reg
        def _coconut_new_partial(func, args, keywords):
            return _coconut_functools.partial(func, *(args if args is not None else ()), **(keywords if keywords is not None else {}))
        _coconut_copy_reg.constructor(_coconut_new_partial)
        def _coconut_reduce_partial(self):
            return (_coconut_new_partial, (self.func, self.args, self.keywords))
        _coconut_copy_reg.pickle(_coconut_functools.partial, _coconut_reduce_partial)
else:
    from builtins import chr, filter, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate
    py_chr, py_hex, py_input, py_int, py_map, py_object, py_oct, py_open, py_print, py_range, py_str, py_zip, py_filter, py_reversed, py_enumerate, py_repr = chr, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate, repr
    _coconut_py_str = str
    if _coconut_sys.version_info < (3, 7):
        def _coconut_default_breakpointhook(*args, **kwargs):
            hookname = _coconut.os.getenv("PYTHONBREAKPOINT")
            if hookname != "0":
                if not hookname:
                    hookname = "pdb.set_trace"
                modname, dot, funcname = hookname.rpartition(".")
                if not dot:
                    modname = "builtins" if _coconut_sys.version_info >= (3,) else "__builtin__"
                if _coconut_sys.version_info >= (2, 7):
                    import importlib
                    module = importlib.import_module(modname)
                else:
                    import imp
                    module = imp.load_module(modname, *imp.find_module(modname))
                hook = _coconut.getattr(module, funcname)
                return hook(*args, **kwargs)
        if not hasattr(_coconut_sys, "__breakpointhook__"):
            _coconut_sys.__breakpointhook__ = _coconut_default_breakpointhook
        def breakpoint(*args, **kwargs):
            return _coconut.getattr(_coconut_sys, "breakpointhook", _coconut_default_breakpointhook)(*args, **kwargs)
    else:
        py_breakpoint = breakpoint
class _coconut(object):
    import collections, copy, functools, types, itertools, operator, threading, os, warnings, contextlib, traceback, weakref
    if _coconut_sys.version_info < (3, 2):
        try:
            from backports.functools_lru_cache import lru_cache
            functools.lru_cache = lru_cache
        except ImportError: pass
    if _coconut_sys.version_info < (3, 4):
        try:
            import trollius as asyncio
        except ImportError:
            class you_need_to_install_trollius: pass
            asyncio = you_need_to_install_trollius()
    else:
        import asyncio
    if _coconut_sys.version_info < (3,):
        import cPickle as pickle
    else:
        import pickle
    OrderedDict = collections.OrderedDict if _coconut_sys.version_info >= (2, 7) else dict
    if _coconut_sys.version_info < (3, 3):
        abc = collections
    else:
        import collections.abc as abc
    if _coconut_sys.version_info < (3, 6):
        class typing(object):
            @staticmethod
            def NamedTuple(name, fields):
                return _coconut.collections.namedtuple(name, [x for x, t in fields])
    else:
        import typing
    zip_longest = itertools.zip_longest if _coconut_sys.version_info >= (3,) else itertools.izip_longest
    Ellipsis, NotImplemented, NotImplementedError, Exception, AttributeError, ImportError, IndexError, KeyError, NameError, TypeError, ValueError, StopIteration, RuntimeError, any, bytes, classmethod, dict, enumerate, filter, float, frozenset, getattr, hasattr, hash, id, int, isinstance, issubclass, iter, len, list, locals, map, min, max, next, object, print, property, range, reversed, set, slice, str, sum, super, tuple, type, vars, zip, repr, bytearray = Ellipsis, NotImplemented, NotImplementedError, Exception, AttributeError, ImportError, IndexError, KeyError, NameError, TypeError, ValueError, StopIteration, RuntimeError, any, bytes, classmethod, dict, enumerate, filter, float, frozenset, getattr, hasattr, hash, id, int, isinstance, issubclass, iter, len, list, locals, map, min, max, next, object, print, property, range, reversed, set, slice, str, sum, super, tuple, type, vars, zip, staticmethod(repr), bytearray
_coconut_sentinel = _coconut.object()
class MatchError(Exception):
    """Pattern-matching error. Has attributes .pattern, .value, and .message."""
    __slots__ = ("pattern", "value", "_message")
    max_val_repr_len = 500
    def __init__(self, pattern, value):
        self.pattern = pattern
        self.value = value
        self._message = None
    @property
    def message(self):
        if self._message is None:
            value_repr = _coconut.repr(self.value)
            self._message = "pattern-matching failed for %s in %s" % (_coconut.repr(self.pattern), value_repr if _coconut.len(value_repr) <= self.max_val_repr_len else value_repr[:self.max_val_repr_len] + "...")
            Exception.__init__(self, self._message)
        return self._message
    def __repr__(self):
        self.message
        return Exception.__repr__(self)
    def __str__(self):
        self.message
        return Exception.__str__(self)
    def __unicode__(self):
        self.message
        return Exception.__unicode__(self)
    def __reduce__(self):
        return (self.__class__, (self.pattern, self.value))
class _coconut_tail_call(object):
    __slots__ = ("func", "args", "kwargs")
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
_coconut_tco_func_dict = {}
def _coconut_tco(func):
    @_coconut.functools.wraps(func)
    def tail_call_optimized_func(*args, **kwargs):
        call_func = func
        while True:
            if _coconut.isinstance(call_func, _coconut_base_pattern_func):
                call_func = call_func._coconut_tco_func
            elif _coconut.isinstance(call_func, _coconut.types.MethodType):
                wkref = _coconut_tco_func_dict.get(_coconut.id(call_func.__func__))
                wkref_func = None if wkref is None else wkref()
                if wkref_func is call_func.__func__:
                    if call_func.__self__ is None:
                        call_func = call_func._coconut_tco_func
                    else:
                        call_func = _coconut.functools.partial(call_func._coconut_tco_func, call_func.__self__)
            else:
                wkref = _coconut_tco_func_dict.get(_coconut.id(call_func))
                wkref_func = None if wkref is None else wkref()
                if wkref_func is call_func:
                    call_func = call_func._coconut_tco_func
            result = call_func(*args, **kwargs)  # pass --no-tco to clean up your traceback
            if not isinstance(result, _coconut_tail_call):
                return result
            call_func, args, kwargs = result.func, result.args, result.kwargs
    tail_call_optimized_func._coconut_tco_func = func
    tail_call_optimized_func.__module__ = _coconut.getattr(func, "__module__", None)
    tail_call_optimized_func.__name__ = _coconut.getattr(func, "__name__", "<coconut tco function (pass --no-tco to remove)>")
    tail_call_optimized_func.__qualname__ = _coconut.getattr(func, "__qualname__", tail_call_optimized_func.__name__)
    _coconut_tco_func_dict[_coconut.id(tail_call_optimized_func)] = _coconut.weakref.ref(tail_call_optimized_func)
    return tail_call_optimized_func
def _coconut_igetitem(iterable, index):
    obj_igetitem = _coconut.getattr(iterable, "__igetitem__", None)
    if obj_igetitem is None:
        obj_igetitem = _coconut.getattr(iterable, "__getitem__", None)
    if obj_igetitem is not None:
        try:
            result = obj_igetitem(index)
        except _coconut.NotImplementedError:
            pass
        else:
            if result is not _coconut.NotImplemented:
                return result
    if not _coconut.isinstance(index, _coconut.slice):
        if index < 0:
            return _coconut.collections.deque(iterable, maxlen=-index)[0]
        try:
            return _coconut.next(_coconut.itertools.islice(iterable, index, index + 1))
        except _coconut.StopIteration:
            raise _coconut.IndexError("$[] index out of range")
    if index.start is not None and index.start < 0 and (index.stop is None or index.stop < 0) and index.step is None:
        queue = _coconut.collections.deque(iterable, maxlen=-index.start)
        if index.stop is not None:
            queue = _coconut.list(queue)[:index.stop - index.start]
        return queue
    if (index.start is None or index.start == 0) and index.stop is None and index.step is not None and index.step == -1:
        obj_reversed = _coconut.getattr(iterable, "__reversed__", None)
        if obj_reversed is not None:
            try:
                result = obj_reversed()
            except _coconut.NotImplementedError:
                pass
            else:
                if result is not _coconut.NotImplemented:
                    return result
    if (index.start is not None and index.start < 0) or (index.stop is not None and index.stop < 0) or (index.step is not None and index.step < 0):
        return _coconut.list(iterable)[index]
    return _coconut.itertools.islice(iterable, index.start, index.stop, index.step)
class _coconut_base_compose(object):
    __slots__ = ("func", "funcstars")
    def __init__(self, func, *funcstars):
        self.func = func
        self.funcstars = []
        for f, stars in funcstars:
            if _coconut.isinstance(f, _coconut_base_compose):
                self.funcstars.append((f.func, stars))
                self.funcstars += f.funcstars
            else:
                self.funcstars.append((f, stars))
    def __call__(self, *args, **kwargs):
        arg = self.func(*args, **kwargs)
        for f, stars in self.funcstars:
            if stars == 0:
                arg = f(arg)
            elif stars == 1:
                arg = f(*arg)
            elif stars == 2:
                arg = f(**arg)
            else:
                raise _coconut.ValueError("invalid arguments to " + _coconut.repr(self))
        return arg
    def __repr__(self):
        return _coconut.repr(self.func) + " " + " ".join(("..*> " if star == 1 else "..**>" if star == 2 else "..> ") + _coconut.repr(f) for f, star in self.funcstars)
    def __reduce__(self):
        return (self.__class__, (self.func,) + _coconut.tuple(self.funcstars))
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return _coconut.functools.partial(self, obj)
def _coconut_forward_compose(func, *funcs): return _coconut_base_compose(func, *((f, 0) for f in funcs))
def _coconut_back_compose(*funcs): return _coconut_forward_compose(*_coconut.reversed(funcs))
def _coconut_forward_star_compose(func, *funcs): return _coconut_base_compose(func, *((f, 1) for f in funcs))
def _coconut_back_star_compose(*funcs): return _coconut_forward_star_compose(*_coconut.reversed(funcs))
def _coconut_forward_dubstar_compose(func, *funcs): return _coconut_base_compose(func, *((f, 2) for f in funcs))
def _coconut_back_dubstar_compose(*funcs): return _coconut_forward_dubstar_compose(*_coconut.reversed(funcs))
def _coconut_pipe(x, f): return f(x)
def _coconut_star_pipe(xs, f): return f(*xs)
def _coconut_dubstar_pipe(kws, f): return f(**kws)
def _coconut_back_pipe(f, x): return f(x)
def _coconut_back_star_pipe(f, xs): return f(*xs)
def _coconut_back_dubstar_pipe(f, kws): return f(**kws)
def _coconut_none_pipe(x, f): return None if x is None else f(x)
def _coconut_none_star_pipe(xs, f): return None if xs is None else f(*xs)
def _coconut_none_dubstar_pipe(kws, f): return None if kws is None else f(**kws)
def _coconut_assert(cond, msg=None): assert cond, msg if msg is not None else "(assert) got falsey value " + _coconut.repr(cond)
def _coconut_bool_and(a, b): return a and b
def _coconut_bool_or(a, b): return a or b
def _coconut_none_coalesce(a, b): return a if a is not None else b
def _coconut_minus(a, *rest):
    if not rest:
        return -a
    for b in rest:
        a = a - b
    return a
@_coconut.functools.wraps(_coconut.itertools.tee)
def tee(iterable, n=2):
    if n >= 0 and _coconut.isinstance(iterable, (_coconut.tuple, _coconut.frozenset)):
        return (iterable,) * n
    if n > 0 and (_coconut.isinstance(iterable, _coconut.abc.Sequence) or _coconut.getattr(iterable, "__copy__", None) is not None):
        return (iterable,) + _coconut.tuple(_coconut.copy.copy(iterable) for _ in _coconut.range(n - 1))
    return _coconut.itertools.tee(iterable, n)
class reiterable(object):
    """Allows an iterator to be iterated over multiple times."""
    __slots__ = ("lock", "iter")
    def __new__(cls, iterable):
        if _coconut.isinstance(iterable, _coconut_reiterable):
            return iterable
        self = _coconut.object.__new__(cls)
        self.lock = _coconut.threading.Lock()
        self.iter = iterable
        return self
    def get_new_iter(self):
        with self.lock:
            self.iter, new_iter = _coconut_tee(self.iter)
        return new_iter
    def __iter__(self):
        return _coconut.iter(self.get_new_iter())
    def __getitem__(self, index):
        return _coconut_igetitem(self.get_new_iter(), index)
    def __reversed__(self):
        return _coconut_reversed(self.get_new_iter())
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "reiterable(%r)" % (self.iter,)
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __copy__(self):
        return self.__class__(self.get_new_iter())
    def __fmap__(self, func):
        return _coconut_map(func, self)
class scan(object):
    """Reduce func over iterable, yielding intermediate results,
    optionally starting from initializer."""
    __slots__ = ("func", "iter", "initializer")
    def __init__(self, function, iterable, initializer=_coconut_sentinel):
        self.func = function
        self.iter = iterable
        self.initializer = initializer
    def __iter__(self):
        acc = self.initializer
        if acc is not _coconut_sentinel:
            yield acc
        for item in self.iter:
            if acc is _coconut_sentinel:
                acc = item
            else:
                acc = self.func(acc, item)
            yield acc
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "scan(%r, %r)" % (self.func, self.iter) if self.initializer is _coconut_sentinel else "scan(%r, %r, %r)" % (self.func, self.iter, self.initializer)
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter, self.initializer))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class reversed(object):
    __slots__ = ("iter",)
    if hasattr(_coconut.map, "__doc__"):
        __doc__ = _coconut.reversed.__doc__
    def __new__(cls, iterable):
        if _coconut.isinstance(iterable, _coconut.range):
            return iterable[::-1]
        if not _coconut.hasattr(iterable, "__reversed__") or _coconut.isinstance(iterable, (_coconut.list, _coconut.tuple)):
            return _coconut.object.__new__(cls)
        return _coconut.reversed(iterable)
    def __init__(self, iterable):
        self.iter = iterable
    def __iter__(self):
        return _coconut.iter(_coconut.reversed(self.iter))
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return _coconut_igetitem(self.iter, _coconut.slice(-(index.start + 1) if index.start is not None else None, -(index.stop + 1) if index.stop else None, -(index.step if index.step is not None else 1)))
        return _coconut_igetitem(self.iter, -(index + 1))
    def __reversed__(self):
        return self.iter
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "reversed(%r)" % (self.iter,)
    def __hash__(self):
        return _coconut.hash((self.__class__, self.iter))
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.iter == other.iter
    def __contains__(self, elem):
        return elem in self.iter
    def count(self, elem):
        """Count the number of times elem appears in the reversed iterable."""
        return self.iter.count(elem)
    def index(self, elem):
        """Find the index of elem in the reversed iterable."""
        return _coconut.len(self.iter) - self.iter.index(elem) - 1
    def __fmap__(self, func):
        return self.__class__(_coconut_map(func, self.iter))
class flatten(object):
    """Flatten an iterable of iterables into a single iterable."""
    __slots__ = ("iter",)
    def __init__(self, iterable):
        self.iter = iterable
    def __iter__(self):
        return _coconut.itertools.chain.from_iterable(self.iter)
    def __reversed__(self):
        return self.__class__(_coconut_reversed(_coconut_map(_coconut_reversed, self.iter)))
    def __len__(self):
        return _coconut.sum(_coconut_map(_coconut.len, self.iter))
    def __repr__(self):
        return "flatten(%r)" % (self.iter,)
    def __hash__(self):
        return _coconut.hash((self.__class__, self.iter))
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.iter == other.iter
    def __contains__(self, elem):
        return _coconut.any(elem in it for it in self.iter)
    def count(self, elem):
        """Count the number of times elem appears in the flattened iterable."""
        return _coconut.sum(it.count(elem) for it in self.iter)
    def index(self, elem):
        ind = 0
        for it in self.iter:
            try:
                return ind + it.index(elem)
            except _coconut.ValueError:
                ind += _coconut.len(it)
        raise ValueError("%r not in %r" % (elem, self))
    def __fmap__(self, func):
        return self.__class__(_coconut_map(_coconut.functools.partial(_coconut_map, func), self.iter))
class map(_coconut.map):
    __slots__ = ("func", "iters")
    if hasattr(_coconut.map, "__doc__"):
        __doc__ = _coconut.map.__doc__
    def __new__(cls, function, *iterables):
        new_map = _coconut.map.__new__(cls, function, *iterables)
        new_map.func = function
        new_map.iters = iterables
        return new_map
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self.func, *(_coconut_igetitem(i, index) for i in self.iters))
        return self.func(*(_coconut_igetitem(i, index) for i in self.iters))
    def __reversed__(self):
        return self.__class__(self.func, *(_coconut_reversed(i) for i in self.iters))
    def __len__(self):
        return _coconut.min(_coconut.len(i) for i in self.iters)
    def __repr__(self):
        return "map(%r, %s)" % (self.func, ", ".join((_coconut.repr(i) for i in self.iters)))
    def __reduce__(self):
        return (self.__class__, (self.func,) + self.iters)
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __iter__(self):
        return _coconut.iter(_coconut.map(self.func, *self.iters))
    def __fmap__(self, func):
        return self.__class__(_coconut_forward_compose(self.func, func), *self.iters)
class _coconut_parallel_concurrent_map_func_wrapper(object):
    __slots__ = ("map_cls", "func",)
    def __init__(self, map_cls, func):
        self.map_cls = map_cls
        self.func = func
    def __reduce__(self):
        return (self.__class__, (self.map_cls, self.func))
    def __call__(self, *args, **kwargs):
        self.map_cls.get_executor_stack().append(None)
        try:
            return self.func(*args, **kwargs)
        except:
            _coconut.print(self.map_cls.__name__ + " error:")
            _coconut.traceback.print_exc()
            raise
        finally:
            self.map_cls.get_executor_stack().pop()
class _coconut_base_parallel_concurrent_map(map):
    __slots__ = ("result")
    @classmethod
    def get_executor_stack(cls):
        return cls.threadlocal_ns.__dict__.setdefault("executor_stack", [None])
    def __new__(cls, function, *iterables):
        self = _coconut_map.__new__(cls, function, *iterables)
        self.result = None
        if cls.get_executor_stack()[-1] is not None:
            return self.get_list()
        return self
    @classmethod
    @_coconut.contextlib.contextmanager
    def multiple_sequential_calls(cls, max_workers=None):
        """Context manager that causes nested calls to use the same pool."""
        if cls.get_executor_stack()[-1] is None:
            with cls.make_executor(max_workers) as executor:
                cls.get_executor_stack()[-1] = executor
                try:
                    yield
                finally:
                    cls.get_executor_stack()[-1] = None
        else:
            yield
    def get_list(self):
        if self.result is None:
            with self.multiple_sequential_calls():
                self.result = _coconut.list(self.get_executor_stack()[-1].map(_coconut_parallel_concurrent_map_func_wrapper(self.__class__, self.func), *self.iters))
        return self.result
    def __iter__(self):
        return _coconut.iter(self.get_list())
class parallel_map(_coconut_base_parallel_concurrent_map):
    """Multi-process implementation of map using concurrent.futures.
    Requires arguments to be pickleable. For multiple sequential calls,
    use `with parallel_map.multiple_sequential_calls():`."""
    __slots__ = ()
    threadlocal_ns = _coconut.threading.local()
    @staticmethod
    def make_executor(max_workers=None):
        from concurrent.futures import ProcessPoolExecutor
        return ProcessPoolExecutor(max_workers)
    def __repr__(self):
        return "parallel_" + _coconut_map.__repr__(self)
class concurrent_map(_coconut_base_parallel_concurrent_map):
    """Multi-thread implementation of map using concurrent.futures.
    For multiple sequential calls, use
    `with concurrent_map.multiple_sequential_calls():`."""
    __slots__ = ()
    threadlocal_ns = _coconut.threading.local()
    @staticmethod
    def make_executor(max_workers=None):
        from concurrent.futures import ThreadPoolExecutor
        from multiprocessing import cpu_count
        return ThreadPoolExecutor(cpu_count() * 5 if max_workers is None else max_workers)
    def __repr__(self):
        return "concurrent_" + _coconut_map.__repr__(self)
class filter(_coconut.filter):
    __slots__ = ("func", "iter")
    if hasattr(_coconut.filter, "__doc__"):
        __doc__ = _coconut.filter.__doc__
    def __new__(cls, function, iterable):
        new_filter = _coconut.filter.__new__(cls, function, iterable)
        new_filter.func = function
        new_filter.iter = iterable
        return new_filter
    def __reversed__(self):
        return self.__class__(self.func, _coconut_reversed(self.iter))
    def __repr__(self):
        return "filter(%r, %r)" % (self.func, self.iter)
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter))
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __iter__(self):
        return _coconut.iter(_coconut.filter(self.func, self.iter))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class zip(_coconut.zip):
    __slots__ = ("iters", "strict")
    if hasattr(_coconut.zip, "__doc__"):
        __doc__ = _coconut.zip.__doc__
    def __new__(cls, *iterables, **kwargs):
        new_zip = _coconut.zip.__new__(cls, *iterables)
        new_zip.iters = iterables
        new_zip.strict = kwargs.pop("strict", False)
        if kwargs:
            raise _coconut.TypeError("zip() got unexpected keyword arguments " + _coconut.repr(kwargs))
        return new_zip
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(*(_coconut_igetitem(i, index) for i in self.iters), strict=self.strict)
        return _coconut.tuple(_coconut_igetitem(i, index) for i in self.iters)
    def __reversed__(self):
        return self.__class__(*(_coconut_reversed(i) for i in self.iters), strict=self.strict)
    def __len__(self):
        return _coconut.min(_coconut.len(i) for i in self.iters)
    def __repr__(self):
        return "zip(%s%s)" % (", ".join((_coconut.repr(i) for i in self.iters)), ", strict=True" if self.strict else "")
    def __reduce__(self):
        return (self.__class__, self.iters, self.strict)
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __setstate__(self, strict):
        self.strict = strict
    def __iter__(self):
        for items in _coconut.iter(_coconut.zip(*self.iters, strict=self.strict) if _coconut_sys.version_info >= (3, 10) else _coconut.zip_longest(*self.iters, fillvalue=_coconut_sentinel) if self.strict else _coconut.zip(*self.iters)):
            if self.strict and _coconut_sys.version_info < (3, 10) and _coconut.any(x is _coconut_sentinel for x in items):
                raise _coconut.ValueError("zip(..., strict=True) arguments have mismatched lengths")
            yield items
    def __fmap__(self, func):
        return _coconut_map(func, self)
class zip_longest(zip):
    __slots__ = ("fillvalue",)
    if hasattr(_coconut.zip_longest, "__doc__"):
        __doc__ = (_coconut.zip_longest).__doc__
    def __new__(cls, *iterables, **kwargs):
        self = _coconut_zip.__new__(cls, *iterables, strict=False)
        self.fillvalue = kwargs.pop("fillvalue", None)
        if kwargs:
            raise _coconut.TypeError("zip_longest() got unexpected keyword arguments " + _coconut.repr(kwargs))
        return self
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            new_ind = _coconut.slice(index.start + self.__len__() if index.start is not None and index.start < 0 else index.start, index.stop + self.__len__() if index.stop is not None and index.stop < 0 else index.stop, index.step)
            return self.__class__(*(_coconut_igetitem(i, new_ind) for i in self.iters))
        if index < 0:
            index += self.__len__()
        result = []
        got_non_default = False
        for it in self.iters:
            try:
                result.append(_coconut_igetitem(it, index))
            except _coconut.IndexError:
                result.append(self.fillvalue)
            else:
                got_non_default = True
        if not got_non_default:
            raise _coconut.IndexError("zip_longest index out of range")
        return _coconut.tuple(result)
    def __len__(self):
        return _coconut.max(_coconut.len(i) for i in self.iters)
    def __repr__(self):
        return "zip_longest(%s, fillvalue=%s)" % (", ".join((_coconut.repr(i) for i in self.iters)), self.fillvalue)
    def __reduce__(self):
        return (self.__class__, self.iters, self.fillvalue)
    def __setstate__(self, fillvalue):
        self.fillvalue = fillvalue
    def __iter__(self):
        return _coconut.iter(_coconut.zip_longest(*self.iters, fillvalue=self.fillvalue))
class enumerate(_coconut.enumerate):
    __slots__ = ("iter", "start")
    if hasattr(_coconut.enumerate, "__doc__"):
        __doc__ = _coconut.enumerate.__doc__
    def __new__(cls, iterable, start=0):
        new_enumerate = _coconut.enumerate.__new__(cls, iterable, start)
        new_enumerate.iter = iterable
        new_enumerate.start = start
        return new_enumerate
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(_coconut_igetitem(self.iter, index), self.start + (0 if index.start is None else index.start if index.start >= 0 else _coconut.len(self.iter) + index.start))
        return (self.start + index, _coconut_igetitem(self.iter, index))
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "enumerate(%r, %r)" % (self.iter, self.start)
    def __reduce__(self):
        return (self.__class__, (self.iter, self.start))
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __iter__(self):
        return _coconut.iter(_coconut.enumerate(self.iter, self.start))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class count(object):
    """count(start, step) returns an infinite iterator starting at start and increasing by step.
    If step is set to 0, count will infinitely repeat its first argument."""
    __slots__ = ("start", "step")
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
    def __iter__(self):
        while True:
            yield self.start
            if self.step:
                self.start += self.step
    def __contains__(self, elem):
        if not self.step:
            return elem == self.start
        if elem < self.start:
            return False
        return (elem - self.start) % self.step == 0
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice) and (index.start is None or index.start >= 0) and (index.stop is None or index.stop >= 0):
            new_start, new_step = self.start, self.step
            if self.step and index.start is not None:
                new_start += self.step * index.start
            if self.step and index.step is not None:
                new_step *= index.step
            if index.stop is None:
                return self.__class__(new_start, new_step)
            if self.step and _coconut.isinstance(self.start, _coconut.int) and _coconut.isinstance(self.step, _coconut.int):
                return _coconut.range(new_start, self.start + self.step * index.stop, new_step)
            return _coconut_map(self.__getitem__, _coconut.range(index.start if index.start is not None else 0, index.stop, index.step if index.step is not None else 1))
        if index < 0:
            raise _coconut.IndexError("count indices must be positive")
        return self.start + self.step * index if self.step else self.start
    def count(self, elem):
        """Count the number of times elem appears in the count."""
        if not self.step:
            return _coconut.float("inf") if elem == self.start else 0
        return int(elem in self)
    def index(self, elem):
        """Find the index of elem in the count."""
        if elem not in self:
            raise _coconut.ValueError(_coconut.repr(elem) + " not in " + _coconut.repr(self))
        return (elem - self.start) // self.step if self.step else 0
    def __reversed__(self):
        if not self.step:
            return self
        raise _coconut.TypeError(_coconut.repr(self) + " object is not reversible")
    def __repr__(self):
        return "count(%r, %r)" % (self.start, self.step)
    def __hash__(self):
        return _coconut.hash((self.start, self.step))
    def __reduce__(self):
        return (self.__class__, (self.start, self.step))
    def __copy__(self):
        return self.__class__(self.start, self.step)
    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.start == other.start and self.step == other.step
    def __fmap__(self, func):
        return _coconut_map(func, self)
class groupsof(object):
    """groupsof(n, iterable) splits iterable into groups of size n.
    If the length of the iterable is not divisible by n, the last group may be of size < n."""
    __slots__ = ("group_size", "iter")
    def __init__(self, n, iterable):
        self.iter = iterable
        try:
            self.group_size = _coconut.int(n)
        except _coconut.ValueError:
            raise _coconut.TypeError("group size must be an int; not %r" % (n,))
        if self.group_size <= 0:
            raise _coconut.ValueError("group size must be > 0; not %r" % (self.group_size,))
    def __iter__(self):
        iterator = _coconut.iter(self.iter)
        loop = True
        while loop:
            group = []
            for _ in _coconut.range(self.group_size):
                try:
                    group.append(_coconut.next(iterator))
                except _coconut.StopIteration:
                    loop = False
                    break
            if group:
                yield _coconut.tuple(group)
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "groupsof(%r)" % (self.iter,)
    def __reduce__(self):
        return (self.__class__, (self.group_size, self.iter))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class recursive_iterator(object):
    """Decorator that optimizes a function for iterator recursion."""
    __slots__ = ("func", "tee_store", "backup_tee_store")
    def __init__(self, func):
        self.func = func
        self.tee_store = {}
        self.backup_tee_store = []
    def __call__(self, *args, **kwargs):
        key = (args, _coconut.frozenset(kwargs))
        use_backup = False
        try:
            _coconut.hash(key)
        except _coconut.Exception:
            try:
                key = _coconut.pickle.dumps(key, -1)
            except _coconut.Exception:
                use_backup = True
        if use_backup:
            for i, (k, v) in _coconut.enumerate(self.backup_tee_store):
                if k == key:
                    to_tee, store_pos = v, i
                    break
            else:
                to_tee = self.func(*args, **kwargs)
                store_pos = None
            to_store, to_return = _coconut_tee(to_tee)
            if store_pos is None:
                self.backup_tee_store.append([key, to_store])
            else:
                self.backup_tee_store[store_pos][1] = to_store
        else:
            it = self.tee_store.get(key)
            if it is None:
                it = self.func(*args, **kwargs)
            self.tee_store[key], to_return = _coconut_tee(it)
        return to_return
    def __repr__(self):
        return "@recursive_iterator(%s)" % (_coconut.repr(self.func),)
    def __reduce__(self):
        return (self.__class__, (self.func,))
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return _coconut.functools.partial(self, obj)
class _coconut_FunctionMatchErrorContext(object):
    __slots__ = ('exc_class', 'taken')
    threadlocal_ns = _coconut.threading.local()
    def __init__(self, exc_class):
        self.exc_class = exc_class
        self.taken = False
    @classmethod
    def get_contexts(cls):
        try:
            return cls.threadlocal_ns.contexts
        except _coconut.AttributeError:
            cls.threadlocal_ns.contexts = []
            return cls.threadlocal_ns.contexts
    def __enter__(self):
        self.get_contexts().append(self)
    def __exit__(self, type, value, traceback):
        self.get_contexts().pop()
def _coconut_get_function_match_error():
    try:
        ctx = _coconut_FunctionMatchErrorContext.get_contexts()[-1]
    except _coconut.IndexError:
        return _coconut_MatchError
    if ctx.taken:
        return _coconut_MatchError
    ctx.taken = True
    return ctx.exc_class
class _coconut_base_pattern_func(object):
    __slots__ = ("FunctionMatchError", "__doc__", "patterns")
    _coconut_is_match = True
    def __init__(self, *funcs):
        self.FunctionMatchError = _coconut.type(_coconut_py_str("MatchError"), (_coconut_MatchError,), {})
        self.__doc__ = None
        self.patterns = []
        for func in funcs:
            self.add_pattern(func)
    def add_pattern(self, func):
        self.__doc__ = _coconut.getattr(func, "__doc__", None) or self.__doc__
        if _coconut.isinstance(func, _coconut_base_pattern_func):
            self.patterns += func.patterns
        else:
            self.patterns.append(func)
    def __call__(self, *args, **kwargs):
        for func in self.patterns[:-1]:
            try:
                with _coconut_FunctionMatchErrorContext(self.FunctionMatchError):
                    return func(*args, **kwargs)
            except self.FunctionMatchError:
                pass
        return self.patterns[-1](*args, **kwargs)
    def _coconut_tco_func(self, *args, **kwargs):
        for func in self.patterns[:-1]:
            try:
                with _coconut_FunctionMatchErrorContext(self.FunctionMatchError):
                    return func(*args, **kwargs)
            except self.FunctionMatchError:
                pass
        return _coconut_tail_call(self.patterns[-1], *args, **kwargs)
    def __repr__(self):
        return "addpattern(%s)(*%s)" % (_coconut.repr(self.patterns[0]), _coconut.repr(self.patterns[1:]))
    def __reduce__(self):
        return (self.__class__, _coconut.tuple(self.patterns))
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return _coconut.functools.partial(self, obj)
def _coconut_mark_as_match(base_func):
    base_func._coconut_is_match = True
    return base_func
def addpattern(base_func, **kwargs):
    """Decorator to add a new case to a pattern-matching function,
    where the new case is checked last."""
    allow_any_func = kwargs.pop("allow_any_func", False)
    if not allow_any_func and not _coconut.getattr(base_func, "_coconut_is_match", False):
        _coconut.warnings.warn("Possible misuse of addpattern with non-pattern-matching function " + _coconut.repr(base_func) + " (pass allow_any_func=True to dismiss)", stacklevel=2)
    if kwargs:
        raise _coconut.TypeError("addpattern() got unexpected keyword arguments " + _coconut.repr(kwargs))
    return _coconut.functools.partial(_coconut_base_pattern_func, base_func)
_coconut_addpattern = addpattern
def prepattern(*args, **kwargs):
    """Deprecated feature 'prepattern' disabled by --strict compilation; use 'addpattern' instead."""
    raise _coconut.NameError("deprecated feature 'prepattern' disabled by --strict compilation; use 'addpattern' instead")
class _coconut_partial(object):
    __slots__ = ("func", "_argdict", "_arglen", "_stargs", "keywords")
    if hasattr(_coconut.functools.partial, "__doc__"):
        __doc__ = _coconut.functools.partial.__doc__
    def __init__(self, func, argdict, arglen, *args, **kwargs):
        self.func = func
        self._argdict = argdict
        self._arglen = arglen
        self._stargs = args
        self.keywords = kwargs
    def __reduce__(self):
        return (self.__class__, (self.func, self._argdict, self._arglen) + self._stargs, self.keywords)
    def __setstate__(self, keywords):
        self.keywords = keywords
    @property
    def args(self):
        return _coconut.tuple(self._argdict.get(i) for i in _coconut.range(self._arglen)) + self._stargs
    def __call__(self, *args, **kwargs):
        callargs = []
        argind = 0
        for i in _coconut.range(self._arglen):
            if i in self._argdict:
                callargs.append(self._argdict[i])
            elif argind >= _coconut.len(args):
                raise _coconut.TypeError("expected at least " + _coconut.str(self._arglen - _coconut.len(self._argdict)) + " argument(s) to " + _coconut.repr(self))
            else:
                callargs.append(args[argind])
                argind += 1
        callargs += self._stargs
        callargs += args[argind:]
        kwargs.update(self.keywords)
        return self.func(*callargs, **kwargs)
    def __repr__(self):
        args = []
        for i in _coconut.range(self._arglen):
            if i in self._argdict:
                args.append(_coconut.repr(self._argdict[i]))
            else:
                args.append("?")
        for arg in self._stargs:
            args.append(_coconut.repr(arg))
        return "%s$(%s)" % (_coconut.repr(self.func), ", ".join(args))
def consume(iterable, keep_last=0):
    """consume(iterable, keep_last) fully exhausts iterable and return the last keep_last elements."""
    return _coconut.collections.deque(iterable, maxlen=keep_last)
class starmap(_coconut.itertools.starmap):
    __slots__ = ("func", "iter")
    if hasattr(_coconut.itertools.starmap, "__doc__"):
        __doc__ = _coconut.itertools.starmap.__doc__
    def __new__(cls, function, iterable):
        new_map = _coconut.itertools.starmap.__new__(cls, function, iterable)
        new_map.func = function
        new_map.iter = iterable
        return new_map
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self.func, _coconut_igetitem(self.iter, index))
        return self.func(*_coconut_igetitem(self.iter, index))
    def __reversed__(self):
        return self.__class__(self.func, *_coconut_reversed(self.iter))
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "starmap(%r, %r)" % (self.func, self.iter)
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter))
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __iter__(self):
        return _coconut.iter(_coconut.itertools.starmap(self.func, self.iter))
    def __fmap__(self, func):
        return self.__class__(_coconut_forward_compose(self.func, func), self.iter)
def makedata(data_type, *args):
    """Construct an object of the given data_type containing the given arguments."""
    if _coconut.hasattr(data_type, "_make") and _coconut.issubclass(data_type, _coconut.tuple):
        return data_type._make(args)
    if _coconut.issubclass(data_type, (_coconut.range, _coconut.abc.Iterator)):
        return args
    if _coconut.issubclass(data_type, _coconut.str):
        return "".join(args)
    return data_type(args)
def datamaker(*args, **kwargs):
    """Deprecated feature 'datamaker' disabled by --strict compilation; use 'makedata' instead."""
    raise _coconut.NameError("deprecated feature 'datamaker' disabled by --strict compilation; use 'makedata' instead")
def fmap(func, obj):
    """fmap(func, obj) creates a copy of obj with func applied to its contents.
    Override by defining obj.__fmap__(func). For numpy arrays, uses np.vectorize."""
    obj_fmap = _coconut.getattr(obj, "__fmap__", None)
    if obj_fmap is not None:
        try:
            result = obj_fmap(func)
        except _coconut.NotImplementedError:
            pass
        else:
            if result is not _coconut.NotImplemented:
                return result
    if obj.__class__.__module__ in ("numpy", "pandas"):
        from numpy import vectorize
        return vectorize(func)(obj)
    return _coconut_makedata(obj.__class__, *(_coconut_starmap(func, obj.items()) if _coconut.isinstance(obj, _coconut.abc.Mapping) else _coconut_map(func, obj)))
def memoize(maxsize=None, *args, **kwargs):
    """Decorator that memoizes a function,
    preventing it from being recomputed if it is called multiple times with the same arguments."""
    return _coconut.functools.lru_cache(maxsize, *args, **kwargs)
def _coconut_call_set_names(cls):
    if _coconut_sys.version_info < (3, 6):
        for k, v in _coconut.vars(cls).items():
            set_name = _coconut.getattr(v, "__set_name__", None)
            if set_name is not None:
                set_name(cls, k)
class override(object):
    def __init__(self, func):
        self.func = func
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self.func
        if _coconut_sys.version_info < (3,):
            return _coconut.types.MethodType(self.func, obj, objtype)
        else:
            return _coconut.types.MethodType(self.func, obj)
    def __set_name__(self, obj, name):
        if not _coconut.hasattr(_coconut.super(obj, obj), name):
            raise _coconut.RuntimeError(obj.__name__ + "." + name + " marked with @override but not overriding anything")
def reveal_type(obj):
    """Special function to get MyPy to print the type of the given expression.
    At runtime, reveal_type is the identity function."""
    return obj
def reveal_locals():
    """Special function to get MyPy to print the type of the current locals.
    At runtime, reveal_locals always returns None."""
    pass
_coconut_MatchError, _coconut_count, _coconut_enumerate, _coconut_filter, _coconut_makedata, _coconut_map, _coconut_reiterable, _coconut_reversed, _coconut_starmap, _coconut_tee, _coconut_zip, TYPE_CHECKING, reduce, takewhile, dropwhile = MatchError, count, enumerate, filter, makedata, map, reiterable, reversed, starmap, tee, zip, False, _coconut.functools.reduce, _coconut.itertools.takewhile, _coconut.itertools.dropwhile

# Compiled Coconut: -----------------------------------------------------------

import setuptools

sys = _coconut_sys
import os.path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "pxprover"))

from constants import version
from constants import requirements
from constants import classifiers

setuptools.setup(name="pxprover", version=version, description="Fork of pyprover, https://github.com/evhub/pyprover", url="https://github.com/vineetvermait/pyprover-px", author="Vineet Verma (Original: Evan Hubinger)", author_email="vineetverma.it@gmail.com", packages=setuptools.find_packages(), install_requires=requirements, classifiers=classifiers)
