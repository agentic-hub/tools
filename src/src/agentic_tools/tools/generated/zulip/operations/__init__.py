# zulip operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all zulip operation tools."""
    tools = []
    from .delete import ZulipDeleteTool
    tools.append(ZulipDeleteTool())
    from .get import ZulipGetTool
    tools.append(ZulipGetTool())
    from .sendprivate import ZulipSendprivateTool
    tools.append(ZulipSendprivateTool())
    from .sendstream import ZulipSendstreamTool
    tools.append(ZulipSendstreamTool())
    from .update import ZulipUpdateTool
    tools.append(ZulipUpdateTool())
    from .updatefile import ZulipUpdatefileTool
    tools.append(ZulipUpdatefileTool())
    from .create import ZulipCreateTool
    tools.append(ZulipCreateTool())
    from .delete import ZulipDeleteTool
    tools.append(ZulipDeleteTool())
    from .getall import ZulipGetallTool
    tools.append(ZulipGetallTool())
    from .getsubscribed import ZulipGetsubscribedTool
    tools.append(ZulipGetsubscribedTool())
    from .update import ZulipUpdateTool
    tools.append(ZulipUpdateTool())
    from .create import ZulipCreateTool
    tools.append(ZulipCreateTool())
    from .deactivate import ZulipDeactivateTool
    tools.append(ZulipDeactivateTool())
    from .get import ZulipGetTool
    tools.append(ZulipGetTool())
    from .getall import ZulipGetallTool
    tools.append(ZulipGetallTool())
    from .update import ZulipUpdateTool
    tools.append(ZulipUpdateTool())
    return tools
