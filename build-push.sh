#!/bin/bash

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 622705945757.dkr.ecr.us-east-1.amazonaws.com
docker build -t lambda-conjur-oracle .
docker tag lambda-conjur-oracle:latest 622705945757.dkr.ecr.us-east-1.amazonaws.com/lambda-conjur-oracle:latest
docker push 622705945757.dkr.ecr.us-east-1.amazonaws.com/lambda-conjur-oracle:latest
