# scade-toolsTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_scade-toolstrigger_tools() -> List[BaseTool]:
    """Get all scade-toolsTrigger tools."""
    from . import operations
    return operations.get_tools()
