# rabbitmq toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_rabbitmq_tools() -> List[BaseTool]:
    """Get all rabbitmq tools."""
    from . import operations
    return operations.get_tools()

class RabbitmqCredentials(BaseModel):
    """Credentials for rabbitmq authentication."""
    rabbitmq: Optional[Dict[str, Any]] = Field(None, description="rabbitmq")

class RabbitmqToolkit(AgenticHubToolkit):
    """Toolkit for interacting with rabbitmq."""

    def __init__(self, credentials: Optional[RabbitmqCredentials] = None):
        """Initialize the rabbitmq toolkit with optional credentials.

        Args:
            credentials: RabbitmqCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all rabbitmq tools with the configured credentials."""
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
        """Get all rabbitmq tools with default credentials."""
        return get_rabbitmq_tools()
