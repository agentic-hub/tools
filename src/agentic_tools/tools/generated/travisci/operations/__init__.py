# travisCi operations
from typing import List
from langchain.tools import BaseTool
from .. import TravisciCredentials

def get_tools() -> List[BaseTool]:
    """Get all travisCi operation tools."""
    tools = []
    from .cancel import TravisciCancelTool
    tools.append(TravisciCancelTool())
    from .get import TravisciGetTool
    tools.append(TravisciGetTool())
    from .getall import TravisciGetallTool
    tools.append(TravisciGetallTool())
    from .restart import TravisciRestartTool
    tools.append(TravisciRestartTool())
    from .trigger import TravisciTriggerTool
    tools.append(TravisciTriggerTool())
    return tools
