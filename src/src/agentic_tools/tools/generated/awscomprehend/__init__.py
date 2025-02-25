# awsComprehend toolkit
from langchain.tools import BaseTool
from typing import List

def get_awscomprehend_tools() -> List[BaseTool]:
    """Get all awsComprehend tools."""
    from . import operations
    return operations.get_tools()
