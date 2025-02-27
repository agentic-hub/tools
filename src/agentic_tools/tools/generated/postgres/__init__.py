# postgres toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_postgres_tools() -> List[BaseTool]:
    """Get all postgres tools."""
    from . import operations
    return operations.get_tools()

class PostgresCredentials(BaseModel):
    """Credentials for postgres authentication."""
    postgres: Optional[Dict[str, Any]] = Field(None, description="postgres")

class PostgresToolkit(AgenticHubToolkit):
    """Toolkit for interacting with postgres."""

    def __init__(self, credentials: Optional[PostgresCredentials] = None):
        """Initialize the postgres toolkit with optional credentials.

        Args:
            credentials: PostgresCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all postgres tools with the configured credentials."""
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
        """Get all postgres tools with default credentials."""
        return get_postgres_tools()
