# crowdDev operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import CrowddevCredentials

def get_tools() -> List[BaseTool]:
    """Get all crowdDev operation tools."""
    tools = []
    from .createwithmember import CrowddevCreatewithmemberTool
    tools.append(CrowddevCreatewithmemberTool())
    from .createformember import CrowddevCreateformemberTool
    tools.append(CrowddevCreateformemberTool())
    from .__custom_api_call__ import Crowddev__custom_api_call__Tool
    tools.append(Crowddev__custom_api_call__Tool())
    from .createorupdate import CrowddevCreateorupdateTool
    tools.append(CrowddevCreateorupdateTool())
    from .delete import CrowddevDeleteTool
    tools.append(CrowddevDeleteTool())
    from .find import CrowddevFindTool
    tools.append(CrowddevFindTool())
    from .update import CrowddevUpdateTool
    tools.append(CrowddevUpdateTool())
    from .__custom_api_call__ import Crowddev__custom_api_call__Tool
    tools.append(Crowddev__custom_api_call__Tool())
    from .create import CrowddevCreateTool
    tools.append(CrowddevCreateTool())
    from .delete import CrowddevDeleteTool
    tools.append(CrowddevDeleteTool())
    from .find import CrowddevFindTool
    tools.append(CrowddevFindTool())
    from .update import CrowddevUpdateTool
    tools.append(CrowddevUpdateTool())
    from .__custom_api_call__ import Crowddev__custom_api_call__Tool
    tools.append(Crowddev__custom_api_call__Tool())
    from .create import CrowddevCreateTool
    tools.append(CrowddevCreateTool())
    from .delete import CrowddevDeleteTool
    tools.append(CrowddevDeleteTool())
    from .find import CrowddevFindTool
    tools.append(CrowddevFindTool())
    from .update import CrowddevUpdateTool
    tools.append(CrowddevUpdateTool())
    from .__custom_api_call__ import Crowddev__custom_api_call__Tool
    tools.append(Crowddev__custom_api_call__Tool())
    from .create import CrowddevCreateTool
    tools.append(CrowddevCreateTool())
    from .delete import CrowddevDeleteTool
    tools.append(CrowddevDeleteTool())
    from .find import CrowddevFindTool
    tools.append(CrowddevFindTool())
    from .update import CrowddevUpdateTool
    tools.append(CrowddevUpdateTool())
    from .__custom_api_call__ import Crowddev__custom_api_call__Tool
    tools.append(Crowddev__custom_api_call__Tool())
    from .create import CrowddevCreateTool
    tools.append(CrowddevCreateTool())
    from .destroy import CrowddevDestroyTool
    tools.append(CrowddevDestroyTool())
    from .find import CrowddevFindTool
    tools.append(CrowddevFindTool())
    from .list import CrowddevListTool
    tools.append(CrowddevListTool())
    from .update import CrowddevUpdateTool
    tools.append(CrowddevUpdateTool())
    from .__custom_api_call__ import Crowddev__custom_api_call__Tool
    tools.append(Crowddev__custom_api_call__Tool())
    return tools
