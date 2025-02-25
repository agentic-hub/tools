# pipedrive operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all pipedrive operation tools."""
    tools = []
    from .create import PipedriveCreateTool
    tools.append(PipedriveCreateTool())
    from .delete import PipedriveDeleteTool
    tools.append(PipedriveDeleteTool())
    from .get import PipedriveGetTool
    tools.append(PipedriveGetTool())
    from .getall import PipedriveGetallTool
    tools.append(PipedriveGetallTool())
    from .update import PipedriveUpdateTool
    tools.append(PipedriveUpdateTool())
    from .__custom_api_call__ import Pipedrive__custom_api_call__Tool
    tools.append(Pipedrive__custom_api_call__Tool())
    from .create import PipedriveCreateTool
    tools.append(PipedriveCreateTool())
    from .delete import PipedriveDeleteTool
    tools.append(PipedriveDeleteTool())
    from .duplicate import PipedriveDuplicateTool
    tools.append(PipedriveDuplicateTool())
    from .get import PipedriveGetTool
    tools.append(PipedriveGetTool())
    from .getall import PipedriveGetallTool
    tools.append(PipedriveGetallTool())
    from .search import PipedriveSearchTool
    tools.append(PipedriveSearchTool())
    from .update import PipedriveUpdateTool
    tools.append(PipedriveUpdateTool())
    from .__custom_api_call__ import Pipedrive__custom_api_call__Tool
    tools.append(Pipedrive__custom_api_call__Tool())
    from .getall import PipedriveGetallTool
    tools.append(PipedriveGetallTool())
    from .__custom_api_call__ import Pipedrive__custom_api_call__Tool
    tools.append(Pipedrive__custom_api_call__Tool())
    from .add import PipedriveAddTool
    tools.append(PipedriveAddTool())
    from .getall import PipedriveGetallTool
    tools.append(PipedriveGetallTool())
    from .remove import PipedriveRemoveTool
    tools.append(PipedriveRemoveTool())
    from .update import PipedriveUpdateTool
    tools.append(PipedriveUpdateTool())
    from .__custom_api_call__ import Pipedrive__custom_api_call__Tool
    tools.append(Pipedrive__custom_api_call__Tool())
    from .create import PipedriveCreateTool
    tools.append(PipedriveCreateTool())
    from .delete import PipedriveDeleteTool
    tools.append(PipedriveDeleteTool())
    from .download import PipedriveDownloadTool
    tools.append(PipedriveDownloadTool())
    from .get import PipedriveGetTool
    tools.append(PipedriveGetTool())
    from .update import PipedriveUpdateTool
    tools.append(PipedriveUpdateTool())
    from .__custom_api_call__ import Pipedrive__custom_api_call__Tool
    tools.append(Pipedrive__custom_api_call__Tool())
    from .create import PipedriveCreateTool
    tools.append(PipedriveCreateTool())
    from .delete import PipedriveDeleteTool
    tools.append(PipedriveDeleteTool())
    from .get import PipedriveGetTool
    tools.append(PipedriveGetTool())
    from .getall import PipedriveGetallTool
    tools.append(PipedriveGetallTool())
    from .update import PipedriveUpdateTool
    tools.append(PipedriveUpdateTool())
    from .__custom_api_call__ import Pipedrive__custom_api_call__Tool
    tools.append(Pipedrive__custom_api_call__Tool())
    from .create import PipedriveCreateTool
    tools.append(PipedriveCreateTool())
    from .delete import PipedriveDeleteTool
    tools.append(PipedriveDeleteTool())
    from .get import PipedriveGetTool
    tools.append(PipedriveGetTool())
    from .getall import PipedriveGetallTool
    tools.append(PipedriveGetallTool())
    from .update import PipedriveUpdateTool
    tools.append(PipedriveUpdateTool())
    from .__custom_api_call__ import Pipedrive__custom_api_call__Tool
    tools.append(Pipedrive__custom_api_call__Tool())
    from .create import PipedriveCreateTool
    tools.append(PipedriveCreateTool())
    from .delete import PipedriveDeleteTool
    tools.append(PipedriveDeleteTool())
    from .get import PipedriveGetTool
    tools.append(PipedriveGetTool())
    from .getall import PipedriveGetallTool
    tools.append(PipedriveGetallTool())
    from .search import PipedriveSearchTool
    tools.append(PipedriveSearchTool())
    from .update import PipedriveUpdateTool
    tools.append(PipedriveUpdateTool())
    from .__custom_api_call__ import Pipedrive__custom_api_call__Tool
    tools.append(Pipedrive__custom_api_call__Tool())
    from .create import PipedriveCreateTool
    tools.append(PipedriveCreateTool())
    from .delete import PipedriveDeleteTool
    tools.append(PipedriveDeleteTool())
    from .get import PipedriveGetTool
    tools.append(PipedriveGetTool())
    from .getall import PipedriveGetallTool
    tools.append(PipedriveGetallTool())
    from .search import PipedriveSearchTool
    tools.append(PipedriveSearchTool())
    from .update import PipedriveUpdateTool
    tools.append(PipedriveUpdateTool())
    from .__custom_api_call__ import Pipedrive__custom_api_call__Tool
    tools.append(Pipedrive__custom_api_call__Tool())
    from .getall import PipedriveGetallTool
    tools.append(PipedriveGetallTool())
    from .__custom_api_call__ import Pipedrive__custom_api_call__Tool
    tools.append(Pipedrive__custom_api_call__Tool())
    return tools
