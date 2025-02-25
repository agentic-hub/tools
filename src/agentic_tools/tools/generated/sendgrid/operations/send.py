from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendgridCredentials(BaseModel):
    """Credentials for sendGrid authentication."""
    send_grid_api: Optional[Dict[str, Any]] = Field(None, description="sendGridApi")

class SendgridSendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SendgridCredentials] = Field(None, description="Custom credentials for authentication")
    content_value: Optional[str] = Field(None, description="Message body of the email to send")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Primary email for the contact")
    subject: Optional[str] = Field(None, description="Subject of the email to send")
    dynamic_template_fields: Optional[Dict[str, Any]] = Field(None, description="Dynamic Template Fields")
    from_name: Optional[str] = Field(None, description="Name of the sender of the email")
    operation: Optional[str] = Field(None, description="Operation")
    template_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="ID of the list")
    content_type: Optional[str] = Field(None, description="MIME type of the email to send")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    to_email: Optional[str] = Field(None, description="Comma-separated list of recipient email addresses")
    from_email: Optional[str] = Field(None, description="Email address of the sender of the email")
    dynamic_template: Optional[bool] = Field(None, description="Whether this email will contain a dynamic template")


class SendgridSendTool(BaseTool):
    name = "sendgrid_send"
    description = "Tool for sendGrid send operation - send operation"
    
    def __init__(self, credentials: Optional[SendgridCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the sendGrid send operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running sendGrid send operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running sendGrid send operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendGrid send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
