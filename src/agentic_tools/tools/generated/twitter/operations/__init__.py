# twitter operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import TwitterCredentials

def get_tools() -> List[BaseTool]:
    """Get all twitter operation tools."""
    tools = []
    from .create import TwitterCreateTool
    tools.append(TwitterCreateTool())
    from .__custom_api_call__ import Twitter__custom_api_call__Tool
    tools.append(Twitter__custom_api_call__Tool())
    from .add import TwitterAddTool
    tools.append(TwitterAddTool())
    from .__custom_api_call__ import Twitter__custom_api_call__Tool
    tools.append(Twitter__custom_api_call__Tool())
    from .create import TwitterCreateTool
    tools.append(TwitterCreateTool())
    from .delete import TwitterDeleteTool
    tools.append(TwitterDeleteTool())
    from .like import TwitterLikeTool
    tools.append(TwitterLikeTool())
    from .retweet import TwitterRetweetTool
    tools.append(TwitterRetweetTool())
    from .search import TwitterSearchTool
    tools.append(TwitterSearchTool())
    from .__custom_api_call__ import Twitter__custom_api_call__Tool
    tools.append(Twitter__custom_api_call__Tool())
    from .searchuser import TwitterSearchuserTool
    tools.append(TwitterSearchuserTool())
    from .__custom_api_call__ import Twitter__custom_api_call__Tool
    tools.append(Twitter__custom_api_call__Tool())
    return tools
