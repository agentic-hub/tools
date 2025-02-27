# box operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import BoxCredentials

def get_tools() -> List[BaseTool]:
    """Get all box operation tools."""
    tools = []
    from .copy import BoxCopyTool
    tools.append(BoxCopyTool())
    from .delete import BoxDeleteTool
    tools.append(BoxDeleteTool())
    from .download import BoxDownloadTool
    tools.append(BoxDownloadTool())
    from .get import BoxGetTool
    tools.append(BoxGetTool())
    from .search import BoxSearchTool
    tools.append(BoxSearchTool())
    from .share import BoxShareTool
    tools.append(BoxShareTool())
    from .upload import BoxUploadTool
    tools.append(BoxUploadTool())
    from .__custom_api_call__ import Box__custom_api_call__Tool
    tools.append(Box__custom_api_call__Tool())
    from .create import BoxCreateTool
    tools.append(BoxCreateTool())
    from .delete import BoxDeleteTool
    tools.append(BoxDeleteTool())
    from .get import BoxGetTool
    tools.append(BoxGetTool())
    from .search import BoxSearchTool
    tools.append(BoxSearchTool())
    from .share import BoxShareTool
    tools.append(BoxShareTool())
    from .update import BoxUpdateTool
    tools.append(BoxUpdateTool())
    from .__custom_api_call__ import Box__custom_api_call__Tool
    tools.append(Box__custom_api_call__Tool())
    return tools
