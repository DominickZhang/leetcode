# Solution

Thinking: What if the interval of two heights is not unit? What if the heights are not integers?

No need to modify the current codes.

An intuitive way to illustrate why there is no need to go through all cases.

If $h(1)<h(n)<h(2)<h(n-1)<h(3)$, then the $(i,j)$ pairs that will be checked in the solution are $(1, n)$, $(2, n)$, $(2, n-1)$, $(3, n-1)$. Note that $(3,n)$ is ignored. Then we will prove that the area of the pair $(3, n)$ is less than one of the pairs that are checked. The answer is $a_{(2,n)}>a_{(3,n)}$.
$$
\begin{eqnarray}
a_{(2,n)}&=&(d(n)-d(2))\cdot\min(h(2), h(n))\\
&=&(d(n)-d(2))\cdot h(n)\\
&>&(d(n)-d(2))\cdot h(n)=a_{(3,n)}
\end{eqnarray}
$$
The complexity can be reduced from $\mathcal{O}(n^2)​$ to $\mathcal{O}(n)​$, intuitively because many cases are not necessary to be compared.