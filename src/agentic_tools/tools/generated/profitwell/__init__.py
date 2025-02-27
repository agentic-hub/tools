# profitwell toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_profitwell_tools() -> List[BaseTool]:
    """Get all profitwell tools."""
    from . import operations
    return operations.get_tools()

class ProfitwellCredentials(BaseModel):
    """Credentials for profitwell authentication."""
    profit_well_api: Optional[Dict[str, Any]] = Field(None, description="profitWellApi")

class ProfitwellToolkit(AgenticHubToolkit):
    """Toolkit for interacting with profitwell."""

    def __init__(self, credentials: Optional[ProfitwellCredentials] = None):
        """Initialize the profitwell toolkit with optional credentials.

        Args:
            credentials: ProfitwellCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all profitwell tools with the configured credentials."""
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
        """Get all profitwell tools with default credentials."""
        return get_profitwell_tools()
