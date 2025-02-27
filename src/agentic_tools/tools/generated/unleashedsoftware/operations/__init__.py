# unleashedSoftware operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import UnleashedsoftwareCredentials

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
