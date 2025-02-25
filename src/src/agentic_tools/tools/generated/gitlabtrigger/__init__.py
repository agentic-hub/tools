# gitlabTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_gitlabtrigger_tools() -> List[BaseTool]:
    """Get all gitlabTrigger tools."""
    from . import operations
    return operations.get_tools()
