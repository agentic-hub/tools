# discourse operations
from typing import List
from langchain.tools import BaseTool
from .. import DiscourseCredentials

def get_tools() -> List[BaseTool]:
    """Get all discourse operation tools."""
    tools = []
    from .create import DiscourseCreateTool
    tools.append(DiscourseCreateTool())
    from .getall import DiscourseGetallTool
    tools.append(DiscourseGetallTool())
    from .update import DiscourseUpdateTool
    tools.append(DiscourseUpdateTool())
    from .__custom_api_call__ import Discourse__custom_api_call__Tool
    tools.append(Discourse__custom_api_call__Tool())
    from .create import DiscourseCreateTool
    tools.append(DiscourseCreateTool())
    from .get import DiscourseGetTool
    tools.append(DiscourseGetTool())
    from .getall import DiscourseGetallTool
    tools.append(DiscourseGetallTool())
    from .update import DiscourseUpdateTool
    tools.append(DiscourseUpdateTool())
    from .__custom_api_call__ import Discourse__custom_api_call__Tool
    tools.append(Discourse__custom_api_call__Tool())
    from .create import DiscourseCreateTool
    tools.append(DiscourseCreateTool())
    from .get import DiscourseGetTool
    tools.append(DiscourseGetTool())
    from .getall import DiscourseGetallTool
    tools.append(DiscourseGetallTool())
    from .update import DiscourseUpdateTool
    tools.append(DiscourseUpdateTool())
    from .__custom_api_call__ import Discourse__custom_api_call__Tool
    tools.append(Discourse__custom_api_call__Tool())
    from .create import DiscourseCreateTool
    tools.append(DiscourseCreateTool())
    from .get import DiscourseGetTool
    tools.append(DiscourseGetTool())
    from .getall import DiscourseGetallTool
    tools.append(DiscourseGetallTool())
    from .__custom_api_call__ import Discourse__custom_api_call__Tool
    tools.append(Discourse__custom_api_call__Tool())
    from .add import DiscourseAddTool
    tools.append(DiscourseAddTool())
    from .remove import DiscourseRemoveTool
    tools.append(DiscourseRemoveTool())
    from .__custom_api_call__ import Discourse__custom_api_call__Tool
    tools.append(Discourse__custom_api_call__Tool())
    return tools
