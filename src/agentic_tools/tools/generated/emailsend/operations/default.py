from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EmailsendCredentials(BaseModel):
    """Credentials for emailSend authentication."""
    smtp: Optional[Dict[str, Any]] = Field(None, description="smtp")

class EmailsendDefaultToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[EmailsendCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    email_format: Optional[str] = Field(None, description="Email Format")


class EmailsendDefaultTool(BaseTool):
    name = "emailsend_default"
    description = "Tool for emailSend default operation - default operation"
    
    def __init__(self, credentials: Optional[EmailsendCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the emailSend default operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running emailSend default operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running emailSend default operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the emailSend default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
