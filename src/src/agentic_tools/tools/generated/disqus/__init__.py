# disqus toolkit
from langchain.tools import BaseTool
from typing import List

def get_disqus_tools() -> List[BaseTool]:
    """Get all disqus tools."""
    from . import operations
    return operations.get_tools()
