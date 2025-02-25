from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwstranscribeCredentials(BaseModel):
    """Credentials for awsTranscribe authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwstranscribeCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwstranscribeCredentials] = Field(None, description="Custom credentials for authentication")
    language_code: Optional[str] = Field(None, description="Language used in the input media file")
    resource: Optional[str] = Field(None, description="Resource")
    media_file_uri: Optional[str] = Field(None, description="The S3 object location of the input media file")
    transcription_job_name: Optional[str] = Field(None, description="The name of the job")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    detect_language: Optional[bool] = Field(None, description="Whether to set this field to true to enable automatic language identification")
    operation: Optional[str] = Field(None, description="Operation")


class AwstranscribeCreateTool(BaseTool):
    name = "awstranscribe_create"
    description = "Tool for awsTranscribe create operation - create operation"
    
    def __init__(self, credentials: Optional[AwstranscribeCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsTranscribe create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsTranscribe create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsTranscribe create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsTranscribe create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
