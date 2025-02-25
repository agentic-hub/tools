from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WoocommerceCredentials(BaseModel):
    """Credentials for wooCommerce authentication."""
    woo_commerce_api: Optional[Dict[str, Any]] = Field(None, description="wooCommerceApi")

class WoocommerceGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[WoocommerceCredentials] = Field(None, description="Custom credentials for authentication")
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
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    metadata_ui: Optional[Dict[str, Any]] = Field(None, description="Meta data")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    product_id: Optional[str] = Field(None, description="Product ID")


class WoocommerceGetallTool(BaseTool):
    name = "woocommerce_getall"
    description = "Tool for wooCommerce getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[WoocommerceCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the wooCommerce getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running wooCommerce getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running wooCommerce getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the wooCommerce getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
