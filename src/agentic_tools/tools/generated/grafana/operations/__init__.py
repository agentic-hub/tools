# grafana operations
from typing import List
from langchain.tools import BaseTool
from .. import GrafanaCredentials

def get_tools() -> List[BaseTool]:
    """Get all grafana operation tools."""
    tools = []
    from .create import GrafanaCreateTool
    tools.append(GrafanaCreateTool())
    from .delete import GrafanaDeleteTool
    tools.append(GrafanaDeleteTool())
    from .get import GrafanaGetTool
    tools.append(GrafanaGetTool())
    from .getall import GrafanaGetallTool
    tools.append(GrafanaGetallTool())
    from .update import GrafanaUpdateTool
    tools.append(GrafanaUpdateTool())
    from .__custom_api_call__ import Grafana__custom_api_call__Tool
    tools.append(Grafana__custom_api_call__Tool())
    from .create import GrafanaCreateTool
    tools.append(GrafanaCreateTool())
    from .delete import GrafanaDeleteTool
    tools.append(GrafanaDeleteTool())
    from .get import GrafanaGetTool
    tools.append(GrafanaGetTool())
    from .getall import GrafanaGetallTool
    tools.append(GrafanaGetallTool())
    from .update import GrafanaUpdateTool
    tools.append(GrafanaUpdateTool())
    from .__custom_api_call__ import Grafana__custom_api_call__Tool
    tools.append(Grafana__custom_api_call__Tool())
    from .add import GrafanaAddTool
    tools.append(GrafanaAddTool())
    from .getall import GrafanaGetallTool
    tools.append(GrafanaGetallTool())
    from .remove import GrafanaRemoveTool
    tools.append(GrafanaRemoveTool())
    from .__custom_api_call__ import Grafana__custom_api_call__Tool
    tools.append(Grafana__custom_api_call__Tool())
    from .delete import GrafanaDeleteTool
    tools.append(GrafanaDeleteTool())
    from .getall import GrafanaGetallTool
    tools.append(GrafanaGetallTool())
    from .update import GrafanaUpdateTool
    tools.append(GrafanaUpdateTool())
    from .__custom_api_call__ import Grafana__custom_api_call__Tool
    tools.append(Grafana__custom_api_call__Tool())
    return tools
