from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JiraCredentials(BaseModel):
    """Credentials for jira authentication."""
    jira_software_cloud_api: Optional[Dict[str, Any]] = Field(None, description="jiraSoftwareCloudApi")
    jira_software_server_api: Optional[Dict[str, Any]] = Field(None, description="jiraSoftwareServerApi")

class JiraChangelogToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[JiraCredentials] = Field(None, description="Custom credentials for authentication")
    comment_json: Optional[str] = Field(None, description="The Atlassian Document Format (ADF). Online builder can be found <a href=\"https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/\">here</a>.")
    comment_id: Optional[str] = Field(None, description="The ID of the comment")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    issue_key: Optional[str] = Field(None, description="Issue Key")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Account ID of the user to delete")
    download: Optional[bool] = Field(None, description="Download")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    comment: Optional[str] = Field(None, description="Comment's text")
    jira_version: Optional[str] = Field(None, description="Jira Version")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    attachment_id: Optional[str] = Field(None, description="The ID of the attachment")


class JiraChangelogTool(BaseTool):
    name = "jira_changelog"
    description = "Tool for jira changelog operation - changelog operation"
    
    def __init__(self, credentials: Optional[JiraCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the jira changelog operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running jira changelog operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running jira changelog operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jira changelog operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
