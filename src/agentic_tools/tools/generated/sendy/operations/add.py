from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendyCredentials(BaseModel):
    """Credentials for sendy authentication."""
    sendy_api: Optional[Dict[str, Any]] = Field(None, description="sendyApi")

class SendyAddToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SendyCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    list_id: Optional[str] = Field(None, description="The list ID you want to subscribe a user to. This encrypted & hashed ID can be found under View all lists section named ID.")
    email: Optional[str] = Field(None, description="Email address of the subscriber")
    operation: Optional[str] = Field(None, description="Operation")


class SendyAddTool(BaseTool):
    name = "sendy_add"
    description = "Tool for sendy add operation - add operation"
    
    def __init__(self, credentials: Optional[SendyCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the sendy add operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running sendy add operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running sendy add operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendy add operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
