# agileCrm operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import AgilecrmCredentials

def get_tools() -> List[BaseTool]:
    """Get all agileCrm operation tools."""
    tools = []
    from .create import AgilecrmCreateTool
    tools.append(AgilecrmCreateTool())
    from .delete import AgilecrmDeleteTool
    tools.append(AgilecrmDeleteTool())
    from .get import AgilecrmGetTool
    tools.append(AgilecrmGetTool())
    from .getall import AgilecrmGetallTool
    tools.append(AgilecrmGetallTool())
    from .update import AgilecrmUpdateTool
    tools.append(AgilecrmUpdateTool())
    from .create import AgilecrmCreateTool
    tools.append(AgilecrmCreateTool())
    from .delete import AgilecrmDeleteTool
    tools.append(AgilecrmDeleteTool())
    from .get import AgilecrmGetTool
    tools.append(AgilecrmGetTool())
    from .getall import AgilecrmGetallTool
    tools.append(AgilecrmGetallTool())
    from .update import AgilecrmUpdateTool
    tools.append(AgilecrmUpdateTool())
    from .create import AgilecrmCreateTool
    tools.append(AgilecrmCreateTool())
    from .delete import AgilecrmDeleteTool
    tools.append(AgilecrmDeleteTool())
    from .get import AgilecrmGetTool
    tools.append(AgilecrmGetTool())
    from .getall import AgilecrmGetallTool
    tools.append(AgilecrmGetallTool())
    from .update import AgilecrmUpdateTool
    tools.append(AgilecrmUpdateTool())
    return tools
