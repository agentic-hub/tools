# wordpress operations
from typing import List
from langchain.tools import BaseTool
from .. import WordpressCredentials

def get_tools() -> List[BaseTool]:
    """Get all wordpress operation tools."""
    tools = []
    from .create import WordpressCreateTool
    tools.append(WordpressCreateTool())
    from .get import WordpressGetTool
    tools.append(WordpressGetTool())
    from .getall import WordpressGetallTool
    tools.append(WordpressGetallTool())
    from .update import WordpressUpdateTool
    tools.append(WordpressUpdateTool())
    from .__custom_api_call__ import Wordpress__custom_api_call__Tool
    tools.append(Wordpress__custom_api_call__Tool())
    from .create import WordpressCreateTool
    tools.append(WordpressCreateTool())
    from .get import WordpressGetTool
    tools.append(WordpressGetTool())
    from .getall import WordpressGetallTool
    tools.append(WordpressGetallTool())
    from .update import WordpressUpdateTool
    tools.append(WordpressUpdateTool())
    from .__custom_api_call__ import Wordpress__custom_api_call__Tool
    tools.append(Wordpress__custom_api_call__Tool())
    return tools
