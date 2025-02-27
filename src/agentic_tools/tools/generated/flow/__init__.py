# flow toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_flow_tools() -> List[BaseTool]:
    """Get all flow tools."""
    from . import operations
    return operations.get_tools()

class FlowCredentials(BaseModel):
    """Credentials for flow authentication."""
    flow_api: Optional[Dict[str, Any]] = Field(None, description="flowApi")

class FlowToolkit(AgenticHubToolkit):
    """Toolkit for interacting with flow."""

    def __init__(self, credentials: Optional[FlowCredentials] = None):
        """Initialize the flow toolkit with optional credentials.

        Args:
            credentials: FlowCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all flow tools with the configured credentials."""
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
        """Get all flow tools with default credentials."""
        return get_flow_tools()
