AWS_PROFILE := mc82nd0821project3

BUCKET_NAME := 	mc82nd0821project3
LOCAL_PORT := 8888

setup-evnironment:
	python3 -m virtualenv env
	source env/bin/activate; \
	pip install -r requirements.txt;


# create-bucket:
#  	aws s3api create-bucket --bucket ${BUCKET_NAME} --region us-east-1 --profile ${AWS_PROFILE} 

remove-spaces:
	sed  "s/\ //g" > data/census_clean.csv  
	
run-main:
	python3 -m src.python.main

run-tests:
	python3 -m pytest -vv

run-app-locally:
	uvicorn src.python.api.app:app --host 0.0.0.0 --port ${LOCAL_PORT}  --h11-max-incomplete-event-size 39999 

live-request:
	python3 -m src.python.api.make_live_api_request
