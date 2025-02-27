# openweathermap toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_openweathermap_tools() -> List[BaseTool]:
    """Get all openweathermap tools."""
    from . import operations
    return operations.get_tools()

class OpenweathermapCredentials(BaseModel):
    """Credentials for openweathermap authentication."""
    open_weather_map_api: Optional[Dict[str, Any]] = Field(None, description="openWeatherMapApi")

class OpenweathermapToolkit(AgenticHubToolkit):
    """Toolkit for interacting with openweathermap."""

    def __init__(self, credentials: Optional[OpenweathermapCredentials] = None):
        """Initialize the openweathermap toolkit with optional credentials.

        Args:
            credentials: OpenweathermapCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all openweathermap tools with the configured credentials."""
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
        """Get all openweathermap tools with default credentials."""
        return get_openweathermap_tools()
