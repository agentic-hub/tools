# html toolkit
from langchain.tools import BaseTool
from typing import List

def get_html_tools() -> List[BaseTool]:
    """Get all html tools."""
    from . import operations
    return operations.get_tools()
