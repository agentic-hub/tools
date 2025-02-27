from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwslambdaCredentials

class AwslambdaInvokeToolInput(BaseModel):
    payload: Optional[str] = Field(None, description="The JSON that you want to provide to your Lambda function as input")
    invocation_type: Optional[str] = Field(None, description="Specify if the workflow should wait for the function to return the results")
    function: Optional[str] = Field(None, description="The function you want to invoke. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    qualifier: Optional[str] = Field(None, description="Specify a version or alias to invoke a published version of the function")
    operation: Optional[str] = Field(None, description="Operation")


class AwslambdaInvokeTool(BaseTool):
    name: str = "awslambda_invoke"
    description: str = "Tool for awsLambda invoke operation - invoke operation"
    args_schema: type[BaseModel] | None = AwslambdaInvokeToolInput
    credentials: Optional[AwslambdaCredentials] = None
