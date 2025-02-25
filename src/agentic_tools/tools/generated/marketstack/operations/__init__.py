# marketstack operations
from typing import List
from langchain.tools import BaseTool
from .. import MarketstackCredentials

def get_tools() -> List[BaseTool]:
    """Get all marketstack operation tools."""
    tools = []
    from .getall import MarketstackGetallTool
    tools.append(MarketstackGetallTool())
    from .get import MarketstackGetTool
    tools.append(MarketstackGetTool())
    from .get import MarketstackGetTool
    tools.append(MarketstackGetTool())
    return tools
