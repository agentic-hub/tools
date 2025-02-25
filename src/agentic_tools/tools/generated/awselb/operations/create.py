from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwselbCredentials(BaseModel):
    """Credentials for awsElb authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwselbCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwselbCredentials] = Field(None, description="Custom credentials for authentication")
    schema: Optional[str] = Field(None, description="Schema")
    name: Optional[str] = Field(None, description="This name must be unique per region per account, can have a maximum of 32 characters")
    certificate_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    load_balancer_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer")
    listener_id: Optional[str] = Field(None, description="Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    subnets: Optional[str] = Field(None, description="subnets")
    ip_address_type: Optional[str] = Field(None, description="The type of IP addresses used by the subnets for your load balancer")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type")


class AwselbCreateTool(BaseTool):
    name = "awselb_create"
    description = "Tool for awsElb create operation - create operation"
    
    def __init__(self, credentials: Optional[AwselbCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsElb create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsElb create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsElb create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsElb create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
