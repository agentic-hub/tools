from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PlivoCredentials(BaseModel):
    """Credentials for plivo authentication."""
    plivo_api: Optional[Dict[str, Any]] = Field(None, description="plivoApi")

class PlivoMakeToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PlivoCredentials] = Field(None, description="Custom credentials for authentication")
    to: Optional[str] = Field(None, description="Phone number to make the call to")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="Message to send")
    answer_url: Optional[str] = Field(None, description="URL to be invoked by Plivo once the call is answered. It should return the XML to handle the call once answered.")
    answer_method: Optional[str] = Field(None, description="HTTP verb to be used when invoking the Answer URL")
    from: Optional[str] = Field(None, description="Caller ID for the call to make")
    operation: Optional[str] = Field(None, description="Operation")


class PlivoMakeTool(BaseTool):
    name = "plivo_make"
    description = "Tool for plivo make operation - make operation"
    
    def __init__(self, credentials: Optional[PlivoCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the plivo make operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running plivo make operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running plivo make operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the plivo make operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
