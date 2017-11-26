# postgres-writer.lambda

CI setup copied from here: https://nicor88.github.io/2017/09/10/build-aws-python-lambda-with-travis.html


# How to update the lambda after the code is in s3


aws lambda update-function-code \
--function-name FunctionName \
--s3-bucket BucketName \
--s3-key path/to/deployment/x.zip \
--publish \
--profile MyProfile \
--region MyRegion

