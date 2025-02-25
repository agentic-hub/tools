# uptimeRobot operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all uptimeRobot operation tools."""
    tools = []
    from .get import UptimerobotGetTool
    tools.append(UptimerobotGetTool())
    from .create import UptimerobotCreateTool
    tools.append(UptimerobotCreateTool())
    from .delete import UptimerobotDeleteTool
    tools.append(UptimerobotDeleteTool())
    from .get import UptimerobotGetTool
    tools.append(UptimerobotGetTool())
    from .getall import UptimerobotGetallTool
    tools.append(UptimerobotGetallTool())
    from .reset import UptimerobotResetTool
    tools.append(UptimerobotResetTool())
    from .update import UptimerobotUpdateTool
    tools.append(UptimerobotUpdateTool())
    from .create import UptimerobotCreateTool
    tools.append(UptimerobotCreateTool())
    from .delete import UptimerobotDeleteTool
    tools.append(UptimerobotDeleteTool())
    from .get import UptimerobotGetTool
    tools.append(UptimerobotGetTool())
    from .getall import UptimerobotGetallTool
    tools.append(UptimerobotGetallTool())
    from .update import UptimerobotUpdateTool
    tools.append(UptimerobotUpdateTool())
    from .create import UptimerobotCreateTool
    tools.append(UptimerobotCreateTool())
    from .delete import UptimerobotDeleteTool
    tools.append(UptimerobotDeleteTool())
    from .get import UptimerobotGetTool
    tools.append(UptimerobotGetTool())
    from .getall import UptimerobotGetallTool
    tools.append(UptimerobotGetallTool())
    from .update import UptimerobotUpdateTool
    tools.append(UptimerobotUpdateTool())
    from .create import UptimerobotCreateTool
    tools.append(UptimerobotCreateTool())
    from .delete import UptimerobotDeleteTool
    tools.append(UptimerobotDeleteTool())
    from .get import UptimerobotGetTool
    tools.append(UptimerobotGetTool())
    from .getall import UptimerobotGetallTool
    tools.append(UptimerobotGetallTool())
    return tools
