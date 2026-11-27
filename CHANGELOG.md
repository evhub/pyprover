# PyProver 1.0.0

A complete rewrite of PyProver in idiomatic [Coconut](http://coconut-lang.org/).

- **A sound prover.** The old resolution engine accepted invalid inferences (e.g. `∀x, P(x) ∨ Q(x) ⊢ (∀x, P(x)) ∨ (∀x, Q(x))`) and could hang ([#6](https://github.com/evhub/pyprover/issues/6)). The new prover combines resolution with superposition-based equality reasoning, which is refutationally complete. It also runs a SAT-based finite countermodel search, which always decides function-free problems. It proves 21 of the classic Pelletier problems.
- **Proof objects.** `prove()` returns a `Proof` with a printable resolution refutation, a proof tree, Graphviz output, and countermodels for failed proofs ([#2](https://github.com/evhub/pyprover/issues/2)).
- **A new parser.** It accepts more notations, gives error messages that point at the problem, and has no dependencies.
- **A `pyprover` command-line tool.**
- **Full documentation** in the README ([#5](https://github.com/evhub/pyprover/issues/5)).
- **No dependencies; requires Python 3.10+.**

Breaking changes:
- `Imp` is binary, though `Imp(a, b, c)` still means `a → (b → c)`.
- `iff()` returns an `Iff` formula.
- In strict mode (a possibly empty universe), free constants are taken to refer to something.
