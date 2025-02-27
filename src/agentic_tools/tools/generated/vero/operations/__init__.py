# vero operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import VeroCredentials

def get_tools() -> List[BaseTool]:
    """Get all vero operation tools."""
    tools = []
    from .addtags import VeroAddtagsTool
    tools.append(VeroAddtagsTool())
    from .alias import VeroAliasTool
    tools.append(VeroAliasTool())
    from .create import VeroCreateTool
    tools.append(VeroCreateTool())
    from .delete import VeroDeleteTool
    tools.append(VeroDeleteTool())
    from .resubscribe import VeroResubscribeTool
    tools.append(VeroResubscribeTool())
    from .removetags import VeroRemovetagsTool
    tools.append(VeroRemovetagsTool())
    from .unsubscribe import VeroUnsubscribeTool
    tools.append(VeroUnsubscribeTool())
    from .track import VeroTrackTool
    tools.append(VeroTrackTool())
    return tools
