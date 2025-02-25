# sendGrid operations
from typing import List
from langchain.tools import BaseTool
from .. import SendgridCredentials

def get_tools() -> List[BaseTool]:
    """Get all sendGrid operation tools."""
    tools = []
    from .create import SendgridCreateTool
    tools.append(SendgridCreateTool())
    from .delete import SendgridDeleteTool
    tools.append(SendgridDeleteTool())
    from .get import SendgridGetTool
    tools.append(SendgridGetTool())
    from .getall import SendgridGetallTool
    tools.append(SendgridGetallTool())
    from .update import SendgridUpdateTool
    tools.append(SendgridUpdateTool())
    from .__custom_api_call__ import Sendgrid__custom_api_call__Tool
    tools.append(Sendgrid__custom_api_call__Tool())
    from .upsert import SendgridUpsertTool
    tools.append(SendgridUpsertTool())
    from .delete import SendgridDeleteTool
    tools.append(SendgridDeleteTool())
    from .get import SendgridGetTool
    tools.append(SendgridGetTool())
    from .getall import SendgridGetallTool
    tools.append(SendgridGetallTool())
    from .__custom_api_call__ import Sendgrid__custom_api_call__Tool
    tools.append(Sendgrid__custom_api_call__Tool())
    from .send import SendgridSendTool
    tools.append(SendgridSendTool())
    from .__custom_api_call__ import Sendgrid__custom_api_call__Tool
    tools.append(Sendgrid__custom_api_call__Tool())
    return tools
