# flow operations
from typing import List
from langchain.tools import BaseTool
from .. import FlowCredentials

def get_tools() -> List[BaseTool]:
    """Get all flow operation tools."""
    tools = []
    from .create import FlowCreateTool
    tools.append(FlowCreateTool())
    from .update import FlowUpdateTool
    tools.append(FlowUpdateTool())
    from .get import FlowGetTool
    tools.append(FlowGetTool())
    from .getall import FlowGetallTool
    tools.append(FlowGetallTool())
    return tools
