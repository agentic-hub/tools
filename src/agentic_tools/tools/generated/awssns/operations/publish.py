from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwssnsCredentials(BaseModel):
    """Credentials for awsSns authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwssnsPublishToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwssnsCredentials] = Field(None, description="Custom credentials for authentication")
    message: Optional[str] = Field(None, description="The message you want to send")
    subject: Optional[str] = Field(None, description="Subject when the message is delivered to email endpoints")
    topic: Optional[str] = Field(None, description="By URL")
    operation: Optional[str] = Field(None, description="Operation")


class AwssnsPublishTool(BaseTool):
    name = "awssns_publish"
    description = "Tool for awsSns publish operation - publish operation"
    
    def __init__(self, credentials: Optional[AwssnsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsSns publish operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsSns publish operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsSns publish operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsSns publish operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
