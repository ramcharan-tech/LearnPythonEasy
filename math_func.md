# Number-theoretic functions

| Method/Operation       | What it does                            | Example                    | Special errors / corner cases                                                                                                         |
| ---------------------- | --------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `math.comb(n, k)`      | Binomial coefficient “n choose k”.      | `math.comb(5, 2)  # 10`    | `TypeError` if `n` or `k` not ints; `ValueError` if negative; returns `0` if `k > n`. ([Python documentation][1])                     |
| `math.perm(n, k=None)` | Number of permutations (order matters). | `math.perm(5, 2)  # 20`    | Same type/value rules as `comb`; if `k` is `None`, returns `n!`. ([Python documentation][1])                                          |
| `math.factorial(n)`    | Factorial of non-negative integer `n`.  | `math.factorial(5)  # 120` | `ValueError` if `n < 0`; `TypeError` if not an integer (floats like `5.0` are rejected in modern Python). ([Python documentation][1]) |
| `math.gcd(*integers)`  | Greatest common divisor.                | `math.gcd(8, 12, 20)  # 4` | Accepts any number of int args; all zero → `0`. `TypeError` for non-ints. ([Python documentation][1])                                 |
| `math.lcm(*integers)`  | Least common multiple.                  | `math.lcm(4, 6)  # 12`     | Any arg `0` → result `0`; no args → `1`. `TypeError` for non-ints. ([Python documentation][1])                                        |
| `math.isqrt(n)`        | Integer square root: `floor(sqrt(n))`.  | `math.isqrt(10)  # 3`      | `ValueError` if `n < 0`; `TypeError` if not int. ([Python documentation][1])                                                          |

[1]: https://docs.python.org/3/library/math.html "math — Mathematical functions — Python 3.14.1 documentation"

# Floating-point arithmetic

| Method/Operation       | What it does                                          | Example                                | Special errors / corner cases                                                                                                                             |
| ---------------------- | ----------------------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `math.ceil(x)`         | Smallest integer ≥ `x`.                               | `math.ceil(1.2)  # 2`                  | Delegates to `x.__ceil__` for non-floats; `TypeError` if object can’t be converted. ([Python documentation][1])                                           |
| `math.floor(x)`        | Largest integer ≤ `x`.                                | `math.floor(-1.2)  # -2`               | Uses `x.__floor__` for non-floats. ([Python documentation][1])                                                                                            |
| `math.trunc(x)`        | Drop fractional part (toward 0).                      | `math.trunc(-1.9)  # -1`               | Uses `x.__trunc__` for non-floats. ([Python documentation][1])                                                                                            |
| `math.fabs(x)`         | Absolute value as float.                              | `math.fabs(-3)  # 3.0`                 | Always returns float even for ints.                                                                                                                       |
| `math.fma(x, y, z)`    | Fused multiply-add: `(x*y) + z` with single rounding. | `math.fma(1e16, 1e-16, 1.0)`           | More numerically stable than `(x*y)+z`; follows IEEE-754 rules, returns NaN for special `0*inf+nan` combos. ([Python documentation][1])                   |
| `math.fmod(x, y)`      | “C-style” remainder of `x / y`.                       | `math.fmod(-1e-100, 1e100)  # -1e-100` | Remainder has sign of `x` (unlike `%` which uses sign of `y`); `ValueError` or `ZeroDivisionError` from platform if `y == 0`. ([Python documentation][1]) |
| `math.modf(x)`         | Split into fractional and integer parts.              | `math.modf(3.5)  # (0.5, 3.0)`         | Both parts are floats with sign of `x`. ([Python documentation][1])                                                                                       |
| `math.remainder(x, y)` | IEEE-754 style remainder (ties to even).              | `math.remainder(5, 2)  # 1.0`          | `ValueError` for `y == 0` or `x` infinite and `y` finite; result magnitude ≤ `0.5*abs(y)`. ([Python documentation][1])                                    |

[1]: https://docs.python.org/3/library/math.html "math — Mathematical functions — Python 3.14.1 documentation"

# Floating-point manipulation

