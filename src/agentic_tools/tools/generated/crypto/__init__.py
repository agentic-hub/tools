# crypto toolkit
from langchain.tools import BaseTool
from typing import List

def get_crypto_tools() -> List[BaseTool]:
    """Get all crypto tools."""
    from . import operations
    return operations.get_tools()

class CryptoToolkit:
    """Toolkit for interacting with crypto."""

    def __init__(self):
        """Initialize the crypto toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all crypto tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all crypto tools with default credentials."""
        return get_crypto_tools()
