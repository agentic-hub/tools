# quickbooks operations
from typing import List
from langchain.tools import BaseTool
from .. import QuickbooksCredentials

def get_tools() -> List[BaseTool]:
    """Get all quickbooks operation tools."""
    tools = []
    from .create import QuickbooksCreateTool
    tools.append(QuickbooksCreateTool())
    from .delete import QuickbooksDeleteTool
    tools.append(QuickbooksDeleteTool())
    from .get import QuickbooksGetTool
    tools.append(QuickbooksGetTool())
    from .getall import QuickbooksGetallTool
    tools.append(QuickbooksGetallTool())
    from .update import QuickbooksUpdateTool
    tools.append(QuickbooksUpdateTool())
    from .__custom_api_call__ import Quickbooks__custom_api_call__Tool
    tools.append(Quickbooks__custom_api_call__Tool())
    from .create import QuickbooksCreateTool
    tools.append(QuickbooksCreateTool())
    from .get import QuickbooksGetTool
    tools.append(QuickbooksGetTool())
    from .getall import QuickbooksGetallTool
    tools.append(QuickbooksGetallTool())
    from .update import QuickbooksUpdateTool
    tools.append(QuickbooksUpdateTool())
    from .__custom_api_call__ import Quickbooks__custom_api_call__Tool
    tools.append(Quickbooks__custom_api_call__Tool())
    from .create import QuickbooksCreateTool
    tools.append(QuickbooksCreateTool())
    from .get import QuickbooksGetTool
    tools.append(QuickbooksGetTool())
    from .getall import QuickbooksGetallTool
    tools.append(QuickbooksGetallTool())
    from .update import QuickbooksUpdateTool
    tools.append(QuickbooksUpdateTool())
    from .__custom_api_call__ import Quickbooks__custom_api_call__Tool
    tools.append(Quickbooks__custom_api_call__Tool())
    from .create import QuickbooksCreateTool
    tools.append(QuickbooksCreateTool())
    from .delete import QuickbooksDeleteTool
    tools.append(QuickbooksDeleteTool())
    from .get import QuickbooksGetTool
    tools.append(QuickbooksGetTool())
    from .getall import QuickbooksGetallTool
    tools.append(QuickbooksGetallTool())
    from .send import QuickbooksSendTool
    tools.append(QuickbooksSendTool())
    from .update import QuickbooksUpdateTool
    tools.append(QuickbooksUpdateTool())
    from .__custom_api_call__ import Quickbooks__custom_api_call__Tool
    tools.append(Quickbooks__custom_api_call__Tool())
    from .create import QuickbooksCreateTool
    tools.append(QuickbooksCreateTool())
    from .delete import QuickbooksDeleteTool
    tools.append(QuickbooksDeleteTool())
    from .get import QuickbooksGetTool
    tools.append(QuickbooksGetTool())
    from .getall import QuickbooksGetallTool
    tools.append(QuickbooksGetallTool())
    from .send import QuickbooksSendTool
    tools.append(QuickbooksSendTool())
    from .update import QuickbooksUpdateTool
    tools.append(QuickbooksUpdateTool())
    from .void import QuickbooksVoidTool
    tools.append(QuickbooksVoidTool())
    from .__custom_api_call__ import Quickbooks__custom_api_call__Tool
    tools.append(Quickbooks__custom_api_call__Tool())
    from .get import QuickbooksGetTool
    tools.append(QuickbooksGetTool())
    from .getall import QuickbooksGetallTool
    tools.append(QuickbooksGetallTool())
    from .__custom_api_call__ import Quickbooks__custom_api_call__Tool
    tools.append(Quickbooks__custom_api_call__Tool())
    from .create import QuickbooksCreateTool
    tools.append(QuickbooksCreateTool())
    from .delete import QuickbooksDeleteTool
    tools.append(QuickbooksDeleteTool())
    from .get import QuickbooksGetTool
    tools.append(QuickbooksGetTool())
    from .getall import QuickbooksGetallTool
    tools.append(QuickbooksGetallTool())
    from .send import QuickbooksSendTool
    tools.append(QuickbooksSendTool())
    from .update import QuickbooksUpdateTool
    tools.append(QuickbooksUpdateTool())
    from .void import QuickbooksVoidTool
    tools.append(QuickbooksVoidTool())
    from .__custom_api_call__ import Quickbooks__custom_api_call__Tool
    tools.append(Quickbooks__custom_api_call__Tool())
    from .get import QuickbooksGetTool
    tools.append(QuickbooksGetTool())
    from .getall import QuickbooksGetallTool
    tools.append(QuickbooksGetallTool())
    from .__custom_api_call__ import Quickbooks__custom_api_call__Tool
    tools.append(Quickbooks__custom_api_call__Tool())
    from .getreport import QuickbooksGetreportTool
    tools.append(QuickbooksGetreportTool())
    from .__custom_api_call__ import Quickbooks__custom_api_call__Tool
    tools.append(Quickbooks__custom_api_call__Tool())
    from .create import QuickbooksCreateTool
    tools.append(QuickbooksCreateTool())
    from .get import QuickbooksGetTool
    tools.append(QuickbooksGetTool())
    from .getall import QuickbooksGetallTool
    tools.append(QuickbooksGetallTool())
    from .update import QuickbooksUpdateTool
    tools.append(QuickbooksUpdateTool())
    from .__custom_api_call__ import Quickbooks__custom_api_call__Tool
    tools.append(Quickbooks__custom_api_call__Tool())
    return tools