| Method/Operation                                | What it does                                                | Example                                                  | Special errors / corner cases                                                                                       |
| ----------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `math.copysign(x, y)`                           | `abs(x)` with sign of `y`.                                  | `math.copysign(1.0, -0.0)  # -1.0`                       | Preserves signed zero on supporting platforms. ([Python documentation][1])                                          |
| `math.frexp(x)`                                 | Decompose float as `(m, e)` with `x == m * 2**e`.           | `math.frexp(8.0)  # (0.5, 4)`                            | Zero returns `(0.0, 0)`; `m`’s range is `[0.5,1)` or `0`. ([Python documentation][1])                               |
| `math.ldexp(x, i)`                              | Inverse of `frexp`: `x * (2**i)`.                           | `math.ldexp(0.5, 4)  # 8.0`                              | May overflow to `inf`. ([Python documentation][1])                                                                  |
| `math.isclose(a, b, rel_tol=1e-9, abs_tol=0.0)` | Test approximate equality.                                  | `math.isclose(0.1+0.2, 0.3, rel_tol=1e-9, abs_tol=1e-9)` | `rel_tol` must be ≥0 and <1; `NaN` is never close to anything, including itself. ([Python documentation][1])        |
| `math.isfinite(x)`                              | True if not inf and not NaN.                                | `math.isfinite(1.0)  # True`                             | Works for ints and floats. ([Python documentation][1])                                                              |
| `math.isinf(x)`                                 | True if ±∞.                                                 | `math.isinf(math.inf)`                                   | – ([Python documentation][1])                                                                                       |
| `math.isnan(x)`                                 | True if NaN.                                                | `math.isnan(math.nan)`                                   | `nan` never compares equal; use this to test. ([Python documentation][1])                                           |
| `math.nextafter(x, y, steps=1)`                 | Next representable float `steps` steps from `x` toward `y`. | `math.nextafter(1.0, math.inf)`                          | `steps` can be negative; if `x == y`, returns `y` unless `steps == 0`. ([Python documentation][1])                  |
| `math.ulp(x)`                                   | Size of least significant bit at `x`.                       | `math.ulp(1.0)`                                          | For `x == 0`, returns smallest positive subnormal float; special rules for `NaN`/`inf`. ([Python documentation][1]) |

[1]: https://docs.python.org/3/library/math.html "math — Mathematical functions — Python 3.14.1 documentation"

# Power, exponential, logarithmic

| Method/Operation           | What it does                            | Example                   | Special errors / corner cases                                                                                                                               |
| -------------------------- | --------------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `math.exp(x)`              | (e^x).                                  | `math.exp(1)  # ~2.71828` | Large positive `x` → `OverflowError`; large negative → underflow to 0.0. ([Python documentation][1])                                                        |
| `math.exp2(x)`             | (2^x).                                  | `math.exp2(3)  # 8.0`     | Same overflow/underflow considerations as `exp`. ([Python documentation][1])                                                                                |
| `math.expm1(x)`            | (e^x - 1) with better precision near 0. | `math.expm1(1e-9)`        | Prefer over `exp(x)-1` for tiny `x`. ([Python documentation][1])                                                                                            |
| `math.log(x, base=math.e)` | Logarithm (natural by default).         | `math.log(8, 2)  # 3.0`   | `ValueError` if `x <= 0` or invalid `base` (`base <= 0` or `base == 1`); `TypeError` for complex → use `cmath`. ([Python documentation][1])                 |
| `math.log1p(x)`            | `log(1 + x)` accurately for small `x`.  | `math.log1p(1e-9)`        | Domain: `x > -1`; `x == -1` → `-inf`; `x < -1` → `ValueError`. ([Python documentation][1])                                                                  |
| `math.log2(x)`             | Base-2 log.                             | `math.log2(8)  # 3.0`     | `ValueError` if `x <= 0`. ([Python documentation][1])                                                                                                       |
| `math.log10(x)`            | Base-10 log.                            | `math.log10(100)  # 2.0`  | `ValueError` if `x <= 0`. ([Python documentation][1])                                                                                                       |
| `math.cbrt(x)`             | Cube root of `x`.                       | `math.cbrt(27)  # 3.0`    | Defined for negative `x` too; result is float. ([Python documentation][1])                                                                                  |
| `math.pow(x, y)`           | Float power `x**y`.                     | `math.pow(2, 3)  # 8.0`   | Always returns float; raises `ValueError` or `OverflowError` for invalid combos (e.g. negative base with non-integer exponent). ([Python documentation][1]) |
| `math.sqrt(x)`             | Square root of non-negative `x`.        | `math.sqrt(9)  # 3.0`     | `ValueError` if `x < 0`; use `cmath.sqrt` for complex. ([Python documentation][1])                                                                          |

[1]: https://docs.python.org/3/library/math.html "math — Mathematical functions — Python 3.14.1 documentation"

# Summation & product

