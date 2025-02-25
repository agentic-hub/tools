from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MarketstackCredentials(BaseModel):
    """Credentials for marketstack authentication."""
    marketstack_api: Optional[Dict[str, Any]] = Field(None, description="marketstackApi")

class MarketstackGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MarketstackCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    exchange: Optional[str] = Field(None, description="Stock exchange to retrieve, specified by <a href=\"https://en.wikipedia.org/wiki/Market_Identifier_Code\">Market Identifier Code</a>, e.g. <code>XNAS</code>")
    operation: Optional[str] = Field(None, description="Operation")
    symbol: Optional[str] = Field(None, description="Stock symbol (ticker) to retrieve, e.g. <code>AAPL</code>")


class MarketstackGetTool(BaseTool):
    name = "marketstack_get"
    description = "Tool for marketstack get operation - get operation"
    
    def __init__(self, credentials: Optional[MarketstackCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the marketstack get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running marketstack get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running marketstack get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the marketstack get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
