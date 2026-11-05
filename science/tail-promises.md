# What stronger photon-tail promises buy

The mean-energy result changes when the experimenter is given a stronger, quantitative promise on the source's photon tail. A fixed integer $s$-th moment gives a stretched exponential copy cost, with exponent $\delta^{-1/s}$. A known exponential moment gives a polynomial upper bound. These are different statistical classes: none of these additional promises is used in the [mean-energy theorem](model.md).

This page proves both sides of the finite-moment hierarchy and a constructive exponential-moment upper. The latter is not a claim about the optimal polynomial exponent. All tasks concern input parity at the prescribed origin, with known transmission $\eta$, and confidence $2/3$ unless indicated otherwise. The lower bounds cover arbitrary collective measurements of the received copies; the upper bounds use separate photon counting and a finite constrained fit.

Throughout, $\hat n$ is the source photon-number operator, $N$ is the copy budget, $\delta$ is a parity accuracy or negative-parity gap, and $\epsilon$ is an auxiliary output-distribution $\ell_1$ tolerance. Logarithms are natural. Write $\nu=1-\eta$.

## 1. Classes and statements

For a fixed integer $s\geq1$ and a known finite budget $M_s>0$, define

$$
\mathcal S_{s,M_s}
=\left\{\rho:\operatorname{Tr}(\hat n^s\rho)\leq M_s\right\}.
\tag{T1}
$$

States are normalized density operators. Let $N_{\rm est}^{(s)}$ and $N_{\rm cert}^{(s)}$ denote the two minimax copy budgets from [model.md](model.md), with this class in place of the mean-energy class. The certification null still has a globally nonnegative Wigner function, and its alternative still has input parity at most $-\delta$.

### Theorem T1: the finite-moment hierarchy

Fix $s\in\{1,2,\ldots\}$, $\eta_0>0$, and $M_s>0$. As $\delta\downarrow0$, uniformly over $\eta\in[\eta_0,1]$,

$$
\boxed{
\log N_{\rm est}^{(s)}(M_s,\eta,\delta,1/3)
=\Theta_{s,M_s,\eta_0}\!
\left(\log\frac1\delta+\nu\delta^{-1/s}\right).
}
\tag{T2}
$$

The same statement holds for $N_{\rm cert}^{(s)}$ if the fixed budget satisfies $M_s>1/2$. The implicit constants and the sufficiently small accuracy threshold depend on the displayed fixed parameters. They are not uniform as $s$ grows or as the certification budget decreases to $1/2$.

For each fixed $0<\eta<1$, this becomes

$$
N_*^{(s)}
=\exp\!\left[\Theta_{s,M_s,\eta}(\delta^{-1/s})\right],
\qquad *\in\{{\rm est},{\rm cert}\},
\tag{T3}
$$

with the corresponding budget condition. Thus no fixed finite integer moment alone gives a polynomial guarantee at fixed nonzero loss. At $\eta=1$, the sharper result is $N_*^{(s)}=\Theta(\delta^{-2})$.

For a varying loss schedule bounded below by $\eta_0$, the uniform law permits a polynomial bound in $1/\delta$ precisely when

$$
\nu=O\!\left(\delta^{1/s}\log\frac1\delta\right).
\tag{T4}
$$

If the ratio in (T4) tends to infinity, the copy count is superpolynomial. If that ratio is merely unbounded, no single polynomial bound covers the full schedule, and a superpolynomial subsequence follows.

For comparison, an exponential-moment class is

$$
\mathcal S_{R,B}^{\exp}
=\left\{\rho:\operatorname{Tr}(R^{\hat n}\rho)\leq B\right\},
\qquad R>1,\quad B<\infty.
\tag{T5}
$$

Section 6 gives an explicit exponent $\gamma_{R,\eta}>0$ for which

$$
N_{\rm est}^{\exp}
=O_{R,B,\eta}\!\left(\delta^{-2/\gamma_{R,\eta}}\right).
\tag{T6}
$$

This yields the same upper order for prescribed-origin certification, by estimating parity more accurately and thresholding. There is no claim that $2/\gamma_{R,\eta}$ is optimal. A stronger exponential promise also allows the familiar unbiased inverse estimator to attain a parametric $O(\delta^{-2})$ upper; Section 7 states a sufficient condition.

