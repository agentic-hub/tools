# gmail operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GmailCredentials

def get_tools() -> List[BaseTool]:
    """Get all gmail operation tools."""
    tools = []
    from .create import GmailCreateTool
    tools.append(GmailCreateTool())
    from .delete import GmailDeleteTool
    tools.append(GmailDeleteTool())
    from .get import GmailGetTool
    tools.append(GmailGetTool())
    from .getall import GmailGetallTool
    tools.append(GmailGetallTool())
    from .create import GmailCreateTool
    tools.append(GmailCreateTool())
    from .delete import GmailDeleteTool
    tools.append(GmailDeleteTool())
    from .get import GmailGetTool
    tools.append(GmailGetTool())
    from .getall import GmailGetallTool
    tools.append(GmailGetallTool())
    from .addlabels import GmailAddlabelsTool
    tools.append(GmailAddlabelsTool())
    from .delete import GmailDeleteTool
    tools.append(GmailDeleteTool())
    from .get import GmailGetTool
    tools.append(GmailGetTool())
    from .getall import GmailGetallTool
    tools.append(GmailGetallTool())
    from .markasread import GmailMarkasreadTool
    tools.append(GmailMarkasreadTool())
    from .markasunread import GmailMarkasunreadTool
    tools.append(GmailMarkasunreadTool())
    from .removelabels import GmailRemovelabelsTool
    tools.append(GmailRemovelabelsTool())
    from .reply import GmailReplyTool
    tools.append(GmailReplyTool())
    from .send import GmailSendTool
    tools.append(GmailSendTool())
    from .addlabels import GmailAddlabelsTool
    tools.append(GmailAddlabelsTool())
    from .delete import GmailDeleteTool
    tools.append(GmailDeleteTool())
    from .get import GmailGetTool
    tools.append(GmailGetTool())
    from .getall import GmailGetallTool
    tools.append(GmailGetallTool())
    from .removelabels import GmailRemovelabelsTool
    tools.append(GmailRemovelabelsTool())
    from .reply import GmailReplyTool
    tools.append(GmailReplyTool())
    from .trash import GmailTrashTool
    tools.append(GmailTrashTool())
    from .untrash import GmailUntrashTool
    tools.append(GmailUntrashTool())
    return tools
