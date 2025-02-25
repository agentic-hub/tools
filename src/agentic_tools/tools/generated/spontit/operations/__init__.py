# spontit operations
from typing import List
from langchain.tools import BaseTool
from .. import SpontitCredentials

def get_tools() -> List[BaseTool]:
    """Get all spontit operation tools."""
    tools = []
    from .create import SpontitCreateTool
    tools.append(SpontitCreateTool())
    return tools
