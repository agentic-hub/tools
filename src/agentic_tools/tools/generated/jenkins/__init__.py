# jenkins toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_jenkins_tools() -> List[BaseTool]:
    """Get all jenkins tools."""
    from . import operations
    return operations.get_tools()

class JenkinsCredentials(BaseModel):
    """Credentials for jenkins authentication."""
    jenkins_api: Optional[Dict[str, Any]] = Field(None, description="jenkinsApi")

class JenkinsToolkit(AgenticHubToolkit):
    """Toolkit for interacting with jenkins."""

    def __init__(self, credentials: Optional[JenkinsCredentials] = None):
        """Initialize the jenkins toolkit with optional credentials.

        Args:
            credentials: JenkinsCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all jenkins tools with the configured credentials."""
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
        """Get all jenkins tools with default credentials."""
        return get_jenkins_tools()