## 2. An $s$-th derivative continuity bound

Write $p_n=\langle n|\rho|n\rangle$, let $P(z)=\sum_n p_nz^n$, and let $T_\eta p$ be the received photon-count law. Take two inputs $p,\widetilde p$ with $s$-th moments at most $M_s$, and suppose

$$
\|T_\eta p-T_\eta\widetilde p\|_1\leq\epsilon.
\tag{T7}
$$

Set $f=P-\widetilde P$. Since $n^{\underline s}\leq n^s$,

$$
\sum_n n^{\underline s}|p_n-\widetilde p_n|\leq2M_s,
\qquad
|f^{(s)}(z)|\leq2M_s\quad(|z|\leq1).
\tag{T8}
$$

The derivative series through order $s$ converge uniformly on the closed unit disk. In particular, the derivatives used below have continuous boundary values; no extension across the unit circle is being assumed.

The loss relation $Q(w)=P(1-\eta+\eta w)$ makes $|f|\leq\epsilon$ on the observed disk with center $c=\nu$ and radius $\eta$. Choose $0<h<\eta$ and define

$$
r=\eta-h,\qquad
x_0=c-r,\qquad
\ell=1+x_0=2\nu+h,
$$

$$
\kappa_\eta(h)
=\frac{\eta}
{(2-\eta)\log[(2-\eta)/(\eta-h)]}.
\tag{T9}
$$

On the smaller disk $|z-c|\leq r$, Cauchy's estimate gives

$$
|f^{(j)}(z)|\leq\frac{j!\epsilon}{h^j},
\qquad 0\leq j\leq s.
\tag{T10}
$$

If a radius-$h$ Cauchy circle touches the unit circle, apply the estimate at every smaller radius and take its limit. This is justified by the continuity just established.

Let $\omega$ be the harmonic measure of the inner boundary in the unit disk with the closed radius-$r$ disk removed. The Green-function barrier proved in [recovery.md](recovery.md), equations (R16)–(R20), gives

$$
\omega(x)\geq\kappa_\eta(h)(1+x),
\qquad -1\leq x\leq x_0.
\tag{T11}
$$

Suppose

$$
L_s=\log\frac{2M_sh^s}{s!\epsilon}>0.
\tag{T12}
$$

Applying the two-constants theorem to the subharmonic function $\log|f^{(s)}|$, with (T8) and (T10) as its two boundary bounds, gives

$$
|f^{(s)}(x)|
\leq 2M_s e^{-\kappa_\eta(h)(1+x)L_s}.
\tag{T13}
$$

Zeros of the derivative cause no difficulty in this subharmonic argument. An identically zero derivative satisfies the displayed conclusion directly.

Taylor's theorem with an integral remainder, expanded from $x_0$ toward $-1$, now yields

$$
\begin{aligned}
|f(-1)|
&\leq
\sum_{j=0}^{s-1}
\frac{\ell^j}{j!}|f^{(j)}(x_0)|
+\frac1{(s-1)!}
\int_{-1}^{x_0}(1+x)^{s-1}|f^{(s)}(x)|\,dx\\
&\leq
\epsilon\sum_{j=0}^{s-1}\left(\frac{\ell}{h}\right)^j
+\frac{2M_s}{(s-1)!}
\int_0^\ell u^{s-1}e^{-\kappa_\eta(h)L_su}\,du\\
&\leq
\boxed{
\epsilon\sum_{j=0}^{s-1}\left(\frac{\ell}{h}\right)^j
+\frac{2M_s}{[\kappa_\eta(h)L_s]^s}.
}
\end{aligned}
\tag{T14}
$$

The remainder kernel is the distance from the target endpoint $-1$, not the distance from the expansion point. This is what turns the continued $s$-th derivative into the power $[\log(1/\epsilon)]^{-s}$.

For fixed $\eta$, taking $h=\eta/2$ shows

