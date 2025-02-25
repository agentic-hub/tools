from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CircleciCredentials(BaseModel):
    """Credentials for circleCi authentication."""
    circle_ci_api: Optional[Dict[str, Any]] = Field(None, description="circleCiApi")

class CircleciTriggerToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CircleciCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    project_slug: Optional[str] = Field(None, description="Project slug in the form org-name/repo-name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    vcs: Optional[str] = Field(None, description="Source control system")
    operation: Optional[str] = Field(None, description="Operation")


class CircleciTriggerTool(BaseTool):
    name = "circleci_trigger"
    description = "Tool for circleCi trigger operation - trigger operation"
    
    def __init__(self, credentials: Optional[CircleciCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the circleCi trigger operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running circleCi trigger operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running circleCi trigger operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the circleCi trigger operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
