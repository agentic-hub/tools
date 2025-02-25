# freshdesk operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all freshdesk operation tools."""
    tools = []
    from .create import FreshdeskCreateTool
    tools.append(FreshdeskCreateTool())
    from .delete import FreshdeskDeleteTool
    tools.append(FreshdeskDeleteTool())
    from .get import FreshdeskGetTool
    tools.append(FreshdeskGetTool())
    from .getall import FreshdeskGetallTool
    tools.append(FreshdeskGetallTool())
    from .update import FreshdeskUpdateTool
    tools.append(FreshdeskUpdateTool())
    from .create import FreshdeskCreateTool
    tools.append(FreshdeskCreateTool())
    from .delete import FreshdeskDeleteTool
    tools.append(FreshdeskDeleteTool())
    from .get import FreshdeskGetTool
    tools.append(FreshdeskGetTool())
    from .getall import FreshdeskGetallTool
    tools.append(FreshdeskGetallTool())
    from .update import FreshdeskUpdateTool
    tools.append(FreshdeskUpdateTool())
    return tools
