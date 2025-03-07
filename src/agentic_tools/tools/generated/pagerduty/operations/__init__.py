# pagerDuty operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import PagerdutyCredentials

def get_tools() -> List[BaseTool]:
    """Get all pagerDuty operation tools."""
    tools = []
    from .create import PagerdutyCreateTool
    tools.append(PagerdutyCreateTool())
    from .get import PagerdutyGetTool
    tools.append(PagerdutyGetTool())
    from .getall import PagerdutyGetallTool
    tools.append(PagerdutyGetallTool())
    from .update import PagerdutyUpdateTool
    tools.append(PagerdutyUpdateTool())
    from .__custom_api_call__ import Pagerduty__custom_api_call__Tool
    tools.append(Pagerduty__custom_api_call__Tool())
    from .create import PagerdutyCreateTool
    tools.append(PagerdutyCreateTool())
    from .getall import PagerdutyGetallTool
    tools.append(PagerdutyGetallTool())
    from .__custom_api_call__ import Pagerduty__custom_api_call__Tool
    tools.append(Pagerduty__custom_api_call__Tool())
    from .get import PagerdutyGetTool
    tools.append(PagerdutyGetTool())
    from .getall import PagerdutyGetallTool
    tools.append(PagerdutyGetallTool())
    from .__custom_api_call__ import Pagerduty__custom_api_call__Tool
    tools.append(Pagerduty__custom_api_call__Tool())
    from .get import PagerdutyGetTool
    tools.append(PagerdutyGetTool())
    from .__custom_api_call__ import Pagerduty__custom_api_call__Tool
    tools.append(Pagerduty__custom_api_call__Tool())
    return tools
