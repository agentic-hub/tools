from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PushoverCredentials(BaseModel):
    """Credentials for pushover authentication."""
    pushover_api: Optional[Dict[str, Any]] = Field(None, description="pushoverApi")

class PushoverPushToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PushoverCredentials] = Field(None, description="Custom credentials for authentication")
    user_key: Optional[str] = Field(None, description="The user/group key (not e-mail address) of your user (or you), viewable when logged into the <a href=\"https://pushover.net/\">dashboard</a> (often referred to as <code>USER_KEY</code> in the <a href=\"https://support.pushover.net/i44-example-code-and-pushover-libraries\">libraries</a> and code examples)")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    priority: Optional[str] = Field(None, description="Send as -2 to generate no notification/alert, -1 to always send as a quiet notification, 1 to display as high-priority and bypass the user's quiet hours, or 2 to also require confirmation from the user")
    expire: Optional[float] = Field(None, description="Specifies how many seconds your notification will continue to be retried for (every retry seconds)")
    message: Optional[str] = Field(None, description="Your message")
    operation: Optional[str] = Field(None, description="Operation")
    retry: Optional[float] = Field(None, description="Specifies how often (in seconds) the Pushover servers will send the same notification to the user. This parameter must have a value of at least 30 seconds between retries.")


class PushoverPushTool(BaseTool):
    name = "pushover_push"
    description = "Tool for pushover push operation - push operation"
    
    def __init__(self, credentials: Optional[PushoverCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the pushover push operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running pushover push operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running pushover push operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pushover push operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
