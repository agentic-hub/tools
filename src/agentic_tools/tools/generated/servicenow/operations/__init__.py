# serviceNow operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import ServicenowCredentials

def get_tools() -> List[BaseTool]:
    """Get all serviceNow operation tools."""
    tools = []
    from .upload import ServicenowUploadTool
    tools.append(ServicenowUploadTool())
    from .delete import ServicenowDeleteTool
    tools.append(ServicenowDeleteTool())
    from .get import ServicenowGetTool
    tools.append(ServicenowGetTool())
    from .getall import ServicenowGetallTool
    tools.append(ServicenowGetallTool())
    from .__custom_api_call__ import Servicenow__custom_api_call__Tool
    tools.append(Servicenow__custom_api_call__Tool())
    from .getall import ServicenowGetallTool
    tools.append(ServicenowGetallTool())
    from .__custom_api_call__ import Servicenow__custom_api_call__Tool
    tools.append(Servicenow__custom_api_call__Tool())
    from .getall import ServicenowGetallTool
    tools.append(ServicenowGetallTool())
    from .__custom_api_call__ import Servicenow__custom_api_call__Tool
    tools.append(Servicenow__custom_api_call__Tool())
    from .getall import ServicenowGetallTool
    tools.append(ServicenowGetallTool())
    from .__custom_api_call__ import Servicenow__custom_api_call__Tool
    tools.append(Servicenow__custom_api_call__Tool())
    from .getall import ServicenowGetallTool
    tools.append(ServicenowGetallTool())
    from .__custom_api_call__ import Servicenow__custom_api_call__Tool
    tools.append(Servicenow__custom_api_call__Tool())
    from .create import ServicenowCreateTool
    tools.append(ServicenowCreateTool())
    from .delete import ServicenowDeleteTool
    tools.append(ServicenowDeleteTool())
    from .get import ServicenowGetTool
    tools.append(ServicenowGetTool())
    from .getall import ServicenowGetallTool
    tools.append(ServicenowGetallTool())
    from .update import ServicenowUpdateTool
    tools.append(ServicenowUpdateTool())
    from .__custom_api_call__ import Servicenow__custom_api_call__Tool
    tools.append(Servicenow__custom_api_call__Tool())
    from .create import ServicenowCreateTool
    tools.append(ServicenowCreateTool())
    from .delete import ServicenowDeleteTool
    tools.append(ServicenowDeleteTool())
    from .get import ServicenowGetTool
    tools.append(ServicenowGetTool())
    from .getall import ServicenowGetallTool
    tools.append(ServicenowGetallTool())
    from .update import ServicenowUpdateTool
    tools.append(ServicenowUpdateTool())
    from .__custom_api_call__ import Servicenow__custom_api_call__Tool
    tools.append(Servicenow__custom_api_call__Tool())
    from .create import ServicenowCreateTool
    tools.append(ServicenowCreateTool())
    from .delete import ServicenowDeleteTool
    tools.append(ServicenowDeleteTool())
    from .get import ServicenowGetTool
    tools.append(ServicenowGetTool())
    from .getall import ServicenowGetallTool
    tools.append(ServicenowGetallTool())
    from .update import ServicenowUpdateTool
    tools.append(ServicenowUpdateTool())
    from .__custom_api_call__ import Servicenow__custom_api_call__Tool
    tools.append(Servicenow__custom_api_call__Tool())
    from .getall import ServicenowGetallTool
    tools.append(ServicenowGetallTool())
    from .__custom_api_call__ import Servicenow__custom_api_call__Tool
    tools.append(Servicenow__custom_api_call__Tool())
    from .getall import ServicenowGetallTool
    tools.append(ServicenowGetallTool())
    from .__custom_api_call__ import Servicenow__custom_api_call__Tool
    tools.append(Servicenow__custom_api_call__Tool())
    return tools
