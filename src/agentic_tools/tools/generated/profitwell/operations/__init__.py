# profitWell operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import ProfitwellCredentials

def get_tools() -> List[BaseTool]:
    """Get all profitWell operation tools."""
    tools = []
    from .getsetting import ProfitwellGetsettingTool
    tools.append(ProfitwellGetsettingTool())
    from .get import ProfitwellGetTool
    tools.append(ProfitwellGetTool())
    return tools
