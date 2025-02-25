# erpNext toolkit
from langchain.tools import BaseTool
from typing import List

def get_erpnext_tools() -> List[BaseTool]:
    """Get all erpNext tools."""
    from . import operations
    return operations.get_tools()
