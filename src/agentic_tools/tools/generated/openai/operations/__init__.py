# openAi operations
from typing import List
from langchain.tools import BaseTool
from .. import OpenaiCredentials

def get_tools() -> List[BaseTool]:
    """Get all openAi operation tools."""
    tools = []
    from .complete import OpenaiCompleteTool
    tools.append(OpenaiCompleteTool())
    from .__custom_api_call__ import Openai__custom_api_call__Tool
    tools.append(Openai__custom_api_call__Tool())
    from .create import OpenaiCreateTool
    tools.append(OpenaiCreateTool())
    from .__custom_api_call__ import Openai__custom_api_call__Tool
    tools.append(Openai__custom_api_call__Tool())
    from .complete import OpenaiCompleteTool
    tools.append(OpenaiCompleteTool())
    from .edit import OpenaiEditTool
    tools.append(OpenaiEditTool())
    from .moderate import OpenaiModerateTool
    tools.append(OpenaiModerateTool())
    from .__custom_api_call__ import Openai__custom_api_call__Tool
    tools.append(Openai__custom_api_call__Tool())
    return tools
