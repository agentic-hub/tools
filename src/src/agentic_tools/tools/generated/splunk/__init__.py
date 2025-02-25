# splunk toolkit
from langchain.tools import BaseTool
from typing import List

def get_splunk_tools() -> List[BaseTool]:
    """Get all splunk tools."""
    from . import operations
    return operations.get_tools()
