# unleashedSoftware operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all unleashedSoftware operation tools."""
    tools = []
    from .getall import UnleashedsoftwareGetallTool
    tools.append(UnleashedsoftwareGetallTool())
    from .get import UnleashedsoftwareGetTool
    tools.append(UnleashedsoftwareGetTool())
    from .getall import UnleashedsoftwareGetallTool
    tools.append(UnleashedsoftwareGetallTool())
    return tools
