# awsS3 operations
from typing import List
from langchain.tools import BaseTool
from .. import Awss3Credentials

def get_tools() -> List[BaseTool]:
    """Get all awsS3 operation tools."""
    tools = []
    from .create import Awss3CreateTool
    tools.append(Awss3CreateTool())
    from .delete import Awss3DeleteTool
    tools.append(Awss3DeleteTool())
    from .getall import Awss3GetallTool
    tools.append(Awss3GetallTool())
    from .search import Awss3SearchTool
    tools.append(Awss3SearchTool())
    from .__custom_api_call__ import Awss3__custom_api_call__Tool
    tools.append(Awss3__custom_api_call__Tool())
    from .create import Awss3CreateTool
    tools.append(Awss3CreateTool())
    from .delete import Awss3DeleteTool
    tools.append(Awss3DeleteTool())
    from .getall import Awss3GetallTool
    tools.append(Awss3GetallTool())
    from .__custom_api_call__ import Awss3__custom_api_call__Tool
    tools.append(Awss3__custom_api_call__Tool())
    from .copy import Awss3CopyTool
    tools.append(Awss3CopyTool())
    from .delete import Awss3DeleteTool
    tools.append(Awss3DeleteTool())
    from .download import Awss3DownloadTool
    tools.append(Awss3DownloadTool())
    from .getall import Awss3GetallTool
    tools.append(Awss3GetallTool())
    from .upload import Awss3UploadTool
    tools.append(Awss3UploadTool())
    from .__custom_api_call__ import Awss3__custom_api_call__Tool
    tools.append(Awss3__custom_api_call__Tool())
    return tools
