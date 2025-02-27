# googleDrive operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GoogledriveCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleDrive operation tools."""
    tools = []
    from .create import GoogledriveCreateTool
    tools.append(GoogledriveCreateTool())
    from .deletedrive import GoogledriveDeletedriveTool
    tools.append(GoogledriveDeletedriveTool())
    from .get import GoogledriveGetTool
    tools.append(GoogledriveGetTool())
    from .list import GoogledriveListTool
    tools.append(GoogledriveListTool())
    from .update import GoogledriveUpdateTool
    tools.append(GoogledriveUpdateTool())
    from .__custom_api_call__ import Googledrive__custom_api_call__Tool
    tools.append(Googledrive__custom_api_call__Tool())
    from .copy import GoogledriveCopyTool
    tools.append(GoogledriveCopyTool())
    from .createfromtext import GoogledriveCreatefromtextTool
    tools.append(GoogledriveCreatefromtextTool())
    from .deletefile import GoogledriveDeletefileTool
    tools.append(GoogledriveDeletefileTool())
    from .download import GoogledriveDownloadTool
    tools.append(GoogledriveDownloadTool())
    from .move import GoogledriveMoveTool
    tools.append(GoogledriveMoveTool())
    from .share import GoogledriveShareTool
    tools.append(GoogledriveShareTool())
    from .update import GoogledriveUpdateTool
    tools.append(GoogledriveUpdateTool())
    from .upload import GoogledriveUploadTool
    tools.append(GoogledriveUploadTool())
    from .__custom_api_call__ import Googledrive__custom_api_call__Tool
    tools.append(Googledrive__custom_api_call__Tool())
    from .search import GoogledriveSearchTool
    tools.append(GoogledriveSearchTool())
    from .__custom_api_call__ import Googledrive__custom_api_call__Tool
    tools.append(Googledrive__custom_api_call__Tool())
    from .create import GoogledriveCreateTool
    tools.append(GoogledriveCreateTool())
    from .deletefolder import GoogledriveDeletefolderTool
    tools.append(GoogledriveDeletefolderTool())
    from .share import GoogledriveShareTool
    tools.append(GoogledriveShareTool())
    from .__custom_api_call__ import Googledrive__custom_api_call__Tool
    tools.append(Googledrive__custom_api_call__Tool())
    return tools
