from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ProfitwellCredentials(BaseModel):
    """Credentials for profitWell authentication."""
    profit_well_api: Optional[Dict[str, Any]] = Field(None, description="profitWellApi")

class ProfitwellGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ProfitwellCredentials] = Field(None, description="Custom credentials for authentication")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    month: Optional[str] = Field(None, description="Can only be the current or previous month. Format should be YYYY-MM.")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type")


class ProfitwellGetTool(BaseTool):
    name = "profitwell_get"
    description = "Tool for profitWell get operation - get operation"
    
    def __init__(self, credentials: Optional[ProfitwellCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the profitWell get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running profitWell get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running profitWell get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the profitWell get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
