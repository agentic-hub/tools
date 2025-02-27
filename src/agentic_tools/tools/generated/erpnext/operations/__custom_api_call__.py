from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ErpnextCredentials

class Erpnext__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    doc_type: Optional[str] = Field(None, description="DocType whose documents to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    document_name: Optional[str] = Field(None, description="The name (ID) of document you would like to get")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class Erpnext__custom_api_call__Tool(BaseTool):
    name: str = "erpnext___custom_api_call__"
    description: str = "Tool for erpNext __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Erpnext__custom_api_call__ToolInput
    credentials: Optional[ErpnextCredentials] = None
