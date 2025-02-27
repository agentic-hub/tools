# hubspot operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import HubspotCredentials

def get_tools() -> List[BaseTool]:
    """Get all hubspot operation tools."""
    tools = []
    from .upsert import HubspotUpsertTool
    tools.append(HubspotUpsertTool())
    from .delete import HubspotDeleteTool
    tools.append(HubspotDeleteTool())
    from .get import HubspotGetTool
    tools.append(HubspotGetTool())
    from .getall import HubspotGetallTool
    tools.append(HubspotGetallTool())
    from .getrecentlycreatedupdated import HubspotGetrecentlycreatedupdatedTool
    tools.append(HubspotGetrecentlycreatedupdatedTool())
    from .search import HubspotSearchTool
    tools.append(HubspotSearchTool())
    from .__custom_api_call__ import Hubspot__custom_api_call__Tool
    tools.append(Hubspot__custom_api_call__Tool())
    from .add import HubspotAddTool
    tools.append(HubspotAddTool())
    from .remove import HubspotRemoveTool
    tools.append(HubspotRemoveTool())
    from .__custom_api_call__ import Hubspot__custom_api_call__Tool
    tools.append(Hubspot__custom_api_call__Tool())
    from .create import HubspotCreateTool
    tools.append(HubspotCreateTool())
    from .delete import HubspotDeleteTool
    tools.append(HubspotDeleteTool())
    from .get import HubspotGetTool
    tools.append(HubspotGetTool())
    from .getall import HubspotGetallTool
    tools.append(HubspotGetallTool())
    from .getrecentlycreatedupdated import HubspotGetrecentlycreatedupdatedTool
    tools.append(HubspotGetrecentlycreatedupdatedTool())
    from .searchbydomain import HubspotSearchbydomainTool
    tools.append(HubspotSearchbydomainTool())
    from .update import HubspotUpdateTool
    tools.append(HubspotUpdateTool())
    from .__custom_api_call__ import Hubspot__custom_api_call__Tool
    tools.append(Hubspot__custom_api_call__Tool())
    from .create import HubspotCreateTool
    tools.append(HubspotCreateTool())
    from .delete import HubspotDeleteTool
    tools.append(HubspotDeleteTool())
    from .get import HubspotGetTool
    tools.append(HubspotGetTool())
    from .getall import HubspotGetallTool
    tools.append(HubspotGetallTool())
    from .getrecentlycreatedupdated import HubspotGetrecentlycreatedupdatedTool
    tools.append(HubspotGetrecentlycreatedupdatedTool())
    from .search import HubspotSearchTool
    tools.append(HubspotSearchTool())
    from .update import HubspotUpdateTool
    tools.append(HubspotUpdateTool())
    from .__custom_api_call__ import Hubspot__custom_api_call__Tool
    tools.append(Hubspot__custom_api_call__Tool())
    from .create import HubspotCreateTool
    tools.append(HubspotCreateTool())
    from .delete import HubspotDeleteTool
    tools.append(HubspotDeleteTool())
    from .get import HubspotGetTool
    tools.append(HubspotGetTool())
    from .getall import HubspotGetallTool
    tools.append(HubspotGetallTool())
    from .__custom_api_call__ import Hubspot__custom_api_call__Tool
    tools.append(Hubspot__custom_api_call__Tool())
    from .create import HubspotCreateTool
    tools.append(HubspotCreateTool())
    from .delete import HubspotDeleteTool
    tools.append(HubspotDeleteTool())
    from .get import HubspotGetTool
    tools.append(HubspotGetTool())
    from .getall import HubspotGetallTool
    tools.append(HubspotGetallTool())
    from .update import HubspotUpdateTool
    tools.append(HubspotUpdateTool())
    from .__custom_api_call__ import Hubspot__custom_api_call__Tool
    tools.append(Hubspot__custom_api_call__Tool())
    return tools
