from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PhilipshueCredentials(BaseModel):
    """Credentials for philipsHue authentication."""
    philips_hue_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="philipsHueOAuth2Api")

class PhilipshueGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PhilipshueCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    light_id: Optional[str] = Field(None, description="Light ID")
    operation: Optional[str] = Field(None, description="Operation")


class PhilipshueGetTool(BaseTool):
    name = "philipshue_get"
    description = "Tool for philipsHue get operation - get operation"
    
    def __init__(self, credentials: Optional[PhilipshueCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the philipsHue get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running philipsHue get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running philipsHue get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the philipsHue get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
