from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ErpnextCredentials

class ErpnextDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    doc_type: Optional[str] = Field(None, description="The type of document you would like to delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    document_name: Optional[str] = Field(None, description="The name (ID) of document you would like to get")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class ErpnextDeleteTool(BaseTool):
    name: str = "erpnext_delete"
    description: str = "Tool for erpNext delete operation - delete operation"
    args_schema: type[BaseModel] | None = ErpnextDeleteToolInput
    credentials: Optional[ErpnextCredentials] = None
