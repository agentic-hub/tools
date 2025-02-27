# servicenow toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_servicenow_tools() -> List[BaseTool]:
    """Get all servicenow tools."""
    from . import operations
    return operations.get_tools()

class ServicenowCredentials(BaseModel):
    """Credentials for servicenow authentication."""
    service_now_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="serviceNowOAuth2Api")
    service_now_basic_api: Optional[Dict[str, Any]] = Field(None, description="serviceNowBasicApi")

class ServicenowToolkit(AgenticHubToolkit):
    """Toolkit for interacting with servicenow."""

    def __init__(self, credentials: Optional[ServicenowCredentials] = None):
        """Initialize the servicenow toolkit with optional credentials.

        Args:
            credentials: ServicenowCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all servicenow tools with the configured credentials."""
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
        """Get all servicenow tools with default credentials."""
        return get_servicenow_tools()
