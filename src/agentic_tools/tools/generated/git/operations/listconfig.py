from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitCredentials(BaseModel):
    """Credentials for git authentication."""
    git_password: Optional[Dict[str, Any]] = Field(None, description="gitPassword")

class GitListconfigToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GitCredentials] = Field(None, description="Custom credentials for authentication")
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitListconfigTool(BaseTool):
    name = "git_listconfig"
    description = "Tool for git listConfig operation - listConfig operation"
    
    def __init__(self, credentials: Optional[GitCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the git listConfig operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running git listConfig operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running git listConfig operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the git listConfig operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
