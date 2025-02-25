# zohoCrm toolkit
from langchain.tools import BaseTool
from typing import List

def get_zohocrm_tools() -> List[BaseTool]:
    """Get all zohoCrm tools."""
    from . import operations
    return operations.get_tools()
