# slack toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_slack_tools() -> List[BaseTool]:
    """Get all slack tools."""
    from . import operations
    return operations.get_tools()

class SlackCredentials(BaseModel):
    """Credentials for slack authentication."""
    slack_api: Optional[Dict[str, Any]] = Field(None, description="slackApi")
    slack_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="slackOAuth2Api")

class SlackToolkit(AgenticHubToolkit):
    """Toolkit for interacting with slack."""

    def __init__(self, credentials: Optional[SlackCredentials] = None):
        """Initialize the slack toolkit with optional credentials.

        Args:
            credentials: SlackCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all slack tools with the configured credentials."""
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
        """Get all slack tools with default credentials."""
        return get_slack_tools()
