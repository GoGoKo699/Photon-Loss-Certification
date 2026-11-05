# Recovering input parity from photon-loss data

The input mean photon number controls one derivative of its probability-generating function. Continuing that derivative from the disk observed through loss, and then integrating to the parity point, gives a logarithmic continuity bound. A finite photon-count measurement and a constrained linear program turn this bound into a uniform estimator with explicit confidence.

The result concerns the Wigner function at the prescribed origin. The transmissivity and an upper bound on the input mean photon number are known. Every measurement acts on copies received **after** the loss channel.

## 1. Model and notation

Let $\rho$ be an arbitrary single-mode state, let $\hat n$ be its photon-number operator, and suppose

```math
\mathrm{Tr}(\hat n\rho)\le E.
\qquad\text{(R1)}
```

The receiver obtains $N$ independent copies of $\mathcal L_\eta(\rho)$, where $0<\eta\le1$ is the known pure-loss transmissivity. Define the input and output photon-count distributions by

```math
p_n=\langle n|\rho|n\rangle,
\qquad
q_k=(T_\eta p)_k
=\sum_{n=k}^{\infty}\binom nk\eta^k(1-\eta)^{n-k}p_n.
\qquad\text{(R2)}
```

Thus $\sum_k kq_k=\eta\sum_n np_n\le\eta E$. Input coherences affect neither this count distribution nor the target

```math
\theta(p)=\mathrm{Tr}[(-1)^{\hat n}\rho]
=\sum_{n=0}^{\infty}(-1)^np_n,
\qquad
W_\rho(0)=\frac2\pi\theta(p).
\qquad\text{(R3)}
```

The convention in (R3) fixes the Wigner normalization. An additive parity error $\delta$ is an additive Wigner-value error $2\delta/\pi$.

For probability distributions, $\Vert p-p'\Vert _1=\sum_n|p_n-p_n'|$; total variation is half this quantity. Natural logarithms are used throughout. The confidence parameter is $0<\beta<1$, so the required success probability is at least $1-\beta$.

Set

```math
\mathcal P_E=
\left\lbrace p:p_n\ge0,\ \sum_n p_n=1,\ \sum_n np_n\le E\right\rbrace .
\qquad\text{(R4)}
```

When $E=0$, the state is the vacuum and its parity is exactly one. The nontrivial statements below assume $E>0$. Transmissivity zero is excluded: the output is then independent of the input.

## 2. A boundary continuity theorem

### Theorem R1: an explicit first-moment modulus

Fix $E>0$, $0<\eta\le1$, and $0\lt h<\eta$. Define

```math
c=1-\eta,
\qquad r=\eta-h,
\qquad
\kappa=\frac{\eta}
{(2-\eta)\log[(2-\eta)/(\eta-h)]}.
\qquad\text{(R5)}
```

If $p,p'\in\mathcal P_E$ satisfy

```math
\Vert T_\eta p-T_\eta p'\Vert _1\le\epsilon,
\qquad 0<\epsilon<2Eh,
\qquad\text{(R6)}
```

then

```math
\boxed{
|\theta(p)-\theta(p')|
\le
\epsilon+
\frac{2E}{\kappa\log(2Eh/\epsilon)}.
}
\qquad\text{(R7)}
```

The right side may also be replaced by its minimum with two. If the output distributions are identical, the input distributions, and hence their parities, are identical.

### Proof: the generating function and its derivative

Write

```math
P(z)=\sum_{n=0}^{\infty}p_nz^n,
\qquad
\widetilde P(z)=\sum_{n=0}^{\infty}p_n'z^n,
\qquad
f(z)=P(z)-\widetilde P(z).
\qquad\text{(R8)}
```

Derivatives of $f$ are written $f^{(1)},f^{(2)},\ldots$. Both generating functions are analytic in the open unit disk and continuous on its closure. Moreover,

```math
\sum_{n=1}^{\infty}n|p_n-p_n'|\le2E.
\qquad\text{(R9)}
```

The derivative series consequently converges uniformly on the closed unit disk, giving a continuous boundary extension and

