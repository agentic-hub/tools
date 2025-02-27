# grafana toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_grafana_tools() -> List[BaseTool]:
    """Get all grafana tools."""
    from . import operations
    return operations.get_tools()

class GrafanaCredentials(BaseModel):
    """Credentials for grafana authentication."""
    grafana_api: Optional[Dict[str, Any]] = Field(None, description="grafanaApi")

class GrafanaToolkit(AgenticHubToolkit):
    """Toolkit for interacting with grafana."""

    def __init__(self, credentials: Optional[GrafanaCredentials] = None):
        """Initialize the grafana toolkit with optional credentials.

        Args:
            credentials: GrafanaCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all grafana tools with the configured credentials."""
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
        """Get all grafana tools with default credentials."""
        return get_grafana_tools()
