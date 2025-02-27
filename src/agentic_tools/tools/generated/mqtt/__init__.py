# mqtt toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mqtt_tools() -> List[BaseTool]:
    """Get all mqtt tools."""
    from . import operations
    return operations.get_tools()

class MqttCredentials(BaseModel):
    """Credentials for mqtt authentication."""
    mqtt: Optional[Dict[str, Any]] = Field(None, description="mqtt")

class MqttToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mqtt."""

    def __init__(self, credentials: Optional[MqttCredentials] = None):
        """Initialize the mqtt toolkit with optional credentials.

        Args:
            credentials: MqttCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mqtt tools with the configured credentials."""
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
        """Get all mqtt tools with default credentials."""
        return get_mqtt_tools()
