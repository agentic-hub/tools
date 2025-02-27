# redis toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_redis_tools() -> List[BaseTool]:
    """Get all redis tools."""
    from . import operations
    return operations.get_tools()

class RedisCredentials(BaseModel):
    """Credentials for redis authentication."""
    redis: Optional[Dict[str, Any]] = Field(None, description="redis")

class RedisToolkit(AgenticHubToolkit):
    """Toolkit for interacting with redis."""

    def __init__(self, credentials: Optional[RedisCredentials] = None):
        """Initialize the redis toolkit with optional credentials.

        Args:
            credentials: RedisCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all redis tools with the configured credentials."""
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
        """Get all redis tools with default credentials."""
        return get_redis_tools()
