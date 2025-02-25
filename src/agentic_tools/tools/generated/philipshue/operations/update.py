from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PhilipshueCredentials(BaseModel):
    """Credentials for philipsHue authentication."""
    philips_hue_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="philipsHueOAuth2Api")

class PhilipshueUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PhilipshueCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    on: Optional[bool] = Field(None, description="On/Off state of the light")
    light_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class PhilipshueUpdateTool(BaseTool):
    name = "philipshue_update"
    description = "Tool for philipsHue update operation - update operation"
    
    def __init__(self, credentials: Optional[PhilipshueCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the philipsHue update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running philipsHue update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running philipsHue update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the philipsHue update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
