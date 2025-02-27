# splunk toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_splunk_tools() -> List[BaseTool]:
    """Get all splunk tools."""
    from . import operations
    return operations.get_tools()

class SplunkCredentials(BaseModel):
    """Credentials for splunk authentication."""
    splunk_api: Optional[Dict[str, Any]] = Field(None, description="splunkApi")

class SplunkToolkit(AgenticHubToolkit):
    """Toolkit for interacting with splunk."""

    def __init__(self, credentials: Optional[SplunkCredentials] = None):
        """Initialize the splunk toolkit with optional credentials.

        Args:
            credentials: SplunkCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all splunk tools with the configured credentials."""
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
        """Get all splunk tools with default credentials."""
        return get_splunk_tools()
