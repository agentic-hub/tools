# salesforce operations
from typing import List
from langchain.tools import BaseTool
from .. import SalesforceCredentials

def get_tools() -> List[BaseTool]:
    """Get all salesforce operation tools."""
    tools = []
    from .addtocampaign import SalesforceAddtocampaignTool
    tools.append(SalesforceAddtocampaignTool())
    from .addnote import SalesforceAddnoteTool
    tools.append(SalesforceAddnoteTool())
    from .create import SalesforceCreateTool
    tools.append(SalesforceCreateTool())
    from .upsert import SalesforceUpsertTool
    tools.append(SalesforceUpsertTool())
    from .delete import SalesforceDeleteTool
    tools.append(SalesforceDeleteTool())
    from .get import SalesforceGetTool
    tools.append(SalesforceGetTool())
    from .getall import SalesforceGetallTool
    tools.append(SalesforceGetallTool())
    from .getsummary import SalesforceGetsummaryTool
    tools.append(SalesforceGetsummaryTool())
    from .update import SalesforceUpdateTool
    tools.append(SalesforceUpdateTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .addtocampaign import SalesforceAddtocampaignTool
    tools.append(SalesforceAddtocampaignTool())
    from .addnote import SalesforceAddnoteTool
    tools.append(SalesforceAddnoteTool())
    from .create import SalesforceCreateTool
    tools.append(SalesforceCreateTool())
    from .upsert import SalesforceUpsertTool
    tools.append(SalesforceUpsertTool())
    from .delete import SalesforceDeleteTool
    tools.append(SalesforceDeleteTool())
    from .get import SalesforceGetTool
    tools.append(SalesforceGetTool())
    from .getall import SalesforceGetallTool
    tools.append(SalesforceGetallTool())
    from .getsummary import SalesforceGetsummaryTool
    tools.append(SalesforceGetsummaryTool())
    from .update import SalesforceUpdateTool
    tools.append(SalesforceUpdateTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .create import SalesforceCreateTool
    tools.append(SalesforceCreateTool())
    from .upsert import SalesforceUpsertTool
    tools.append(SalesforceUpsertTool())
    from .delete import SalesforceDeleteTool
    tools.append(SalesforceDeleteTool())
    from .get import SalesforceGetTool
    tools.append(SalesforceGetTool())
    from .getall import SalesforceGetallTool
    tools.append(SalesforceGetallTool())
    from .update import SalesforceUpdateTool
    tools.append(SalesforceUpdateTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .upload import SalesforceUploadTool
    tools.append(SalesforceUploadTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .addnote import SalesforceAddnoteTool
    tools.append(SalesforceAddnoteTool())
    from .create import SalesforceCreateTool
    tools.append(SalesforceCreateTool())
    from .upsert import SalesforceUpsertTool
    tools.append(SalesforceUpsertTool())
    from .delete import SalesforceDeleteTool
    tools.append(SalesforceDeleteTool())
    from .get import SalesforceGetTool
    tools.append(SalesforceGetTool())
    from .getall import SalesforceGetallTool
    tools.append(SalesforceGetallTool())
    from .getsummary import SalesforceGetsummaryTool
    tools.append(SalesforceGetsummaryTool())
    from .update import SalesforceUpdateTool
    tools.append(SalesforceUpdateTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .addnote import SalesforceAddnoteTool
    tools.append(SalesforceAddnoteTool())
    from .create import SalesforceCreateTool
    tools.append(SalesforceCreateTool())
    from .upsert import SalesforceUpsertTool
    tools.append(SalesforceUpsertTool())
    from .delete import SalesforceDeleteTool
    tools.append(SalesforceDeleteTool())
    from .get import SalesforceGetTool
    tools.append(SalesforceGetTool())
    from .getall import SalesforceGetallTool
    tools.append(SalesforceGetallTool())
    from .getsummary import SalesforceGetsummaryTool
    tools.append(SalesforceGetsummaryTool())
    from .update import SalesforceUpdateTool
    tools.append(SalesforceUpdateTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .query import SalesforceQueryTool
    tools.append(SalesforceQueryTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .addcomment import SalesforceAddcommentTool
    tools.append(SalesforceAddcommentTool())
    from .create import SalesforceCreateTool
    tools.append(SalesforceCreateTool())
    from .delete import SalesforceDeleteTool
    tools.append(SalesforceDeleteTool())
    from .get import SalesforceGetTool
    tools.append(SalesforceGetTool())
    from .getall import SalesforceGetallTool
    tools.append(SalesforceGetallTool())
    from .getsummary import SalesforceGetsummaryTool
    tools.append(SalesforceGetsummaryTool())
    from .update import SalesforceUpdateTool
    tools.append(SalesforceUpdateTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .create import SalesforceCreateTool
    tools.append(SalesforceCreateTool())
    from .delete import SalesforceDeleteTool
    tools.append(SalesforceDeleteTool())
    from .get import SalesforceGetTool
    tools.append(SalesforceGetTool())
    from .getall import SalesforceGetallTool
    tools.append(SalesforceGetallTool())
    from .getsummary import SalesforceGetsummaryTool
    tools.append(SalesforceGetsummaryTool())
    from .update import SalesforceUpdateTool
    tools.append(SalesforceUpdateTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .create import SalesforceCreateTool
    tools.append(SalesforceCreateTool())
    from .delete import SalesforceDeleteTool
    tools.append(SalesforceDeleteTool())
    from .get import SalesforceGetTool
    tools.append(SalesforceGetTool())
    from .getall import SalesforceGetallTool
    tools.append(SalesforceGetallTool())
    from .getsummary import SalesforceGetsummaryTool
    tools.append(SalesforceGetsummaryTool())
    from .update import SalesforceUpdateTool
    tools.append(SalesforceUpdateTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .get import SalesforceGetTool
    tools.append(SalesforceGetTool())
    from .getall import SalesforceGetallTool
    tools.append(SalesforceGetallTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    from .getall import SalesforceGetallTool
    tools.append(SalesforceGetallTool())
    from .invoke import SalesforceInvokeTool
    tools.append(SalesforceInvokeTool())
    from .__custom_api_call__ import Salesforce__custom_api_call__Tool
    tools.append(Salesforce__custom_api_call__Tool())
    return tools
