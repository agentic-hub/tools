# mindee toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mindee_tools() -> List[BaseTool]:
    """Get all mindee tools."""
    from . import operations
    return operations.get_tools()

class MindeeCredentials(BaseModel):
    """Credentials for mindee authentication."""
    mindee_receipt_api: Optional[Dict[str, Any]] = Field(None, description="mindeeReceiptApi")
    mindee_invoice_api: Optional[Dict[str, Any]] = Field(None, description="mindeeInvoiceApi")

class MindeeToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mindee."""

    def __init__(self, credentials: Optional[MindeeCredentials] = None):
        """Initialize the mindee toolkit with optional credentials.

        Args:
            credentials: MindeeCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mindee tools with the configured credentials."""
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
        """Get all mindee tools with default credentials."""
        return get_mindee_tools()
