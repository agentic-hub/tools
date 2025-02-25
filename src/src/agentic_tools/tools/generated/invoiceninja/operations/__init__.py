# invoiceNinja operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all invoiceNinja operation tools."""
    tools = []
    from .create import InvoiceninjaCreateTool
    tools.append(InvoiceninjaCreateTool())
    from .delete import InvoiceninjaDeleteTool
    tools.append(InvoiceninjaDeleteTool())
    from .get import InvoiceninjaGetTool
    tools.append(InvoiceninjaGetTool())
    from .getall import InvoiceninjaGetallTool
    tools.append(InvoiceninjaGetallTool())
    from .__custom_api_call__ import Invoiceninja__custom_api_call__Tool
    tools.append(Invoiceninja__custom_api_call__Tool())
    from .create import InvoiceninjaCreateTool
    tools.append(InvoiceninjaCreateTool())
    from .delete import InvoiceninjaDeleteTool
    tools.append(InvoiceninjaDeleteTool())
    from .email import InvoiceninjaEmailTool
    tools.append(InvoiceninjaEmailTool())
    from .get import InvoiceninjaGetTool
    tools.append(InvoiceninjaGetTool())
    from .getall import InvoiceninjaGetallTool
    tools.append(InvoiceninjaGetallTool())
    from .__custom_api_call__ import Invoiceninja__custom_api_call__Tool
    tools.append(Invoiceninja__custom_api_call__Tool())
    from .create import InvoiceninjaCreateTool
    tools.append(InvoiceninjaCreateTool())
    from .delete import InvoiceninjaDeleteTool
    tools.append(InvoiceninjaDeleteTool())
    from .get import InvoiceninjaGetTool
    tools.append(InvoiceninjaGetTool())
    from .getall import InvoiceninjaGetallTool
    tools.append(InvoiceninjaGetallTool())
    from .__custom_api_call__ import Invoiceninja__custom_api_call__Tool
    tools.append(Invoiceninja__custom_api_call__Tool())
    from .create import InvoiceninjaCreateTool
    tools.append(InvoiceninjaCreateTool())
    from .delete import InvoiceninjaDeleteTool
    tools.append(InvoiceninjaDeleteTool())
    from .get import InvoiceninjaGetTool
    tools.append(InvoiceninjaGetTool())
    from .getall import InvoiceninjaGetallTool
    tools.append(InvoiceninjaGetallTool())
    from .__custom_api_call__ import Invoiceninja__custom_api_call__Tool
    tools.append(Invoiceninja__custom_api_call__Tool())
    from .create import InvoiceninjaCreateTool
    tools.append(InvoiceninjaCreateTool())
    from .delete import InvoiceninjaDeleteTool
    tools.append(InvoiceninjaDeleteTool())
    from .get import InvoiceninjaGetTool
    tools.append(InvoiceninjaGetTool())
    from .getall import InvoiceninjaGetallTool
    tools.append(InvoiceninjaGetallTool())
    from .__custom_api_call__ import Invoiceninja__custom_api_call__Tool
    tools.append(Invoiceninja__custom_api_call__Tool())
    from .create import InvoiceninjaCreateTool
    tools.append(InvoiceninjaCreateTool())
    from .delete import InvoiceninjaDeleteTool
    tools.append(InvoiceninjaDeleteTool())
    from .email import InvoiceninjaEmailTool
    tools.append(InvoiceninjaEmailTool())
    from .get import InvoiceninjaGetTool
    tools.append(InvoiceninjaGetTool())
    from .getall import InvoiceninjaGetallTool
    tools.append(InvoiceninjaGetallTool())
    from .__custom_api_call__ import Invoiceninja__custom_api_call__Tool
    tools.append(Invoiceninja__custom_api_call__Tool())
    return tools
