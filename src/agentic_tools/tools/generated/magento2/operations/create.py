from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Magento2Credentials

class Magento2CreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    customer_id: Optional[str] = Field(None, description="ID of the customer to update")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://devdocs.magento.com/guides/v2.4/rest/performing-searches.html\" target=\"_blank\">Magento guide</a> to creating filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    sku: Optional[str] = Field(None, description="Stock-keeping unit of the product")
    price: Optional[float] = Field(None, description="Price")
    email: Optional[str] = Field(None, description="Email address of the user to create")
    operation: Optional[str] = Field(None, description="Operation")
    lastname: Optional[str] = Field(None, description="Last name of the user to create")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filter_json: Optional[str] = Field(None, description="Filters (JSON)")
    order_id: Optional[str] = Field(None, description="Order ID")
    firstname: Optional[str] = Field(None, description="First name of the user to create")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    attribute_set_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filter_type: Optional[str] = Field(None, description="Filter")
    match_type: Optional[str] = Field(None, description="Must Match")


class Magento2CreateTool(BaseTool):
    name: str = "magento2_create"
    connector_id: str = "nodes-base.magento2"
    description: str = "Tool for magento2 create operation - create operation"
    args_schema: type[BaseModel] | None = Magento2CreateToolInput
    credentials: Optional[Magento2Credentials] = None
