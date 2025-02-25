# youTube operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all youTube operation tools."""
    tools = []
    from .get import YoutubeGetTool
    tools.append(YoutubeGetTool())
    from .getall import YoutubeGetallTool
    tools.append(YoutubeGetallTool())
    from .update import YoutubeUpdateTool
    tools.append(YoutubeUpdateTool())
    from .uploadbanner import YoutubeUploadbannerTool
    tools.append(YoutubeUploadbannerTool())
    from .__custom_api_call__ import Youtube__custom_api_call__Tool
    tools.append(Youtube__custom_api_call__Tool())
    from .create import YoutubeCreateTool
    tools.append(YoutubeCreateTool())
    from .delete import YoutubeDeleteTool
    tools.append(YoutubeDeleteTool())
    from .get import YoutubeGetTool
    tools.append(YoutubeGetTool())
    from .getall import YoutubeGetallTool
    tools.append(YoutubeGetallTool())
    from .update import YoutubeUpdateTool
    tools.append(YoutubeUpdateTool())
    from .__custom_api_call__ import Youtube__custom_api_call__Tool
    tools.append(Youtube__custom_api_call__Tool())
    from .add import YoutubeAddTool
    tools.append(YoutubeAddTool())
    from .delete import YoutubeDeleteTool
    tools.append(YoutubeDeleteTool())
    from .get import YoutubeGetTool
    tools.append(YoutubeGetTool())
    from .getall import YoutubeGetallTool
    tools.append(YoutubeGetallTool())
    from .__custom_api_call__ import Youtube__custom_api_call__Tool
    tools.append(Youtube__custom_api_call__Tool())
    from .delete import YoutubeDeleteTool
    tools.append(YoutubeDeleteTool())
    from .get import YoutubeGetTool
    tools.append(YoutubeGetTool())
    from .getall import YoutubeGetallTool
    tools.append(YoutubeGetallTool())
    from .rate import YoutubeRateTool
    tools.append(YoutubeRateTool())
    from .update import YoutubeUpdateTool
    tools.append(YoutubeUpdateTool())
    from .upload import YoutubeUploadTool
    tools.append(YoutubeUploadTool())
    from .__custom_api_call__ import Youtube__custom_api_call__Tool
    tools.append(Youtube__custom_api_call__Tool())
    from .getall import YoutubeGetallTool
    tools.append(YoutubeGetallTool())
    from .__custom_api_call__ import Youtube__custom_api_call__Tool
    tools.append(Youtube__custom_api_call__Tool())
    return tools