| Method/Operation               | What it does                                        | Example                              | Special errors / corner cases                                                            |
| ------------------------------ | --------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------- |
| `math.fsum(iterable)`          | High-precision sum of floats.                       | `math.fsum([0.1]*10)  # exactly 1.0` | More accurate than built-in `sum` for floats; may be slower. ([Python documentation][1]) |
| `math.prod(iterable, start=1)` | Product of all elements (optionally times `start`). | `math.prod([1,2,3,4])  # 24`         | Empty iterable returns `start`. ([Python documentation][1])                              |
| `math.dist(p, q)`              | Euclidean distance between points `p`, `q`.         | `math.dist((0,0), (3,4))  # 5.0`     | `p` and `q` must be same length; else `ValueError`. ([Python documentation][1])          |
| `math.hypot(*coords)`          | Euclidean norm; generalized Pythagoras.             | `math.hypot(3, 4)  # 5.0`            | Multi-D norm: `math.hypot(*p)` ≈ `math.dist((0,...,0), p)`. ([Python documentation][1])  |
| `math.sumprod(p, q)`           | Sum of products: Σ `p[i]*q[i]`.                     | `math.sumprod([1,2],[3,4])  # 11`    | Iterables must be same length; otherwise `ValueError`. ([Python documentation][1])       |

[1]: https://docs.python.org/3/library/math.html "math — Mathematical functions — Python 3.14.1 documentation"

# Angular conversion

| Method/Operation  | What it does       | Example                          | Special errors / corner cases                                       |
| ----------------- | ------------------ | -------------------------------- | ------------------------------------------------------------------- |
| `math.degrees(x)` | Radians → degrees. | `math.degrees(math.pi)  # 180.0` | Accepts any real number; returns float. ([Python documentation][1]) |
| `math.radians(x)` | Degrees → radians. | `math.radians(180)  # ~3.14159`  | – ([Python documentation][1])                                       |

[1]: https://docs.python.org/3/library/math.html "math — Mathematical functions — Python 3.14.1 documentation"

# Trigonometric functions

| Method/Operation   | What it does                              | Example                       | Special errors / corner cases                                                                        |   |                                   |
| ------------------ | ----------------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------- | - | --------------------------------- |
| `math.sin(x)`      | Sine.                                     | `math.sin(math.pi/2)  # 1.0`  | Argument is real only; complex → use `cmath.sin`. ([Python documentation][1])                        |   |                                   |
| `math.cos(x)`      | Cosine.                                   | `math.cos(0)  # 1.0`          | –                                                                                                    |   |                                   |
| `math.tan(x)`      | Tangent.                                  | `math.tan(math.pi/4)  # ~1.0` | Near odd multiples of `pi/2`, result can be huge due to floating-point.                              |   |                                   |
| `math.asin(x)`     | Inverse sine (result in `[-pi/2, pi/2]`). | `math.asin(1)  # pi/2`        | `ValueError` if `                                                                                    | x | > 1`. ([Python documentation][1]) |
| `math.acos(x)`     | Inverse cosine (result in `[0, pi]`).     | `math.acos(-1)  # pi`         | `ValueError` if `                                                                                    | x | > 1`. ([Python documentation][1]) |
| `math.atan(x)`     | Inverse tangent (range `(-pi/2, pi/2)`).  | `math.atan(1)  # ~pi/4`       | Any real `x`.                                                                                        |   |                                   |
| `math.atan2(y, x)` | `atan(y/x)` with correct quadrant.        | `math.atan2(1, 1)`            | Handles `x=0`, signs of both args; much safer than `atan(y/x)` directly. ([Python documentation][1]) |   |                                   |

[1]: https://docs.python.org/3/library/math.html "math — Mathematical functions — Python 3.14.1 documentation"

# Hyperbolic functions

| Method/Operation | What it does                | Example                | Special errors / corner cases                                                |
| ---------------- | --------------------------- | ---------------------- | ---------------------------------------------------------------------------- |
| `math.sinh(x)`   | Hyperbolic sine.            | `math.sinh(0)  # 0.0`  | Large |x| may overflow. ([Python documentation][1])                          |
| `math.cosh(x)`   | Hyperbolic cosine.          | `math.cosh(0)  # 1.0`  | Even function; may overflow. ([Python documentation][1])                     |
| `math.tanh(x)`   | Hyperbolic tangent.         | `math.tanh(0)  # 0.0`  | As |x| → ∞, → ±1. ([Python documentation][1])                                |
| `math.asinh(x)`  | Inverse hyperbolic sine.    | `math.asinh(0)  # 0.0` | Domain all reals. ([Python documentation][1])                                |
| `math.acosh(x)`  | Inverse hyperbolic cosine.  | `math.acosh(1)  # 0.0` | `ValueError` if `x < 1`. ([Python documentation][1])                         |
| `math.atanh(x)`  | Inverse hyperbolic tangent. | `math.atanh(0)  # 0.0` | Domain `(-1, 1)`; `ValueError` at or outside ±1. ([Python documentation][1]) |

