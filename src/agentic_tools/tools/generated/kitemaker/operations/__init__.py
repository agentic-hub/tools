# kitemaker operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import KitemakerCredentials

def get_tools() -> List[BaseTool]:
    """Get all kitemaker operation tools."""
    tools = []
    from .get import KitemakerGetTool
    tools.append(KitemakerGetTool())
    from .getall import KitemakerGetallTool
    tools.append(KitemakerGetallTool())
    from .getall import KitemakerGetallTool
    tools.append(KitemakerGetallTool())
    from .create import KitemakerCreateTool
    tools.append(KitemakerCreateTool())
    from .get import KitemakerGetTool
    tools.append(KitemakerGetTool())
    from .getall import KitemakerGetallTool
    tools.append(KitemakerGetallTool())
    from .update import KitemakerUpdateTool
    tools.append(KitemakerUpdateTool())
    return tools
