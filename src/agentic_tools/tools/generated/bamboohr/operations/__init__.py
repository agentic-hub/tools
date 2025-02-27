# bambooHr operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import BamboohrCredentials

def get_tools() -> List[BaseTool]:
    """Get all bambooHr operation tools."""
    tools = []
    from .create import BamboohrCreateTool
    tools.append(BamboohrCreateTool())
    from .get import BamboohrGetTool
    tools.append(BamboohrGetTool())
    from .getall import BamboohrGetallTool
    tools.append(BamboohrGetallTool())
    from .update import BamboohrUpdateTool
    tools.append(BamboohrUpdateTool())
    from .delete import BamboohrDeleteTool
    tools.append(BamboohrDeleteTool())
    from .download import BamboohrDownloadTool
    tools.append(BamboohrDownloadTool())
    from .getall import BamboohrGetallTool
    tools.append(BamboohrGetallTool())
    from .update import BamboohrUpdateTool
    tools.append(BamboohrUpdateTool())
    from .upload import BamboohrUploadTool
    tools.append(BamboohrUploadTool())
    from .delete import BamboohrDeleteTool
    tools.append(BamboohrDeleteTool())
    from .download import BamboohrDownloadTool
    tools.append(BamboohrDownloadTool())
    from .getall import BamboohrGetallTool
    tools.append(BamboohrGetallTool())
    from .update import BamboohrUpdateTool
    tools.append(BamboohrUpdateTool())
    from .upload import BamboohrUploadTool
    tools.append(BamboohrUploadTool())
    from .get import BamboohrGetTool
    tools.append(BamboohrGetTool())
    return tools
