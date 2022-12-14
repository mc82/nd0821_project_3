AWS_PROFILE := mc82nd0821project3

BUCKET_NAME := 	mc82nd0821project3

setup-evnironment:
	python3 -m virtualenv env
	source env/bin/activate; \
	pip install -r requirements.txt;


# create-bucket:
#  	aws s3api create-bucket --bucket ${BUCKET_NAME} --region us-east-1 --profile ${AWS_PROFILE} 

remove-spaces:
	sed  "s/\ //g" > data/census_clean.csv  
	
train-model:
	python3 -m src.python.train_model

run-tests:
	python3 -m pytest -vv


run-app:
	python3 -m python.ml.main