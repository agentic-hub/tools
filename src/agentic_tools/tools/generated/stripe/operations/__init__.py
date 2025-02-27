# stripe operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import StripeCredentials

def get_tools() -> List[BaseTool]:
    """Get all stripe operation tools."""
    tools = []
    from .get import StripeGetTool
    tools.append(StripeGetTool())
    from .__custom_api_call__ import Stripe__custom_api_call__Tool
    tools.append(Stripe__custom_api_call__Tool())
    from .add import StripeAddTool
    tools.append(StripeAddTool())
    from .get import StripeGetTool
    tools.append(StripeGetTool())
    from .remove import StripeRemoveTool
    tools.append(StripeRemoveTool())
    from .__custom_api_call__ import Stripe__custom_api_call__Tool
    tools.append(Stripe__custom_api_call__Tool())
    from .create import StripeCreateTool
    tools.append(StripeCreateTool())
    from .get import StripeGetTool
    tools.append(StripeGetTool())
    from .getall import StripeGetallTool
    tools.append(StripeGetallTool())
    from .update import StripeUpdateTool
    tools.append(StripeUpdateTool())
    from .__custom_api_call__ import Stripe__custom_api_call__Tool
    tools.append(Stripe__custom_api_call__Tool())
    from .create import StripeCreateTool
    tools.append(StripeCreateTool())
    from .getall import StripeGetallTool
    tools.append(StripeGetallTool())
    from .__custom_api_call__ import Stripe__custom_api_call__Tool
    tools.append(Stripe__custom_api_call__Tool())
    from .create import StripeCreateTool
    tools.append(StripeCreateTool())
    from .delete import StripeDeleteTool
    tools.append(StripeDeleteTool())
    from .get import StripeGetTool
    tools.append(StripeGetTool())
    from .getall import StripeGetallTool
    tools.append(StripeGetallTool())
    from .update import StripeUpdateTool
    tools.append(StripeUpdateTool())
    from .__custom_api_call__ import Stripe__custom_api_call__Tool
    tools.append(Stripe__custom_api_call__Tool())
    from .create import StripeCreateTool
    tools.append(StripeCreateTool())
    from .delete import StripeDeleteTool
    tools.append(StripeDeleteTool())
    from .get import StripeGetTool
    tools.append(StripeGetTool())
    from .__custom_api_call__ import Stripe__custom_api_call__Tool
    tools.append(Stripe__custom_api_call__Tool())
    from .create import StripeCreateTool
    tools.append(StripeCreateTool())
    from .__custom_api_call__ import Stripe__custom_api_call__Tool
    tools.append(Stripe__custom_api_call__Tool())
    return tools
