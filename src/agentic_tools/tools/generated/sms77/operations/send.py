from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Sms77Credentials(BaseModel):
    """Credentials for sms77 authentication."""
    sms77_api: Optional[Dict[str, Any]] = Field(None, description="sms77Api")

class Sms77SendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[Sms77Credentials] = Field(None, description="Custom credentials for authentication")
    to: Optional[str] = Field(None, description="The number of your recipient(s) separated by comma. Can be regular numbers or contact/groups from seven.")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to send. Max. 1520 characters")
    from: Optional[str] = Field(None, description="The caller ID displayed in the receivers display. Max 16 numeric or 11 alphanumeric characters.")
    operation: Optional[str] = Field(None, description="Operation")


class Sms77SendTool(BaseTool):
    name = "sms77_send"
    description = "Tool for sms77 send operation - send operation"
    
    def __init__(self, credentials: Optional[Sms77Credentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the sms77 send operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running sms77 send operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running sms77 send operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sms77 send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
