# microsoftGraphSecurity toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsoftgraphsecurity_tools() -> List[BaseTool]:
    """Get all microsoftGraphSecurity tools."""
    from . import operations
    return operations.get_tools()
