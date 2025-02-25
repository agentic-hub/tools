# syncroMsp operations
from typing import List
from langchain.tools import BaseTool
from .. import SyncromspCredentials

def get_tools() -> List[BaseTool]:
    """Get all syncroMsp operation tools."""
    tools = []
    from .create import SyncromspCreateTool
    tools.append(SyncromspCreateTool())
    from .delete import SyncromspDeleteTool
    tools.append(SyncromspDeleteTool())
    from .get import SyncromspGetTool
    tools.append(SyncromspGetTool())
    from .getall import SyncromspGetallTool
    tools.append(SyncromspGetallTool())
    from .update import SyncromspUpdateTool
    tools.append(SyncromspUpdateTool())
    from .create import SyncromspCreateTool
    tools.append(SyncromspCreateTool())
    from .delete import SyncromspDeleteTool
    tools.append(SyncromspDeleteTool())
    from .get import SyncromspGetTool
    tools.append(SyncromspGetTool())
    from .getall import SyncromspGetallTool
    tools.append(SyncromspGetallTool())
    from .update import SyncromspUpdateTool
    tools.append(SyncromspUpdateTool())
    from .create import SyncromspCreateTool
    tools.append(SyncromspCreateTool())
    from .delete import SyncromspDeleteTool
    tools.append(SyncromspDeleteTool())
    from .get import SyncromspGetTool
    tools.append(SyncromspGetTool())
    from .getall import SyncromspGetallTool
    tools.append(SyncromspGetallTool())
    from .update import SyncromspUpdateTool
    tools.append(SyncromspUpdateTool())
    from .create import SyncromspCreateTool
    tools.append(SyncromspCreateTool())
    from .delete import SyncromspDeleteTool
    tools.append(SyncromspDeleteTool())
    from .get import SyncromspGetTool
    tools.append(SyncromspGetTool())
    from .getall import SyncromspGetallTool
    tools.append(SyncromspGetallTool())
    from .mute import SyncromspMuteTool
    tools.append(SyncromspMuteTool())
    return tools
