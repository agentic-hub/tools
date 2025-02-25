from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DropboxCredentials(BaseModel):
    """Credentials for dropbox authentication."""
    dropbox_api: Optional[Dict[str, Any]] = Field(None, description="dropboxApi")
    dropbox_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="dropboxOAuth2Api")

class DropboxUploadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[DropboxCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    to_path: Optional[str] = Field(None, description="The destination path of file or folder")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Means of authenticating with the service")
    file_content: Optional[str] = Field(None, description="The text content of the file to upload")
    binary_data: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to upload. Has to contain the full path. The parent folder has to exist. Existing files get overwritten.")


class DropboxUploadTool(BaseTool):
    name = "dropbox_upload"
    description = "Tool for dropbox upload operation - upload operation"
    
    def __init__(self, credentials: Optional[DropboxCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the dropbox upload operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running dropbox upload operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running dropbox upload operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the dropbox upload operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
