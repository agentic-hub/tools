from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BoxCredentials(BaseModel):
    """Credentials for box authentication."""
    box_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="boxOAuth2Api")

class BoxDownloadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[BoxCredentials] = Field(None, description="Custom credentials for authentication")
    parent_id: Optional[str] = Field(None, description="The ID of folder to copy the file to. If not defined will be copied to the root folder.")
    role: Optional[str] = Field(None, description="The level of access granted")
    file_id: Optional[str] = Field(None, description="File ID")
    user_id: Optional[str] = Field(None, description="The user's ID to share the file with")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The user's email address to share the file with")
    folder_id: Optional[str] = Field(None, description="Folder ID")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    accessible_by: Optional[str] = Field(None, description="The type of object the file will be shared with")
    group_id: Optional[str] = Field(None, description="The group's ID to share the file with")
    query: Optional[str] = Field(None, description="The string to search for. This query is matched against item names, descriptions, text content of files, and various other fields of the different item types.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    use_email: Optional[bool] = Field(None, description="Whether identify the user by email or ID")


class BoxDownloadTool(BaseTool):
    name = "box_download"
    description = "Tool for box download operation - download operation"
    
    def __init__(self, credentials: Optional[BoxCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the box download operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running box download operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running box download operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the box download operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
