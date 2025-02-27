# jira toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_jira_tools() -> List[BaseTool]:
    """Get all jira tools."""
    from . import operations
    return operations.get_tools()

class JiraCredentials(BaseModel):
    """Credentials for jira authentication."""
    jira_software_cloud_api: Optional[Dict[str, Any]] = Field(None, description="jiraSoftwareCloudApi")
    jira_software_server_api: Optional[Dict[str, Any]] = Field(None, description="jiraSoftwareServerApi")

class JiraToolkit(AgenticHubToolkit):
    """Toolkit for interacting with jira."""

    def __init__(self, credentials: Optional[JiraCredentials] = None):
        """Initialize the jira toolkit with optional credentials.

        Args:
            credentials: JiraCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all jira tools with the configured credentials."""
        from . import operations
        return self.get_tools_from_operations(operations)
        # Apply credentials to each tool if provided
        if self.credentials:
            for tool in tools:
                # Set credentials on each tool instance
                tool.credentials = self.credentials
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all jira tools with default credentials."""
        return get_jira_tools()
