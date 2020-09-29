from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from hitcounter import HitCounter

class Demo2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        my_lambda = _lambda.Function(
            self, "HelloHandler",
            code=_lambda.Code.from_asset('lambda'),
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler='hello.handler'
        )
       
        hello_with_counter = HitCounter(
           self, "HelloHitCounter",
           downstream= my_lambda
        )

        
        my_apigw = apigw.LambdaRestApi(
            self, "Endpoint",
            handler=hello_with_counter.handler,
        )        
