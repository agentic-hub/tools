from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwssesCredentials(BaseModel):
    """Credentials for awsSes authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwssesCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwssesCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    html_part: Optional[str] = Field(None, description="The HTML body of the email")
    template_subject: Optional[str] = Field(None, description="The subject line of the custom verification email")
    failure_redirection_url: Optional[str] = Field(None, description="The URL that the recipient of the verification email is sent to if his or her address is not successfully verified")
    subject_part: Optional[str] = Field(None, description="The subject line of the email")
    to_addresses: Optional[str] = Field(None, description="Email addresses of the recipients")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    success_redirection_url: Optional[str] = Field(None, description="The URL that the recipient of the verification email is sent to if his or her address is successfully verified")
    from_email_address: Optional[str] = Field(None, description="The email address that the custom verification email is sent from")
    template_content: Optional[str] = Field(None, description="The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    from_email: Optional[str] = Field(None, description="Email address of the sender")
    template_name: Optional[str] = Field(None, description="The name of the custom verification email template")


class AwssesCreateTool(BaseTool):
    name = "awsses_create"
    description = "Tool for awsSes create operation - create operation"
    
    def __init__(self, credentials: Optional[AwssesCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsSes create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsSes create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsSes create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsSes create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