```math
|f^{(1)}(z)|\le2E
\qquad (|z|\le1).
\qquad\text{(R10)}
```

This first-derivative bound, including its boundary continuity, is the specific regularity supplied by the mean-energy promise.

Let $Q$ and $\widetilde Q$ be the corresponding output generating functions. Binomial thinning gives

```math
Q(w)=P(c+\eta w),
\qquad
\widetilde Q(w)=\widetilde P(c+\eta w).
\qquad\text{(R11)}
```

The series are absolutely convergent for $|w|\le1$, so (R6) implies

```math
|f(z)|\le\epsilon
\qquad
\text{on }D_\eta=\lbrace z:|z-c|\le\eta\rbrace .
\qquad\text{(R12)}
```

The observed disk touches the unit circle at $z=1$. On the strictly smaller disk $D_r=\lbrace z:|z-c|\le r\rbrace$, Cauchy's derivative estimate gives

```math
|f^{(1)}(z)|\le\frac\epsilon h.
\qquad\text{(R13)}
```

To justify (R13) even when a Cauchy circle of radius $h$ touches $z=1$, first use every radius $h'\lt h$ and then let $h'$ increase to $h$. No analytic extension across the unit circle is assumed.

### Proof: harmonic measure and an explicit barrier

Consider the doubly connected domain

```math
\Omega=\lbrace z:|z|<1\rbrace \setminus D_r.
\qquad\text{(R14)}
```

Its two boundary circles are disjoint because $c+r=1-h<1$. Let $\omega$ be harmonic on $\Omega$, continuous on its closure, equal to one on the inner circle and zero on the outer circle. The two-constants theorem, applied to the subharmonic function $\log|f^{(1)}|$, gives

```math
|f^{(1)}(z)|
\le 2E\exp[-\omega(z)L],
\qquad
L=\log\frac{2Eh}{\epsilon}>0.
\qquad\text{(R15)}
```

Equivalently, subtract the harmonic function $\log(2E)-\omega L$ from $\log|f^{(1)}|$ and apply the maximum principle. Zeros of the derivative are allowed: the logarithm is subharmonic with value minus infinity there. If the derivative vanishes identically, the conclusion follows directly.

The Green function of the unit disk with its pole at $c$ is

```math
g(z)=-\log\left|\frac{z-c}{1-cz}\right|.
\qquad\text{(R16)}
```

Its pole is inside the removed disk. It is positive and harmonic on $\Omega$, and zero on the outer circle. On the inner circle,

```math
g(z)=\log\frac{|1-cz|}{r}
\le\log\frac{1+c}{r}=:\mathcal M.
\qquad\text{(R17)}
```

Here $\mathcal M>0$. The maximum principle applied to $\omega-g/\mathcal M$ therefore yields

```math
\omega(z)\ge\frac{g(z)}{\mathcal M}.
\qquad\text{(R18)}
```

Let $x_0=c-r$. For $-1\le x\le x_0$, the ratio $(c-x)/(1-cx)$ lies in $(0,1]$. Hence

```math
\begin{aligned}
g(x)
&=-\log\frac{c-x}{1-cx}\\
&\ge1-\frac{c-x}{1-cx}\\
&=\frac{(1-c)(1+x)}{1-cx}\\
&\ge\frac{\eta(1+x)}{2-\eta}.
\end{aligned}
\qquad\text{(R19)}
```

Together, (R18) and (R19) give the explicit lower bound

```math
\omega(x)\ge\kappa(1+x).
\qquad\text{(R20)}
```

### Proof: integration to the parity point

The point $x_0$ belongs to the observed disk, so $|f(x_0)|\le\epsilon$. The boundary continuity of the derivative established in (R9) allows integration along the closed interval $[-1,x_0]$. Using (R15) and (R20),

