from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WoocommerceCredentials

class WoocommerceCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    customer_id: Optional[str] = Field(None, description="ID of the customer to delete")
    dimensions_ui: Optional[Dict[str, Any]] = Field(None, description="Product dimensions")
    shipping_lines_ui: Optional[Dict[str, Any]] = Field(None, description="Shipping line data")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    images_ui: Optional[Dict[str, Any]] = Field(None, description="Product Image")
    email: Optional[str] = Field(None, description="Email")
    fee_lines_ui: Optional[Dict[str, Any]] = Field(None, description="Fee line data")
    line_items_ui: Optional[Dict[str, Any]] = Field(None, description="Line item data")
    operation: Optional[str] = Field(None, description="Operation")
    billing_ui: Optional[Dict[str, Any]] = Field(None, description="Billing address")
    name: Optional[str] = Field(None, description="Product name")
    shipping_ui: Optional[Dict[str, Any]] = Field(None, description="Shipping address")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    coupon_lines_ui: Optional[Dict[str, Any]] = Field(None, description="Coupons line data")
    order_id: Optional[str] = Field(None, description="Order ID")
    metadata_ui: Optional[Dict[str, Any]] = Field(None, description="Meta data")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    product_id: Optional[str] = Field(None, description="Product ID")


class WoocommerceCreateTool(BaseTool):
    name: str = "woocommerce_create"
    description: str = "Tool for wooCommerce create operation - create operation"
    args_schema: type[BaseModel] | None = WoocommerceCreateToolInput
    credentials: Optional[WoocommerceCredentials] = None
