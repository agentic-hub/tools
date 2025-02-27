from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ShopifyCredentials

class ShopifyCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="The name of the product")
    order_id: Optional[str] = Field(None, description="Order ID")
    lime_items_ui: Optional[Dict[str, Any]] = Field(None, description="Line Items")
    product_id: Optional[str] = Field(None, description="Product ID")
    operation: Optional[str] = Field(None, description="Operation")


class ShopifyCreateTool(BaseTool):
    name: str = "shopify_create"
    description: str = "Tool for shopify create operation - create operation"
    args_schema: type[BaseModel] | None = ShopifyCreateToolInput
    credentials: Optional[ShopifyCredentials] = None
