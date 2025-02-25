from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PushbulletCredentials(BaseModel):
    """Credentials for pushbullet authentication."""
    pushbullet_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="pushbulletOAuth2Api")

class PushbulletGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PushbulletCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="The value to be set depending on the target selected. For example, if the target selected is email then this field would take the email address of the person you are trying to send the push to.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    push_id: Optional[str] = Field(None, description="Push ID")
    operation: Optional[str] = Field(None, description="Operation")


class PushbulletGetallTool(BaseTool):
    name = "pushbullet_getall"
    description = "Tool for pushbullet getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[PushbulletCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the pushbullet getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running pushbullet getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running pushbullet getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pushbullet getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
