from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwselbCredentials(BaseModel):
    """Credentials for awsElb authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwselbDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwselbCredentials] = Field(None, description="Custom credentials for authentication")
    certificate_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    load_balancer_id: Optional[str] = Field(None, description="ID of loadBalancer to delete")
    listener_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    subnets: Optional[str] = Field(None, description="subnets")
    operation: Optional[str] = Field(None, description="Operation")


class AwselbDeleteTool(BaseTool):
    name = "awselb_delete"
    description = "Tool for awsElb delete operation - delete operation"
    
    def __init__(self, credentials: Optional[AwselbCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsElb delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsElb delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsElb delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsElb delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
