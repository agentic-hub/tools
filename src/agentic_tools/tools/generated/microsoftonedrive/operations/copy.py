from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftonedriveCredentials(BaseModel):
    """Credentials for microsoftOneDrive authentication."""
    microsoft_one_drive_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftOneDriveOAuth2Api")

class MicrosoftonedriveCopyToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MicrosoftonedriveCredentials] = Field(None, description="Custom credentials for authentication")
    parent_reference: Optional[Dict[str, Any]] = Field(None, description="Reference to the parent item the copy will be created in <a href=\"https://docs.microsoft.com/en-us/onedrive/developer/rest-api/resources/itemreference?view=odsp-graph-online\"> Details </a>")
    file_id: Optional[str] = Field(None, description="File ID")
    type: Optional[str] = Field(None, description="The type of sharing link to create")
    item_id: Optional[str] = Field(None, description="ID of the file")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    folder_id: Optional[str] = Field(None, description="Folder ID")
    operation: Optional[str] = Field(None, description="Operation")
    scope: Optional[str] = Field(None, description="The type of sharing link to create")
    query: Optional[str] = Field(None, description="The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    new_name: Optional[str] = Field(None, description="New name for file")


class MicrosoftonedriveCopyTool(BaseTool):
    name = "microsoftonedrive_copy"
    description = "Tool for microsoftOneDrive copy operation - copy operation"
    
    def __init__(self, credentials: Optional[MicrosoftonedriveCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the microsoftOneDrive copy operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running microsoftOneDrive copy operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running microsoftOneDrive copy operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftOneDrive copy operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
