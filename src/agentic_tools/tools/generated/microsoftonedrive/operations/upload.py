from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftonedriveCredentials(BaseModel):
    """Credentials for microsoftOneDrive authentication."""
    microsoft_one_drive_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftOneDriveOAuth2Api")

class MicrosoftonedriveUploadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MicrosoftonedriveCredentials] = Field(None, description="Custom credentials for authentication")
    parent_id: Optional[str] = Field(None, description="ID of the parent folder that will contain the file")
    file_id: Optional[str] = Field(None, description="File ID")
    type: Optional[str] = Field(None, description="The type of sharing link to create")
    item_id: Optional[str] = Field(None, description="ID of the file")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    file_content: Optional[str] = Field(None, description="The text content of the file")
    folder_id: Optional[str] = Field(None, description="Folder ID")
    binary_data: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    operation: Optional[str] = Field(None, description="Operation")
    scope: Optional[str] = Field(None, description="The type of sharing link to create")
    query: Optional[str] = Field(None, description="The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content.")
    resource: Optional[str] = Field(None, description="Resource")
    new_name: Optional[str] = Field(None, description="New name for file")
    file_name: Optional[str] = Field(None, description="The name the file should be saved as")


class MicrosoftonedriveUploadTool(BaseTool):
    name = "microsoftonedrive_upload"
    description = "Tool for microsoftOneDrive upload operation - upload operation"
    
    def __init__(self, credentials: Optional[MicrosoftonedriveCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the microsoftOneDrive upload operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running microsoftOneDrive upload operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running microsoftOneDrive upload operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftOneDrive upload operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
