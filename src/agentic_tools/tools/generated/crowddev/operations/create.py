from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CrowddevCredentials(BaseModel):
    """Credentials for crowdDev authentication."""
    crowd_dev_api: Optional[Dict[str, Any]] = Field(None, description="crowdDevApi")

class CrowddevCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CrowddevCredentials] = Field(None, description="Custom credentials for authentication")
    timestamp: Optional[str] = Field(None, description="Date and time when the activity took place")
    platform: Optional[str] = Field(None, description="Platform on which the activity took place")
    type: Optional[str] = Field(None, description="Type of activity")
    source_id: Optional[str] = Field(None, description="The ID of the activity in the platform (e.g. the ID of the message in Discord)")
    trigger: Optional[str] = Field(None, description="What will trigger an automation")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    id: Optional[str] = Field(None, description="The ID of the member")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the organization")
    body: Optional[str] = Field(None, description="The body of the note")
    url: Optional[str] = Field(None, description="URL to POST webhook data to")
    username: Optional[Dict[str, Any]] = Field(None, description="Username")
    resource: Optional[str] = Field(None, description="Resource")


class CrowddevCreateTool(BaseTool):
    name = "crowddev_create"
    description = "Tool for crowdDev create operation - create operation"
    
    def __init__(self, credentials: Optional[CrowddevCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the crowdDev create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running crowdDev create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running crowdDev create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the crowdDev create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
