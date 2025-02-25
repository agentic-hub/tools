# dropbox operations
from typing import List
from langchain.tools import BaseTool
from .. import DropboxCredentials

def get_tools() -> List[BaseTool]:
    """Get all dropbox operation tools."""
    tools = []
    from .copy import DropboxCopyTool
    tools.append(DropboxCopyTool())
    from .delete import DropboxDeleteTool
    tools.append(DropboxDeleteTool())
    from .download import DropboxDownloadTool
    tools.append(DropboxDownloadTool())
    from .move import DropboxMoveTool
    tools.append(DropboxMoveTool())
    from .upload import DropboxUploadTool
    tools.append(DropboxUploadTool())
    from .__custom_api_call__ import Dropbox__custom_api_call__Tool
    tools.append(Dropbox__custom_api_call__Tool())
    from .copy import DropboxCopyTool
    tools.append(DropboxCopyTool())
    from .create import DropboxCreateTool
    tools.append(DropboxCreateTool())
    from .delete import DropboxDeleteTool
    tools.append(DropboxDeleteTool())
    from .list import DropboxListTool
    tools.append(DropboxListTool())
    from .move import DropboxMoveTool
    tools.append(DropboxMoveTool())
    from .__custom_api_call__ import Dropbox__custom_api_call__Tool
    tools.append(Dropbox__custom_api_call__Tool())
    from .query import DropboxQueryTool
    tools.append(DropboxQueryTool())
    from .__custom_api_call__ import Dropbox__custom_api_call__Tool
    tools.append(Dropbox__custom_api_call__Tool())
    return tools
