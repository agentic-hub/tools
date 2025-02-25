from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwscomprehendCredentials(BaseModel):
    """Credentials for awsComprehend authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwscomprehendDetectsentimentToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwscomprehendCredentials] = Field(None, description="Custom credentials for authentication")
    language_code: Optional[str] = Field(None, description="The language code for text")
    resource: Optional[str] = Field(None, description="The resource to perform")
    text: Optional[str] = Field(None, description="The text to send")
    operation: Optional[str] = Field(None, description="Operation")


class AwscomprehendDetectsentimentTool(BaseTool):
    name = "awscomprehend_detectsentiment"
    description = "Tool for awsComprehend detectSentiment operation - detectSentiment operation"
    
    def __init__(self, credentials: Optional[AwscomprehendCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsComprehend detectSentiment operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsComprehend detectSentiment operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsComprehend detectSentiment operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsComprehend detectSentiment operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
