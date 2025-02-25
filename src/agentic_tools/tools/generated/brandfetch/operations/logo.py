from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BrandfetchCredentials(BaseModel):
    """Credentials for Brandfetch authentication."""
    brandfetch_api: Optional[Dict[str, Any]] = Field(None, description="brandfetchApi")

class BrandfetchLogoToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[BrandfetchCredentials] = Field(None, description="Custom credentials for authentication")
    image_types: Optional[str] = Field(None, description="imageTypes")
    download: Optional[bool] = Field(None, description="Name of the binary property to which to write the data of the read file")
    image_formats: Optional[str] = Field(None, description="imageFormats")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain name of the company")


class BrandfetchLogoTool(BaseTool):
    name = "brandfetch_logo"
    description = "Tool for Brandfetch logo operation - logo operation"
    
    def __init__(self, credentials: Optional[BrandfetchCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the Brandfetch logo operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running Brandfetch logo operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running Brandfetch logo operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the Brandfetch logo operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
