from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HumanticaiCredentials(BaseModel):
    """Credentials for humanticAi authentication."""
    humantic_ai_api: Optional[Dict[str, Any]] = Field(None, description="humanticAiApi")

class HumanticaiGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HumanticaiCredentials] = Field(None, description="Custom credentials for authentication")
    user_id: Optional[str] = Field(None, description="This value is the same as the User ID that was provided when the analysis was created. This could be a LinkedIn URL, email ID, or a unique string in case of resume based analysis.")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    send_resume: Optional[bool] = Field(None, description="Whether to send a resume for a resume based analysis")
    operation: Optional[str] = Field(None, description="Operation")


class HumanticaiGetTool(BaseTool):
    name = "humanticai_get"
    description = "Tool for humanticAi get operation - get operation"
    
    def __init__(self, credentials: Optional[HumanticaiCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the humanticAi get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running humanticAi get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running humanticAi get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the humanticAi get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