[1]: https://docs.python.org/3/library/math.html "math — Mathematical functions — Python 3.14.1 documentation"

# Special functions

| Method/Operation | What it does                               | Example                      | Special errors / corner cases                                                                                        |
| ---------------- | ------------------------------------------ | ---------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `math.erf(x)`    | Error function.                            | `math.erf(0)  # 0.0`         | Smooth from -1 to 1; used for probability / stats. ([Python documentation][1])                                       |
| `math.erfc(x)`   | Complementary error function `1 - erf(x)`. | `math.erfc(0)  # 1.0`        | More accurate than `1 - erf(x)` for large `x`. ([Python documentation][1])                                           |
| `math.gamma(x)`  | Gamma function (≈ factorial generalized).  | `math.gamma(6)  # 120.0`     | Has poles at non-positive integers (raises `ValueError` or returns `inf`); can overflow. ([Python documentation][1]) |
| `math.lgamma(x)` | Natural log of `abs(gamma(x))`.            | `math.lgamma(6)  # log(120)` | Useful when `gamma(x)` would overflow; still `ValueError` at poles. ([Python documentation][1])                      |

[1]: https://docs.python.org/3/library/math.html "math — Mathematical functions — Python 3.14.1 documentation"

# Constants

| Constant   | What it does          | Example                  | Special errors / corner cases                                                 |
| ---------- | --------------------- | ------------------------ | ----------------------------------------------------------------------------- |
| `math.pi`  | π ≈ 3.14159…          | `circ = 2*math.pi*r`     | Double-precision float; not exact mathematical π. ([Python documentation][1]) |
| `math.e`   | e ≈ 2.71828…          | `growth = math.e**t`     | Same floating-point caveats. ([Python documentation][1])                      |
| `math.tau` | τ = 2π ≈ 6.28318…     | `full_circle = math.tau` | Full turn in radians. ([Python documentation][1])                             |
| `math.inf` | Positive infinity.    | `math.isinf(math.inf)`   | Use `-math.inf` for negative infinity. ([Python documentation][1])            |
| `math.nan` | NaN (“not a number”). | `math.isnan(math.nan)`   | NaN != NaN; only test with `isnan`. ([Python documentation][1])               |

[1]: https://docs.python.org/3/library/math.html "math — Mathematical functions — Python 3.14.1 documentation"

Common numeric operations & built-ins (not in math, but used with it)

| Method/Operation        | What it does                         | Example                 | Special errors / corner cases                                                                                                                                                                |
| ----------------------- | ------------------------------------ | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `+  -  *  /  //  %  **` | Basic arithmetic / power.            | `a + b`, `a**2`, `a//b` | `ZeroDivisionError` for `/`, `//`, `%` with zero divisor; `OverflowError` only for huge ints in some C implementations (Python ints are unbounded conceptually). ([Python documentation][1]) |
| `abs(x)`                | Absolute value / magnitude.          | `abs(-3)  # 3`          | Works for complex (returns magnitude); for `complex` use `math` only for reals. ([Python documentation][1])                                                                                  |
| `round(x, ndigits=0)`   | Round to nearest; ties to even.      | `round(2.5)  # 2`       | Bankers’ rounding (2.5→2, 3.5→4); `ndigits` can be negative. ([Python documentation][1])                                                                                                     |
| `pow(x, y, mod=None)`   | Built-in power with optional modulo. | `pow(2, 10, 1000)`      | With 3 args uses modular exponentiation (important for big ints); different from `math.pow` (which returns float, no modulus). ([Python documentation][1])                                   |
| `divmod(a, b)`          | `(a//b, a % b)` in one step.         | `q, r = divmod(7, 3)`   | `ZeroDivisionError` if `b == 0`. ([Python documentation][1])                                                                                                                                 |

[1]: https://docs.python.org/3/library/functions.html?utm_source=chatgpt.com "Built-in Functions — Python 3.14.1 documentation"

## notes / corner cases for the math module

No complex numbers: math functions reject complex inputs (TypeError); for complex use cmath. 
Python documentation
+1

Unless explicitly documented, math functions return floats (even if given ints). 
Python documentation

Many functions may raise:

ValueError for invalid domain (e.g. sqrt(-1), log(0)),

OverflowError if result magnitude is too large for a float,

TypeError for unsupported types.
