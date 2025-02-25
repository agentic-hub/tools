# trello operations
from typing import List
from langchain.tools import BaseTool
from .. import TrelloCredentials

def get_tools() -> List[BaseTool]:
    """Get all trello operation tools."""
    tools = []
    from .create import TrelloCreateTool
    tools.append(TrelloCreateTool())
    from .delete import TrelloDeleteTool
    tools.append(TrelloDeleteTool())
    from .get import TrelloGetTool
    tools.append(TrelloGetTool())
    from .getall import TrelloGetallTool
    tools.append(TrelloGetallTool())
    from .__custom_api_call__ import Trello__custom_api_call__Tool
    tools.append(Trello__custom_api_call__Tool())
    from .create import TrelloCreateTool
    tools.append(TrelloCreateTool())
    from .delete import TrelloDeleteTool
    tools.append(TrelloDeleteTool())
    from .get import TrelloGetTool
    tools.append(TrelloGetTool())
    from .update import TrelloUpdateTool
    tools.append(TrelloUpdateTool())
    from .__custom_api_call__ import Trello__custom_api_call__Tool
    tools.append(Trello__custom_api_call__Tool())
    from .add import TrelloAddTool
    tools.append(TrelloAddTool())
    from .getall import TrelloGetallTool
    tools.append(TrelloGetallTool())
    from .invite import TrelloInviteTool
    tools.append(TrelloInviteTool())
    from .remove import TrelloRemoveTool
    tools.append(TrelloRemoveTool())
    from .__custom_api_call__ import Trello__custom_api_call__Tool
    tools.append(Trello__custom_api_call__Tool())
    from .create import TrelloCreateTool
    tools.append(TrelloCreateTool())
    from .delete import TrelloDeleteTool
    tools.append(TrelloDeleteTool())
    from .get import TrelloGetTool
    tools.append(TrelloGetTool())
    from .update import TrelloUpdateTool
    tools.append(TrelloUpdateTool())
    from .__custom_api_call__ import Trello__custom_api_call__Tool
    tools.append(Trello__custom_api_call__Tool())
    from .create import TrelloCreateTool
    tools.append(TrelloCreateTool())
    from .delete import TrelloDeleteTool
    tools.append(TrelloDeleteTool())
    from .update import TrelloUpdateTool
    tools.append(TrelloUpdateTool())
    from .__custom_api_call__ import Trello__custom_api_call__Tool
    tools.append(Trello__custom_api_call__Tool())
    from .create import TrelloCreateTool
    tools.append(TrelloCreateTool())
    from .createcheckitem import TrelloCreatecheckitemTool
    tools.append(TrelloCreatecheckitemTool())
    from .delete import TrelloDeleteTool
    tools.append(TrelloDeleteTool())
    from .deletecheckitem import TrelloDeletecheckitemTool
    tools.append(TrelloDeletecheckitemTool())
    from .get import TrelloGetTool
    tools.append(TrelloGetTool())
    from .getcheckitem import TrelloGetcheckitemTool
    tools.append(TrelloGetcheckitemTool())
    from .completedcheckitems import TrelloCompletedcheckitemsTool
    tools.append(TrelloCompletedcheckitemsTool())
    from .getall import TrelloGetallTool
    tools.append(TrelloGetallTool())
    from .updatecheckitem import TrelloUpdatecheckitemTool
    tools.append(TrelloUpdatecheckitemTool())
    from .__custom_api_call__ import Trello__custom_api_call__Tool
    tools.append(Trello__custom_api_call__Tool())
    from .addlabel import TrelloAddlabelTool
    tools.append(TrelloAddlabelTool())
    from .create import TrelloCreateTool
    tools.append(TrelloCreateTool())
    from .delete import TrelloDeleteTool
    tools.append(TrelloDeleteTool())
    from .get import TrelloGetTool
    tools.append(TrelloGetTool())
    from .getall import TrelloGetallTool
    tools.append(TrelloGetallTool())
    from .removelabel import TrelloRemovelabelTool
    tools.append(TrelloRemovelabelTool())
    from .update import TrelloUpdateTool
    tools.append(TrelloUpdateTool())
    from .__custom_api_call__ import Trello__custom_api_call__Tool
    tools.append(Trello__custom_api_call__Tool())
    from .archive import TrelloArchiveTool
    tools.append(TrelloArchiveTool())
    from .create import TrelloCreateTool
    tools.append(TrelloCreateTool())
    from .get import TrelloGetTool
    tools.append(TrelloGetTool())
    from .getcards import TrelloGetcardsTool
    tools.append(TrelloGetcardsTool())
    from .getall import TrelloGetallTool
    tools.append(TrelloGetallTool())
    from .update import TrelloUpdateTool
    tools.append(TrelloUpdateTool())
    from .__custom_api_call__ import Trello__custom_api_call__Tool
    tools.append(Trello__custom_api_call__Tool())
    return tools
