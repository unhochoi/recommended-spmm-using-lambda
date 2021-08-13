import json
import boto3
import sys

# EFS 내의 Package 를 Import 가능하도록 경로 추가
sys.path.append("/mnt/efs/packages")

# package import
import numpy as np
import tensorflow as tf

# EFS 내의 Model 을 Load 하기
sp_smdm_dnn_model = tf.keras.models.load_model('/mnt/efs/model/dnn_sp_smdm_model')
bz_smsm_dnn_model = tf.keras.models.load_model('/mnt/efs/model/dnn_bz_smsm_model')

# 메인 함수
def lambda_handler(event, context):
    
    # event 로부터 feature 전처리
    lr = event["lr"]
    lc = event["lc"]
    rc = event["rc"]
    ld = event["ld"]
    rd = event["rd"]
    lnnz = event["lnnz"]
    rnnz = event["rnnz"]

    # 모델 입력으로 사용할 input_feature 생성
    input_feature = np.array([[lr,lc,rc,ld,rd,lnnz,rnnz]])
    
    # input_feature 에 대한 모델별 예측값 생성
    sp_smdm_dnn_result = sp_smdm_dnn_model.predict(input_feature)
    bz_smsm_dnn_result = bz_smsm_dnn_model.predict(input_feature)
    
    # sp_smdm 이 최적일 경우
    if (sp_smdm_dnn_result[0] <= bz_smsm_dnn_result[0]):
        optim_method = "sp_smdm"
    # bz_smsm 이 최적일 경우
    else:
        optim_method = "bz_smsm"
    
	# 결과 생성
    result = "sp_smdm : " + str(sp_smdm_dnn_result[0]) + " , " + \
		"bz_smsm : " + str(bz_smsm_dnn_result[0]) + " , " + \
		"optim_method : " + optim_method

	# 결과 반환
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
