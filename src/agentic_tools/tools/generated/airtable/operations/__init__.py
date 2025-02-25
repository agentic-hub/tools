# airtable operations
from typing import List
from langchain.tools import BaseTool
from .. import AirtableCredentials

def get_tools() -> List[BaseTool]:
    """Get all airtable operation tools."""
    tools = []
    from .create import AirtableCreateTool
    tools.append(AirtableCreateTool())
    from .upsert import AirtableUpsertTool
    tools.append(AirtableUpsertTool())
    from .deleterecord import AirtableDeleterecordTool
    tools.append(AirtableDeleterecordTool())
    from .get import AirtableGetTool
    tools.append(AirtableGetTool())
    from .search import AirtableSearchTool
    tools.append(AirtableSearchTool())
    from .update import AirtableUpdateTool
    tools.append(AirtableUpdateTool())
    from .__custom_api_call__ import Airtable__custom_api_call__Tool
    tools.append(Airtable__custom_api_call__Tool())
    from .getmany import AirtableGetmanyTool
    tools.append(AirtableGetmanyTool())
    from .getschema import AirtableGetschemaTool
    tools.append(AirtableGetschemaTool())
    from .__custom_api_call__ import Airtable__custom_api_call__Tool
    tools.append(Airtable__custom_api_call__Tool())
    return tools
