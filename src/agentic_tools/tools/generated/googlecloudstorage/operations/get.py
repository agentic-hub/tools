from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglecloudstorageCredentials(BaseModel):
    """Credentials for googleCloudStorage authentication."""
    google_cloud_storage_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleCloudStorageOAuth2Api")

class GooglecloudstorageGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglecloudstorageCredentials] = Field(None, description="Custom credentials for authentication")
    alt: Optional[str] = Field(None, description="Return Data")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    get_filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    operation: Optional[str] = Field(None, description="Operation")
    encryption_headers: Optional[Dict[str, Any]] = Field(None, description="Encryption Headers")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    get_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional Parameters")
    projection: Optional[str] = Field(None, description="Projection")
    resource: Optional[str] = Field(None, description="Resource")
    object_name: Optional[str] = Field(None, description="Object Name")


class GooglecloudstorageGetTool(BaseTool):
    name = "googlecloudstorage_get"
    description = "Tool for googleCloudStorage get operation - get operation"
    
    def __init__(self, credentials: Optional[GooglecloudstorageCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleCloudStorage get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleCloudStorage get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleCloudStorage get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleCloudStorage get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
