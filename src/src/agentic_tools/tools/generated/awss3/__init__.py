# awsS3 toolkit
from langchain.tools import BaseTool
from typing import List

def get_awss3_tools() -> List[BaseTool]:
    """Get all awsS3 tools."""
    from . import operations
    return operations.get_tools()
