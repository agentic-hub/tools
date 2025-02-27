# odoo toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_odoo_tools() -> List[BaseTool]:
    """Get all odoo tools."""
    from . import operations
    return operations.get_tools()

class OdooCredentials(BaseModel):
    """Credentials for odoo authentication."""
    odoo_api: Optional[Dict[str, Any]] = Field(None, description="odooApi")

class OdooToolkit(AgenticHubToolkit):
    """Toolkit for interacting with odoo."""

    def __init__(self, credentials: Optional[OdooCredentials] = None):
        """Initialize the odoo toolkit with optional credentials.

        Args:
            credentials: OdooCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all odoo tools with the configured credentials."""
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
        """Get all odoo tools with default credentials."""
        return get_odoo_tools()
