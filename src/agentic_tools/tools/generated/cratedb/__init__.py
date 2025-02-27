# cratedb toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_cratedb_tools() -> List[BaseTool]:
    """Get all cratedb tools."""
    from . import operations
    return operations.get_tools()

class CratedbCredentials(BaseModel):
    """Credentials for cratedb authentication."""
    crate_db: Optional[Dict[str, Any]] = Field(None, description="crateDb")

class CratedbToolkit(AgenticHubToolkit):
    """Toolkit for interacting with cratedb."""

    def __init__(self, credentials: Optional[CratedbCredentials] = None):
        """Initialize the cratedb toolkit with optional credentials.

        Args:
            credentials: CratedbCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all cratedb tools with the configured credentials."""
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
        """Get all cratedb tools with default credentials."""
        return get_cratedb_tools()
