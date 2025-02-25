# profitWell operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all profitWell operation tools."""
    tools = []
    from .getsetting import ProfitwellGetsettingTool
    tools.append(ProfitwellGetsettingTool())
    from .get import ProfitwellGetTool
    tools.append(ProfitwellGetTool())
    return tools
