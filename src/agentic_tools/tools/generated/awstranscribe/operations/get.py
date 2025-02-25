from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwstranscribeCredentials(BaseModel):
    """Credentials for awsTranscribe authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwstranscribeGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwstranscribeCredentials] = Field(None, description="Custom credentials for authentication")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    transcription_job_name: Optional[str] = Field(None, description="The name of the job")
    return_transcript: Optional[bool] = Field(None, description="By default, the response only contains metadata about the transcript. Enable this option to retrieve the transcript instead.")
    operation: Optional[str] = Field(None, description="Operation")


class AwstranscribeGetTool(BaseTool):
    name = "awstranscribe_get"
    description = "Tool for awsTranscribe get operation - get operation"
    
    def __init__(self, credentials: Optional[AwstranscribeCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsTranscribe get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsTranscribe get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsTranscribe get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsTranscribe get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
