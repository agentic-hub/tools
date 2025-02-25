# securityScorecard toolkit
from langchain.tools import BaseTool
from typing import List

def get_securityscorecard_tools() -> List[BaseTool]:
    """Get all securityScorecard tools."""
    from . import operations
    return operations.get_tools()
