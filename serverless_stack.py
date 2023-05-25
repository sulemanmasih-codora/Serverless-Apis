from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
    aws_iam as iam_,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb,
    # aws_sqs as sqs,
)
from constructs import Construct

class ServerlessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        

    # ------------------------------LAMBDA FUNCTION-----------------------------------------
        lambda_role=self.Create_role()
        lambdaFunction =self.My_Lambda('Suleman_Lambda','testlambda.LambdaHandler','./resource',lambda_role)

    # ---------------------------------DynamoDB----------------------------------------------
        apiDB=dynamodb.Table(self, "APITable",
                partition_key=dynamodb.Attribute(name="Timestamp", type=dynamodb.AttributeType.STRING)
                )


        lambdaFunction.add_environment("APIDB", apiDB.table_name)

    # -----------------------------------"API 1"------------------------------------------
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_apigateway/LambdaRestApi.html
        api1 = apigateway.LambdaRestApi(self, "rest-api",
                        handler=lambdaFunction,
                        endpoint_configuration=apigateway.EndpointConfiguration(
                                        types=[apigateway.EndpointType.EDGE]),
                        proxy=False
                    )
        lambdaFunction.grant_invoke(iam_.ServicePrincipal("apigateway.amazonaws.com"))

        event_value1 = api1.root.add_resource("Event1")
        event_value1.add_method("POST") 
        event_value1.add_method("GET") 
        event_value1.add_method("DELETE")



    # Create Lambda Function
    # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda/Function.html
    def My_Lambda(self,id,handler,asset,role):
        return lambda_.Function(self, "MyFunction",
                runtime=lambda_.Runtime.PYTHON_3_7,
                handler=handler,
                code=lambda_.Code.from_asset(asset),
                role=role)
  
    def Create_role(self):
        return iam_.Role(self, "Role",
                assumed_by=iam_.ServicePrincipal("lambda.amazonaws.com"),
                 managed_policies=[
                            iam_.ManagedPolicy.from_aws_managed_policy_name('CloudWatchFullAccess'),
                            iam_.ManagedPolicy.from_aws_managed_policy_name('AmazonDynamoDBFullAccess')
                           ]
                )

   