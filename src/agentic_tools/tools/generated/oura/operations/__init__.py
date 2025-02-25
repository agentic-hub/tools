# oura operations
from typing import List
from langchain.tools import BaseTool
from .. import OuraCredentials

def get_tools() -> List[BaseTool]:
    """Get all oura operation tools."""
    tools = []
    from .get import OuraGetTool
    tools.append(OuraGetTool())
    from .getactivity import OuraGetactivityTool
    tools.append(OuraGetactivityTool())
    from .getreadiness import OuraGetreadinessTool
    tools.append(OuraGetreadinessTool())
    from .getsleep import OuraGetsleepTool
    tools.append(OuraGetsleepTool())
    return tools
