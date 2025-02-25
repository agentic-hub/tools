# magento2 toolkit
from langchain.tools import BaseTool
from typing import List

def get_magento2_tools() -> List[BaseTool]:
    """Get all magento2 tools."""
    from . import operations
    return operations.get_tools()