$$
|\theta(p)-\theta(\widetilde p)|
\leq
O_{s,\eta}(\epsilon)
+O_{s,\eta}\!\left(
\frac{M_s}{[\log(M_s/\epsilon)]^s}
\right)
\quad\text{as }\epsilon\downarrow0.
\tag{T15}
$$

When the output distance is zero, injectivity of thinning gives $p=\widetilde p$ directly. The logarithmic expressions are unnecessary in that case.

## 3. A uniform choice as the loss decreases

Fix $\eta_0>0$ and $\eta\in[\eta_0,1)$. Assume

$$
0<\delta\leq
\min\left\{\frac14,\,
8M_s\left(\frac{\eta_0}{4}\right)^s\right\}.
$$

Define

$$
b=\left(\frac{\delta}{8M_s}\right)^{1/s},
\qquad
h=\min\left\{\frac\eta2,\max\{\nu,b\}\right\},
\qquad
\kappa=\kappa_\eta(h),
$$

$$
C_0=1+\frac4{\eta_0},
\qquad
A_{s,\eta_0}=\sum_{j=0}^{s-1}C_0^j.
\tag{T16}
$$

Here $b\leq\eta_0/4$, $h\geq b$, $h\leq\nu+b$, and $\eta-h\geq\eta/2$. Furthermore,

$$
\frac{\ell}{h}\leq C_0,
\qquad
\frac1\kappa
\leq\frac{8\nu+4h}{\eta_0^2}
\leq\frac{12(\nu+b)}{\eta_0^2}.
\tag{T17}
$$

For the first inequality, either $h\geq\nu$ or $h=\eta/2$. For the second, use
$\log[(2-\eta)/(\eta-h)]\leq(2\nu+h)/(\eta-h)$ in (T9).

Choose

$$
\boxed{
\epsilon_*=
\frac{\delta}{4s!A_{s,\eta_0}}
\exp\left[
-\frac{(8M_s/\delta)^{1/s}}{\kappa}
\right].
}
\tag{T18}
$$

Since $2M_sh^s\geq\delta/4$, this choice satisfies

$$
L_s\geq
\frac{(8M_s/\delta)^{1/s}}{\kappa}>0.
$$

The second term in (T14) is therefore at most $\delta/4$. The first is at most $\delta/(4s!)\leq\delta/4$. Thus

$$
\|T_\eta p-T_\eta\widetilde p\|_1\leq\epsilon_*
\quad\Longrightarrow\quad
|\theta(p)-\theta(\widetilde p)|\leq\delta/2.
\tag{T19}
$$

The tolerance also has the explicit lower bound

$$
\epsilon_*
\geq
\frac{e^{-12/\eta_0^2}}{4s!A_{s,\eta_0}}\,
\delta\,
\exp\left[
-\frac{12}{\eta_0^2}
\nu\left(\frac{8M_s}{\delta}\right)^{1/s}
\right].
\tag{T20}
$$

Consequently, any count-distribution estimator costing a fixed polynomial in $1/\epsilon_*$ gives

$$
\log N
=O_{s,M_s,\eta_0}\!
\left(\log\frac1\delta+\nu\delta^{-1/s}\right).
\tag{T21}
$$

The next section supplies such an estimator without assuming finite input support. At $\eta=1$, direct parity measurement supplies the stated upper more simply.

## 4. A finite estimator under a moment budget

