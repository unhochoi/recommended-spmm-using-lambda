# recommended-spmm-using-lambda

- API Gateway 로부터 POST 받았을 시, 최적의 SPMM 방법을 추천해주는 Lambda Function 구현 (EFS 기반)
  - xgb_lambda_function.py 
    - xgbregressor 모델 기반 추천
  - dnn_lambda_function.py
    - dnn 모델 기반 추천

### Post command example

```
curl \
-H "Content-Type: application/json" \
-X POST "APIGATEWAYPOSTURL" \
-d '{
  "lr": 97366,
  "lc": 33288,
  "rc": 5958,
  "ld": 0.00056263,
  "rd": 0.13,
  "lnnz": 1823595,
  "rnnz": 25785518
}'
```

