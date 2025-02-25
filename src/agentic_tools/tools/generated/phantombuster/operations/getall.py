from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PhantombusterCredentials(BaseModel):
    """Credentials for phantombuster authentication."""
    phantombuster_api: Optional[Dict[str, Any]] = Field(None, description="phantombusterApi")

class PhantombusterGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PhantombusterCredentials] = Field(None, description="Custom credentials for authentication")
    resolve_data: Optional[bool] = Field(None, description="By default the outpout is presented as string. If this option gets activated, it will resolve the data automatically.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    agent_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class PhantombusterGetallTool(BaseTool):
    name = "phantombuster_getall"
    description = "Tool for phantombuster getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[PhantombusterCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the phantombuster getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running phantombuster getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running phantombuster getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the phantombuster getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
