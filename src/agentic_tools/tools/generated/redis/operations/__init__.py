# redis operations
from typing import List
from langchain.tools import BaseTool
from .. import RedisCredentials

def get_tools() -> List[BaseTool]:
    """Get all redis operation tools."""
    tools = []
    from .delete import RedisDeleteTool
    tools.append(RedisDeleteTool())
    from .get import RedisGetTool
    tools.append(RedisGetTool())
    from .incr import RedisIncrTool
    tools.append(RedisIncrTool())
    from .info import RedisInfoTool
    tools.append(RedisInfoTool())
    from .keys import RedisKeysTool
    tools.append(RedisKeysTool())
    from .pop import RedisPopTool
    tools.append(RedisPopTool())
    from .publish import RedisPublishTool
    tools.append(RedisPublishTool())
    from .push import RedisPushTool
    tools.append(RedisPushTool())
    from .set import RedisSetTool
    tools.append(RedisSetTool())
    return tools
