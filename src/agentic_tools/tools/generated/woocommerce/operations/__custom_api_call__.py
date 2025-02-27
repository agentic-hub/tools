from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WoocommerceCredentials

class Woocommerce__custom_api_call__ToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    customer_id: Optional[str] = Field(None, description="ID of the customer to delete")
    dimensions_ui: Optional[Dict[str, Any]] = Field(None, description="Product dimensions")
    shipping_lines_ui: Optional[Dict[str, Any]] = Field(None, description="Shipping line data")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    images_ui: Optional[Dict[str, Any]] = Field(None, description="Product Image")
    fee_lines_ui: Optional[Dict[str, Any]] = Field(None, description="Fee line data")
    line_items_ui: Optional[Dict[str, Any]] = Field(None, description="Line item data")
    operation: Optional[str] = Field(None, description="Operation")
    billing_ui: Optional[Dict[str, Any]] = Field(None, description="Billing address")
    shipping_ui: Optional[Dict[str, Any]] = Field(None, description="Shipping address")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    coupon_lines_ui: Optional[Dict[str, Any]] = Field(None, description="Coupons line data")
    order_id: Optional[str] = Field(None, description="Order ID")
    metadata_ui: Optional[Dict[str, Any]] = Field(None, description="Meta data")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    product_id: Optional[str] = Field(None, description="Product ID")


class Woocommerce__custom_api_call__Tool(BaseTool):
    name: str = "woocommerce___custom_api_call__"
    description: str = "Tool for wooCommerce __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Woocommerce__custom_api_call__ToolInput
    credentials: Optional[WoocommerceCredentials] = None
