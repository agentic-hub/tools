# goToWebinar operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all goToWebinar operation tools."""
    tools = []
    from .get import GotowebinarGetTool
    tools.append(GotowebinarGetTool())
    from .getall import GotowebinarGetallTool
    tools.append(GotowebinarGetallTool())
    from .getdetails import GotowebinarGetdetailsTool
    tools.append(GotowebinarGetdetailsTool())
    from .__custom_api_call__ import Gotowebinar__custom_api_call__Tool
    tools.append(Gotowebinar__custom_api_call__Tool())
    from .create import GotowebinarCreateTool
    tools.append(GotowebinarCreateTool())
    from .delete import GotowebinarDeleteTool
    tools.append(GotowebinarDeleteTool())
    from .getall import GotowebinarGetallTool
    tools.append(GotowebinarGetallTool())
    from .reinvite import GotowebinarReinviteTool
    tools.append(GotowebinarReinviteTool())
    from .__custom_api_call__ import Gotowebinar__custom_api_call__Tool
    tools.append(Gotowebinar__custom_api_call__Tool())
    from .create import GotowebinarCreateTool
    tools.append(GotowebinarCreateTool())
    from .delete import GotowebinarDeleteTool
    tools.append(GotowebinarDeleteTool())
    from .getall import GotowebinarGetallTool
    tools.append(GotowebinarGetallTool())
    from .reinvite import GotowebinarReinviteTool
    tools.append(GotowebinarReinviteTool())
    from .__custom_api_call__ import Gotowebinar__custom_api_call__Tool
    tools.append(Gotowebinar__custom_api_call__Tool())
    from .create import GotowebinarCreateTool
    tools.append(GotowebinarCreateTool())
    from .delete import GotowebinarDeleteTool
    tools.append(GotowebinarDeleteTool())
    from .get import GotowebinarGetTool
    tools.append(GotowebinarGetTool())
    from .getall import GotowebinarGetallTool
    tools.append(GotowebinarGetallTool())
    from .__custom_api_call__ import Gotowebinar__custom_api_call__Tool
    tools.append(Gotowebinar__custom_api_call__Tool())
    from .get import GotowebinarGetTool
    tools.append(GotowebinarGetTool())
    from .getall import GotowebinarGetallTool
    tools.append(GotowebinarGetallTool())
    from .getdetails import GotowebinarGetdetailsTool
    tools.append(GotowebinarGetdetailsTool())
    from .__custom_api_call__ import Gotowebinar__custom_api_call__Tool
    tools.append(Gotowebinar__custom_api_call__Tool())
    from .create import GotowebinarCreateTool
    tools.append(GotowebinarCreateTool())
    from .get import GotowebinarGetTool
    tools.append(GotowebinarGetTool())
    from .getall import GotowebinarGetallTool
    tools.append(GotowebinarGetallTool())
    from .update import GotowebinarUpdateTool
    tools.append(GotowebinarUpdateTool())
    from .__custom_api_call__ import Gotowebinar__custom_api_call__Tool
    tools.append(Gotowebinar__custom_api_call__Tool())
    return tools
