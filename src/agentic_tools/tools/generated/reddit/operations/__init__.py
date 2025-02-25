# reddit operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all reddit operation tools."""
    tools = []
    from .create import RedditCreateTool
    tools.append(RedditCreateTool())
    from .getall import RedditGetallTool
    tools.append(RedditGetallTool())
    from .delete import RedditDeleteTool
    tools.append(RedditDeleteTool())
    from .reply import RedditReplyTool
    tools.append(RedditReplyTool())
    from .__custom_api_call__ import Reddit__custom_api_call__Tool
    tools.append(Reddit__custom_api_call__Tool())
    from .get import RedditGetTool
    tools.append(RedditGetTool())
    from .__custom_api_call__ import Reddit__custom_api_call__Tool
    tools.append(Reddit__custom_api_call__Tool())
    from .get import RedditGetTool
    tools.append(RedditGetTool())
    from .getall import RedditGetallTool
    tools.append(RedditGetallTool())
    from .__custom_api_call__ import Reddit__custom_api_call__Tool
    tools.append(Reddit__custom_api_call__Tool())
    from .create import RedditCreateTool
    tools.append(RedditCreateTool())
    from .delete import RedditDeleteTool
    tools.append(RedditDeleteTool())
    from .get import RedditGetTool
    tools.append(RedditGetTool())
    from .getall import RedditGetallTool
    tools.append(RedditGetallTool())
    from .search import RedditSearchTool
    tools.append(RedditSearchTool())
    from .__custom_api_call__ import Reddit__custom_api_call__Tool
    tools.append(Reddit__custom_api_call__Tool())
    from .get import RedditGetTool
    tools.append(RedditGetTool())
    from .__custom_api_call__ import Reddit__custom_api_call__Tool
    tools.append(Reddit__custom_api_call__Tool())
    return tools
