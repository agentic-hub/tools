from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SegmentCredentials(BaseModel):
    """Credentials for segment authentication."""
    segment_api: Optional[Dict[str, Any]] = Field(None, description="segmentApi")

class SegmentCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SegmentCredentials] = Field(None, description="Custom credentials for authentication")
    user_id: Optional[str] = Field(None, description="User ID")
    resource: Optional[str] = Field(None, description="Resource")
    context: Optional[Dict[str, Any]] = Field(None, description="Context")
    integrations: Optional[Dict[str, Any]] = Field(None, description="Integration")
    traits: Optional[Dict[str, Any]] = Field(None, description="Traits")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class SegmentCreateTool(BaseTool):
    name = "segment_create"
    description = "Tool for segment create operation - create operation"
    
    def __init__(self, credentials: Optional[SegmentCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the segment create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running segment create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running segment create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the segment create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
