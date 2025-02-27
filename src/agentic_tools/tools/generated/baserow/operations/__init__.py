# baserow operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import BaserowCredentials

def get_tools() -> List[BaseTool]:
    """Get all baserow operation tools."""
    tools = []
    from .create import BaserowCreateTool
    tools.append(BaserowCreateTool())
    from .delete import BaserowDeleteTool
    tools.append(BaserowDeleteTool())
    from .get import BaserowGetTool
    tools.append(BaserowGetTool())
    from .getall import BaserowGetallTool
    tools.append(BaserowGetallTool())
    from .update import BaserowUpdateTool
    tools.append(BaserowUpdateTool())
    return tools
