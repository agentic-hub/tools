from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class S3Credentials(BaseModel):
    """Credentials for s3 authentication."""
    s3: Optional[Dict[str, Any]] = Field(None, description="s3")

class S3DownloadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[S3Credentials] = Field(None, description="Custom credentials for authentication")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="A succinct description of the nature, symptoms, cause, or effect of the bucket")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    file_name: Optional[str] = Field(None, description="File Name")
    file_key: Optional[str] = Field(None, description="File Key")


class S3DownloadTool(BaseTool):
    name = "s3_download"
    description = "Tool for s3 download operation - download operation"
    
    def __init__(self, credentials: Optional[S3Credentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the s3 download operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running s3 download operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running s3 download operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the s3 download operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
