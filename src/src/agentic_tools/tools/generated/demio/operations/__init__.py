# demio operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all demio operation tools."""
    tools = []
    from .get import DemioGetTool
    tools.append(DemioGetTool())
    from .getall import DemioGetallTool
    tools.append(DemioGetallTool())
    from .register import DemioRegisterTool
    tools.append(DemioRegisterTool())
    from .get import DemioGetTool
    tools.append(DemioGetTool())
    return tools
