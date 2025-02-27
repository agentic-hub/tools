# onfleet operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import OnfleetCredentials

def get_tools() -> List[BaseTool]:
    """Get all onfleet operation tools."""
    tools = []
    from .create import OnfleetCreateTool
    tools.append(OnfleetCreateTool())
    from .delete import OnfleetDeleteTool
    tools.append(OnfleetDeleteTool())
    from .getall import OnfleetGetallTool
    tools.append(OnfleetGetallTool())
    from .update import OnfleetUpdateTool
    tools.append(OnfleetUpdateTool())
    from .addtask import OnfleetAddtaskTool
    tools.append(OnfleetAddtaskTool())
    from .get import OnfleetGetTool
    tools.append(OnfleetGetTool())
    from .updatetask import OnfleetUpdatetaskTool
    tools.append(OnfleetUpdatetaskTool())
    from .create import OnfleetCreateTool
    tools.append(OnfleetCreateTool())
    from .get import OnfleetGetTool
    tools.append(OnfleetGetTool())
    from .create import OnfleetCreateTool
    tools.append(OnfleetCreateTool())
    from .getall import OnfleetGetallTool
    tools.append(OnfleetGetallTool())
    from .update import OnfleetUpdateTool
    tools.append(OnfleetUpdateTool())
    from .get import OnfleetGetTool
    tools.append(OnfleetGetTool())
    from .getdelegatee import OnfleetGetdelegateeTool
    tools.append(OnfleetGetdelegateeTool())
    from .create import OnfleetCreateTool
    tools.append(OnfleetCreateTool())
    from .get import OnfleetGetTool
    tools.append(OnfleetGetTool())
    from .update import OnfleetUpdateTool
    tools.append(OnfleetUpdateTool())
    from .clone import OnfleetCloneTool
    tools.append(OnfleetCloneTool())
    from .complete import OnfleetCompleteTool
    tools.append(OnfleetCompleteTool())
    from .create import OnfleetCreateTool
    tools.append(OnfleetCreateTool())
    from .delete import OnfleetDeleteTool
    tools.append(OnfleetDeleteTool())
    from .get import OnfleetGetTool
    tools.append(OnfleetGetTool())
    from .getall import OnfleetGetallTool
    tools.append(OnfleetGetallTool())
    from .update import OnfleetUpdateTool
    tools.append(OnfleetUpdateTool())
    from .autodispatch import OnfleetAutodispatchTool
    tools.append(OnfleetAutodispatchTool())
    from .create import OnfleetCreateTool
    tools.append(OnfleetCreateTool())
    from .delete import OnfleetDeleteTool
    tools.append(OnfleetDeleteTool())
    from .get import OnfleetGetTool
    tools.append(OnfleetGetTool())
    from .getall import OnfleetGetallTool
    tools.append(OnfleetGetallTool())
    from .gettimeestimates import OnfleetGettimeestimatesTool
    tools.append(OnfleetGettimeestimatesTool())
    from .update import OnfleetUpdateTool
    tools.append(OnfleetUpdateTool())
    from .create import OnfleetCreateTool
    tools.append(OnfleetCreateTool())
    from .delete import OnfleetDeleteTool
    tools.append(OnfleetDeleteTool())
    from .get import OnfleetGetTool
    tools.append(OnfleetGetTool())
    from .getall import OnfleetGetallTool
    tools.append(OnfleetGetallTool())
    from .getschedule import OnfleetGetscheduleTool
    tools.append(OnfleetGetscheduleTool())
    from .update import OnfleetUpdateTool
    tools.append(OnfleetUpdateTool())
    return tools
