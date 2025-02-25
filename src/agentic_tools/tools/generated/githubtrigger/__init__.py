# githubTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_githubtrigger_tools() -> List[BaseTool]:
    """Get all githubTrigger tools."""
    from . import operations
    return operations.get_tools()
