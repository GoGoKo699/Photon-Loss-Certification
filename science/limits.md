# Statistical limits after photon loss

This page proves the lower bounds used in the [model and main theorems](model.md). The observer receives independent copies of a known pure-loss channel output and may perform an arbitrary collective POVM. The source has mean photon number at most $E$, and the quantity to recover is its parity

```math
\theta(\rho)=\mathrm{Tr}[(-1)^{\hat n}\rho]
=\frac{\pi}{2}W_\rho(0).
```

Here $\eta\in(0,1]$ is the known transmission, $N$ is the copy budget, and $\delta$ is a parity accuracy or a negative-parity gap. Confidence is $2/3$ unless another value is stated. The positive-null certification task is exactly the origin promise in [model.md](model.md): the null is globally Wigner-positive, and the alternative has $\theta\leq-\delta$. No upper bound for searching for an unknown negative point is inferred from this page.

The statistical reduction is the usual two-point method. Related quantum error-mitigation bounds use the same distinguishability principle; see [TTG23](../references/REFERENCES.md#ttg23). The contribution of the construction below is an explicit energy-bounded pair, a globally Wigner-positive null, and the resulting accuracy dependence. The elementary probability and Wigner identities are proved here so their constants and scope are checkable.

## 1. An exactly tractable pair

For an integer $m\geq2$, define two Fock-diagonal states by the distributions

```math
b_m(n)=2^{-m}\binom mn\mathbf 1_{\lbrace 0\leq n\leq m\rbrace },
\qquad
o_m(n)=2b_m(n)\mathbf 1_{\lbrace n\text{ odd}\rbrace }.
\tag{L1}
```

The binomial distribution has equal even and odd mass. Thus $o_m$ is normalized and is precisely $b_m$ conditioned on odd photon number. We use the same letters for the corresponding diagonal density operators when the meaning is clear.

### Probability generating functions and parity

Their probability generating functions are

```math
B_m(z)=\left(\frac{1+z}{2}\right)^m,
\qquad
O_m(z)=B_m(z)-B_m(-z).
\tag{L2}
```

Consequently

```math
O_m(z)-B_m(z)=-\left(\frac{1-z}{2}\right)^m,
\qquad
B_m(-1)=0,
\qquad O_m(-1)=-1.
\tag{L3}
```

The input parities therefore differ by exactly one.

### Equal moments

For every integer $j<m$, all derivatives through order $j$ of $O_m-B_m$ vanish at $z=1$. Their falling-factorial moments agree through order $m-1$, and hence so do their ordinary photon moments. In particular, for $m\geq2$,

```math
\mathbb E_{b_m}n=\mathbb E_{o_m}n=\frac m2.
\tag{L4}
```

The condition $m\geq2$ matters: the odd-conditioned $m=1$ distribution is concentrated at one photon and has mean one, whereas $b_1$ has mean $1/2$.

For later use, if $s<m$, the common $s$-th ordinary moment is

```math
\mu_s(m)
=2^{-m}\sum_{n=0}^m n^s\binom mn
=\sum_{j=1}^s
\left\lbrace \begin{matrix}s\\j\end{matrix}\right\rbrace
\frac{m^{\underline j}}{2^j}.
\tag{L5}
```

Here the braces are Stirling numbers of the second kind and $m^{\underline j}=m(m-1)\cdots(m-j+1)$. In particular,

```math
\mu_s(m)=\left(\frac m2\right)^s+O_s(m^{s-1}),
\qquad \mu_s(m)\leq m^s.
\tag{L6}
```

The last inequality also bounds each distribution's $s$-th moment without requiring $s<m$, because both supports lie in $\lbrace 0,\ldots,m\rbrace$.

### A globally Wigner-positive member

With the Wigner convention fixed in [model.md](model.md), the number-state Wigner function is

```math
W_{|n\rangle}(\alpha)
=\frac2\pi(-1)^n e^{-2|\alpha|^2}L_n(4|\alpha|^2).
```

The parity normalization is the standard one; see [Royer77](../references/REFERENCES.md#royer77). Expanding the Laguerre polynomials and using the binomial theorem gives

```math
\sum_{n=0}^m\binom mn(-1)^nL_n(x)=\frac{x^m}{m!}.
```

For example, the coefficient of $x^j/j!$ is

```math
(-1)^j\sum_{n=j}^m(-1)^n\binom mn\binom nj
=\binom mj\sum_{r=0}^{m-j}(-1)^r\binom{m-j}{r},
```

which vanishes unless $j=m$. Therefore

```math
\boxed{
W_{b_m}(\alpha)
=\frac2\pi e^{-2|\alpha|^2}
\frac{(2|\alpha|^2)^m}{m!}\geq0.
}
\tag{L7}
```

This also follows by viewing $b_m$ as the output of $50\%$ loss applied to $|m\rangle$, but (L7) supplies an explicit pointwise certificate. For $m\geq1$, its value at the origin is zero. In contrast, $W_{o_m}(0)=-2/\pi$.

## 2. Exact distinguishability after loss

For a Fock-diagonal source, pure loss is binomial thinning. If $P$ is its input generating function, the received generating function is

```math
Q(z)=P(1-\eta+\eta z).
\tag{L8}
```

Let $Q_b=T_\eta b_m$ and $Q_o=T_\eta o_m$. Then

```math
Q_b=\mathrm{Bin}(m,\eta/2),
\qquad
Q_o(z)-Q_b(z)=-\left(\frac{\eta(1-z)}2\right)^m.
\tag{L9}
```

For $0\leq k\leq m$, write

```math
q_{b,k}=\binom mk
\left(\frac\eta2\right)^k
\left(1-\frac\eta2\right)^{m-k},
\qquad
d_k=q_{o,k}-q_{b,k}
=-\left(\frac\eta2\right)^m(-1)^k\binom mk.
\tag{L10}
```

The total variation distance is consequently

```math
\mathrm{TV}(Q_o,Q_b)
=\frac12\sum_k|d_k|=\frac{\eta^m}{2}.
\tag{L11}
```

For independent copies, the following chi-square identity gives the more useful bound. We use

```math
\chi^2(Q_1\Vert Q_0)
=\sum_{k:q_{0,k}>0}\frac{(q_{1,k}-q_{0,k})^2}{q_{0,k}},
```

with the value $+\infty$ if absolute continuity fails. The two laws in (L10) have compatible finite supports, and direct summation gives

```math
\begin{aligned}
\chi^2(Q_o\Vert Q_b)
&=\left(\frac\eta2\right)^{2m}
\sum_{k=0}^m\binom mk
\left(\frac\eta2\right)^{-k}
\left(1-\frac\eta2\right)^{-(m-k)}\\
&=\left(\frac\eta2\right)^{2m}
\left[\frac2\eta+\frac2{2-\eta}\right]^m\\
&=\boxed{\left(\frac\eta{2-\eta}\right)^m}.
\end{aligned}
\tag{L12}
```

At $\eta=1$, this equals one. At every fixed $\eta<1$, it is exponentially small in $m$.

### Dilution by a common state

Let $t$ be any common input probability distribution and $0<w\leq1$. Define

```math
p_0=(1-w)t+w b_m,
\qquad p_1=(1-w)t+w o_m.
\tag{L13}
```

Their parity difference is $w$. Writing $t_\eta=T_\eta t$, their output difference is $w(Q_o-Q_b)$, while the null output satisfies

```math
(1-w)t_{\eta,k}+wq_{b,k}\geq wq_{b,k}.
```

It follows that

```math
\boxed{
\chi^2(T_\eta p_1\Vert T_\eta p_0)
\leq w\left(\frac\eta{2-\eta}\right)^m.
}
\tag{L14}
```

No assumption about $t$'s support is needed. Common-baseline dilution also preserves equality of every photon moment for which $b_m$ and $o_m$ agree.

## 3. A converse for every collective POVM

The received states for (L13) are diagonal. Their $N$-copy states have the form

```math
\sigma_j^{\otimes N}
=\sum_{\boldsymbol k}
q_j^{\otimes N}(\boldsymbol k)
|\boldsymbol k\rangle\langle\boldsymbol k|,
\qquad j=0,1.
```

For any collective POVM $M(dy)$, the conditional law

```math
K(dy\mid\boldsymbol k)
=\langle\boldsymbol k|M(dy)|\boldsymbol k\rangle
```

is a classical stochastic kernel. Thus its outcome law is a postprocessing of the complete photon-number string. Total variation contracts under such kernels. This covers joint quantum measurements, adaptive procedures, private randomization, and a procedure that uses fewer than $N$ copies on some branches. The model does not supply an input reference system or access to the lost environment; see [model.md](model.md).

Let $a$ be an upper bound on the one-copy chi-square divergence. Tensorization and Cauchy–Schwarz imply

```math
\chi^2(Q_1^{\otimes N}\Vert Q_0^{\otimes N})
=(1+\chi^2(Q_1\Vert Q_0))^N-1
\leq e^{Na}-1,
```

```math
\mathrm{TV}(Q_1^{\otimes N},Q_0^{\otimes N})
\leq\frac12\sqrt{e^{Na}-1}.
\tag{L15}
```

Every binary test therefore has worst-case error at least its optimal equal-prior average error, hence at least

```math
\max(\alpha_{\rm I},\alpha_{\rm II})
\geq\frac12-\frac14\sqrt{e^{Na}-1}.
\tag{L16}
```

This is the usual binary discrimination bound; [Wat18](../references/REFERENCES.md#wat18) gives the quantum formulation. In particular, put

```math
c_{\rm LC}=\log(5/4).
```

If $Na\leq c_{\rm LC}$, the right side of (L16) is $3/8>1/3$. Every test with both errors at most $1/3$ must therefore use

```math
N>\frac{c_{\rm LC}}a.
\tag{L17}
```

For the diluted pair this becomes

```math
\boxed{
N>\frac{c_{\rm LC}}w
\left(\frac{2-\eta}{\eta}\right)^m.
}
\tag{L18}
```

For other fixed confidence levels one can use (L16) directly. There is no dependence here on an estimator being unbiased, linear, or based on photon counting.

## 4. Mean-energy parity estimation

For this task choose the common baseline to be vacuum. Then (L13) has

```math
\mathrm{Tr}(\hat n\rho_0)
=\mathrm{Tr}(\hat n\rho_1)=\frac{wm}{2},
\qquad
\theta(\rho_0)=1-w,
\quad \theta(\rho_1)=1-2w.
\tag{L19}
```

Fix $E>0$, and suppose

```math
0<\delta\leq\min\lbrace 1/8,E/4\rbrace .
```

Set

```math
w=4\delta,
\qquad
m=\left\lfloor\frac{E}{2\delta}\right\rfloor\geq2.
\tag{L20}
```

Both states satisfy the mean bound, and their parities differ by $4\delta$. An estimator that is within $\delta$ of the correct parity with probability at least $2/3$ on both states induces a test with both errors at most $1/3$, by thresholding at the midpoint of their parities. Equation (L18) yields the explicit converse

```math
\boxed{
N_{\rm est}(E,\eta,\delta,1/3)
>
\frac{c_{\rm LC}}{4\delta}
\left(\frac{2-\eta}{\eta}\right)^{\left\lfloor E/(2\delta)\right\rfloor}.
}
\tag{L21}
```

These parities need not be negative. The estimation lower bound holds at every fixed $E>0$, including $E<1/2$.

### Revealing the exact common energy does not remove the obstruction

The two states already have the same mean. One can additionally make that mean exactly equal to the announced budget $E$, without changing $w$, $m$, or (L18). Let

```math
a=\frac{E-wm/2}{1-w},
\qquad
\xi_a=(1-a)|0\rangle\langle0|+a|1\rangle\langle1|.
```

For $m=\lfloor2E/w\rfloor$ and $w\leq1/2$,

```math
0\leq a<\frac{w}{2(1-w)}\leq\frac12.
```

Replacing the vacuum baseline by $\xi_a$ makes both means exactly $E$. Their parity difference remains $w$, and the common-baseline chi-square bound remains (L14). Thus a procedure given the exact common mean, in addition to the inequality promise, still faces the same pair.

This is a lower-bound refinement. The upper-bound model and its compact feasible class use $\mathrm{Tr}(\hat n\rho)\leq E$; the set with equality need not be compact, as discussed below.

## 5. Globally positive null versus origin negativity

Use the common baseline

```math
\tau=\frac{|0\rangle\langle0|+|1\rangle\langle1|}{2}=b_1.
```

Its mean is $1/2$, its origin parity is zero, and its Wigner function is globally nonnegative by (L7). Consequently

```math
\rho_0=(1-w)\tau+w b_m,
\qquad
\rho_1=(1-w)\tau+w o_m
\tag{L22}
```

satisfy

```math
W_{\rho_0}(\alpha)\geq0\quad\text{for every }\alpha,
\qquad
\theta(\rho_0)=0,
\qquad \theta(\rho_1)=-w,
```

```math
\mathrm{Tr}(\hat n\rho_j)
=\frac{1+w(m-1)}2,
\qquad j=0,1.
\tag{L23}
```

For $E>1/2$ and

```math
0<\delta\leq\min\lbrace 1/2,2E-1\rbrace ,
```

take

```math
w=\delta,
\qquad
m=\left\lfloor1+\frac{2E-1}{\delta}\right\rfloor\geq2.
\tag{L24}
```

This is a valid null/alternative pair for the certification promise. Hence

```math
\boxed{
N_{\rm cert}(E,\eta,\delta,1/3)
>
\frac{c_{\rm LC}}{\delta}
\left(\frac{2-\eta}{\eta}\right)^{
\left\lfloor1+(2E-1)/\delta\right\rfloor}.
}
\tag{L25}
```

The null is positive at every phase-space point, not only at the tested origin. Therefore this same pair also obstructs any broader uniform negativity-certification task whose alternatives include these states. The matching upper theorem remains the prescribed-origin task.

### Exact-energy version with a positive baseline

Let $e_w=[1+w(m-1)]/2\leq E$, with $m$ from (L24). Its slack obeys $0\leq E-e_w<w/2$. Set

```math
a=\frac{E-wm/2}{1-w}
=\frac12+\frac{E-e_w}{1-w},
\qquad
\tau_a=(2-2a)b_1+(2a-1)b_2.
\tag{L26}
```

For $w\leq1/2$, one has $1/2\leq a\leq1$, so $\tau_a$ is a probability mixture. Its mean is $a$, its parity is zero, and its Wigner function is globally nonnegative. Replacing $\tau$ by $\tau_a$ in (L22) gives two states with mean exactly $E$, with the same null/alternative parities and the same chi-square bound. The harder statistical conclusion therefore survives exact common-energy side information.

## 6. Parametric lower bounds

The exponential mechanism alone is insufficient at $\eta=1$. A separate two-level construction supplies the usual $\delta^{-2}$ term uniformly up to the lossless endpoint.

### Estimation

Let

```math
a_E=\min\lbrace E/2,1/4\rbrace >0,
\qquad
\rho_t=(1-t)|0\rangle\langle0|+t|1\rangle\langle1|.
```

For $\delta\leq a_E/2$, the two states $\rho_{a_E}$ and $\rho_{a_E+2\delta}$ both have mean at most $E$, and their parities differ by $4\delta$. Their received laws are Bernoulli with success probabilities $\eta a_E$ and $\eta(a_E+2\delta)$. Thus

```math
\chi^2
=\frac{4\eta\delta^2}{a_E(1-\eta a_E)}
\leq\frac{4\delta^2}{a_E(1-a_E)}.
```

Equations (L16)–(L17) imply

```math
\boxed{
N_{\rm est}(E,\eta,\delta,1/3)
>\frac{c_{\rm LC} a_E(1-a_E)}{4\delta^2}.
}
\tag{L27}
```

The constant depends on the fixed energy budget, but not on $\eta\in(0,1]$.

### Positive-null certification

Take $\rho_{1/2}=\tau$ for the null and $\rho_{(1+\delta)/2}$ for the alternative. The latter has parity $-\delta$ and mean $(1+\delta)/2$. For $\delta\leq\min\lbrace 1,2E-1\rbrace$, both states are allowed. Their received chi-square divergence is

```math
\chi^2
=\frac{\eta\delta^2}{2-\eta}
\leq\delta^2.
```

Consequently

```math
\boxed{
N_{\rm cert}(E,\eta,\delta,1/3)
>\frac{c_{\rm LC}}{\delta^2}.
}
\tag{L28}
```

## 7. Uniform weak-loss consequence

Write $\nu=1-\eta$. For $\eta\in[\eta_0,1]$,

```math
\lambda_\eta
:=\log\frac{2-\eta}{\eta}
=2\mathrm{artanh}\nu,
```

```math
2\nu\leq\lambda_\eta
\leq\frac{2\nu}{\eta_0(2-\eta_0)}.
\tag{L29}
```

For fixed $E>0$, (L21) and (L27), together with

```math
\left\lfloor\frac{E}{2\delta}\right\rfloor
\geq\frac{E}{4\delta}
\quad\text{when }\delta\leq E/4,
```

give the lower half of

```math
\log N_{\rm est}(E,\eta,\delta,1/3)
=\Theta_{E,\eta_0} \left(
\log\frac1\delta+\frac{\nu}{\delta}\right).
\tag{L30}
```

The upper half is proved in [recovery.md](recovery.md). One takes the maximum of the parametric and the hard-tail lower bounds; the maximum of two nonnegative scales is within a factor two of their sum. Fixed multiplicative constants and their logarithms are absorbed by choosing a sufficiently small $\delta_0(E,\eta_0)>0$.

Similarly, for fixed $E>1/2$, (L25) and (L28) give the lower half of the same law for $N_{\rm cert}$. In the certification exponent the explicit lower energy scale is $E-1/2$, whereas the upper uses $E$. There is no uniform matching assertion as $E\downarrow1/2$ together with $\delta$.

At $\eta=1$, (L27)–(L28) match direct parity sampling and yield $N=\Theta(\delta^{-2})$ in the corresponding nontrivial fixed-budget classes. For any fixed $\eta<1$, the lower bounds are exponential in $1/\delta$.

For a varying loss schedule and fixed $E$, the complete uniform law permits a polynomial bound in $1/\delta$ precisely when $\nu=O(\delta\log(1/\delta))$. The stronger condition $\nu E=O(\delta)$ is sufficient for direct, uncorrected parity sampling because its loss bias is at most $2\nu E$; it is not the full polynomial/superpolynomial boundary.

## 8. Budgets, compactness, and endpoints

- **Zero energy.** At $E=0$, the source is vacuum and parity is known without copies. Bounds that divide by $E$ or use $a_E>0$ do not apply.
- **Empty negative alternative.** Since $p_{\rm odd}=(1-\theta)/2$ and $\mathbb E n\geq p_{\rm odd}$, the promise $\theta\leq-\delta$ requires $E\geq(1+\delta)/2$. This condition is also sufficient, by the vacuum/one-photon mixture above. In particular, no positive origin gap is possible for $E\leq1/2$.
- **Coarse estimation.** The full parity range under mean budget $E$ is $[1-2\min\lbrace E,1\rbrace ,1]$. For accuracy at least $\min\lbrace E,1\rbrace$, a constant estimate suffices. The theorems concern the small-$\delta$ regime with a fixed nonzero budget.
- **Sublevel compactness.** The diagonal class $\lbrace p:\sum p_n=1,\ \sum n p_n\leq E\rbrace$ is compact in $\ell_1$: its tails are uniformly bounded by $E/(M+1)$, and the moment inequality is closed under $\ell_1$ convergence by Fatou's lemma. This supports existence of constrained extremizers. Parity and binomial thinning are continuous in this topology.
- **Exact-energy levels are different.** The class $\sum n p_n=E$ need not be closed in $\ell_1$: for $m\to\infty$, $(1-E/m)|0\rangle\langle0|+(E/m)|m\rangle\langle m|$ has mean $E$ and converges to vacuum. The exact-energy lower constructions above do not assert compactness of that equality class or replace the upper-bound inequality model.
- **Identifiability.** For every $\eta>0$, binomial thinning is injective on probability distributions: equality of output generating functions gives equality of input generating functions on an open disk, hence everywhere in the unit disk by the identity theorem and at $-1$ by continuity. The obstruction is sample complexity, not nonidentifiability. At $\eta=0$, all outputs are vacuum and this argument fails; that endpoint is excluded.
- **No claim of a leading exponential constant.** Equations (L21), (L25), and the recovery bounds establish matching logarithmic order. They do not identify the exact optimal exponent multiplying $1/\delta$.

The higher-moment and exponential-moment variants, including their budget thresholds and constructive upper bounds, are proved separately in [tail-promises.md](tail-promises.md).
