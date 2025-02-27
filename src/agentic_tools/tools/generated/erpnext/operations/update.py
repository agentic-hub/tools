from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ErpnextCredentials

class ErpnextUpdateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    doc_type: Optional[str] = Field(None, description="The type of document you would like to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    document_name: Optional[str] = Field(None, description="The name (ID) of document you would like to get")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties of request body")
    operation: Optional[str] = Field(None, description="Operation")


class ErpnextUpdateTool(BaseTool):
    name: str = "erpnext_update"
    connector_id: str = "nodes-base.erpNext"
    description: str = "Tool for erpNext update operation - update operation"
    args_schema: type[BaseModel] | None = ErpnextUpdateToolInput
    credentials: Optional[ErpnextCredentials] = None
