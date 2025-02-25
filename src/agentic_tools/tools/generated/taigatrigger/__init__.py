# taigaTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_taigatrigger_tools() -> List[BaseTool]:
    """Get all taigaTrigger tools."""
    from . import operations
    return operations.get_tools()
