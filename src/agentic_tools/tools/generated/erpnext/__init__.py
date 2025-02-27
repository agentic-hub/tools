# erpnext toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_erpnext_tools() -> List[BaseTool]:
    """Get all erpnext tools."""
    from . import operations
    return operations.get_tools()

class ErpnextCredentials(BaseModel):
    """Credentials for erpnext authentication."""
    erp_next_api: Optional[Dict[str, Any]] = Field(None, description="erpNextApi")

class ErpnextToolkit(AgenticHubToolkit):
    """Toolkit for interacting with erpnext."""

    def __init__(self, credentials: Optional[ErpnextCredentials] = None):
        """Initialize the erpnext toolkit with optional credentials.

        Args:
            credentials: ErpnextCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all erpnext tools with the configured credentials."""
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
        """Get all erpnext tools with default credentials."""
        return get_erpnext_tools()
