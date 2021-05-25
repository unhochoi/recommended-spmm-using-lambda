import json
import boto3
import sys

# EFS 경로의 패키지를 import 가능하게 수정
sys.path.append("/mnt/efs/packages")
import numpy as np
import xgboost as xgb

# S3에서 모델 다운로드
s3 = boto3.client('s3')
s3.download_file('unho-spmm', 'model/sp_smdm_xgb.model', '/tmp/sp_smdm_xgb.model' )
s3.download_file('unho-spmm', 'model/bz_smsm_xgb.model', '/tmp/bz_smsm_xgb.model' )

# 모델 불러오기
sp_smdm_xgb_model = xgb.XGBRegressor()
bz_smsm_xgb_model = xgb.XGBRegressor()
sp_smdm_xgb_model.load_model('/tmp/sp_smdm_xgb.model')
bz_smsm_xgb_model.load_model('/tmp/bz_smsm_xgb.model')

def lambda_handler(event, context):
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
