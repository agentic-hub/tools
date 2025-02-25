# crypto toolkit
from langchain.tools import BaseTool
from typing import List

def get_crypto_tools() -> List[BaseTool]:
    """Get all crypto tools."""
    from . import operations
    return operations.get_tools()
