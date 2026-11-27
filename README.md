# PyProver

PyProver is an automated theorem prover for first-order logic with equality. You can write formulas with Python operators or in standard mathematical notation. It will prove things (and show you the proof), find countermodels for things that aren't true, and convert formulas into the usual normal forms.

PyProver is written in [Coconut](http://coconut-lang.org/), a functional programming language that compiles to Python. It has no dependencies and runs on any Python 3.10+.

```
pip install pyprover
```

```python
>>> from pyprover import *
>>> proves(FA(x, F(x) >> G(x)) & F(a), G(a))
True
>>> print(prove(expr("∀x, Man(x) → Mortal(x)"), expr("Man(socrates) → Mortal(socrates)")))
Proved: Man(socrates) → Mortal(socrates)
from premises:
  1. ∀x, Man(x) → Mortal(x)
by resolution refutation:
  1. Mortal(?x) ∨ ¬Man(?x)  [premise 1]
  2. Man(socrates)  [negated conclusion]
  3. ¬Mortal(socrates)  [negated conclusion]
  4. Mortal(socrates)  [resolution 1, 2]
  5. ⊥  [resolution 4, 3]
>>> print(prove(TE(x, F(x)) & TE(x, G(x)), TE(x, F(x) & G(x))))
Disproved: ∃x, F(x) ∧ G(x)
from premises:
  1. (∃x, F(x)) ∧ (∃x, G(x))
countermodel:
  domain: {0, 1}
  sk1 = 0, sk2 = 1
  true: F(0), G(1)
  (everything else is false)
```

## Contents

- [Writing formulas](#writing-formulas)
- [Parsing formulas](#parsing-formulas)
- [Proving things](#proving-things)
- [Proofs and countermodels](#proofs-and-countermodels)
- [Normal forms and simplification](#normal-forms-and-simplification)
- [The empty universe](#the-empty-universe)
- [Command line](#command-line)
- [API reference](#api-reference)
- [How it works](#how-it-works)
- [Development](#development)

## Writing formulas

`from pyprover import *` imports all of PyProver. It also makes the uppercase letters `A`–`Z` propositions (call them to get predicates, as in `F(x)`) and the lowercase letters `a`–`z` constants (call them to get functions, as in `f(x)`). In a Python file it's usually better to import only what you need and make your own atoms:

```python
from pyprover import props, terms, proves, FA

Man, Mortal = props("Man Mortal")
socrates, x = terms("socrates x")
assert proves((FA(x, Man(x) >> Mortal(x)), Man(socrates)), Mortal(socrates))
```

Build formulas with these:

| PyProver              | Meaning                          |
|-----------------------|----------------------------------|
| `A & B`, `And(A, B)`  | A and B                          |
| `A \| B`, `Or(A, B)`  | A or B                           |
| `~A`, `Not(A)`        | not A                            |
| `A >> B`, `Imp(A, B)` | A implies B (`A << B` is B → A)  |
| `Iff(A, B)`           | A if and only if B               |
| `A ^ B`               | A exclusive-or B                 |
| `top`, `bot`          | true (⊤) and false (⊥)           |
| `FA(x, F(x))`         | for all x, F(x) (also `ForAll`)  |
| `TE(x, F(x))`         | there exists x such that F(x) (also `Exists`, `EX`) |
| `Eq(a, b)`            | a = b                            |

`FA(x, y, F(x, y))` is shorthand for `FA(x, FA(y, F(x, y)))`, and `Imp(A, B, C)` is shorthand for `A >> (B >> C)`.

_Watch out for Python's operator precedence:_ `>>` binds more tightly than `&` and `|`, so write `(A & B) >> C` rather than `A & B >> C`, and `A >> (B >> C)` rather than `A >> B >> C`.

Formulas are immutable, hashable values. Comparison ignores the order of `&` and `|`, the names of bound variables, and the order of the two sides of `Eq`:

```python
assert A & B == B & A
assert FA(x, F(x)) == FA(y, F(y))
assert Eq(a, b) == Eq(b, a)
```

Formulas print in standard notation (`str`) or as Python code (`repr`):

```python
>>> f = FA(x, F(x) >> ~Eq(x, a))
>>> print(f)
∀x, F(x) → x ≠ a
>>> f
FA(x, F(x) >> ~Eq(x, a))
```

If your terminal can't show the logic symbols, call `use_ascii()` to switch to `FA x, F(x) -> x != a`. `use_unicode()` switches back.

Besides constants, there are schematic variables, written `?x` and made with `Var("x")` or `variables("x y")`. A free schematic variable in a premise or conclusion is universally quantified. Unification works on them: `unify(F(Var("x"), b), F(a, Var("y")))` returns `{Var("x"): a, Var("y"): b}`.

## Parsing formulas

`expr` parses formulas written in standard mathematical notation:

```python
assert expr(r"∀x, F(x) → G(x)") == FA(x, F(x) >> G(x))
assert expr(r"A x. E y. F(x) \/ G(y)") == FA(x, TE(y, F(x) | G(y)))
assert expr(r"a = b /\ b = c") == Eq(a, b) & Eq(b, c)
assert expr(r"forall x: Man, Mortal(x)") == FA(x, Man(x) >> Mortal(x))
```

Each connective can be written several ways:

| Connective | Accepted spellings |
|------------|--------------------|
| ⊤ / ⊥      | `⊤ top true` / `⊥ bot false _\|_` |
| not        | `¬ ~ - ! not` |
| and        | `∧ & /\ and` |
| or         | `∨ \| \/ or` |
| implies    | `→ -> >> => implies` (right associative) |
| iff        | `↔ <-> <=> iff` |
| equality   | `=`, and `≠ != /=` for inequality |
| for all    | `∀x, …` `∀x. …` `A x. …` `FA x, …` `forall x, …` |
| exists     | `∃x, …` `E x. …` `TE x, …` `EX x, …` `exists x, …` |

Binding is loosest to tightest: quantifiers (which extend as far right as possible), then ↔, then →, then ∨, then ∧, then ¬. A quantifier can bind several variables (`∀x y, F(x, y)`). It can also be restricted: `forall x: A, B(x)` means `∀x, A(x) → B(x)`, and `exists x: A, B(x)` means `∃x, A(x) ∧ B(x)`.

Propositions and predicates must start with an uppercase letter. Constants, variables and functions must start with a lowercase letter, digit or underscore, and can end in primes (`x'`). Schematic variables are written `?x`. A malformed formula raises `ParseError` (a `ValueError`) pointing at the problem:

```
>>> expr("A ∧ ∧ B")
pyprover.parser.ParseError: expected a formula (found '∧') at position 4:
  A ∧ ∧ B
      ^
```

`str` output always parses back to the same formula.

## Proving things

`proves(premises, conclusion)` returns whether the conclusion follows from the premises. Premises can be a single formula or any iterable of formulas.

_The backtick infix syntax below is Coconut. In Python, write `proves(x, y)` instead of ``x `proves` y``._

```python
from pyprover import *

# propositional logic
assert (E, E >> F, F >> G) `proves` G
assert ~~E `proves` E
assert top `proves` (E >> F) | (F >> E)

# predicate logic
assert R(j) `proves` TE(x, R(x))
assert (FA(x, R(x) >> S(x)), TE(y, R(y))) `proves` TE(z, S(z))
assert ~FA(x, R(x)) `proves` TE(y, ~R(y))
assert top `proves` TE(x, D(x) >> FA(y, D(y)))     # the drinker paradox
assert not FA(x, R(x) | S(x)) `proves` FA(x, R(x)) | FA(x, S(x))

# equality
assert Eq(a, b) & F(a) `proves` F(b)
assert FA(x, Eq(f(f(x)), x)) `proves` FA(x, TE(y, Eq(f(y), x)))
assert (P(a), P(b), ~Eq(a, b)) `proves` TE(x, TE(y, P(x) & P(y) & ~Eq(x, y)))
assert not (P(a), P(b)) `proves` TE(x, TE(y, P(x) & P(y) & ~Eq(x, y)))

# group theory: a left identity and left inverses make a right identity
group = (
    FA(x, Eq(m(e, x), x)),
    FA(x, Eq(m(i(x), x), e)),
    FA(x, y, z, Eq(m(m(x, y), z), m(x, m(y, z)))),
)
assert group `proves` FA(x, Eq(m(x, e), x))
```

Other ways to ask:

- `valid(f)`: is `f` true in every interpretation?
- `satisfiable(f)`: is `f` true in some interpretation?
- `equivalent(f, g)` (also `proves_and_proved_by`): do `f` and `g` prove each other?
- `countermodel(premises, conclusion)`: a finite model where the premises are true and the conclusion is false, or `None`.

First-order logic is only semi-decidable, so no prover can answer every question. PyProver always decides problems without function symbols (once existential quantifiers are replaced by Skolem functions); this covers most textbook exercises. For other problems it searches for a proof and a finite countermodel at the same time. If it finds neither within the limits (10 seconds and 20,000 clauses by default), `proves` gives a `RuntimeWarning` and returns `False`. You can pass `timeout=` (seconds) and `max_clauses=` to change the limits. `prove` (below) tells you explicitly when it doesn't know.

## Proofs and countermodels

`prove(premises, conclusion)` returns a `Proof` object instead of a bool. It is truthy exactly when the conclusion was proved. Its `status` is `"proved"`, `"disproved"`, or `"unknown"`.

A proved result comes with a resolution refutation in `proof.steps` (a list of `ProofStep(num, formula, rule, parents)`). Each step is a clause: a disjunction of literals in which `?x` variables are universally quantified and `sk` functions are Skolem functions. The steps start from the premises and the negated conclusion and end in a contradiction (⊥). `str(proof)` lists the steps, `proof.tree()` draws them as a tree, and `proof.to_dot()` gives a [Graphviz](https://graphviz.org/) graph you can render as a diagram:

```python
>>> print(prove((FA(x, R(x) >> S(x)), R(j)), S(j)).tree())
⊥  [resolution]
├── S(j)  [resolution]
│   ├── S(?x) ∨ ¬R(?x)  [premise 1]
│   └── R(j)  [premise 2]
└── ¬S(j)  [negated conclusion]
```

The inference rules that appear in proofs:

- **resolution:** from `A ∨ C` and `¬A' ∨ D`, where `A` and `A'` unify, derive `C ∨ D`.
- **factoring:** merge two literals of a clause that unify.
- **superposition:** use an equation `l = r` to replace an instance of `l` with `r` in another clause.
- **demodulation:** rewrite a clause with a unit equation, oriented so that terms get simpler.
- **equality resolution:** drop a literal `s ≠ t` where `s` and `t` unify.
- **equality factoring:** a technical rule needed to make equality reasoning complete.

A disproved result usually comes with a `Countermodel`. This is a finite model in which every premise is true and the conclusion is false. Its domain is `{0, 1, …}`, and it records the value of every constant and function and which atoms are true. Constants named `sk1`, `sk2`, … are Skolem constants: witnesses for existential quantifiers in the premises or the negated conclusion.

```python
>>> print(countermodel(FA(x, P(x) >> P(f(x))), P(a)))
domain: {0}
a = 0
f(0) = 0
true: (nothing)
(everything else is false)
```

## Normal forms and simplification

| Function | Result |
|----------|--------|
| `simplify(f)` | an equivalent, standardized formula: prenex form with a simplified DNF matrix |
| `nnf(f)` | negation normal form: only ∧, ∨, quantifiers, and negated atoms |
| `prenex(f)` | prenex normal form: all quantifiers at the front |
| `cnf(f)` / `dnf(f)` | prenex form with a conjunctive / disjunctive normal form matrix |
| `simplest_form(f)` | whichever of `cnf(f)` and `dnf(f)` is smaller |
| `skolemize(f)` | Skolem normal form: an equisatisfiable CNF formula without quantifiers |
| `substitute(f, {old: new})` | replace terms with terms, or propositions with formulas or booleans (capture-avoiding) |

```python
assert simplify(FA(x, F(x)) & FA(y, G(y))) == FA(x, F(x) & G(x))
assert simplify((A >> B) & A) == A & B
assert simplest_form(A ^ B) == (A | B) & (~A | ~B)
assert skolemize(FA(x, TE(y, F(x, y)))) == F(Var("x"), Func("sk1", Var("x")))
assert substitute(A ^ B, {A: True, B: False}) |> simplify == top
```

## The empty universe

Standard first-order logic assumes that something exists. That's why `top `proves` TE(x, top)` and `FA(x, F(x)) `proves` TE(x, F(x))` both hold. Every function with a `strict_` prefix drops that assumption: `strict_proves`, `strict_prove`, `strict_simplify`, `strict_cnf`, `strict_dnf`, `strict_prenex`, `strict_simplest_form`, and `strict_proves_and_proved_by`. You can also pass `nonempty_universe=False`. In the empty universe, every `∀` is true and every `∃` is false:

```python
assert not top `strict_proves` TE(x, top)
assert not FA(x, F(x)) `strict_proves` TE(x, F(x))
assert FA(x, F(x)) & TE(x, top) `strict_proves` TE(x, F(x))
assert strict_simplify(FA(x, F(x)) & G) == FA(x, F(x)) & G   # can't pull ∀x out of ∧
```

A free constant must refer to something, so mentioning one implies that something exists. For example, `(R(j), FA(x, R(x) >> S(x))) `strict_proves` S(j)` holds.

## Command line

Installing PyProver also installs a `pyprover` command (or run `python -m pyprover`):

```console
$ pyprover prove 'A x. Man(x) -> Mortal(x)' 'Man(socrates)' 'Mortal(socrates)'
Proved: Mortal(socrates)
...
$ pyprover prove --tree '~(P \/ Q)' '~P /\ ~Q'
$ pyprover prove --dot 'A -> B' 'B -> C' 'A -> C' | dot -Tpng > proof.png
$ pyprover simplify '(A -> B) /\ A'
A ∧ B
$ pyprover cnf 'A | (B & C)'
(A ∨ B) ∧ (A ∨ C)
```

`pyprover prove` takes the premises followed by the conclusion. It exits with status 0 if the conclusion was proved, 1 if it was disproved, and 2 if the answer is unknown. Other options are `--strict` (the universe may be empty), `--timeout SECONDS`, `--quiet`, `--tree`, `--dot`, and `--ascii`. The other subcommands are `simplify`, `simplest`, `nnf`, `prenex`, `cnf`, `dnf`, and `skolemize`.

## API reference

Everything below can be imported from `pyprover`.

**Formulas:** `Prop(name)` / `Proposition`, `Pred(name, *terms)` / `Predicate`, `Eq(a, b)` / `Equals`, `Not(f)`, `And(*fs)`, `Or(*fs)`, `Imp(*fs)` / `Implies`, `Iff(f, g)`, `ForAll(var, f)` / `FA`, `Exists(var, f)` / `TE` / `EX`, `top` / `true`, `bot` / `false`. These are all subclasses of `Expr`, which supports the operators above and the methods `.substitute(subs)`, `.find_unification(other)`, and `.simplify()`.

**Terms:** `Const(name)` / `Constant`, `Var(name)` / `Variable` (schematic `?x` variables), `Func(name, *terms)` / `Function`. These are all subclasses of `Term`.

**Constructors:** `props("A B C")`, `terms("a b c")`, `variables("x y z")`, `iff(f, g)`, `expr(text)` / `parse(text)`.

**Namespaces:** `StandardMath` (uppercase propositions, lowercase constants), `LowercasePropositions`, `UppercasePropositions`, `LowercaseVariables`, `UppercaseVariables`. Each has `.use(globals())` to add its letters to a namespace, and `with ....use_in(globals()):` to add them temporarily.

**Proving:** `proves`, `strict_proves`, `prove`, `strict_prove`, `valid`, `satisfiable`, `equivalent` / `proves_and_proved_by`, `strict_proves_and_proved_by`, `countermodel`, `no_proof_of`, `solve` (⊥ if unsatisfiable, otherwise the CNF), `simplest_solution`. The classes `Proof`, `ProofStep`, and `Countermodel` are described above.

**Normal forms:** `simplify`, `nnf` / `prop_simp`, `prenex`, `cnf`, `dnf`, `simplest_form`, `skolemize`, `universal_closure`, and their `strict_` versions.

**Utilities:** `substitute`, `unify`, `free_terms`, `free_consts`, `free_vars`, `size`, `wff`, `isvar`, `use_ascii`, `use_unicode`.

## How it works

To decide whether premises prove a conclusion, PyProver:

1. checks the empty universe, for `strict_` functions;
2. puts each premise and the negated conclusion into negation normal form, replaces existential quantifiers with Skolem functions, and converts the result to clauses. To avoid exponential blowup, nested `↔`s and large subformulas are replaced with new definition predicates;
3. looks for a small finite countermodel by encoding "is there a model of size n?" as a SAT problem for n = 1, 2, …, and solves it with a built-in CDCL SAT solver. For function-free problems, a model exists only if there is one no bigger than the number of constants, so this decides the problem;
4. searches for a contradiction with the given-clause algorithm. The calculus combines resolution and factoring with superposition-style equality reasoning (superposition, equality resolution, equality factoring, and demodulation, ordered by the Knuth–Bendix ordering). It deletes tautologies and subsumed clauses, and picks the next clause by a mix of smallest-first and oldest-first. The calculus is refutationally complete, so if the conclusion follows, the search finds a proof given enough time.

The test suite includes 21 of the classic [Pelletier problems](https://doi.org/10.1007/BF02432151), including Andrews' challenge (P34) and the Aunt Agatha puzzle (P55). PyProver proves each of them in a few seconds or less.

## Development

The source is in the `.coco` files in `pyprover/`. They compile to the `.py` files next to them, which are committed so that PyProver can be installed without Coconut.

```bash
make setup      # install Coconut and pytest
make build      # compile the .coco files
make test       # build, install, and run the tests
make watch      # recompile whenever a .coco file changes
```

To release a new version, bump `version` in `pyprover/constants.coco`, update `CHANGELOG.md`, and merge to `master`. CI then publishes the new version to PyPI and creates the matching tag and GitHub release.

Released under the Apache License 2.0.
