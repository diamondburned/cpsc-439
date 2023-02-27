```py
ab  =  NAND(a, b)
bc  =  NAND(b, c)
ac  =  NAND(a, c)
abc =  NAND(ab, bc)
return NAND(abc, ac)
```
