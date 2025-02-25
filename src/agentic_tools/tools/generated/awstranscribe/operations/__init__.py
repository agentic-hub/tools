# awsTranscribe operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all awsTranscribe operation tools."""
    tools = []
    from .create import AwstranscribeCreateTool
    tools.append(AwstranscribeCreateTool())
    from .delete import AwstranscribeDeleteTool
    tools.append(AwstranscribeDeleteTool())
    from .get import AwstranscribeGetTool
    tools.append(AwstranscribeGetTool())
    from .getall import AwstranscribeGetallTool
    tools.append(AwstranscribeGetallTool())
    from .__custom_api_call__ import Awstranscribe__custom_api_call__Tool
    tools.append(Awstranscribe__custom_api_call__Tool())
    return tools
