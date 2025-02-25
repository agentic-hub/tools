# emailReadImap operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all emailReadImap operation tools."""
    tools = []
    from .default import EmailreadimapDefaultTool
    tools.append(EmailreadimapDefaultTool())
    return tools
