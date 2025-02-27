# microsoftsql toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_microsoftsql_tools() -> List[BaseTool]:
    """Get all microsoftsql tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftsqlCredentials(BaseModel):
    """Credentials for microsoftsql authentication."""
    microsoft_sql: Optional[Dict[str, Any]] = Field(None, description="microsoftSql")

class MicrosoftsqlToolkit(AgenticHubToolkit):
    """Toolkit for interacting with microsoftsql."""

    def __init__(self, credentials: Optional[MicrosoftsqlCredentials] = None):
        """Initialize the microsoftsql toolkit with optional credentials.

        Args:
            credentials: MicrosoftsqlCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftsql tools with the configured credentials."""
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
        """Get all microsoftsql tools with default credentials."""
        return get_microsoftsql_tools()
