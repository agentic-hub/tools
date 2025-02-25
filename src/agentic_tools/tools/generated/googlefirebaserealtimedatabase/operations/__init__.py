# googleFirebaseRealtimeDatabase operations
from typing import List
from langchain.tools import BaseTool
from .. import GooglefirebaserealtimedatabaseCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleFirebaseRealtimeDatabase operation tools."""
    tools = []
    from .create import GooglefirebaserealtimedatabaseCreateTool
    tools.append(GooglefirebaserealtimedatabaseCreateTool())
    from .delete import GooglefirebaserealtimedatabaseDeleteTool
    tools.append(GooglefirebaserealtimedatabaseDeleteTool())
    from .get import GooglefirebaserealtimedatabaseGetTool
    tools.append(GooglefirebaserealtimedatabaseGetTool())
    from .push import GooglefirebaserealtimedatabasePushTool
    tools.append(GooglefirebaserealtimedatabasePushTool())
    from .update import GooglefirebaserealtimedatabaseUpdateTool
    tools.append(GooglefirebaserealtimedatabaseUpdateTool())
    from .__custom_api_call__ import Googlefirebaserealtimedatabase__custom_api_call__Tool
    tools.append(Googlefirebaserealtimedatabase__custom_api_call__Tool())
    return tools
