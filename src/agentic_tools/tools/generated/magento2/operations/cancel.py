from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Magento2Credentials

class Magento2CancelToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    customer_id: Optional[str] = Field(None, description="ID of the customer to update")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://devdocs.magento.com/guides/v2.4/rest/performing-searches.html\" target=\"_blank\">Magento guide</a> to creating filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    sku: Optional[str] = Field(None, description="Stock-keeping unit of the product")
    email: Optional[str] = Field(None, description="Email address of the user to create")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filter_json: Optional[str] = Field(None, description="Filters (JSON)")
    order_id: Optional[str] = Field(None, description="Order ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    filter_type: Optional[str] = Field(None, description="Filter")
    match_type: Optional[str] = Field(None, description="Must Match")


class Magento2CancelTool(BaseTool):
    name: str = "magento2_cancel"
    connector_id: str = "nodes-base.magento2"
    description: str = "Tool for magento2 cancel operation - cancel operation"
    args_schema: type[BaseModel] | None = Magento2CancelToolInput
    credentials: Optional[Magento2Credentials] = None
