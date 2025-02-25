from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogledriveCredentials(BaseModel):
    """Credentials for googleDrive authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_drive_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleDriveOAuth2Api")

class GoogledriveDeletefolderToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GoogledriveCredentials] = Field(None, description="Custom credentials for authentication")
    query_string: Optional[str] = Field(None, description="The name of the file or folder to search for. Returns also files and folders whose names partially match this search term.")
    file_id: Optional[Dict[str, Any]] = Field(None, description="The file to copy")
    input_data_field_name: Optional[str] = Field(None, description="Find the name of input field containing the binary data to update the file in the Input panel on the left, in the Binary tab")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    drive_id: Optional[Dict[str, Any]] = Field(None, description="The shared drive to delete")
    folder_id: Optional[Dict[str, Any]] = Field(None, description="The folder where to save the copied file")
    operation: Optional[str] = Field(None, description="Operation")
    permissions_ui: Optional[Dict[str, Any]] = Field(None, description="Permissions")
    name: Optional[str] = Field(None, description="The name of the shared drive to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    folder_no_root_id: Optional[Dict[str, Any]] = Field(None, description="The folder to delete")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")


class GoogledriveDeletefolderTool(BaseTool):
    name = "googledrive_deletefolder"
    description = "Tool for googleDrive deleteFolder operation - deleteFolder operation"
    
    def __init__(self, credentials: Optional[GoogledriveCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleDrive deleteFolder operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleDrive deleteFolder operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleDrive deleteFolder operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleDrive deleteFolder operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
