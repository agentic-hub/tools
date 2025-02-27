# googleCloudStorage operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GooglecloudstorageCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleCloudStorage operation tools."""
    tools = []
    from .create import GooglecloudstorageCreateTool
    tools.append(GooglecloudstorageCreateTool())
    from .delete import GooglecloudstorageDeleteTool
    tools.append(GooglecloudstorageDeleteTool())
    from .get import GooglecloudstorageGetTool
    tools.append(GooglecloudstorageGetTool())
    from .getall import GooglecloudstorageGetallTool
    tools.append(GooglecloudstorageGetallTool())
    from .update import GooglecloudstorageUpdateTool
    tools.append(GooglecloudstorageUpdateTool())
    from .__custom_api_call__ import Googlecloudstorage__custom_api_call__Tool
    tools.append(Googlecloudstorage__custom_api_call__Tool())
    from .create import GooglecloudstorageCreateTool
    tools.append(GooglecloudstorageCreateTool())
    from .delete import GooglecloudstorageDeleteTool
    tools.append(GooglecloudstorageDeleteTool())
    from .get import GooglecloudstorageGetTool
    tools.append(GooglecloudstorageGetTool())
    from .getall import GooglecloudstorageGetallTool
    tools.append(GooglecloudstorageGetallTool())
    from .update import GooglecloudstorageUpdateTool
    tools.append(GooglecloudstorageUpdateTool())
    from .__custom_api_call__ import Googlecloudstorage__custom_api_call__Tool
    tools.append(Googlecloudstorage__custom_api_call__Tool())
    return tools
