# s3 operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all s3 operation tools."""
    tools = []
    from .create import S3CreateTool
    tools.append(S3CreateTool())
    from .delete import S3DeleteTool
    tools.append(S3DeleteTool())
    from .getall import S3GetallTool
    tools.append(S3GetallTool())
    from .search import S3SearchTool
    tools.append(S3SearchTool())
    from .create import S3CreateTool
    tools.append(S3CreateTool())
    from .delete import S3DeleteTool
    tools.append(S3DeleteTool())
    from .getall import S3GetallTool
    tools.append(S3GetallTool())
    from .copy import S3CopyTool
    tools.append(S3CopyTool())
    from .delete import S3DeleteTool
    tools.append(S3DeleteTool())
    from .download import S3DownloadTool
    tools.append(S3DownloadTool())
    from .getall import S3GetallTool
    tools.append(S3GetallTool())
    from .upload import S3UploadTool
    tools.append(S3UploadTool())
    return tools
