from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GithubCredentials(BaseModel):
    """Credentials for github authentication."""
    github_api: Optional[Dict[str, Any]] = Field(None, description="githubApi")
    github_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="githubOAuth2Api")

class GithubUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GithubCredentials] = Field(None, description="Custom credentials for authentication")
    file_path: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    review_id: Optional[str] = Field(None, description="ID of the review")
    release_id: Optional[str] = Field(None, description="Release ID")
    issue_number: Optional[float] = Field(None, description="The number of the issue on which to create the comment on")
    operation: Optional[str] = Field(None, description="Operation")
    pull_request_number: Optional[float] = Field(None, description="The number of the pull request")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    repository: Optional[str] = Field(None, description="Link")
    body: Optional[str] = Field(None, description="The body of the review")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    additional_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="Link")


class GithubUpdateTool(BaseTool):
    name = "github_update"
    description = "Tool for github update operation - update operation"
    
    def __init__(self, credentials: Optional[GithubCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the github update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running github update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running github update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the github update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
