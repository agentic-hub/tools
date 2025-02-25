from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DisqusCredentials(BaseModel):
    """Credentials for disqus authentication."""
    disqus_api: Optional[Dict[str, Any]] = Field(None, description="disqusApi")

class DisqusGetthreadsToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[DisqusCredentials] = Field(None, description="Custom credentials for authentication")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="The short name(aka ID) of the forum to get Threads")
    operation: Optional[str] = Field(None, description="Operation")


class DisqusGetthreadsTool(BaseTool):
    name = "disqus_getthreads"
    description = "Tool for disqus getThreads operation - getThreads operation"
    
    def __init__(self, credentials: Optional[DisqusCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the disqus getThreads operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running disqus getThreads operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running disqus getThreads operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the disqus getThreads operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
