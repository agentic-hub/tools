# citrixAdc toolkit
from langchain.tools import BaseTool
from typing import List

def get_citrixadc_tools() -> List[BaseTool]:
    """Get all citrixAdc tools."""
    from . import operations
    return operations.get_tools()
