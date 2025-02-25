from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwslambdaInvokeToolInput(BaseModel):
    payload: Optional[str] = Field(None, description="The JSON that you want to provide to your Lambda function as input")
    invocationType: Optional[str] = Field(None, description="Specify if the workflow should wait for the function to return the results")
    function: Optional[str] = Field(None, description="The function you want to invoke. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    qualifier: Optional[str] = Field(None, description="Specify a version or alias to invoke a published version of the function")
    operation: Optional[str] = Field(None, description="Operation")


class AwslambdaInvokeTool(BaseTool):
    name = "awslambda_invoke"
    description = "Tool for awsLambda invoke operation - invoke operation"
    
    def _run(self, **kwargs):
        """Run the awsLambda invoke operation."""
        # Implement the tool logic here
        return f"Running awsLambda invoke operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsLambda invoke operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
