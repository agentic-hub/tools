from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OuraCredentials(BaseModel):
    """Credentials for oura authentication."""
    oura_api: Optional[Dict[str, Any]] = Field(None, description="ouraApi")

class OuraGetreadinessToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[OuraCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class OuraGetreadinessTool(BaseTool):
    name = "oura_getreadiness"
    description = "Tool for oura getReadiness operation - getReadiness operation"
    
    def __init__(self, credentials: Optional[OuraCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the oura getReadiness operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running oura getReadiness operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running oura getReadiness operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the oura getReadiness operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
