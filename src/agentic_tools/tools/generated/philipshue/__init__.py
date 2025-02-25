# philipsHue toolkit
from langchain.tools import BaseTool
from typing import List

def get_philipshue_tools() -> List[BaseTool]:
    """Get all philipsHue tools."""
    from . import operations
    return operations.get_tools()
