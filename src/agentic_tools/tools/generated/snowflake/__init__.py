# snowflake toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_snowflake_tools() -> List[BaseTool]:
    """Get all snowflake tools."""
    from . import operations
    return operations.get_tools()

class SnowflakeCredentials(BaseModel):
    """Credentials for snowflake authentication."""
    snowflake: Optional[Dict[str, Any]] = Field(None, description="snowflake")

class SnowflakeToolkit(AgenticHubToolkit):
    """Toolkit for interacting with snowflake."""

    def __init__(self, credentials: Optional[SnowflakeCredentials] = None):
        """Initialize the snowflake toolkit with optional credentials.

        Args:
            credentials: SnowflakeCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all snowflake tools with the configured credentials."""
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
        """Get all snowflake tools with default credentials."""
        return get_snowflake_tools()
