from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PhilipshueCredentials(BaseModel):
    """Credentials for philipsHue authentication."""
    philips_hue_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="philipsHueOAuth2Api")

class PhilipshueGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PhilipshueCredentials] = Field(None, description="Custom credentials for authentication")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    light_id: Optional[str] = Field(None, description="Light ID")
    operation: Optional[str] = Field(None, description="Operation")


class PhilipshueGetallTool(BaseTool):
    name = "philipshue_getall"
    description = "Tool for philipsHue getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[PhilipshueCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the philipsHue getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running philipsHue getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running philipsHue getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the philipsHue getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
