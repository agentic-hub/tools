# onesimpleapi toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_onesimpleapi_tools() -> List[BaseTool]:
    """Get all onesimpleapi tools."""
    from . import operations
    return operations.get_tools()

class OnesimpleapiCredentials(BaseModel):
    """Credentials for onesimpleapi authentication."""
    one_simple_api: Optional[Dict[str, Any]] = Field(None, description="oneSimpleApi")

class OnesimpleapiToolkit(AgenticHubToolkit):
    """Toolkit for interacting with onesimpleapi."""

    def __init__(self, credentials: Optional[OnesimpleapiCredentials] = None):
        """Initialize the onesimpleapi toolkit with optional credentials.

        Args:
            credentials: OnesimpleapiCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all onesimpleapi tools with the configured credentials."""
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
        """Get all onesimpleapi tools with default credentials."""
        return get_onesimpleapi_tools()
