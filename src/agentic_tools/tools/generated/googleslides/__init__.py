# googleSlides toolkit
from langchain.tools import BaseTool
from typing import List

def get_googleslides_tools() -> List[BaseTool]:
    """Get all googleSlides tools."""
    from . import operations
    return operations.get_tools()
