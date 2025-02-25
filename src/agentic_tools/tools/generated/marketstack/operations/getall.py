from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MarketstackCredentials(BaseModel):
    """Credentials for marketstack authentication."""
    marketstack_api: Optional[Dict[str, Any]] = Field(None, description="marketstackApi")

class MarketstackGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MarketstackCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    symbols: Optional[str] = Field(None, description="One or multiple comma-separated stock symbols (tickers) to retrieve, e.g. <code>AAPL</code> or <code>AAPL,MSFT</code>")
    operation: Optional[str] = Field(None, description="Operation")


class MarketstackGetallTool(BaseTool):
    name = "marketstack_getall"
    description = "Tool for marketstack getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[MarketstackCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the marketstack getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running marketstack getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running marketstack getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the marketstack getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
