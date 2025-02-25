from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JenkinsCredentials(BaseModel):
    """Credentials for jenkins authentication."""
    jenkins_api: Optional[Dict[str, Any]] = Field(None, description="jenkinsApi")

class JenkinsExitToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[JenkinsCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    instance_notice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsExitTool(BaseTool):
    name = "jenkins_exit"
    description = "Tool for jenkins exit operation - exit operation"
    
    def __init__(self, credentials: Optional[JenkinsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the jenkins exit operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running jenkins exit operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running jenkins exit operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jenkins exit operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
