from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AdaloCredentials(BaseModel):
    """Credentials for adalo authentication."""
    adalo_api: Optional[Dict[str, Any]] = Field(None, description="adaloApi")

class AdaloDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AdaloCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    collection_id: Optional[str] = Field(None, description="Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation")
    row_id: Optional[str] = Field(None, description="Row ID")
    operation: Optional[str] = Field(None, description="Operation")


class AdaloDeleteTool(BaseTool):
    name = "adalo_delete"
    description = "Tool for adalo delete operation - delete operation"
    
    def __init__(self, credentials: Optional[AdaloCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the adalo delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running adalo delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running adalo delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the adalo delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
