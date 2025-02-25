# quickbase operations
from typing import List
from langchain.tools import BaseTool
from .. import QuickbaseCredentials

def get_tools() -> List[BaseTool]:
    """Get all quickbase operation tools."""
    tools = []
    from .getall import QuickbaseGetallTool
    tools.append(QuickbaseGetallTool())
    from .delete import QuickbaseDeleteTool
    tools.append(QuickbaseDeleteTool())
    from .download import QuickbaseDownloadTool
    tools.append(QuickbaseDownloadTool())
    from .create import QuickbaseCreateTool
    tools.append(QuickbaseCreateTool())
    from .upsert import QuickbaseUpsertTool
    tools.append(QuickbaseUpsertTool())
    from .delete import QuickbaseDeleteTool
    tools.append(QuickbaseDeleteTool())
    from .getall import QuickbaseGetallTool
    tools.append(QuickbaseGetallTool())
    from .update import QuickbaseUpdateTool
    tools.append(QuickbaseUpdateTool())
    from .get import QuickbaseGetTool
    tools.append(QuickbaseGetTool())
    from .run import QuickbaseRunTool
    tools.append(QuickbaseRunTool())
    return tools
