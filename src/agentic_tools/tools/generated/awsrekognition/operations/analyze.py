from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwsrekognitionCredentials(BaseModel):
    """Credentials for awsRekognition authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwsrekognitionAnalyzeToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwsrekognitionCredentials] = Field(None, description="Custom credentials for authentication")
    name: Optional[str] = Field(None, description="S3 object key name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    operation: Optional[str] = Field(None, description="Operation")
    bucket: Optional[str] = Field(None, description="Name of the S3 bucket")
    binary_data: Optional[bool] = Field(None, description="Whether the image to analyze should be taken from binary field")
    type: Optional[str] = Field(None, description="Type")


class AwsrekognitionAnalyzeTool(BaseTool):
    name = "awsrekognition_analyze"
    description = "Tool for awsRekognition analyze operation - analyze operation"
    
    def __init__(self, credentials: Optional[AwsrekognitionCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsRekognition analyze operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsRekognition analyze operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsRekognition analyze operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsRekognition analyze operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
