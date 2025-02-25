from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HumanticaiCredentials(BaseModel):
    """Credentials for humanticAi authentication."""
    humantic_ai_api: Optional[Dict[str, Any]] = Field(None, description="humanticAiApi")

class HumanticaiUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HumanticaiCredentials] = Field(None, description="Custom credentials for authentication")
    user_id: Optional[str] = Field(None, description="This value is the same as the User ID that was provided when the analysis was created. Currently only supported for profiles created using LinkedIn URL.")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    send_resume: Optional[bool] = Field(None, description="Whether to send a resume for a resume of the user")
    text: Optional[str] = Field(None, description="Additional text written by the user")
    operation: Optional[str] = Field(None, description="Operation")


class HumanticaiUpdateTool(BaseTool):
    name = "humanticai_update"
    description = "Tool for humanticAi update operation - update operation"
    
    def __init__(self, credentials: Optional[HumanticaiCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the humanticAi update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running humanticAi update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running humanticAi update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the humanticAi update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
