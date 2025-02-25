# graphql toolkit
from langchain.tools import BaseTool
from typing import List

def get_graphql_tools() -> List[BaseTool]:
    """Get all graphql tools."""
    from . import operations
    return operations.get_tools()
