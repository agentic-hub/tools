# awsDynamoDb toolkit
from langchain.tools import BaseTool
from typing import List

def get_awsdynamodb_tools() -> List[BaseTool]:
    """Get all awsDynamoDb tools."""
    from . import operations
    return operations.get_tools()
