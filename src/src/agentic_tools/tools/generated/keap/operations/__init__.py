# keap operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all keap operation tools."""
    tools = []
    from .create import KeapCreateTool
    tools.append(KeapCreateTool())
    from .getall import KeapGetallTool
    tools.append(KeapGetallTool())
    from .__custom_api_call__ import Keap__custom_api_call__Tool
    tools.append(Keap__custom_api_call__Tool())
    from .upsert import KeapUpsertTool
    tools.append(KeapUpsertTool())
    from .delete import KeapDeleteTool
    tools.append(KeapDeleteTool())
    from .get import KeapGetTool
    tools.append(KeapGetTool())
    from .getall import KeapGetallTool
    tools.append(KeapGetallTool())
    from .__custom_api_call__ import Keap__custom_api_call__Tool
    tools.append(Keap__custom_api_call__Tool())
    from .create import KeapCreateTool
    tools.append(KeapCreateTool())
    from .delete import KeapDeleteTool
    tools.append(KeapDeleteTool())
    from .get import KeapGetTool
    tools.append(KeapGetTool())
    from .getall import KeapGetallTool
    tools.append(KeapGetallTool())
    from .update import KeapUpdateTool
    tools.append(KeapUpdateTool())
    from .__custom_api_call__ import Keap__custom_api_call__Tool
    tools.append(Keap__custom_api_call__Tool())
    from .create import KeapCreateTool
    tools.append(KeapCreateTool())
    from .delete import KeapDeleteTool
    tools.append(KeapDeleteTool())
    from .getall import KeapGetallTool
    tools.append(KeapGetallTool())
    from .__custom_api_call__ import Keap__custom_api_call__Tool
    tools.append(Keap__custom_api_call__Tool())
    from .create import KeapCreateTool
    tools.append(KeapCreateTool())
    from .get import KeapGetTool
    tools.append(KeapGetTool())
    from .delete import KeapDeleteTool
    tools.append(KeapDeleteTool())
    from .getall import KeapGetallTool
    tools.append(KeapGetallTool())
    from .__custom_api_call__ import Keap__custom_api_call__Tool
    tools.append(Keap__custom_api_call__Tool())
    from .create import KeapCreateTool
    tools.append(KeapCreateTool())
    from .delete import KeapDeleteTool
    tools.append(KeapDeleteTool())
    from .get import KeapGetTool
    tools.append(KeapGetTool())
    from .getall import KeapGetallTool
    tools.append(KeapGetallTool())
    from .__custom_api_call__ import Keap__custom_api_call__Tool
    tools.append(Keap__custom_api_call__Tool())
    from .createrecord import KeapCreaterecordTool
    tools.append(KeapCreaterecordTool())
    from .getall import KeapGetallTool
    tools.append(KeapGetallTool())
    from .send import KeapSendTool
    tools.append(KeapSendTool())
    from .__custom_api_call__ import Keap__custom_api_call__Tool
    tools.append(Keap__custom_api_call__Tool())
    from .delete import KeapDeleteTool
    tools.append(KeapDeleteTool())
    from .getall import KeapGetallTool
    tools.append(KeapGetallTool())
    from .upload import KeapUploadTool
    tools.append(KeapUploadTool())
    from .__custom_api_call__ import Keap__custom_api_call__Tool
    tools.append(Keap__custom_api_call__Tool())
    return tools
