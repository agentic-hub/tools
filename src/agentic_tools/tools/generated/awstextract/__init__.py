# awsTextract toolkit
from langchain.tools import BaseTool
from typing import List

def get_awstextract_tools() -> List[BaseTool]:
    """Get all awsTextract tools."""
    from . import operations
    return operations.get_tools()
