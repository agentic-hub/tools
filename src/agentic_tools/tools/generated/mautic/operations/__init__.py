# mautic operations
from typing import List
from langchain.tools import BaseTool
from .. import MauticCredentials

def get_tools() -> List[BaseTool]:
    """Get all mautic operation tools."""
    tools = []
    from .create import MauticCreateTool
    tools.append(MauticCreateTool())
    from .delete import MauticDeleteTool
    tools.append(MauticDeleteTool())
    from .get import MauticGetTool
    tools.append(MauticGetTool())
    from .getall import MauticGetallTool
    tools.append(MauticGetallTool())
    from .update import MauticUpdateTool
    tools.append(MauticUpdateTool())
    from .__custom_api_call__ import Mautic__custom_api_call__Tool
    tools.append(Mautic__custom_api_call__Tool())
    from .create import MauticCreateTool
    tools.append(MauticCreateTool())
    from .delete import MauticDeleteTool
    tools.append(MauticDeleteTool())
    from .editcontactpoint import MauticEditcontactpointTool
    tools.append(MauticEditcontactpointTool())
    from .editdonotcontactlist import MauticEditdonotcontactlistTool
    tools.append(MauticEditdonotcontactlistTool())
    from .get import MauticGetTool
    tools.append(MauticGetTool())
    from .getall import MauticGetallTool
    tools.append(MauticGetallTool())
    from .sendemail import MauticSendemailTool
    tools.append(MauticSendemailTool())
    from .update import MauticUpdateTool
    tools.append(MauticUpdateTool())
    from .__custom_api_call__ import Mautic__custom_api_call__Tool
    tools.append(Mautic__custom_api_call__Tool())
    from .add import MauticAddTool
    tools.append(MauticAddTool())
    from .remove import MauticRemoveTool
    tools.append(MauticRemoveTool())
    from .__custom_api_call__ import Mautic__custom_api_call__Tool
    tools.append(Mautic__custom_api_call__Tool())
    from .add import MauticAddTool
    tools.append(MauticAddTool())
    from .remove import MauticRemoveTool
    tools.append(MauticRemoveTool())
    from .__custom_api_call__ import Mautic__custom_api_call__Tool
    tools.append(Mautic__custom_api_call__Tool())
    from .add import MauticAddTool
    tools.append(MauticAddTool())
    from .remove import MauticRemoveTool
    tools.append(MauticRemoveTool())
    from .__custom_api_call__ import Mautic__custom_api_call__Tool
    tools.append(Mautic__custom_api_call__Tool())
    from .send import MauticSendTool
    tools.append(MauticSendTool())
    from .__custom_api_call__ import Mautic__custom_api_call__Tool
    tools.append(Mautic__custom_api_call__Tool())
    return tools
