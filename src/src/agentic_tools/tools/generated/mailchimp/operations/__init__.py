# mailchimp operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all mailchimp operation tools."""
    tools = []
    from .create import MailchimpCreateTool
    tools.append(MailchimpCreateTool())
    from .delete import MailchimpDeleteTool
    tools.append(MailchimpDeleteTool())
    from .get import MailchimpGetTool
    tools.append(MailchimpGetTool())
    from .getall import MailchimpGetallTool
    tools.append(MailchimpGetallTool())
    from .update import MailchimpUpdateTool
    tools.append(MailchimpUpdateTool())
    from .__custom_api_call__ import Mailchimp__custom_api_call__Tool
    tools.append(Mailchimp__custom_api_call__Tool())
    from .create import MailchimpCreateTool
    tools.append(MailchimpCreateTool())
    from .delete import MailchimpDeleteTool
    tools.append(MailchimpDeleteTool())
    from .__custom_api_call__ import Mailchimp__custom_api_call__Tool
    tools.append(Mailchimp__custom_api_call__Tool())
    from .getall import MailchimpGetallTool
    tools.append(MailchimpGetallTool())
    from .__custom_api_call__ import Mailchimp__custom_api_call__Tool
    tools.append(Mailchimp__custom_api_call__Tool())
    from .delete import MailchimpDeleteTool
    tools.append(MailchimpDeleteTool())
    from .get import MailchimpGetTool
    tools.append(MailchimpGetTool())
    from .getall import MailchimpGetallTool
    tools.append(MailchimpGetallTool())
    from .replicate import MailchimpReplicateTool
    tools.append(MailchimpReplicateTool())
    from .resend import MailchimpResendTool
    tools.append(MailchimpResendTool())
    from .send import MailchimpSendTool
    tools.append(MailchimpSendTool())
    from .__custom_api_call__ import Mailchimp__custom_api_call__Tool
    tools.append(Mailchimp__custom_api_call__Tool())
    return tools
