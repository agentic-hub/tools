# sentryIo operations
from typing import List
from langchain.tools import BaseTool
from .. import SentryioCredentials

def get_tools() -> List[BaseTool]:
    """Get all sentryIo operation tools."""
    tools = []
    from .get import SentryioGetTool
    tools.append(SentryioGetTool())
    from .getall import SentryioGetallTool
    tools.append(SentryioGetallTool())
    from .__custom_api_call__ import Sentryio__custom_api_call__Tool
    tools.append(Sentryio__custom_api_call__Tool())
    from .delete import SentryioDeleteTool
    tools.append(SentryioDeleteTool())
    from .get import SentryioGetTool
    tools.append(SentryioGetTool())
    from .getall import SentryioGetallTool
    tools.append(SentryioGetallTool())
    from .update import SentryioUpdateTool
    tools.append(SentryioUpdateTool())
    from .__custom_api_call__ import Sentryio__custom_api_call__Tool
    tools.append(Sentryio__custom_api_call__Tool())
    from .create import SentryioCreateTool
    tools.append(SentryioCreateTool())
    from .get import SentryioGetTool
    tools.append(SentryioGetTool())
    from .getall import SentryioGetallTool
    tools.append(SentryioGetallTool())
    from .update import SentryioUpdateTool
    tools.append(SentryioUpdateTool())
    from .__custom_api_call__ import Sentryio__custom_api_call__Tool
    tools.append(Sentryio__custom_api_call__Tool())
    from .create import SentryioCreateTool
    tools.append(SentryioCreateTool())
    from .delete import SentryioDeleteTool
    tools.append(SentryioDeleteTool())
    from .get import SentryioGetTool
    tools.append(SentryioGetTool())
    from .getall import SentryioGetallTool
    tools.append(SentryioGetallTool())
    from .update import SentryioUpdateTool
    tools.append(SentryioUpdateTool())
    from .__custom_api_call__ import Sentryio__custom_api_call__Tool
    tools.append(Sentryio__custom_api_call__Tool())
    from .create import SentryioCreateTool
    tools.append(SentryioCreateTool())
    from .delete import SentryioDeleteTool
    tools.append(SentryioDeleteTool())
    from .get import SentryioGetTool
    tools.append(SentryioGetTool())
    from .getall import SentryioGetallTool
    tools.append(SentryioGetallTool())
    from .update import SentryioUpdateTool
    tools.append(SentryioUpdateTool())
    from .__custom_api_call__ import Sentryio__custom_api_call__Tool
    tools.append(Sentryio__custom_api_call__Tool())
    from .create import SentryioCreateTool
    tools.append(SentryioCreateTool())
    from .delete import SentryioDeleteTool
    tools.append(SentryioDeleteTool())
    from .get import SentryioGetTool
    tools.append(SentryioGetTool())
    from .getall import SentryioGetallTool
    tools.append(SentryioGetallTool())
    from .update import SentryioUpdateTool
    tools.append(SentryioUpdateTool())
    from .__custom_api_call__ import Sentryio__custom_api_call__Tool
    tools.append(Sentryio__custom_api_call__Tool())
    return tools
