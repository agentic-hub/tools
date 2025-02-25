from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitlabCredentials(BaseModel):
    """Credentials for gitlab authentication."""
    gitlab_api: Optional[Dict[str, Any]] = Field(None, description="gitlabApi")
    gitlab_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="gitlabOAuth2Api")

class GitlabDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GitlabCredentials] = Field(None, description="Custom credentials for authentication")
    file_path: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path or leave it empty for root folder.")
    commit_message: Optional[str] = Field(None, description="Commit Message")
    tag_name: Optional[str] = Field(None, description="The Git tag the release is associated with")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    issue_number: Optional[float] = Field(None, description="The number of the issue on which to create the comment on")
    operation: Optional[str] = Field(None, description="Operation")
    repository: Optional[str] = Field(None, description="The name of the project")
    body: Optional[str] = Field(None, description="The body of the issue")
    branch: Optional[str] = Field(None, description="Name of the new branch to create. The commit is added to this branch.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    project_id: Optional[str] = Field(None, description="The ID or URL-encoded path of the project")
    authentication: Optional[str] = Field(None, description="Authentication")
    additional_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="User, group or namespace of the project")


class GitlabDeleteTool(BaseTool):
    name = "gitlab_delete"
    description = "Tool for gitlab delete operation - delete operation"
    
    def __init__(self, credentials: Optional[GitlabCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the gitlab delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running gitlab delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running gitlab delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gitlab delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
