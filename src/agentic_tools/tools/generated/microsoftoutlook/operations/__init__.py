# microsoftOutlook operations
from typing import List
from langchain.tools import BaseTool
from .. import MicrosoftoutlookCredentials

def get_tools() -> List[BaseTool]:
    """Get all microsoftOutlook operation tools."""
    tools = []
    from .create import MicrosoftoutlookCreateTool
    tools.append(MicrosoftoutlookCreateTool())
    from .delete import MicrosoftoutlookDeleteTool
    tools.append(MicrosoftoutlookDeleteTool())
    from .get import MicrosoftoutlookGetTool
    tools.append(MicrosoftoutlookGetTool())
    from .getall import MicrosoftoutlookGetallTool
    tools.append(MicrosoftoutlookGetallTool())
    from .update import MicrosoftoutlookUpdateTool
    tools.append(MicrosoftoutlookUpdateTool())
    from .create import MicrosoftoutlookCreateTool
    tools.append(MicrosoftoutlookCreateTool())
    from .delete import MicrosoftoutlookDeleteTool
    tools.append(MicrosoftoutlookDeleteTool())
    from .get import MicrosoftoutlookGetTool
    tools.append(MicrosoftoutlookGetTool())
    from .getall import MicrosoftoutlookGetallTool
    tools.append(MicrosoftoutlookGetallTool())
    from .update import MicrosoftoutlookUpdateTool
    tools.append(MicrosoftoutlookUpdateTool())
    from .create import MicrosoftoutlookCreateTool
    tools.append(MicrosoftoutlookCreateTool())
    from .delete import MicrosoftoutlookDeleteTool
    tools.append(MicrosoftoutlookDeleteTool())
    from .get import MicrosoftoutlookGetTool
    tools.append(MicrosoftoutlookGetTool())
    from .send import MicrosoftoutlookSendTool
    tools.append(MicrosoftoutlookSendTool())
    from .update import MicrosoftoutlookUpdateTool
    tools.append(MicrosoftoutlookUpdateTool())
    from .create import MicrosoftoutlookCreateTool
    tools.append(MicrosoftoutlookCreateTool())
    from .delete import MicrosoftoutlookDeleteTool
    tools.append(MicrosoftoutlookDeleteTool())
    from .get import MicrosoftoutlookGetTool
    tools.append(MicrosoftoutlookGetTool())
    from .getall import MicrosoftoutlookGetallTool
    tools.append(MicrosoftoutlookGetallTool())
    from .update import MicrosoftoutlookUpdateTool
    tools.append(MicrosoftoutlookUpdateTool())
    from .create import MicrosoftoutlookCreateTool
    tools.append(MicrosoftoutlookCreateTool())
    from .delete import MicrosoftoutlookDeleteTool
    tools.append(MicrosoftoutlookDeleteTool())
    from .get import MicrosoftoutlookGetTool
    tools.append(MicrosoftoutlookGetTool())
    from .getall import MicrosoftoutlookGetallTool
    tools.append(MicrosoftoutlookGetallTool())
    from .update import MicrosoftoutlookUpdateTool
    tools.append(MicrosoftoutlookUpdateTool())
    from .getall import MicrosoftoutlookGetallTool
    tools.append(MicrosoftoutlookGetallTool())
    from .delete import MicrosoftoutlookDeleteTool
    tools.append(MicrosoftoutlookDeleteTool())
    from .get import MicrosoftoutlookGetTool
    tools.append(MicrosoftoutlookGetTool())
    from .getall import MicrosoftoutlookGetallTool
    tools.append(MicrosoftoutlookGetallTool())
    from .move import MicrosoftoutlookMoveTool
    tools.append(MicrosoftoutlookMoveTool())
    from .reply import MicrosoftoutlookReplyTool
    tools.append(MicrosoftoutlookReplyTool())
    from .send import MicrosoftoutlookSendTool
    tools.append(MicrosoftoutlookSendTool())
    from .update import MicrosoftoutlookUpdateTool
    tools.append(MicrosoftoutlookUpdateTool())
    from .add import MicrosoftoutlookAddTool
    tools.append(MicrosoftoutlookAddTool())
    from .download import MicrosoftoutlookDownloadTool
    tools.append(MicrosoftoutlookDownloadTool())
    from .get import MicrosoftoutlookGetTool
    tools.append(MicrosoftoutlookGetTool())
    from .getall import MicrosoftoutlookGetallTool
    tools.append(MicrosoftoutlookGetallTool())
    return tools
