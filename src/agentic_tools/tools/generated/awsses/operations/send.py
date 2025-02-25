from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwssesCredentials(BaseModel):
    """Credentials for awsSes authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwssesSendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwssesCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    is_body_html: Optional[bool] = Field(None, description="Whether body is HTML or simple text")
    to_addresses: Optional[str] = Field(None, description="Email addresses of the recipients")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The email address to verify")
    subject: Optional[str] = Field(None, description="Subject")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    body: Optional[str] = Field(None, description="The message to be sent")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    from_email: Optional[str] = Field(None, description="Email address of the sender")
    template_name: Optional[str] = Field(None, description="The name of the custom verification email template to use when sending the verification email")


class AwssesSendTool(BaseTool):
    name = "awsses_send"
    description = "Tool for awsSes send operation - send operation"
    
    def __init__(self, credentials: Optional[AwssesCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsSes send operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsSes send operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsSes send operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsSes send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
