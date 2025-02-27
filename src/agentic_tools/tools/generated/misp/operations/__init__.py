# misp operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MispCredentials

def get_tools() -> List[BaseTool]:
    """Get all misp operation tools."""
    tools = []
    from .create import MispCreateTool
    tools.append(MispCreateTool())
    from .delete import MispDeleteTool
    tools.append(MispDeleteTool())
    from .get import MispGetTool
    tools.append(MispGetTool())
    from .getall import MispGetallTool
    tools.append(MispGetallTool())
    from .update import MispUpdateTool
    tools.append(MispUpdateTool())
    from .__custom_api_call__ import Misp__custom_api_call__Tool
    tools.append(Misp__custom_api_call__Tool())
    from .create import MispCreateTool
    tools.append(MispCreateTool())
    from .delete import MispDeleteTool
    tools.append(MispDeleteTool())
    from .get import MispGetTool
    tools.append(MispGetTool())
    from .getall import MispGetallTool
    tools.append(MispGetallTool())
    from .publish import MispPublishTool
    tools.append(MispPublishTool())
    from .unpublish import MispUnpublishTool
    tools.append(MispUnpublishTool())
    from .update import MispUpdateTool
    tools.append(MispUpdateTool())
    from .__custom_api_call__ import Misp__custom_api_call__Tool
    tools.append(Misp__custom_api_call__Tool())
    from .add import MispAddTool
    tools.append(MispAddTool())
    from .remove import MispRemoveTool
    tools.append(MispRemoveTool())
    from .__custom_api_call__ import Misp__custom_api_call__Tool
    tools.append(Misp__custom_api_call__Tool())
    from .create import MispCreateTool
    tools.append(MispCreateTool())
    from .disable import MispDisableTool
    tools.append(MispDisableTool())
    from .enable import MispEnableTool
    tools.append(MispEnableTool())
    from .get import MispGetTool
    tools.append(MispGetTool())
    from .getall import MispGetallTool
    tools.append(MispGetallTool())
    from .update import MispUpdateTool
    tools.append(MispUpdateTool())
    from .__custom_api_call__ import Misp__custom_api_call__Tool
    tools.append(Misp__custom_api_call__Tool())
    from .delete import MispDeleteTool
    tools.append(MispDeleteTool())
    from .get import MispGetTool
    tools.append(MispGetTool())
    from .getall import MispGetallTool
    tools.append(MispGetallTool())
    from .__custom_api_call__ import Misp__custom_api_call__Tool
    tools.append(Misp__custom_api_call__Tool())
    from .get import MispGetTool
    tools.append(MispGetTool())
    from .getall import MispGetallTool
    tools.append(MispGetallTool())
    from .__custom_api_call__ import Misp__custom_api_call__Tool
    tools.append(Misp__custom_api_call__Tool())
    from .create import MispCreateTool
    tools.append(MispCreateTool())
    from .delete import MispDeleteTool
    tools.append(MispDeleteTool())
    from .get import MispGetTool
    tools.append(MispGetTool())
    from .getall import MispGetallTool
    tools.append(MispGetallTool())
    from .update import MispUpdateTool
    tools.append(MispUpdateTool())
    from .__custom_api_call__ import Misp__custom_api_call__Tool
    tools.append(Misp__custom_api_call__Tool())
    from .create import MispCreateTool
    tools.append(MispCreateTool())
    from .delete import MispDeleteTool
    tools.append(MispDeleteTool())
    from .getall import MispGetallTool
    tools.append(MispGetallTool())
    from .update import MispUpdateTool
    tools.append(MispUpdateTool())
    from .__custom_api_call__ import Misp__custom_api_call__Tool
    tools.append(Misp__custom_api_call__Tool())
    from .create import MispCreateTool
    tools.append(MispCreateTool())
    from .delete import MispDeleteTool
    tools.append(MispDeleteTool())
    from .get import MispGetTool
    tools.append(MispGetTool())
    from .getall import MispGetallTool
    tools.append(MispGetallTool())
    from .update import MispUpdateTool
    tools.append(MispUpdateTool())
    from .__custom_api_call__ import Misp__custom_api_call__Tool
    tools.append(Misp__custom_api_call__Tool())
    from .get import MispGetTool
    tools.append(MispGetTool())
    from .getall import MispGetallTool
    tools.append(MispGetallTool())
    from .__custom_api_call__ import Misp__custom_api_call__Tool
    tools.append(Misp__custom_api_call__Tool())
    return tools
