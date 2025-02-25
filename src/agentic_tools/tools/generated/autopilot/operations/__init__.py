# autopilot operations
from typing import List
from langchain.tools import BaseTool
from .. import AutopilotCredentials

def get_tools() -> List[BaseTool]:
    """Get all autopilot operation tools."""
    tools = []
    from .upsert import AutopilotUpsertTool
    tools.append(AutopilotUpsertTool())
    from .delete import AutopilotDeleteTool
    tools.append(AutopilotDeleteTool())
    from .get import AutopilotGetTool
    tools.append(AutopilotGetTool())
    from .getall import AutopilotGetallTool
    tools.append(AutopilotGetallTool())
    from .add import AutopilotAddTool
    tools.append(AutopilotAddTool())
    from .add import AutopilotAddTool
    tools.append(AutopilotAddTool())
    from .exist import AutopilotExistTool
    tools.append(AutopilotExistTool())
    from .getall import AutopilotGetallTool
    tools.append(AutopilotGetallTool())
    from .remove import AutopilotRemoveTool
    tools.append(AutopilotRemoveTool())
    from .create import AutopilotCreateTool
    tools.append(AutopilotCreateTool())
    from .getall import AutopilotGetallTool
    tools.append(AutopilotGetallTool())
    return tools
