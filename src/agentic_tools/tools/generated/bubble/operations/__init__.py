# bubble operations
from typing import List
from langchain.tools import BaseTool
from .. import BubbleCredentials

def get_tools() -> List[BaseTool]:
    """Get all bubble operation tools."""
    tools = []
    from .create import BubbleCreateTool
    tools.append(BubbleCreateTool())
    from .delete import BubbleDeleteTool
    tools.append(BubbleDeleteTool())
    from .get import BubbleGetTool
    tools.append(BubbleGetTool())
    from .getall import BubbleGetallTool
    tools.append(BubbleGetallTool())
    from .update import BubbleUpdateTool
    tools.append(BubbleUpdateTool())
    return tools
