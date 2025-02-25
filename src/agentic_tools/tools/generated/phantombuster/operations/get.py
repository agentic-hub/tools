from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PhantombusterCredentials(BaseModel):
    """Credentials for phantombuster authentication."""
    phantombuster_api: Optional[Dict[str, Any]] = Field(None, description="phantombusterApi")

class PhantombusterGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PhantombusterCredentials] = Field(None, description="Custom credentials for authentication")
    resolve_data: Optional[bool] = Field(None, description="By default the outpout is presented as string. If this option gets activated, it will resolve the data automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    agent_id: Optional[str] = Field(None, description="Agent ID")
    operation: Optional[str] = Field(None, description="Operation")


class PhantombusterGetTool(BaseTool):
    name = "phantombuster_get"
    description = "Tool for phantombuster get operation - get operation"
    
    def __init__(self, credentials: Optional[PhantombusterCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the phantombuster get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running phantombuster get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running phantombuster get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the phantombuster get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
