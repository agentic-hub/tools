from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KeapCredentials

class KeapCreateToolInput(BaseModel):
    order_type: Optional[str] = Field(None, description="Order Type")
    order_title: Optional[str] = Field(None, description="Order Title")
    order_items_ui: Optional[Dict[str, Any]] = Field(None, description="Order Items")
    tag_ids: Optional[str] = Field(None, description="tagIds")
    user_id: Optional[str] = Field(None, description="The infusionsoft user to create the note on behalf of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    addresses_ui: Optional[Dict[str, Any]] = Field(None, description="Addresses")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    product_name: Optional[str] = Field(None, description="Product Name")
    address_ui: Optional[Dict[str, Any]] = Field(None, description="Shipping Address")
    operation: Optional[str] = Field(None, description="Operation")
    company_name: Optional[str] = Field(None, description="Company Name")
    phones_ui: Optional[Dict[str, Any]] = Field(None, description="Phones")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    order_date: Optional[str] = Field(None, description="Order Date")
    order_id: Optional[str] = Field(None, description="Order ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    note_id: Optional[str] = Field(None, description="Note ID")
    faxes_ui: Optional[Dict[str, Any]] = Field(None, description="Faxes")
    product_id: Optional[str] = Field(None, description="Product ID")


class KeapCreateTool(BaseTool):
    name: str = "keap_create"
    connector_id: str = "nodes-base.keap"
    description: str = "Tool for keap create operation - create operation"
    args_schema: type[BaseModel] | None = KeapCreateToolInput
    credentials: Optional[KeapCredentials] = None
