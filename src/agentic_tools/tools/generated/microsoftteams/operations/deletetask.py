from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftteamsCredentials(BaseModel):
    """Credentials for microsoftTeams authentication."""
    microsoft_teams_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftTeamsOAuth2Api")

class MicrosoftteamsDeletetaskToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MicrosoftteamsCredentials] = Field(None, description="Custom credentials for authentication")
    team_id: Optional[Dict[str, Any]] = Field(None, description="Select the team from the list, by URL, or by ID (the ID is the \"groupId\" parameter in the URL you get from \"Get a link to the team\")")
    channel_id: Optional[Dict[str, Any]] = Field(None, description="Select the channel from the list, by URL, or by ID (the ID is the \"threadId\" in the URL)")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="The ID of the task to delete")
    name: Optional[str] = Field(None, description="The name of the new channel you want to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    plan_id: Optional[Dict[str, Any]] = Field(None, description="The plan for the task to belong to")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The content of the message to be sent")
    chat_id: Optional[Dict[str, Any]] = Field(None, description="Select the chat from the list, by URL, or by ID (find the chat ID after \"conversations/\" in the URL)")
    content_type: Optional[str] = Field(None, description="Whether the message is plain text or HTML")
    group_id: Optional[Dict[str, Any]] = Field(None, description="Team")
    resource: Optional[str] = Field(None, description="Resource")


class MicrosoftteamsDeletetaskTool(BaseTool):
    name = "microsoftteams_deletetask"
    description = "Tool for microsoftTeams deleteTask operation - deleteTask operation"
    
    def __init__(self, credentials: Optional[MicrosoftteamsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the microsoftTeams deleteTask operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running microsoftTeams deleteTask operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running microsoftTeams deleteTask operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftTeams deleteTask operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
