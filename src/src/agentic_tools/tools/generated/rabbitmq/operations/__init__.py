# rabbitmq operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all rabbitmq operation tools."""
    tools = []
    from .sendmessage import RabbitmqSendmessageTool
    tools.append(RabbitmqSendmessageTool())
    from .deletemessage import RabbitmqDeletemessageTool
    tools.append(RabbitmqDeletemessageTool())
    return tools