```math
\begin{aligned}
|f(-1)|
&\le |f(x_0)|+\int_{-1}^{x_0}|f^{(1)}(x)| dx\\
&\le\epsilon+
2E\int_{-1}^{x_0}e^{-\kappa L(1+x)} dx\\
&=\epsilon+
\frac{2E[1-e^{-\kappa L(1+x_0)}]}{\kappa L}\\
&\le\epsilon+\frac{2E}{\kappa L}.
\end{aligned}
\qquad\text{(R21)}
```

Since $f(-1)=\theta(p)-\theta(p')$, this proves (R7). If the output distance is zero, (R11) makes $f$ vanish on an open disk; the identity theorem and continuity give $f=0$ on the closed unit disk. This completes the proof.

For fixed $0<\eta<1$, taking $h=\eta/2$ makes $\kappa$ a positive constant depending only on $\eta$. The resulting modulus is of order $E/\log(E/\epsilon)$ as $\epsilon$ tends to zero. The derivative and its integral are essential to this estimate; continuing only the bound on $f$ does not give this calculation.

## 3. A finite estimator with confidence and overflow

The following result separates estimation of the received distribution from continuation to the input parity. It also makes the measurement and optimization finite.

### Theorem R2: finite constrained recovery of a count distribution

Let $E>0$, $0<\eta\le1$, $0<\epsilon<1$, and $0<\beta<1$. Set

```math
M=\left\lceil\frac{8E}{\epsilon}\right\rceil,
\qquad
H_M=\sum_{j=1}^{M}\frac1j,
\qquad
A_M=2+\sqrt{\eta E H_M},
\qquad\text{(R22)}
```

and take

```math
\boxed{
N\ge
\left\lceil
\frac{16}{\epsilon^2}
\left[A_M+\sqrt{2\log(1/\beta)}\right]^2
\right\rceil.
}
\qquad\text{(R23)}
```

On each received copy perform the finite measurement with outcomes

```math
0,1,\ldots,M,\ast.
\qquad\text{(R24)}
```

The first $M+1$ effects are $|k\rangle\langle k|$, and the overflow effect is $I-\sum_{k=0}^{M}|k\rangle\langle k|$. Let $\widehat q_k$ and $\widehat q_{\ast}$ be the empirical frequencies.

Use a deterministic linear-program rule to find a probability vector $\widehat p=(\widehat p_0,\ldots,\widehat p_M)$ satisfying

```math
\widehat p_n\ge0,
\qquad
\sum_{n=0}^{M}\widehat p_n=1,
\qquad
\sum_{n=0}^{M}n\widehat p_n\le E,
\qquad\text{(R25)}
```

and

```math
\sum_{k=0}^{M}
\left|(T_\eta\widehat p)_k-\widehat q_k\right|
+\widehat q_{\ast}
\le\frac\epsilon2.
\qquad\text{(R26)}
```

Absolute values in (R26) are implemented with nonnegative linear-program slack variables. If the system is infeasible, report an arbitrary parity estimate in $[-1,1]$, for example zero. Otherwise report

```math
\widehat\theta=\sum_{n=0}^{M}(-1)^n\widehat p_n.
\qquad\text{(R27)}
```

For every $p\in\mathcal P_E$, with probability at least $1-\beta$ the constraints are feasible and every feasible fit satisfies

```math
\Vert T_\eta\widehat p-T_\eta p\Vert _1
\le\frac{3\epsilon}{4}\le\epsilon.
\qquad\text{(R28)}
```

Consequently, whenever $\epsilon<2Eh$, Theorem R1 gives on the same event

```math
|\widehat\theta-\theta(p)|
\le
\epsilon+\frac{2E}{\kappa\log(2Eh/\epsilon)}.
\qquad\text{(R29)}
```

### Proof: concentration of the finite histogram

Let $\mathsf A_M$ aggregate a distribution into the categories in (R24), and write $\overline q=\mathsf A_Mq$. For any category, the empirical variance is $\overline q_j(1-\overline q_j)/N$, so

```math
\mathbb E|\widehat q_j-\overline q_j|
\le\sqrt{\frac{\overline q_j}{N}}.
\qquad\text{(R30)}
```

The zero-count and overflow categories each contribute at most $1/\sqrt N$. For the remaining categories, weighted Cauchy–Schwarz gives

```math
\begin{aligned}
\sum_{k=1}^{M}\sqrt{q_k}
&=\sum_{k=1}^{M}\frac{\sqrt{kq_k}}{\sqrt k}\\
&\le
\sqrt{\left(\sum_{k=1}^{M}kq_k\right)H_M}\\
&\le\sqrt{\eta E H_M}.
\end{aligned}
\qquad\text{(R31)}
```

It follows that

```math
\mathbb E\Vert \widehat q-\overline q\Vert _1
\le\frac{A_M}{\sqrt N}.
\qquad\text{(R32)}
```

Changing one sample changes the empirical vector by at most $2/N$ in $\ell^1$ and hence changes its distance from $\overline q$ by at most $2/N$. The bounded-differences inequality therefore yields

```math
\Pr \left\lbrace
\Vert \widehat q-\overline q\Vert _1
>\frac{A_M}{\sqrt N}+t
\right\rbrace
\le e^{-Nt^2/2}.
\qquad\text{(R33)}
```

Taking $t=\sqrt{2\log(1/\beta)/N}$ and using (R23) proves that, with probability at least $1-\beta$,

```math
\Vert \widehat q-\mathsf A_Mq\Vert _1\le\frac\epsilon4.
\qquad\text{(R34)}
```

### Proof: feasibility without inverting a truncated tail

For analysis only, move the true input tail above $M$ to the vacuum:

```math
p^{[M]}_0=p_0+\sum_{n>M}p_n,
\qquad
p^{[M]}_n=p_n\quad(1\le n\le M),
\qquad
p^{[M]}_n=0\quad(n>M).
\qquad\text{(R35)}
```

This preserves normalization and decreases the mean. Since every photon number in the removed tail is at least $M+1$,

```math
\Vert p-p^{[M]}\Vert _1
=2\sum_{n>M}p_n
\le\frac{2E}{M+1}
\le\frac\epsilon4.
\qquad\text{(R36)}
```

The stochastic maps $T_\eta$ and $\mathsf A_M$ contract $\ell^1$ distance. On event (R34),

```math
\left\Vert
\mathsf A_MT_\eta p^{[M]}-\widehat q
\right\Vert _1
\le\frac\epsilon4+\frac\epsilon4
=\frac\epsilon2.
\qquad\text{(R37)}
```

Thus $p^{[M]}$ is a feasible candidate for (R25)–(R26). It is only a proof witness; the estimator never needs to know the true tail.

For every fitted input supported on $0,\ldots,M$, the thinned law also has no mass above $M$. Consequently aggregation causes **no loss of distance** when comparing it with the true output:

```math
\begin{aligned}
\Vert T_\eta\widehat p-q\Vert _1
&=\sum_{k=0}^{M}|(T_\eta\widehat p)_k-q_k|
+\sum_{k>M}q_k\\
&=\left\Vert
\mathsf A_MT_\eta\widehat p-\mathsf A_Mq
\right\Vert _1.
\end{aligned}
\qquad\text{(R38)}
```

Combining (R26), (R34), and (R38) gives (R28). Both $p$ and $\widehat p$ have mean at most $E$, so Theorem R1 applies to them directly. No inverse channel is applied to a discarded tail, and no projection of the full quantum state is used. This proves the theorem.

### Certified channel coefficients

There is a useful finite-precision version of the same construction. Suppose the finite channel table $\widetilde T$ obeys the certified column bound

```math
\max_{0\le n\le M}
\sum_{k=0}^{M}
|\widetilde T_{kn}-(T_\eta)_{kn}|
\le\frac\epsilon8.
\qquad\text{(R39)}
```

Keep normalization, positivity and the mean constraint (R25), and replace (R26) by

```math
\sum_{k=0}^{M}
| (\widetilde T\widehat p)_k-\widehat q_k |
+\widehat q_{\ast}
\le\frac{5\epsilon}{8}.
\qquad\text{(R40)}
```

On event (R34), the witness $p^{[M]}$ remains feasible: its sampling, truncation and channel-table errors sum to at most $\epsilon/4+\epsilon/4+\epsilon/8=5\epsilon/8$. Every feasible fit has

```math
\Vert T_\eta\widehat p-q\Vert _1
\le\frac\epsilon8+\frac{5\epsilon}{8}
+\frac\epsilon4=\epsilon.
\qquad\text{(R41)}
```

Thus (R29) remains valid. A sufficient entrywise table accuracy is $\epsilon/[8(M+1)]$. Approximate optimization must also certify the displayed normalization, mean and residual constraints; an uncharged numerical residual is not part of the guarantee.

For rational parameters, these are finite rational linear programs. If an analytic parameter choice below is irrational, a certified rational $\epsilon$ between one half and one times that choice preserves all bounds up to numerical constants. The statistical theorem treats $E$ and $\eta$ as known parameters; it does not include calibration uncertainty in either quantity.

## 4. Explicit choices for any positive transmissivity

### Corollary R3: parity accuracy with a finite sample bound

Let $E>0$, $0<\eta\le1$, $0<\delta\le1$, and $0<\beta<1$. Choose any $h\in(0,\eta)$, use (R5), and set

```math
\epsilon
=\min\left\lbrace \frac\delta8,Eh\right\rbrace
\exp\left[-\frac{8E}{\kappa\delta}\right].
\qquad\text{(R42)}
```

Use the measurement, sample count and fit in Theorem R2, or its certified-coefficient version. Then

```math
\Pr \left\lbrace
|\widehat\theta-\theta(p)|>\frac{3\delta}{8}
\right\rbrace \le\beta
\qquad\text{for every }p\in\mathcal P_E.
\qquad\text{(R43)}
```

Indeed $\epsilon\le\delta/8$ and

```math
\log\frac{2Eh}{\epsilon}
\ge\log2+\frac{8E}{\kappa\delta},
\qquad\text{(R44)}
```

so the second term in (R29) is at most $\delta/4$. All constants in the construction are explicit, and no asymptotic statement is required for (R43).

For fixed $E>0$, fixed $0<\eta<1$, and fixed confidence, choosing $h=\eta/2$ yields a sample upper bound exponential in $E/\delta$, up to polynomial and logarithmic factors. The constants displayed here are sufficient constants, not optimal leading exponential constants.

## 5. A bound uniform as loss vanishes

A fixed choice such as $h=\eta/2$ is adequate at a fixed loss rate, but does not expose the correct weak-loss behavior. The next choice retains an ordinary polynomial sample cost when the loss vanishes sufficiently quickly.

### Corollary R4: uniform weak-loss upper bound

Fix $0<\eta_0\le1$. Suppose

```math
\eta\in[\eta_0,1],
\qquad
0<\delta\le\min\left\lbrace \frac14,\eta_0E\right\rbrace .
\qquad\text{(R45)}
```

Define

```math
\nu=1-\eta,
\qquad b=\frac{\delta}{4E},
\qquad
h=\min\left\lbrace \frac\eta2,\max\lbrace \nu,b\rbrace \right\rbrace ,
\qquad\text{(R46)}
```

and use $\kappa$ from (R5). The choice

```math
\epsilon=\frac\delta8
\exp\left[-\frac{8E}{\kappa\delta}\right]
\qquad\text{(R47)}
```

and the explicit sample count (R23) satisfy (R43). In particular, for constants depending only on $\eta_0$,

```math
N\le
C_{\eta_0}\delta^{-2}
\left[
1+E\left(
1+\log\frac{E+1}{\delta}
+\frac{\nu E}{\delta}
\right)
+\log\frac1\beta
\right]
\exp\left[C_{\eta_0}\frac{\nu E}{\delta}\right].
\qquad\text{(R48)}
```

Here and below an upper bound on $N$ refers to choosing $N$ equal to the sufficient integer in (R23), rather than to every larger sample count. At confidence $2/3$, (R48) implies

```math
\log N
=O_{\eta_0}\left(
\log\frac{E+1}{\delta}
+\frac{(1-\eta)E}{\delta}
\right).
\qquad\text{(R49)}
```

### Proof of uniformity and explicit conservative constants

The restriction (R45) gives $b\le\eta_0/4\le\eta/4$. Therefore

```math
b\le h\le\frac\eta2,
\qquad
h\le\nu+b,
\qquad
r=\eta-h\ge\frac\eta2.
\qquad\text{(R50)}
```

Using $\log(1+x)\le x$,

```math
\begin{aligned}
\frac1\kappa
&=\frac{2-\eta}{\eta}
\log\left(1+\frac{2\nu+h}{\eta-h}\right)\\
&\le\frac4{\eta_0^2}(2\nu+h)\\
&\le\frac{12}{\eta_0^2}(\nu+b).
\end{aligned}
\qquad\text{(R51)}
```

Since $Eh\ge\delta/4$, (R47) is exactly the choice (R42) in this regime. Also

```math
\epsilon\ge c_0\delta e^{-C_0R},
\qquad
R=\frac{\nu E}{\delta},
\qquad
c_0=\frac18e^{-24/\eta_0^2},
\qquad
C_0=\frac{96}{\eta_0^2}.
\qquad\text{(R52)}
```

For a fully numerical, deliberately conservative form of (R48), $H_M\le1+\log M$ and $M\le1+8E/\epsilon$ yield

```math
\begin{aligned}
N\le 1+48c_0^{-2}\delta^{-2}e^{2C_0R}
\bigg[4
&+E\left\lbrace 1+
\log\left(1+\frac{8E}{c_0\delta}\right)
+C_0R\right\rbrace \\
&+2\log\frac1\beta\bigg].
\end{aligned}
\qquad\text{(R53)}
```

To obtain this expression, apply $(x+y+z)^2\le3(x^2+y^2+z^2)$ to (R23), use $\eta\le1$, and bound

```math
\log\left(1+\frac{8E}{\epsilon}\right)
\le
\log\left(1+\frac{8E}{c_0\delta}\right)+C_0R.
\qquad\text{(R54)}
```

Absorbing constants and logarithms in (R53) gives (R48). To check that (R49) is uniform in the energy bound, put $L_\delta=\log[(E+1)/\delta]$. Assumption (R45) gives $L_\delta\ge\log4$. The logarithm of the prefactor in (R48) is at most a constant depending only on $\eta_0$, plus

```math
\log(E+1)+\log(1+L_\delta+R)
+\log[1+\log(1/\beta)].
```

Use $\log(E+1)\le L_\delta$ and $\log(1+L_\delta+R)\le L_\delta+R$. This proves the more general bound

```math
\log N\le C_{\eta_0}
\left\lbrace
L_\delta+R+\log[1+\log(1/\beta)]
\right\rbrace ,
```

and yields (R49) when $\beta=1/3$. Any other fixed confidence changes only constants. The bounds stay finite at $\eta=1$ and introduce no factor $\log[1/(1-\eta)]$. No exact coefficient in the sample-complexity exponent is asserted.

At fixed $E$, the upper bound is polynomial in $1/\delta$ whenever $(1-\eta)E/\delta=O(\log(1/\delta))$. The necessity of a corresponding loss budget requires the lower bound; it is not inferred from this construction alone.

## 6. Direct parity in the loss-free and very weak-loss regimes

There is a simpler estimator when the bias from loss is already below the required accuracy. Let $K$ be the received photon count. Conditional on an input count $n$, the lost count $L$ is binomial with mean $\nu n$, and $K=n-L$. Therefore

```math
\begin{aligned}
\left|\mathbb E[(-1)^K\mid n]-(-1)^n\right|
&\le2\Pr\lbrace L\text{ is odd}\mid n\rbrace \\
&\le2\Pr\lbrace L\ge1\mid n\rbrace \\
&\le2\nu n.
\end{aligned}
\qquad\text{(R55)}
```

Averaging proves

```math
|\theta(T_\eta p)-\theta(p)|\le2\nu E.
\qquad\text{(R56)}
```

The empirical mean of received parity outcomes, each in $\lbrace -1,1\rbrace$, obeys Hoeffding's bound

```math
\Pr\lbrace  |\widehat\theta_{\rm out}-\theta(T_\eta p)|>t\rbrace
\le2e^{-Nt^2/2}.
\qquad\text{(R57)}
```

Whenever $\delta>2\nu E$, the choice

```math
N\ge\frac{2\log(2/\beta)}{(\delta-2\nu E)^2}
\qquad\text{(R58)}
```

suffices for input-parity error at most $\delta$. In particular:

- At $\eta=1$, $N\ge2\delta^{-2}\log(2/\beta)$ suffices.
- If $\nu E\le\delta/4$, $N\ge8\delta^{-2}\log(2/\beta)$ suffices.
- If $2E\le\delta$, the constant estimate one already has error at most $\delta$, because $1-\theta(p)=2\sum_{n\text{ odd}}p_n\le2E$.

These statements give explicit alternatives to solving the reconstruction program in regimes where it is unnecessary.

## 7. Certification at the prescribed origin

Consider the promise problem

```math
H_0:\ W_\rho(\alpha)\ge0\text{ for all }\alpha,
\qquad
H_1:\ \theta(p)\le-\delta,
\qquad\text{(R59)}
```

with the same mean-energy promise. The null implies $\theta(p)\ge0$. Use Corollary R3 or R4 with parameter $\delta$ and declare the negative alternative when

```math
\widehat\theta<-\frac\delta2.
\qquad\text{(R60)}
```

On event (R43), every null gives $\widehat\theta\ge-3\delta/8$, and every alternative gives $\widehat\theta\le-5\delta/8$. The test therefore has error probability at most $\beta$ under either promise. Its alternative has Wigner depth at least $2\delta/\pi$ at the origin.

The same test works for the larger null class $\theta(p)\ge0$. It does not certify global Wigner positivity when it accepts the null, and its guarantee does not include searching phase space for an unknown negative point. The globally positive null in (R59) is useful for comparison with the lower bound, while the recovery construction itself only uses the parity sign at the prescribed origin.

## 8. Charged resources and interpretation

The sample count charges every received copy, including observations assigned to overflow. There is no conditioning on a successful filter, no access to the loss environment, and no operation before attenuation. The construction uses independent finite photon-count measurements, so it is an allowed strategy within a model that also permits arbitrary collective output POVMs.

The statistical bound does not imply a small reconstruction problem. The finite measurement has $M+2$ outcomes and resolves counts through $M$. The linear program has $M+1$ probability variables, $O(M)$ absolute-value slack variables and $O(M)$ constraints; its channel table has $O(M^2)$ entries. At the uniform choice (R47),

```math
M\le1+\frac{8E}{c_0\delta}
\exp\left[C_0\frac{(1-\eta)E}{\delta}\right].
\qquad\text{(R61)}
```

Thus both the detector cutoff used by this estimator and its optimization dimension can be exponentially large in the hard regime. These are costs of this sufficient construction, not lower bounds on every estimator's detector resolution or running time.

For rational finite inputs, standard linear programming gives a running time polynomial in the program's dimension and total coefficient bit length. Coefficients must be represented exactly or certified to a tolerance such as (R39). The empirical histogram uses $O(M)$ counters and can be accumulated in $O(N)$ updates; storing all individual records is unnecessary. Computation is consequently finite, but this result makes no claim of an algorithm polynomial in $E$ and $1/\delta$ at a fixed nonzero loss rate. Photon-number resolution, arithmetic precision and optimization are distinct from the number of received copies.

The inverse-channel linear-program viewpoint and complex-analytic continuation tools have substantial precedents; see [population recovery](../references/REFERENCES.md#psw17) and [quantitative analytic continuation](../references/REFERENCES.md#tre20). The estimate proved here uses the mean constraint to control the derivative at the boundary, evaluates a harmonic barrier for the loss disk, and integrates that derivative to the parity point. The resulting finite-confidence upper bound and its uniform weak-loss behavior are the claims established on this page.