This section makes the truncation, probability of success, and optimization size explicit. It is a moment-budget version of the constrained-fit construction in [recovery.md](recovery.md). The general use of constrained estimation and complex continuation in inverse problems is inherited methodology; see [PSW17](../references/REFERENCES.md#psw17). The derivative modulus and budget calculations needed here are given above.

### Estimating the received distribution

The $s$-th input moment implies

$$
\mathbb E n\leq E_1:=M_s^{1/s},
\qquad
\mathbb E K\leq E_1,
\qquad
\mathbb E K^s\leq M_s,
\tag{T22}
$$

where $K$ is the received count. The first inequality is the moment inequality for a probability law. The last follows by coupling the thinning so that $K\leq n$.

For the full empirical distribution $\widehat q$ of $N$ count samples and any integer $J\geq1$,

$$
\begin{aligned}
\mathbb E\|\widehat q-q\|_1
&\leq
\frac{1+\sum_{k=1}^J\sqrt{q_k}}{\sqrt N}
+2\sum_{k>J}q_k\\
&\leq
\frac{1+\sqrt{E_1H_J}}{\sqrt N}
+\frac{2E_1}{J+1},
\qquad
H_J=\sum_{k=1}^J\frac1k.
\end{aligned}
\tag{T23}
$$

The first line uses the binomial variance bound for each frequency and a direct tail bound; the second uses Cauchy–Schwarz with weights $k$.

Given $0<\epsilon<1$, take

$$
J=\max\{1,\lceil48E_1/\epsilon\rceil\},
\qquad
N\geq
\left\lceil
\frac{24^2}{\epsilon^2}
(1+\sqrt{E_1H_J})^2
\right\rceil.
\tag{T24}
$$

Then $\mathbb E\|\widehat q-q\|_1\leq\epsilon/12$, so Markov's inequality gives

$$
\Pr\{\|\widehat q-q\|_1>\epsilon/4\}\leq1/3.
\tag{T25}
$$

For $s\geq2$, the logarithmic prefactor can be removed: Cauchy–Schwarz gives

$$
\sum_{k=1}^\infty\sqrt{q_k}
\leq\sqrt{M_s\zeta(s)}.
$$

Hence the alternative choice

$$
N\geq
\left\lceil
\frac{144}{\epsilon^2}
(1+\sqrt{M_s\zeta(s)})^2
\right\rceil
\tag{T26}
$$

also implies (T25). These estimates are deliberately elementary. They are sufficient for the copy orders claimed here.

### Truncating the input without amplifying its tail

Set

$$
M=\left\lceil
\left(\frac{16M_s}{\epsilon}\right)^{1/s}
\right\rceil.
\tag{T27}
$$

For a true input $p$, move all its mass above $M$ to zero and call the result $p^{[M]}$. This is an allowed finite-support probability law because the moment decreases. Moreover,

$$
\|p-p^{[M]}\|_1
=2\sum_{n>M}p_n
\leq\frac{2M_s}{(M+1)^s}
\leq\epsilon/8.
\tag{T28}
$$

Thinning contracts $\ell_1$, so the same upper bound holds between the two output laws. The input tail is never passed through an unbounded algebraic inverse.

The physical measurement may have only $M+2$ outcomes: photon counts $0,\ldots,M$ and one overflow outcome $*$. Let $\widehat q_0,\ldots,\widehat q_M,\widehat q_*$ be their frequencies. The empirical bound (T25) remains valid for this coarsened law, because coarsening contracts $\ell_1$. The full empirical law in the proof is only a convenient theoretical refinement of this finite measurement.

Find any vector $u=(u_0,\ldots,u_M)$ satisfying the finite linear constraints

$$
u_n\geq0,\qquad
\sum_{n=0}^M u_n=1,\qquad
\sum_{n=0}^M n^su_n\leq M_s,
$$

$$
\sum_{k=0}^M
\left|(T_\eta u)_k-\widehat q_k\right|
+\widehat q_*
\leq\epsilon/2.
\tag{T29}
$$

Absolute values are implemented with nonnegative slack variables. A deterministic linear-program rule can select a feasible vector. On infeasibility, return any value in $[-1,1]$.

On the event (T25), $p^{[M]}$ has residual at most $3\epsilon/8$, so the constraints are feasible. Every feasible $u$ obeys

$$
\|T_\eta u-T_\eta p\|_1
\leq\epsilon/2+\epsilon/4
=3\epsilon/4<\epsilon.
\tag{T30}
$$

This is a full, uncoarsened output distance: the candidate output has no mass above $M$, so its distance to the true output tail equals the single true overflow probability. Thus no unknown composition of that overflow is being discarded in (T30).

Report $\widehat\theta=\sum_{n=0}^M(-1)^nu_n$. With $\epsilon=\epsilon_*$ from (T18), (T19) gives parity error at most $\delta/2$ with probability at least $2/3$. The copy cost satisfies

$$
N=
O\!\left(
\frac{1+E_1\log(1+E_1/\epsilon_*)}{\epsilon_*^2}
\right),
\tag{T31}
$$

or the sharper fixed-$s\geq2$ expression in (T26). Equations (T20) and (T31) prove the upper half of (T2).

For certification, run the estimator with requested accuracy $\delta/3$ and threshold at $-\delta/2$. Global Wigner positivity implies nonnegative origin parity; the alternative has parity at most $-\delta$. Both errors are therefore at most $1/3$. Repeating independent fixed-confidence procedures and taking a median, or a majority for testing, raises the confidence to $1-\beta$ with an additional $O(\log(1/\beta))$ copy factor.

This is a finite sample construction, not a practical efficiency claim in the difficult regime. The input cutoff (T27) itself can be stretched exponential in $1/\delta$ at fixed loss. The linear program has $O(M)$ variables and constraints and a thinning matrix of at most $(M+1)^2$ entries. No exact bit-complexity bound, numerical conditioning guarantee, or polynomial-in-$1/\delta$ runtime is asserted for finite moment classes.

## 5. Matching lower bounds for every collective measurement

Use the binomial and odd-conditioned distributions $b_m,o_m$ from [limits.md](limits.md). For $m>s$, both have the same first $s$ moments and common $s$-th moment

$$
\mu_s(m)=\mathbb E_{b_m}n^s
=\mathbb E_{o_m}n^s
\leq m^s.
$$

They have parity zero and minus one, respectively; $b_m$ is globally Wigner-positive. For any common baseline $t$ and weight $w$,

$$
p_0=(1-w)t+wb_m,\qquad
p_1=(1-w)t+wo_m
$$

have received chi-square divergence at most

$$
w\left(\frac{\eta}{2-\eta}\right)^m.
$$

The collective-POVM reduction and Le Cam bound proved in [limits.md](limits.md) consequently require

$$
N>
\frac{c_{\rm LC}}{w}
\left(\frac{2-\eta}{\eta}\right)^m,
\qquad
c_{\rm LC}=\log(5/4),
\tag{T32}
$$

for any test with both errors at most $1/3$. All inputs used here are diagonal, so an arbitrary joint quantum measurement cannot improve their distinguishability beyond the classical count experiment.

### Estimation

Take $t$ to be vacuum and set

$$
w=4\delta,\qquad
m=\left\lfloor
\left(\frac{M_s}{4\delta}\right)^{1/s}
\right\rfloor.
\tag{T33}
$$

For example, the conditions

$$
0<\delta\leq
\min\left\{\frac18,\frac{M_s}{4(s+1)^s}\right\}
$$

ensure $w\leq1/2$ and $m>s$. Both moments are at most $wm^s\leq M_s$, and their parities differ by $4\delta$. Midpoint thresholding of a successful $\delta$-accurate estimator therefore gives a test to which (T32) applies:

$$
\boxed{
N_{\rm est}^{(s)}
>
\frac{c_{\rm LC}}{4\delta}
\left(\frac{2-\eta}{\eta}\right)^{
\left\lfloor(M_s/(4\delta))^{1/s}\right\rfloor}.
}
\tag{T34}
$$

### Globally positive null

Assume $M_s>1/2$. The baseline
$\tau=(|0\rangle\langle0|+|1\rangle\langle1|)/2$
has every positive integer moment equal to $1/2$, zero parity, and a globally nonnegative Wigner function. Set

$$
w=\delta,\qquad
m=\left\lfloor
\left(\frac{M_s-1/2}{\delta}\right)^{1/s}
\right\rfloor.
\tag{T35}
$$

For

$$
0<\delta\leq
\min\left\{\frac12,\frac{M_s-1/2}{(s+1)^s}\right\},
$$

the two mixtures have equal $s$-th moments bounded by

$$
(1-\delta)\frac12+\delta\mu_s(m)
\leq\frac12+\delta m^s\leq M_s.
$$

The null is globally Wigner-positive and has parity zero, while the alternative has parity $-\delta$. Therefore

$$
\boxed{
N_{\rm cert}^{(s)}
>
\frac{c_{\rm LC}}{\delta}
\left(\frac{2-\eta}{\eta}\right)^{
\left\lfloor((M_s-1/2)/\delta)^{1/s}\right\rfloor}.
}
\tag{T36}
$$

The lower exponent explicitly uses the slack $M_s-1/2$. The upper uses $M_s$. Their matching statement fixes a budget strictly above $1/2$, rather than asserting a uniform law as that slack vanishes.

### The parametric part and the uniform conclusion

On a vacuum/one-photon mixture, every positive integer photon moment equals the one-photon probability. Hence the two-level lower bounds in [limits.md](limits.md), Section 6, apply with $E$ replaced by $M_s$. In particular, with

$$
a_s=\min\{M_s/2,1/4\}>0,
$$

one has, for sufficiently small $\delta$,

$$
N_{\rm est}^{(s)}
>\frac{c_{\rm LC}a_s(1-a_s)}{4\delta^2},
\qquad
N_{\rm cert}^{(s)}
>\frac{c_{\rm LC}}{\delta^2}
\quad(M_s>1/2).
\tag{T37}
$$

Finally,

$$
2\nu
\leq\log\frac{2-\eta}{\eta}
\leq\frac{2\nu}{\eta_0(2-\eta_0)}
\qquad(\eta\geq\eta_0).
$$

Combining (T34) or (T36) with (T37) proves the lower half of (T2). The maximum of the logarithmic parametric scale and the loss scale is within a constant factor of their sum. This completes the finite-moment theorem.

### Additional fixed budgets

If a separate mean budget $E$ is also imposed and $s>1$, the same lower order persists for fixed $E>0$ in estimation and fixed $E>1/2$ in certification. Indeed, the estimation construction has mean $O(\delta^{1-1/s})\to0$, and the certification construction has mean $1/2+O(\delta^{1-1/s})\to1/2$.

More generally, finitely many fixed moment bounds through order $s$ do not remove the hard family if the lower-order budgets are strictly positive for estimation, or strictly greater than $1/2$ for certification. For $j<s$, its additional $j$-th moment is of order $\delta m^j=O(\delta^{1-j/s})$. The highest-moment upper remains valid, and the lower-order constraints are eventually satisfied. Constants and the required accuracy threshold can depend on every supplied budget.

## 6. Exponential moments: a polynomial constructive upper

Suppose $R>1$ and

$$
\sum_n R^np_n\leq B.
$$

For two allowed inputs, $f=P-\widetilde P$ is analytic on $|z|<R$, continuous on its closure, and bounded there by $2B$. The observed disk $D=\{z:|z-c|\leq\eta\}$, with $c=1-\eta$, is strictly inside that larger disk because $c+\eta=1<R$.

If $0<\eta<1$, the parity point $-1$ lies between the two boundary circles. Let $\omega_R$ be harmonic measure of the inner boundary in $\{|z|<R\}\setminus D$. The two-constants theorem gives

$$
|f(-1)|
\leq(2B)^{1-\omega_R(-1)}\epsilon^{\omega_R(-1)}
\quad\text{if }\|T_\eta p-T_\eta\widetilde p\|_1\leq\epsilon\leq2B.
\tag{T38}
$$

An explicit barrier makes this quantitative. The radius-$R$ disk Green function with pole at $c$ is

$$
g_R(z)=
\log\left|\frac{R^2-cz}{R(z-c)}\right|.
$$

It is positive and harmonic on the doubly connected region and zero on its outer boundary. On the inner boundary, $|z-c|=\eta$ and $|z|\leq1$, so

$$
g_R(z)\leq
\log\frac{R^2+c}{R\eta}
=:\mathcal M_R.
$$

The maximum principle implies $\omega_R\geq g_R/\mathcal M_R$. Evaluating at the parity point gives

$$
\gamma_{R,\eta}
:=
\frac{
\log[(R^2+c)/(R(1+c))]
}{
\log[(R^2+c)/(R\eta)]
}
\leq\omega_R(-1).
\tag{T39}
$$

Both logarithms are positive, and $0<\gamma_{R,\eta}<1$ for $\eta<1$. Since $\epsilon/(2B)\leq1$, (T38) yields the explicit Hölder modulus

$$
\boxed{
|\theta(p)-\theta(\widetilde p)|
\leq
(2B)^{1-\gamma_{R,\eta}}
\epsilon^{\gamma_{R,\eta}}.
}
\tag{T40}
$$

The displayed exponent is a lower bound on harmonic measure obtained from a simple barrier, not an optimized exponent. At $\eta=1$, the formula has $\gamma_{R,1}=1$, and the direct bound $|f(-1)|\leq\epsilon$ applies. The exponent increases with $\eta$: as $c$ increases, the numerator in (T39) decreases and its positive denominator increases. Thus $\eta\geq\eta_0>0$ gives a uniform positive exponent $\gamma_{R,\eta_0}$.

Choose

$$
\epsilon_*=
2B\left(\frac{\delta}{4B}\right)^{1/\gamma_{R,\eta}}.
\tag{T41}
$$

For $0<\delta\leq1$ and $B\geq1$, this satisfies $\epsilon_*\leq\delta/2$, and (T40) makes the parity modulus at most $\delta/2$.

### Sample count and finite fit

The received law has the same exponential-moment upper bound:

$$
\sum_k R^kq_k
=P(1-\eta+\eta R)
\leq P(R)\leq B.
$$

Consequently,

$$
\sum_{k=0}^{\infty}\sqrt{q_k}
\leq
\left(\sum_kR^kq_k\right)^{1/2}
\left(\sum_kR^{-k}\right)^{1/2}
\leq\sqrt{\frac{BR}{R-1}}.
$$

The empirical output distribution therefore obeys

$$
\mathbb E\|\widehat q-q\|_1
\leq
\sqrt{\frac{BR}{(R-1)N}}.
\tag{T42}
$$

With $\epsilon=\epsilon_*$, take

$$
N\geq
\left\lceil
\frac{144BR}{(R-1)\epsilon^2}
\right\rceil,
\qquad
M=\left\lceil
\frac{\log(16B/\epsilon)}{\log R}
\right\rceil.
\tag{T43}
$$

The empirical $\ell_1$ error is then at most $\epsilon/4$ with probability at least $2/3$. Moving the input tail above $M$ to zero changes it by at most

$$
2\sum_{n>M}p_n
\leq2BR^{-(M+1)}
\leq\epsilon/8.
$$

Use the same finite count-plus-overflow measurement and linear program as in (T29), replacing the moment constraint by

$$
\sum_{n=0}^{M}R^nu_n\leq B.
\tag{T44}
$$

Tail transfer to zero decreases this exponential moment. The feasibility and full-output-distance proof (T28)–(T30) is unchanged. Equation (T40) then gives a valid parity estimator with

$$
N=O_{R,B,\eta}\!\left(\delta^{-2/\gamma_{R,\eta}}\right),
\qquad
M=O_{R,B,\eta}\!\left(\log\frac1\delta\right).
\tag{T45}
$$

For $\eta\geq\eta_0$, use $\gamma_{R,\eta_0}$ for a uniform polynomial upper. The optimization has only $O(\log(1/\delta))$ variables and constraints for fixed parameters, besides the work of acquiring and recording the samples. As elsewhere, this does not assert an optimal runtime or an exact bit-complexity bound for real-valued known transmission.

## 7. A sufficient exponential promise for parametric recovery

The ordinary inverse-loss parity weight on a received photon count is

$$
g_\eta(k)=\left(1-\frac2\eta\right)^k.
\tag{T46}
$$

Its rapidly increasing magnitude under loss, and the resulting variance problem, are classical photodetection facts; see [Ban99](../references/REFERENCES.md#ban99), Section III and Eqs. (20)–(22). They do not by themselves prove a minimax converse for regularized or nonlinear estimators.

If the known exponential promise satisfies

$$
R\geq R_{\rm var}(\eta):=\frac4\eta-3,
\tag{T47}
$$

then this particular inverse estimator has controlled second moment:

$$
\mathbb E[g_\eta(K)^2]
=P\!\left(1-\eta+\eta(1-2/\eta)^2\right)
=P(4/\eta-3)
\leq B.
\tag{T48}
$$

Absolute integrability also holds. Indeed,

$$
\mathbb E|g_\eta(K)|
=P(3-2\eta)\leq B,
\qquad
3-2\eta\leq4/\eta-3.
$$

Thus the exchange of sums is justified, and conditioning on the source count gives

$$
\mathbb E[g_\eta(K)\mid n]
=(1-\eta+\eta(1-2/\eta))^n=(-1)^n.
$$

The empirical average of (T46) is unbiased for $\theta$ and has variance at most $B/N$. Chebyshev's inequality gives failure probability at most $1/3$ at accuracy $\delta$ when $N\geq3B/\delta^2$. Clipping the final estimate to $[-1,1]$ cannot increase its error.

For fixed $R,B,\eta$ with $B>1$, the two-level parametric lower from [limits.md](limits.md) also applies to this class: its allowable one-photon probability is at most $(B-1)/(R-1)$, and a small nonzero interval is available. Thus (T47) gives $N_{\rm est}^{\exp}=\Theta(\delta^{-2})$. The same statement holds for certification when $B>(1+R)/2$. Uniformly over $\eta\geq\eta_0$, the sufficient condition is $R\geq4/\eta_0-3$.

Condition (T47) is sufficient for this unbiased estimator. It is not asserted to be necessary for optimal parametric estimation by other procedures. When it fails, (T45) still supplies a polynomial upper under the exponential promise, without assuming that (T46) has finite variance.

## 8. Budgets, endpoints, and the scope of the conclusions

- **Moment nontriviality.** At $M_s=0$, the input is vacuum. Since $n^s\geq\mathbf 1_{\{n\ {\rm odd}\}}$, an origin-negative gap $\delta$ is possible under the $s$-th moment promise exactly when $M_s\geq(1+\delta)/2$. A vacuum/one-photon mixture attains that threshold. Fixed-budget certification therefore requires $M_s>1/2$ as $\delta\downarrow0$.
- **Exponential nontriviality.** The class is empty if $B<1$, and consists only of vacuum if $B=1$. Moreover $R^n\geq1+(R-1)\mathbf 1_{\{n\ {\rm odd}\}}$. The origin-negative alternative is nonempty exactly when $B\geq(1+R)/2+(R-1)\delta/2$, again attained by a vacuum/one-photon mixture. A fixed nontrivial certification class requires $B>(1+R)/2$.
- **An implied mean bound.** The integer-moment promise gives mean at most $M_s^{1/s}$. The exponential promise gives mean at most $\log B/\log R$ by Jensen's inequality. These facts justify using moment-class inputs in finite count estimation; they do not turn the main mean-only theorem into a stronger-tail statement.
- **Compact sublevel classes.** The diagonal moment classes are compact in $\ell_1$, using uniform tails $M_s/(M+1)^s$ or $BR^{-(M+1)}$ and Fatou's lemma for closedness. Equality of a moment to a specified budget need not define a closed class. The upper constructions use inequalities throughout.
- **Transmission endpoints.** Transmission zero is excluded because all received states are vacuum. At transmission one, direct parity sampling gives the parametric rate. The uniform theorems keep transmission bounded below by a positive $\eta_0$; no constants uniform down to zero are asserted.
- **Fixed versus growing moment order.** The constants, Cauchy factorials, and feasible cutoffs depend on $s$. Equations (T2)–(T4) concern fixed finite integers. They do not justify choosing $s$ to grow with accuracy, or infer an exponential-moment promise from a collection of unspecified finite moments.
- **What is not matched here.** The exponential-moment upper uses a conservative harmonic-measure exponent and does not determine the optimal polynomial exponent for all $R,B,\eta$. No claim is made to classify every intermediate tail condition.
- **The certification point is supplied.** Every matching certification statement concerns negativity at the prescribed origin. Searching for an unknown negative point over all phase space requires an additional analysis and is outside these upper bounds.

The finite-moment result is driven by the regularity that the supplied moment controls: one additional derivative changes the inverse modulus from a reciprocal logarithm to a higher reciprocal power. An exponential moment instead moves the parity point into the interior of a larger analytic domain, where continuation has a positive Hölder exponent. The estimator and hard-family constructions above make those distinctions quantitative.
