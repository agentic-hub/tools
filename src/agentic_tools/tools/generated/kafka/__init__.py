# kafka toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_kafka_tools() -> List[BaseTool]:
    """Get all kafka tools."""
    from . import operations
    return operations.get_tools()

class KafkaCredentials(BaseModel):
    """Credentials for kafka authentication."""
    kafka: Optional[Dict[str, Any]] = Field(None, description="kafka")

class KafkaToolkit(AgenticHubToolkit):
    """Toolkit for interacting with kafka."""

    def __init__(self, credentials: Optional[KafkaCredentials] = None):
        """Initialize the kafka toolkit with optional credentials.

        Args:
            credentials: KafkaCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all kafka tools with the configured credentials."""
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
        """Get all kafka tools with default credentials."""
        return get_kafka_tools()
