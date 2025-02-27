# mysql toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mysql_tools() -> List[BaseTool]:
    """Get all mysql tools."""
    from . import operations
    return operations.get_tools()

class MysqlCredentials(BaseModel):
    """Credentials for mysql authentication."""
    my_sql: Optional[Dict[str, Any]] = Field(None, description="mySql")

class MysqlToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mysql."""

    def __init__(self, credentials: Optional[MysqlCredentials] = None):
        """Initialize the mysql toolkit with optional credentials.

        Args:
            credentials: MysqlCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mysql tools with the configured credentials."""
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
        """Get all mysql tools with default credentials."""
        return get_mysql_tools()
