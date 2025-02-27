# monicacrm toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_monicacrm_tools() -> List[BaseTool]:
    """Get all monicacrm tools."""
    from . import operations
    return operations.get_tools()

class MonicacrmCredentials(BaseModel):
    """Credentials for monicacrm authentication."""
    monica_crm_api: Optional[Dict[str, Any]] = Field(None, description="monicaCrmApi")

class MonicacrmToolkit(AgenticHubToolkit):
    """Toolkit for interacting with monicacrm."""

    def __init__(self, credentials: Optional[MonicacrmCredentials] = None):
        """Initialize the monicacrm toolkit with optional credentials.

        Args:
            credentials: MonicacrmCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all monicacrm tools with the configured credentials."""
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
        """Get all monicacrm tools with default credentials."""
        return get_monicacrm_tools()
