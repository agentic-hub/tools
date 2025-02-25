from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Awss3Credentials(BaseModel):
    """Credentials for awsS3 authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class Awss3DeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[Awss3Credentials] = Field(None, description="Custom credentials for authentication")
    folder_key: Optional[str] = Field(None, description="Folder Key")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the AWS S3 bucket to delete")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    file_name: Optional[str] = Field(None, description="File Name")
    file_key: Optional[str] = Field(None, description="File Key")


class Awss3DeleteTool(BaseTool):
    name = "awss3_delete"
    description = "Tool for awsS3 delete operation - delete operation"
    
    def __init__(self, credentials: Optional[Awss3Credentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsS3 delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsS3 delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsS3 delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsS3 delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
