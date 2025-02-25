from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PushbulletCredentials(BaseModel):
    """Credentials for pushbullet authentication."""
    pushbullet_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="pushbulletOAuth2Api")

class PushbulletCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PushbulletCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    value: Optional[str] = Field(None, description="The value to be set depending on the target selected. For example, if the target selected is email then this field would take the email address of the person you are trying to send the push to.")
    target: Optional[str] = Field(None, description="Define the medium that will be used to send the push")
    body: Optional[str] = Field(None, description="Body of the push")
    url: Optional[str] = Field(None, description="URL of the push")
    title: Optional[str] = Field(None, description="Title of the push")
    push_id: Optional[str] = Field(None, description="Push ID")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type")


class PushbulletCreateTool(BaseTool):
    name = "pushbullet_create"
    description = "Tool for pushbullet create operation - create operation"
    
    def __init__(self, credentials: Optional[PushbulletCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the pushbullet create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running pushbullet create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running pushbullet create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pushbullet create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
