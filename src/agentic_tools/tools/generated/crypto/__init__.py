# crypto toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_crypto_tools() -> List[BaseTool]:
    """Get all crypto tools."""
    from . import operations
    return operations.get_tools()

class CryptoToolkit(AgenticHubToolkit):
    """Toolkit for interacting with crypto."""

    def __init__(self):
        """Initialize the crypto toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all crypto tools with the configured credentials."""
        from . import operations
        return self.get_tools_from_operations(operations)
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all crypto tools with default credentials."""
        return get_crypto_tools()
