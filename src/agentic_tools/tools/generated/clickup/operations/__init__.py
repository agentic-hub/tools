# clickUp operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all clickUp operation tools."""
    tools = []
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .update import ClickupUpdateTool
    tools.append(ClickupUpdateTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .update import ClickupUpdateTool
    tools.append(ClickupUpdateTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .getall import ClickupGetallTool
    tools.append(ClickupGetallTool())
    from .update import ClickupUpdateTool
    tools.append(ClickupUpdateTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .get import ClickupGetTool
    tools.append(ClickupGetTool())
    from .getall import ClickupGetallTool
    tools.append(ClickupGetallTool())
    from .update import ClickupUpdateTool
    tools.append(ClickupUpdateTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .get import ClickupGetTool
    tools.append(ClickupGetTool())
    from .getall import ClickupGetallTool
    tools.append(ClickupGetallTool())
    from .update import ClickupUpdateTool
    tools.append(ClickupUpdateTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .update import ClickupUpdateTool
    tools.append(ClickupUpdateTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .add import ClickupAddTool
    tools.append(ClickupAddTool())
    from .remove import ClickupRemoveTool
    tools.append(ClickupRemoveTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .add import ClickupAddTool
    tools.append(ClickupAddTool())
    from .remove import ClickupRemoveTool
    tools.append(ClickupRemoveTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .getall import ClickupGetallTool
    tools.append(ClickupGetallTool())
    from .update import ClickupUpdateTool
    tools.append(ClickupUpdateTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .get import ClickupGetTool
    tools.append(ClickupGetTool())
    from .getall import ClickupGetallTool
    tools.append(ClickupGetallTool())
    from .member import ClickupMemberTool
    tools.append(ClickupMemberTool())
    from .setcustomfield import ClickupSetcustomfieldTool
    tools.append(ClickupSetcustomfieldTool())
    from .update import ClickupUpdateTool
    tools.append(ClickupUpdateTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .get import ClickupGetTool
    tools.append(ClickupGetTool())
    from .getall import ClickupGetallTool
    tools.append(ClickupGetallTool())
    from .start import ClickupStartTool
    tools.append(ClickupStartTool())
    from .stop import ClickupStopTool
    tools.append(ClickupStopTool())
    from .update import ClickupUpdateTool
    tools.append(ClickupUpdateTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .add import ClickupAddTool
    tools.append(ClickupAddTool())
    from .getall import ClickupGetallTool
    tools.append(ClickupGetallTool())
    from .remove import ClickupRemoveTool
    tools.append(ClickupRemoveTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    from .create import ClickupCreateTool
    tools.append(ClickupCreateTool())
    from .customfields import ClickupCustomfieldsTool
    tools.append(ClickupCustomfieldsTool())
    from .delete import ClickupDeleteTool
    tools.append(ClickupDeleteTool())
    from .get import ClickupGetTool
    tools.append(ClickupGetTool())
    from .getall import ClickupGetallTool
    tools.append(ClickupGetallTool())
    from .member import ClickupMemberTool
    tools.append(ClickupMemberTool())
    from .update import ClickupUpdateTool
    tools.append(ClickupUpdateTool())
    from .__custom_api_call__ import Clickup__custom_api_call__Tool
    tools.append(Clickup__custom_api_call__Tool())
    return tools
