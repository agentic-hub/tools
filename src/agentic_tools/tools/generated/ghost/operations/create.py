from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GhostCredentials(BaseModel):
    """Credentials for ghost authentication."""
    ghost_admin_api: Optional[Dict[str, Any]] = Field(None, description="ghostAdminApi")
    ghost_content_api: Optional[Dict[str, Any]] = Field(None, description="ghostContentApi")

class GhostCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GhostCredentials] = Field(None, description="Custom credentials for authentication")
    content: Optional[str] = Field(None, description="The content of the post to create")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Admin API")
    post_id: Optional[str] = Field(None, description="The ID of the post to delete")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    title: Optional[str] = Field(None, description="Post's title")
    content_format: Optional[str] = Field(None, description="The format of the post")
    operation: Optional[str] = Field(None, description="Operation")


class GhostCreateTool(BaseTool):
    name = "ghost_create"
    description = "Tool for ghost create operation - create operation"
    
    def __init__(self, credentials: Optional[GhostCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the ghost create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running ghost create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running ghost create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ghost create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
