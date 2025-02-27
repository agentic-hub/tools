# zendesk operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import ZendeskCredentials

def get_tools() -> List[BaseTool]:
    """Get all zendesk operation tools."""
    tools = []
    from .create import ZendeskCreateTool
    tools.append(ZendeskCreateTool())
    from .delete import ZendeskDeleteTool
    tools.append(ZendeskDeleteTool())
    from .get import ZendeskGetTool
    tools.append(ZendeskGetTool())
    from .getall import ZendeskGetallTool
    tools.append(ZendeskGetallTool())
    from .recover import ZendeskRecoverTool
    tools.append(ZendeskRecoverTool())
    from .update import ZendeskUpdateTool
    tools.append(ZendeskUpdateTool())
    from .__custom_api_call__ import Zendesk__custom_api_call__Tool
    tools.append(Zendesk__custom_api_call__Tool())
    from .get import ZendeskGetTool
    tools.append(ZendeskGetTool())
    from .getall import ZendeskGetallTool
    tools.append(ZendeskGetallTool())
    from .__custom_api_call__ import Zendesk__custom_api_call__Tool
    tools.append(Zendesk__custom_api_call__Tool())
    from .create import ZendeskCreateTool
    tools.append(ZendeskCreateTool())
    from .delete import ZendeskDeleteTool
    tools.append(ZendeskDeleteTool())
    from .get import ZendeskGetTool
    tools.append(ZendeskGetTool())
    from .getall import ZendeskGetallTool
    tools.append(ZendeskGetallTool())
    from .getorganizations import ZendeskGetorganizationsTool
    tools.append(ZendeskGetorganizationsTool())
    from .getrelateddata import ZendeskGetrelateddataTool
    tools.append(ZendeskGetrelateddataTool())
    from .search import ZendeskSearchTool
    tools.append(ZendeskSearchTool())
    from .update import ZendeskUpdateTool
    tools.append(ZendeskUpdateTool())
    from .__custom_api_call__ import Zendesk__custom_api_call__Tool
    tools.append(Zendesk__custom_api_call__Tool())
    from .count import ZendeskCountTool
    tools.append(ZendeskCountTool())
    from .create import ZendeskCreateTool
    tools.append(ZendeskCreateTool())
    from .delete import ZendeskDeleteTool
    tools.append(ZendeskDeleteTool())
    from .get import ZendeskGetTool
    tools.append(ZendeskGetTool())
    from .getall import ZendeskGetallTool
    tools.append(ZendeskGetallTool())
    from .getrelateddata import ZendeskGetrelateddataTool
    tools.append(ZendeskGetrelateddataTool())
    from .update import ZendeskUpdateTool
    tools.append(ZendeskUpdateTool())
    from .__custom_api_call__ import Zendesk__custom_api_call__Tool
    tools.append(Zendesk__custom_api_call__Tool())
    return tools
