from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NextcloudCredentials(BaseModel):
    """Credentials for nextCloud authentication."""
    next_cloud_api: Optional[Dict[str, Any]] = Field(None, description="nextCloudApi")
    next_cloud_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="nextCloudOAuth2Api")

class NextcloudShareToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[NextcloudCredentials] = Field(None, description="Custom credentials for authentication")
    to_path: Optional[str] = Field(None, description="The destination path of file or folder. The path should start with \"/\".")
    path: Optional[str] = Field(None, description="The file path of the file to share. Has to contain the full path. The path should start with \"/\".")
    user_id: Optional[str] = Field(None, description="Username the user will have")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The Email address to share with")
    share_type: Optional[str] = Field(None, description="The share permissions to set")
    circle_id: Optional[str] = Field(None, description="The ID of the circle to share with")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    group_id: Optional[str] = Field(None, description="The ID of the group to share with")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    user: Optional[str] = Field(None, description="The user to share with")


class NextcloudShareTool(BaseTool):
    name = "nextcloud_share"
    description = "Tool for nextCloud share operation - share operation"
    
    def __init__(self, credentials: Optional[NextcloudCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the nextCloud share operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running nextCloud share operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running nextCloud share operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the nextCloud share operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
