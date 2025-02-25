from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwslambdaCredentials(BaseModel):
    """Credentials for awsLambda authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwslambdaInvokeToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwslambdaCredentials] = Field(None, description="Custom credentials for authentication")
    payload: Optional[str] = Field(None, description="The JSON that you want to provide to your Lambda function as input")
    invocation_type: Optional[str] = Field(None, description="Specify if the workflow should wait for the function to return the results")
    function: Optional[str] = Field(None, description="The function you want to invoke. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    qualifier: Optional[str] = Field(None, description="Specify a version or alias to invoke a published version of the function")
    operation: Optional[str] = Field(None, description="Operation")


class AwslambdaInvokeTool(BaseTool):
    name = "awslambda_invoke"
    description = "Tool for awsLambda invoke operation - invoke operation"
    
    def __init__(self, credentials: Optional[AwslambdaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsLambda invoke operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsLambda invoke operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsLambda invoke operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsLambda invoke operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
