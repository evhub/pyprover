# PyProver

PyProver is a resolution theorem prover for first-order predicate logic. PyProver is written in [Coconut](http://coconut-lang.org/) which compiles to pure, universal Python, allowing PyProver to work on any Python version.

Installing PyProver is as simple as
```
pip install pyprover
```

## Usage

To use PyProver from a Python interpreter, it is recommended to
```python
from pyprover import *
```
which will populate the global namespace with capital letters as propositions/predicates, and lowercase letters as constants/variables/functions. When using PyProver from a Python file, however, it is recommended to only import what you need.

Formulas can be constructed using the built-in Python operators on propositions and terms combined with `Exists` (or `TE`), `ForAll` (or `FA`), `Eq`, `top`, and `bot`. For example:
```python
A & B
A | ~B
~(A | B)
P >> Q
P >> (Q >> P)
(F & G) >> H
E >> top
bot >> E
FA(x, F(x))
TE(x, F(x) | G(x))
FA(x, F(f(x)) >> F(x))
Eq(a, b)
```

Alternatively, the `expr(formula)` function can be used, which parses a formula in standard mathematical notation. For example:
```
F ∧ G ∨ (C → ¬D)
F /\ G \/ (C -> ~D)
F & G | (C -> -D)
⊤ ∧ ⊥
top /\ bot
F -> G -> H
A x. F(x) /\ G(x)
∀x. F(x) /\ G(x)
E x. C(x) \/ D(x)
∃x. C(x) \/ D(x)
∀x. ∃y. G(f(x, y))
a = b
```

Once a formula has been constructed, various functions are provided to work with them. Some of the most important of these are:

- `strict_simplify(expr)` finds an equivalent, standardized version of the given `expr`,
- `simplify(expr)` is the same as `strict_simplify`, but it implicitly assumes `TE(x, top)` (something exists),
- `strict_proves(givens, concl)` determines if `concl` can be derived from `givens`, and
- `proves(givens, concl)` is the same as `strict_proves`, but it implicitly assumes `TE(x, top)` (something exists).

To construct additional propositions/predicates, the function `props("name1 name2 name3 ...")` will return propositions/predicates for the given names, and to construct additional constants/variables/functions, the function `terms("name1 name2 name3 ...")` can be used similarly.

## Examples

_The backtick infix syntax here is from [Coconut](http://coconut-lang.org/). If using Python instead simply adjust to standard function call syntax._

```python
from pyprover import *

# constructive propositional logic
assert (E, E>>F, F>>G) `proves` G
assert (E>>F, F>>G) `proves` E>>G

# classical propositional logic
assert ~~E `proves` E
assert top `proves` (E>>F)|(F>>E)

# constructive predicate logic
assert R(j) `proves` TE(x, R(x))
assert (FA(x, R(x) >> S(x)), TE(y, R(y))) `proves` TE(z, S(z))

# classical predicate logic
assert ~FA(x, R(x)) `proves` TE(y, ~R(y))
assert top `proves` TE(x, D(x)) | FA(x, ~D(x))

# use of expr parser
assert expr(r"A x. E y. F(x) \/ G(y)") == FA(x, TE(y, F(x) | G(y)))
assert expr(r"a = b /\ b = c") == Eq(a, b) & Eq(b, c)
```

## Compiling PyProver

If you want to compile PyProver yourself instead of installing it from PyPI with `pip`, you can

1. clone the `git` repository,
2. run `make setup`, and
3. run `make install`.
