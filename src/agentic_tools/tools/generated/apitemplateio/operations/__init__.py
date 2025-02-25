# apiTemplateIo operations
from typing import List
from langchain.tools import BaseTool
from .. import ApitemplateioCredentials

def get_tools() -> List[BaseTool]:
    """Get all apiTemplateIo operation tools."""
    tools = []
    from .create import ApitemplateioCreateTool
    tools.append(ApitemplateioCreateTool())
    from .__custom_api_call__ import Apitemplateio__custom_api_call__Tool
    tools.append(Apitemplateio__custom_api_call__Tool())
    from .create import ApitemplateioCreateTool
    tools.append(ApitemplateioCreateTool())
    from .__custom_api_call__ import Apitemplateio__custom_api_call__Tool
    tools.append(Apitemplateio__custom_api_call__Tool())
    from .get import ApitemplateioGetTool
    tools.append(ApitemplateioGetTool())
    from .__custom_api_call__ import Apitemplateio__custom_api_call__Tool
    tools.append(Apitemplateio__custom_api_call__Tool())
    return tools
