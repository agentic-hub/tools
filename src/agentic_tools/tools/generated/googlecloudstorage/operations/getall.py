from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglecloudstorageCredentials(BaseModel):
    """Credentials for googleCloudStorage authentication."""
    google_cloud_storage_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleCloudStorageOAuth2Api")

class GooglecloudstorageGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglecloudstorageCredentials] = Field(None, description="Custom credentials for authentication")
    list_filters: Optional[Dict[str, Any]] = Field(None, description="Additional Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    max_results: Optional[float] = Field(None, description="Max number of results to return")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    prefix: Optional[str] = Field(None, description="Prefix")
    projection: Optional[str] = Field(None, description="Projection")
    resource: Optional[str] = Field(None, description="Resource")
    project_id: Optional[str] = Field(None, description="Project ID")


class GooglecloudstorageGetallTool(BaseTool):
    name = "googlecloudstorage_getall"
    description = "Tool for googleCloudStorage getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[GooglecloudstorageCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleCloudStorage getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleCloudStorage getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleCloudStorage getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleCloudStorage getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
