# activeCampaign operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all activeCampaign operation tools."""
    tools = []
    from .create import ActivecampaignCreateTool
    tools.append(ActivecampaignCreateTool())
    from .delete import ActivecampaignDeleteTool
    tools.append(ActivecampaignDeleteTool())
    from .get import ActivecampaignGetTool
    tools.append(ActivecampaignGetTool())
    from .getall import ActivecampaignGetallTool
    tools.append(ActivecampaignGetallTool())
    from .update import ActivecampaignUpdateTool
    tools.append(ActivecampaignUpdateTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .create import ActivecampaignCreateTool
    tools.append(ActivecampaignCreateTool())
    from .delete import ActivecampaignDeleteTool
    tools.append(ActivecampaignDeleteTool())
    from .get import ActivecampaignGetTool
    tools.append(ActivecampaignGetTool())
    from .getall import ActivecampaignGetallTool
    tools.append(ActivecampaignGetallTool())
    from .update import ActivecampaignUpdateTool
    tools.append(ActivecampaignUpdateTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .create import ActivecampaignCreateTool
    tools.append(ActivecampaignCreateTool())
    from .delete import ActivecampaignDeleteTool
    tools.append(ActivecampaignDeleteTool())
    from .update import ActivecampaignUpdateTool
    tools.append(ActivecampaignUpdateTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .add import ActivecampaignAddTool
    tools.append(ActivecampaignAddTool())
    from .remove import ActivecampaignRemoveTool
    tools.append(ActivecampaignRemoveTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .add import ActivecampaignAddTool
    tools.append(ActivecampaignAddTool())
    from .remove import ActivecampaignRemoveTool
    tools.append(ActivecampaignRemoveTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .getall import ActivecampaignGetallTool
    tools.append(ActivecampaignGetallTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .create import ActivecampaignCreateTool
    tools.append(ActivecampaignCreateTool())
    from .delete import ActivecampaignDeleteTool
    tools.append(ActivecampaignDeleteTool())
    from .get import ActivecampaignGetTool
    tools.append(ActivecampaignGetTool())
    from .getall import ActivecampaignGetallTool
    tools.append(ActivecampaignGetallTool())
    from .update import ActivecampaignUpdateTool
    tools.append(ActivecampaignUpdateTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .create import ActivecampaignCreateTool
    tools.append(ActivecampaignCreateTool())
    from .createnote import ActivecampaignCreatenoteTool
    tools.append(ActivecampaignCreatenoteTool())
    from .delete import ActivecampaignDeleteTool
    tools.append(ActivecampaignDeleteTool())
    from .get import ActivecampaignGetTool
    tools.append(ActivecampaignGetTool())
    from .getall import ActivecampaignGetallTool
    tools.append(ActivecampaignGetallTool())
    from .update import ActivecampaignUpdateTool
    tools.append(ActivecampaignUpdateTool())
    from .updatenote import ActivecampaignUpdatenoteTool
    tools.append(ActivecampaignUpdatenoteTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .create import ActivecampaignCreateTool
    tools.append(ActivecampaignCreateTool())
    from .delete import ActivecampaignDeleteTool
    tools.append(ActivecampaignDeleteTool())
    from .get import ActivecampaignGetTool
    tools.append(ActivecampaignGetTool())
    from .getall import ActivecampaignGetallTool
    tools.append(ActivecampaignGetallTool())
    from .update import ActivecampaignUpdateTool
    tools.append(ActivecampaignUpdateTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .create import ActivecampaignCreateTool
    tools.append(ActivecampaignCreateTool())
    from .delete import ActivecampaignDeleteTool
    tools.append(ActivecampaignDeleteTool())
    from .get import ActivecampaignGetTool
    tools.append(ActivecampaignGetTool())
    from .getall import ActivecampaignGetallTool
    tools.append(ActivecampaignGetallTool())
    from .update import ActivecampaignUpdateTool
    tools.append(ActivecampaignUpdateTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .create import ActivecampaignCreateTool
    tools.append(ActivecampaignCreateTool())
    from .delete import ActivecampaignDeleteTool
    tools.append(ActivecampaignDeleteTool())
    from .get import ActivecampaignGetTool
    tools.append(ActivecampaignGetTool())
    from .getall import ActivecampaignGetallTool
    tools.append(ActivecampaignGetallTool())
    from .update import ActivecampaignUpdateTool
    tools.append(ActivecampaignUpdateTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    from .getall import ActivecampaignGetallTool
    tools.append(ActivecampaignGetallTool())
    from .getbyproductid import ActivecampaignGetbyproductidTool
    tools.append(ActivecampaignGetbyproductidTool())
    from .getbyorderid import ActivecampaignGetbyorderidTool
    tools.append(ActivecampaignGetbyorderidTool())
    from .__custom_api_call__ import Activecampaign__custom_api_call__Tool
    tools.append(Activecampaign__custom_api_call__Tool())
    return tools
