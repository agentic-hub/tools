# demio toolkit
from langchain.tools import BaseTool
from typing import List

def get_demio_tools() -> List[BaseTool]:
    """Get all demio tools."""
    from . import operations
    return operations.get_tools()
