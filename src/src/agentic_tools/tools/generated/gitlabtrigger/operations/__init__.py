# gitlabTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all gitlabTrigger operation tools."""
    tools = []
    from .default import GitlabtriggerDefaultTool
    tools.append(GitlabtriggerDefaultTool())
    return tools
