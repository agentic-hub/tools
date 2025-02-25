# googleSlides operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all googleSlides operation tools."""
    tools = []
    from .create import GoogleslidesCreateTool
    tools.append(GoogleslidesCreateTool())
    from .get import GoogleslidesGetTool
    tools.append(GoogleslidesGetTool())
    from .getslides import GoogleslidesGetslidesTool
    tools.append(GoogleslidesGetslidesTool())
    from .replacetext import GoogleslidesReplacetextTool
    tools.append(GoogleslidesReplacetextTool())
    from .__custom_api_call__ import Googleslides__custom_api_call__Tool
    tools.append(Googleslides__custom_api_call__Tool())
    from .get import GoogleslidesGetTool
    tools.append(GoogleslidesGetTool())
    from .getthumbnail import GoogleslidesGetthumbnailTool
    tools.append(GoogleslidesGetthumbnailTool())
    from .__custom_api_call__ import Googleslides__custom_api_call__Tool
    tools.append(Googleslides__custom_api_call__Tool())
    return tools
