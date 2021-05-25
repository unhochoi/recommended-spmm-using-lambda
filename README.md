# recommended-spmm-using-lambda


### Post command example

```
curl -X POST APIGATEWAYPOSTURL \
-d '{
  "lr": 97366,
  "lc": 33288,
  "rc": 5958,
  "ld": 0.00056263,
  "rd": 0.13,
  "lnnz": 1823595,
  "rnnz": 25785518,
  "lr*lc": 3241119408,
  "lc*rc": 198329904,
  "lr*rc": 580106628,
  "lr*lc*rc": 1.93E+13,
  "ld*rd": 7.31E-05,
  "lr*rc*ld*rd": 42430.10097,
  "lr*lc*rc*ld*rd": 1412413201,
  "lnnz*rnnz": 4.70E+13
}'
```
