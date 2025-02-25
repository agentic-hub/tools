from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MailerliteCredentials(BaseModel):
    """Credentials for mailerLite authentication."""
    mailer_lite_api: Optional[Dict[str, Any]] = Field(None, description="mailerLiteApi")

class MailerliteCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MailerliteCredentials] = Field(None, description="Custom credentials for authentication")
    subscriber_id: Optional[str] = Field(None, description="Email of subscriber")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="Email of new subscriber")
    operation: Optional[str] = Field(None, description="Operation")


class MailerliteCreateTool(BaseTool):
    name = "mailerlite_create"
    description = "Tool for mailerLite create operation - create operation"
    
    def __init__(self, credentials: Optional[MailerliteCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mailerLite create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mailerLite create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mailerLite create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailerLite create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
