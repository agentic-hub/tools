# cloudflare operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all cloudflare operation tools."""
    tools = []
    from .delete import CloudflareDeleteTool
    tools.append(CloudflareDeleteTool())
    from .get import CloudflareGetTool
    tools.append(CloudflareGetTool())
    from .getmany import CloudflareGetmanyTool
    tools.append(CloudflareGetmanyTool())
    from .upload import CloudflareUploadTool
    tools.append(CloudflareUploadTool())
    from .__custom_api_call__ import Cloudflare__custom_api_call__Tool
    tools.append(Cloudflare__custom_api_call__Tool())
    return tools
