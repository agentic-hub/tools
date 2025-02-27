from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ErpnextCredentials

class ErpnextCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    doc_type: Optional[str] = Field(None, description="DocType you would like to create. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    document_name: Optional[str] = Field(None, description="The name (ID) of document you would like to get")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class ErpnextCreateTool(BaseTool):
    name: str = "erpnext_create"
    description: str = "Tool for erpNext create operation - create operation"
    args_schema: type[BaseModel] | None = ErpnextCreateToolInput
    credentials: Optional[ErpnextCredentials] = None
