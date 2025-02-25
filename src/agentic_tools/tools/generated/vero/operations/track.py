from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class VeroCredentials(BaseModel):
    """Credentials for vero authentication."""
    vero_api: Optional[Dict[str, Any]] = Field(None, description="veroApi")

class VeroTrackToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[VeroCredentials] = Field(None, description="Custom credentials for authentication")
    event_name: Optional[str] = Field(None, description="The name of the event tracked")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="Email")
    tags: Optional[str] = Field(None, description="Tags to add separated by \",\"")
    data_attributes_json: Optional[str] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    data_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="Key value pairs that represent any properties you want to track with this event")
    extra_attributes_json: Optional[str] = Field(None, description="Key value pairs that represent reserved, Vero-specific operators. Refer to the note on “deduplication” below.")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier of the customer")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    extra_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="Key value pairs that represent reserved, Vero-specific operators. Refer to the note on “deduplication” below.")


class VeroTrackTool(BaseTool):
    name = "vero_track"
    description = "Tool for vero track operation - track operation"
    
    def __init__(self, credentials: Optional[VeroCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the vero track operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running vero track operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running vero track operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the vero track operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
