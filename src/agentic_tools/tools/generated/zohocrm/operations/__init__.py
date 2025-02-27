# zohoCrm operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import ZohocrmCredentials

def get_tools() -> List[BaseTool]:
    """Get all zohoCrm operation tools."""
    tools = []
    from .create import ZohocrmCreateTool
    tools.append(ZohocrmCreateTool())
    from .upsert import ZohocrmUpsertTool
    tools.append(ZohocrmUpsertTool())
    from .delete import ZohocrmDeleteTool
    tools.append(ZohocrmDeleteTool())
    from .get import ZohocrmGetTool
    tools.append(ZohocrmGetTool())
    from .getall import ZohocrmGetallTool
    tools.append(ZohocrmGetallTool())
    from .update import ZohocrmUpdateTool
    tools.append(ZohocrmUpdateTool())
    from .__custom_api_call__ import Zohocrm__custom_api_call__Tool
    tools.append(Zohocrm__custom_api_call__Tool())
    from .create import ZohocrmCreateTool
    tools.append(ZohocrmCreateTool())
    from .upsert import ZohocrmUpsertTool
    tools.append(ZohocrmUpsertTool())
    from .delete import ZohocrmDeleteTool
    tools.append(ZohocrmDeleteTool())
    from .get import ZohocrmGetTool
    tools.append(ZohocrmGetTool())
    from .getall import ZohocrmGetallTool
    tools.append(ZohocrmGetallTool())
    from .update import ZohocrmUpdateTool
    tools.append(ZohocrmUpdateTool())
    from .__custom_api_call__ import Zohocrm__custom_api_call__Tool
    tools.append(Zohocrm__custom_api_call__Tool())
    from .create import ZohocrmCreateTool
    tools.append(ZohocrmCreateTool())
    from .upsert import ZohocrmUpsertTool
    tools.append(ZohocrmUpsertTool())
    from .delete import ZohocrmDeleteTool
    tools.append(ZohocrmDeleteTool())
    from .get import ZohocrmGetTool
    tools.append(ZohocrmGetTool())
    from .getall import ZohocrmGetallTool
    tools.append(ZohocrmGetallTool())
    from .update import ZohocrmUpdateTool
    tools.append(ZohocrmUpdateTool())
    from .__custom_api_call__ import Zohocrm__custom_api_call__Tool
    tools.append(Zohocrm__custom_api_call__Tool())
    from .create import ZohocrmCreateTool
    tools.append(ZohocrmCreateTool())
    from .upsert import ZohocrmUpsertTool
    tools.append(ZohocrmUpsertTool())
    from .delete import ZohocrmDeleteTool
    tools.append(ZohocrmDeleteTool())
    from .get import ZohocrmGetTool
    tools.append(ZohocrmGetTool())
    from .getall import ZohocrmGetallTool
    tools.append(ZohocrmGetallTool())
    from .update import ZohocrmUpdateTool
    tools.append(ZohocrmUpdateTool())
    from .__custom_api_call__ import Zohocrm__custom_api_call__Tool
    tools.append(Zohocrm__custom_api_call__Tool())
    from .create import ZohocrmCreateTool
    tools.append(ZohocrmCreateTool())
    from .upsert import ZohocrmUpsertTool
    tools.append(ZohocrmUpsertTool())
    from .delete import ZohocrmDeleteTool
    tools.append(ZohocrmDeleteTool())
    from .get import ZohocrmGetTool
    tools.append(ZohocrmGetTool())
    from .getfields import ZohocrmGetfieldsTool
    tools.append(ZohocrmGetfieldsTool())
    from .getall import ZohocrmGetallTool
    tools.append(ZohocrmGetallTool())
    from .update import ZohocrmUpdateTool
    tools.append(ZohocrmUpdateTool())
    from .__custom_api_call__ import Zohocrm__custom_api_call__Tool
    tools.append(Zohocrm__custom_api_call__Tool())
    from .create import ZohocrmCreateTool
    tools.append(ZohocrmCreateTool())
    from .upsert import ZohocrmUpsertTool
    tools.append(ZohocrmUpsertTool())
    from .delete import ZohocrmDeleteTool
    tools.append(ZohocrmDeleteTool())
    from .get import ZohocrmGetTool
    tools.append(ZohocrmGetTool())
    from .getall import ZohocrmGetallTool
    tools.append(ZohocrmGetallTool())
    from .update import ZohocrmUpdateTool
    tools.append(ZohocrmUpdateTool())
    from .__custom_api_call__ import Zohocrm__custom_api_call__Tool
    tools.append(Zohocrm__custom_api_call__Tool())
    from .create import ZohocrmCreateTool
    tools.append(ZohocrmCreateTool())
    from .upsert import ZohocrmUpsertTool
    tools.append(ZohocrmUpsertTool())
    from .delete import ZohocrmDeleteTool
    tools.append(ZohocrmDeleteTool())
    from .get import ZohocrmGetTool
    tools.append(ZohocrmGetTool())
    from .getall import ZohocrmGetallTool
    tools.append(ZohocrmGetallTool())
    from .update import ZohocrmUpdateTool
    tools.append(ZohocrmUpdateTool())
    from .__custom_api_call__ import Zohocrm__custom_api_call__Tool
    tools.append(Zohocrm__custom_api_call__Tool())
    from .create import ZohocrmCreateTool
    tools.append(ZohocrmCreateTool())
    from .upsert import ZohocrmUpsertTool
    tools.append(ZohocrmUpsertTool())
    from .delete import ZohocrmDeleteTool
    tools.append(ZohocrmDeleteTool())
    from .get import ZohocrmGetTool
    tools.append(ZohocrmGetTool())
    from .getall import ZohocrmGetallTool
    tools.append(ZohocrmGetallTool())
    from .update import ZohocrmUpdateTool
    tools.append(ZohocrmUpdateTool())
    from .__custom_api_call__ import Zohocrm__custom_api_call__Tool
    tools.append(Zohocrm__custom_api_call__Tool())
    from .create import ZohocrmCreateTool
    tools.append(ZohocrmCreateTool())
    from .upsert import ZohocrmUpsertTool
    tools.append(ZohocrmUpsertTool())
    from .delete import ZohocrmDeleteTool
    tools.append(ZohocrmDeleteTool())
    from .get import ZohocrmGetTool
    tools.append(ZohocrmGetTool())
    from .getall import ZohocrmGetallTool
    tools.append(ZohocrmGetallTool())
    from .update import ZohocrmUpdateTool
    tools.append(ZohocrmUpdateTool())
    from .__custom_api_call__ import Zohocrm__custom_api_call__Tool
    tools.append(Zohocrm__custom_api_call__Tool())
    from .create import ZohocrmCreateTool
    tools.append(ZohocrmCreateTool())
    from .upsert import ZohocrmUpsertTool
    tools.append(ZohocrmUpsertTool())
    from .delete import ZohocrmDeleteTool
    tools.append(ZohocrmDeleteTool())
    from .get import ZohocrmGetTool
    tools.append(ZohocrmGetTool())
    from .getall import ZohocrmGetallTool
    tools.append(ZohocrmGetallTool())
    from .update import ZohocrmUpdateTool
    tools.append(ZohocrmUpdateTool())
    from .__custom_api_call__ import Zohocrm__custom_api_call__Tool
    tools.append(Zohocrm__custom_api_call__Tool())
    return tools
