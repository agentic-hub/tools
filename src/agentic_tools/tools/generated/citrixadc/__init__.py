# citrixadc toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_citrixadc_tools() -> List[BaseTool]:
    """Get all citrixadc tools."""
    from . import operations
    return operations.get_tools()

class CitrixadcCredentials(BaseModel):
    """Credentials for citrixadc authentication."""
    citrix_adc_api: Optional[Dict[str, Any]] = Field(None, description="citrixAdcApi")

class CitrixadcToolkit(AgenticHubToolkit):
    """Toolkit for interacting with citrixadc."""

    def __init__(self, credentials: Optional[CitrixadcCredentials] = None):
        """Initialize the citrixadc toolkit with optional credentials.

        Args:
            credentials: CitrixadcCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all citrixadc tools with the configured credentials."""
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
        """Get all citrixadc tools with default credentials."""
        return get_citrixadc_tools()
