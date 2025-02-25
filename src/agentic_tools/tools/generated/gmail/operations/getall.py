from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GmailCredentials(BaseModel):
    """Credentials for gmail authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    gmail_o_auth2: Optional[Dict[str, Any]] = Field(None, description="gmailOAuth2")

class GmailGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GmailCredentials] = Field(None, description="Custom credentials for authentication")
    thread_id: Optional[str] = Field(None, description="The ID of the thread you are operating on")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    subject: Optional[str] = Field(None, description="Subject")
    operation: Optional[str] = Field(None, description="Operation")
    email_type: Optional[str] = Field(None, description="Email Type")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    message_id: Optional[str] = Field(None, description="Draft ID")
    filters_notice: Optional[str] = Field(None, description="Fetching a lot of messages may take a long time. Consider using filters to speed things up")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    label_ids: Optional[str] = Field(None, description="labelIds")


class GmailGetallTool(BaseTool):
    name = "gmail_getall"
    description = "Tool for gmail getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[GmailCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the gmail getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running gmail getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running gmail getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gmail getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
