from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OdooCredentials

class OdooCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    custom_resource: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    custom_resource_id: Optional[str] = Field(None, description="Custom Resource ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    memo: Optional[str] = Field(None, description="Memo")
    operation: Optional[str] = Field(None, description="Operation")
    opportunity_id: Optional[str] = Field(None, description="Opportunity ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_create_or_update: Optional[Dict[str, Any]] = Field(None, description="Fields")
    opportunity_name: Optional[str] = Field(None, description="Name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    contact_name: Optional[str] = Field(None, description="Name")
    note_id: Optional[str] = Field(None, description="Note ID")


class OdooCreateTool(BaseTool):
    name: str = "odoo_create"
    connector_id: str = "nodes-base.odoo"
    description: str = "Tool for odoo create operation - create operation"
    args_schema: type[BaseModel] | None = OdooCreateToolInput
    credentials: Optional[OdooCredentials] = None
