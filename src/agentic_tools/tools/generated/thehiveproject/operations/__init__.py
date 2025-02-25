# theHiveProject operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all theHiveProject operation tools."""
    tools = []
    from .create import ThehiveprojectCreateTool
    tools.append(ThehiveprojectCreateTool())
    from .deletealert import ThehiveprojectDeletealertTool
    tools.append(ThehiveprojectDeletealertTool())
    from .executeresponder import ThehiveprojectExecuteresponderTool
    tools.append(ThehiveprojectExecuteresponderTool())
    from .get import ThehiveprojectGetTool
    tools.append(ThehiveprojectGetTool())
    from .merge import ThehiveprojectMergeTool
    tools.append(ThehiveprojectMergeTool())
    from .promote import ThehiveprojectPromoteTool
    tools.append(ThehiveprojectPromoteTool())
    from .search import ThehiveprojectSearchTool
    tools.append(ThehiveprojectSearchTool())
    from .update import ThehiveprojectUpdateTool
    tools.append(ThehiveprojectUpdateTool())
    from .status import ThehiveprojectStatusTool
    tools.append(ThehiveprojectStatusTool())
    from .__custom_api_call__ import Thehiveproject__custom_api_call__Tool
    tools.append(Thehiveproject__custom_api_call__Tool())
    from .addattachment import ThehiveprojectAddattachmentTool
    tools.append(ThehiveprojectAddattachmentTool())
    from .create import ThehiveprojectCreateTool
    tools.append(ThehiveprojectCreateTool())
    from .deleteattachment import ThehiveprojectDeleteattachmentTool
    tools.append(ThehiveprojectDeleteattachmentTool())
    from .deletecase import ThehiveprojectDeletecaseTool
    tools.append(ThehiveprojectDeletecaseTool())
    from .executeresponder import ThehiveprojectExecuteresponderTool
    tools.append(ThehiveprojectExecuteresponderTool())
    from .get import ThehiveprojectGetTool
    tools.append(ThehiveprojectGetTool())
    from .getattachment import ThehiveprojectGetattachmentTool
    tools.append(ThehiveprojectGetattachmentTool())
    from .gettimeline import ThehiveprojectGettimelineTool
    tools.append(ThehiveprojectGettimelineTool())
    from .search import ThehiveprojectSearchTool
    tools.append(ThehiveprojectSearchTool())
    from .update import ThehiveprojectUpdateTool
    tools.append(ThehiveprojectUpdateTool())
    from .__custom_api_call__ import Thehiveproject__custom_api_call__Tool
    tools.append(Thehiveproject__custom_api_call__Tool())
    from .add import ThehiveprojectAddTool
    tools.append(ThehiveprojectAddTool())
    from .deletecomment import ThehiveprojectDeletecommentTool
    tools.append(ThehiveprojectDeletecommentTool())
    from .search import ThehiveprojectSearchTool
    tools.append(ThehiveprojectSearchTool())
    from .update import ThehiveprojectUpdateTool
    tools.append(ThehiveprojectUpdateTool())
    from .__custom_api_call__ import Thehiveproject__custom_api_call__Tool
    tools.append(Thehiveproject__custom_api_call__Tool())
    from .addattachment import ThehiveprojectAddattachmentTool
    tools.append(ThehiveprojectAddattachmentTool())
    from .create import ThehiveprojectCreateTool
    tools.append(ThehiveprojectCreateTool())
    from .deletelog import ThehiveprojectDeletelogTool
    tools.append(ThehiveprojectDeletelogTool())
    from .deleteattachment import ThehiveprojectDeleteattachmentTool
    tools.append(ThehiveprojectDeleteattachmentTool())
    from .executeresponder import ThehiveprojectExecuteresponderTool
    tools.append(ThehiveprojectExecuteresponderTool())
    from .get import ThehiveprojectGetTool
    tools.append(ThehiveprojectGetTool())
    from .search import ThehiveprojectSearchTool
    tools.append(ThehiveprojectSearchTool())
    from .__custom_api_call__ import Thehiveproject__custom_api_call__Tool
    tools.append(Thehiveproject__custom_api_call__Tool())
    from .create import ThehiveprojectCreateTool
    tools.append(ThehiveprojectCreateTool())
    from .deleteobservable import ThehiveprojectDeleteobservableTool
    tools.append(ThehiveprojectDeleteobservableTool())
    from .executeanalyzer import ThehiveprojectExecuteanalyzerTool
    tools.append(ThehiveprojectExecuteanalyzerTool())
    from .executeresponder import ThehiveprojectExecuteresponderTool
    tools.append(ThehiveprojectExecuteresponderTool())
    from .get import ThehiveprojectGetTool
    tools.append(ThehiveprojectGetTool())
    from .search import ThehiveprojectSearchTool
    tools.append(ThehiveprojectSearchTool())
    from .update import ThehiveprojectUpdateTool
    tools.append(ThehiveprojectUpdateTool())
    from .__custom_api_call__ import Thehiveproject__custom_api_call__Tool
    tools.append(Thehiveproject__custom_api_call__Tool())
    from .create import ThehiveprojectCreateTool
    tools.append(ThehiveprojectCreateTool())
    from .deletepage import ThehiveprojectDeletepageTool
    tools.append(ThehiveprojectDeletepageTool())
    from .search import ThehiveprojectSearchTool
    tools.append(ThehiveprojectSearchTool())
    from .update import ThehiveprojectUpdateTool
    tools.append(ThehiveprojectUpdateTool())
    from .__custom_api_call__ import Thehiveproject__custom_api_call__Tool
    tools.append(Thehiveproject__custom_api_call__Tool())
    from .executequery import ThehiveprojectExecutequeryTool
    tools.append(ThehiveprojectExecutequeryTool())
    from .__custom_api_call__ import Thehiveproject__custom_api_call__Tool
    tools.append(Thehiveproject__custom_api_call__Tool())
    from .create import ThehiveprojectCreateTool
    tools.append(ThehiveprojectCreateTool())
    from .deletetask import ThehiveprojectDeletetaskTool
    tools.append(ThehiveprojectDeletetaskTool())
    from .executeresponder import ThehiveprojectExecuteresponderTool
    tools.append(ThehiveprojectExecuteresponderTool())
    from .get import ThehiveprojectGetTool
    tools.append(ThehiveprojectGetTool())
    from .search import ThehiveprojectSearchTool
    tools.append(ThehiveprojectSearchTool())
    from .update import ThehiveprojectUpdateTool
    tools.append(ThehiveprojectUpdateTool())
    from .__custom_api_call__ import Thehiveproject__custom_api_call__Tool
    tools.append(Thehiveproject__custom_api_call__Tool())
    return tools
