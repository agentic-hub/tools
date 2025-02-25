# nextCloud operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all nextCloud operation tools."""
    tools = []
    from .copy import NextcloudCopyTool
    tools.append(NextcloudCopyTool())
    from .delete import NextcloudDeleteTool
    tools.append(NextcloudDeleteTool())
    from .download import NextcloudDownloadTool
    tools.append(NextcloudDownloadTool())
    from .move import NextcloudMoveTool
    tools.append(NextcloudMoveTool())
    from .share import NextcloudShareTool
    tools.append(NextcloudShareTool())
    from .upload import NextcloudUploadTool
    tools.append(NextcloudUploadTool())
    from .__custom_api_call__ import Nextcloud__custom_api_call__Tool
    tools.append(Nextcloud__custom_api_call__Tool())
    from .copy import NextcloudCopyTool
    tools.append(NextcloudCopyTool())
    from .create import NextcloudCreateTool
    tools.append(NextcloudCreateTool())
    from .delete import NextcloudDeleteTool
    tools.append(NextcloudDeleteTool())
    from .list import NextcloudListTool
    tools.append(NextcloudListTool())
    from .move import NextcloudMoveTool
    tools.append(NextcloudMoveTool())
    from .share import NextcloudShareTool
    tools.append(NextcloudShareTool())
    from .__custom_api_call__ import Nextcloud__custom_api_call__Tool
    tools.append(Nextcloud__custom_api_call__Tool())
    from .create import NextcloudCreateTool
    tools.append(NextcloudCreateTool())
    from .delete import NextcloudDeleteTool
    tools.append(NextcloudDeleteTool())
    from .get import NextcloudGetTool
    tools.append(NextcloudGetTool())
    from .getall import NextcloudGetallTool
    tools.append(NextcloudGetallTool())
    from .update import NextcloudUpdateTool
    tools.append(NextcloudUpdateTool())
    from .__custom_api_call__ import Nextcloud__custom_api_call__Tool
    tools.append(Nextcloud__custom_api_call__Tool())
    return tools
