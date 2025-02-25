# githubTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all githubTrigger operation tools."""
    tools = []
    from .default import GithubtriggerDefaultTool
    tools.append(GithubtriggerDefaultTool())
    return tools
