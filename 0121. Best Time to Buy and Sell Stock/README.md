## Solution

The following codes are more straightforward.

```python
curr = 0; maxpro = 0
for i in range(n - 1):
    curr = max(0, curr + prices[i+1] - prices[i])
    maxpro = max(curr, maxpro)
return maxpro
```

