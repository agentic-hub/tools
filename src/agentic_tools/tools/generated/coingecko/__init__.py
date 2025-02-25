# coinGecko toolkit
from langchain.tools import BaseTool
from typing import List

def get_coingecko_tools() -> List[BaseTool]:
    """Get all coinGecko tools."""
    from . import operations
    return operations.get_tools()
