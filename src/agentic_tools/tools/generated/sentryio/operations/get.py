from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SentryioCredentials(BaseModel):
    """Credentials for sentryIo authentication."""
    sentry_io_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="sentryIoOAuth2Api")
    sentry_io_api: Optional[Dict[str, Any]] = Field(None, description="sentryIoApi")
    sentry_io_server_api: Optional[Dict[str, Any]] = Field(None, description="sentryIoServerApi")

class SentryioGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SentryioCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    project_slug: Optional[str] = Field(None, description="The slug of the project the events belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The slug of the organization the team should be created for")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    organization_slug: Optional[str] = Field(None, description="The slug of the organization the events belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    projects: Optional[str] = Field(None, description="projects")
    version: Optional[str] = Field(None, description="The version identifier of the release")
    team_slug: Optional[str] = Field(None, description="The slug of the team to get. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    event_id: Optional[str] = Field(None, description="The ID of the event to retrieve (either the numeric primary-key or the hexadecimal ID as reported by the raven client)")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    issue_id: Optional[str] = Field(None, description="ID of issue to get")
    sentry_version: Optional[str] = Field(None, description="Sentry Version")


class SentryioGetTool(BaseTool):
    name = "sentryio_get"
    description = "Tool for sentryIo get operation - get operation"
    
    def __init__(self, credentials: Optional[SentryioCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the sentryIo get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running sentryIo get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running sentryIo get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sentryIo get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
