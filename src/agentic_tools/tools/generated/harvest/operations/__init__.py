# harvest operations
from typing import List
from langchain.tools import BaseTool
from .. import HarvestCredentials

def get_tools() -> List[BaseTool]:
    """Get all harvest operation tools."""
    tools = []
    from .create import HarvestCreateTool
    tools.append(HarvestCreateTool())
    from .delete import HarvestDeleteTool
    tools.append(HarvestDeleteTool())
    from .get import HarvestGetTool
    tools.append(HarvestGetTool())
    from .getall import HarvestGetallTool
    tools.append(HarvestGetallTool())
    from .update import HarvestUpdateTool
    tools.append(HarvestUpdateTool())
    from .__custom_api_call__ import Harvest__custom_api_call__Tool
    tools.append(Harvest__custom_api_call__Tool())
    from .get import HarvestGetTool
    tools.append(HarvestGetTool())
    from .__custom_api_call__ import Harvest__custom_api_call__Tool
    tools.append(Harvest__custom_api_call__Tool())
    from .create import HarvestCreateTool
    tools.append(HarvestCreateTool())
    from .delete import HarvestDeleteTool
    tools.append(HarvestDeleteTool())
    from .get import HarvestGetTool
    tools.append(HarvestGetTool())
    from .getall import HarvestGetallTool
    tools.append(HarvestGetallTool())
    from .update import HarvestUpdateTool
    tools.append(HarvestUpdateTool())
    from .__custom_api_call__ import Harvest__custom_api_call__Tool
    tools.append(Harvest__custom_api_call__Tool())
    from .create import HarvestCreateTool
    tools.append(HarvestCreateTool())
    from .delete import HarvestDeleteTool
    tools.append(HarvestDeleteTool())
    from .get import HarvestGetTool
    tools.append(HarvestGetTool())
    from .getall import HarvestGetallTool
    tools.append(HarvestGetallTool())
    from .update import HarvestUpdateTool
    tools.append(HarvestUpdateTool())
    from .__custom_api_call__ import Harvest__custom_api_call__Tool
    tools.append(Harvest__custom_api_call__Tool())
    from .create import HarvestCreateTool
    tools.append(HarvestCreateTool())
    from .delete import HarvestDeleteTool
    tools.append(HarvestDeleteTool())
    from .get import HarvestGetTool
    tools.append(HarvestGetTool())
    from .getall import HarvestGetallTool
    tools.append(HarvestGetallTool())
    from .update import HarvestUpdateTool
    tools.append(HarvestUpdateTool())
    from .__custom_api_call__ import Harvest__custom_api_call__Tool
    tools.append(Harvest__custom_api_call__Tool())
    from .create import HarvestCreateTool
    tools.append(HarvestCreateTool())
    from .delete import HarvestDeleteTool
    tools.append(HarvestDeleteTool())
    from .get import HarvestGetTool
    tools.append(HarvestGetTool())
    from .getall import HarvestGetallTool
    tools.append(HarvestGetallTool())
    from .update import HarvestUpdateTool
    tools.append(HarvestUpdateTool())
    from .__custom_api_call__ import Harvest__custom_api_call__Tool
    tools.append(Harvest__custom_api_call__Tool())
    from .create import HarvestCreateTool
    tools.append(HarvestCreateTool())
    from .delete import HarvestDeleteTool
    tools.append(HarvestDeleteTool())
    from .get import HarvestGetTool
    tools.append(HarvestGetTool())
    from .getall import HarvestGetallTool
    tools.append(HarvestGetallTool())
    from .update import HarvestUpdateTool
    tools.append(HarvestUpdateTool())
    from .__custom_api_call__ import Harvest__custom_api_call__Tool
    tools.append(Harvest__custom_api_call__Tool())
    from .create import HarvestCreateTool
    tools.append(HarvestCreateTool())
    from .delete import HarvestDeleteTool
    tools.append(HarvestDeleteTool())
    from .get import HarvestGetTool
    tools.append(HarvestGetTool())
    from .getall import HarvestGetallTool
    tools.append(HarvestGetallTool())
    from .update import HarvestUpdateTool
    tools.append(HarvestUpdateTool())
    from .__custom_api_call__ import Harvest__custom_api_call__Tool
    tools.append(Harvest__custom_api_call__Tool())
    from .createbyduration import HarvestCreatebydurationTool
    tools.append(HarvestCreatebydurationTool())
    from .createbystartend import HarvestCreatebystartendTool
    tools.append(HarvestCreatebystartendTool())
    from .delete import HarvestDeleteTool
    tools.append(HarvestDeleteTool())
    from .deleteexternal import HarvestDeleteexternalTool
    tools.append(HarvestDeleteexternalTool())
    from .get import HarvestGetTool
    tools.append(HarvestGetTool())
    from .getall import HarvestGetallTool
    tools.append(HarvestGetallTool())
    from .restarttime import HarvestRestarttimeTool
    tools.append(HarvestRestarttimeTool())
    from .stoptime import HarvestStoptimeTool
    tools.append(HarvestStoptimeTool())
    from .update import HarvestUpdateTool
    tools.append(HarvestUpdateTool())
    from .__custom_api_call__ import Harvest__custom_api_call__Tool
    tools.append(Harvest__custom_api_call__Tool())
    from .create import HarvestCreateTool
    tools.append(HarvestCreateTool())
    from .delete import HarvestDeleteTool
    tools.append(HarvestDeleteTool())
    from .get import HarvestGetTool
    tools.append(HarvestGetTool())
    from .getall import HarvestGetallTool
    tools.append(HarvestGetallTool())
    from .me import HarvestMeTool
    tools.append(HarvestMeTool())
    from .update import HarvestUpdateTool
    tools.append(HarvestUpdateTool())
    from .__custom_api_call__ import Harvest__custom_api_call__Tool
    tools.append(Harvest__custom_api_call__Tool())
    return tools
