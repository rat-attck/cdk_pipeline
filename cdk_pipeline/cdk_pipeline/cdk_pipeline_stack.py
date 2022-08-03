from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    pipelines as pipelines
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # Create a CodeCommit repo called exampleRepo
        repo = codecommit.Repository(
            self, "exampleRepo", repository_name="exampleRepo"
        )

        # Pipeline code
        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            self_mutation=False,
            synth=pipelines.ShellStep(
                "Build",
                input=pipelines.CodePipelineSource.code_commit(repo, "master"),
                # Environment vars for codebuild
                env={
                    "ExampleKey": "ExampleValue"
                },
                commands=[
                    # Installs the cdk cli on Codebuild
                    "npm install -g aws-cdk",
                    # Instructs Codebuild to install required packages
                    "pip install -r requirements.txt",
                    # Run rest of build spec in sh file
                    "./infra_cdk/build.sh"
                ]
            ),
        )
