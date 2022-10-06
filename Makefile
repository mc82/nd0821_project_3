AWS_PROFILE := mc82nd0821project3

BUCKET_NAME := 	mc82nd0821project3

setup-evnironment:
	python3 -m virtualenv env
	source env/bin/activate; \
	pip install -r requirements.txt;


create-bucket:
 	aws s3api create-bucket --bucket ${BUCKET_NAME} --region us-east-1 --profile ${AWS_PROFILE} 