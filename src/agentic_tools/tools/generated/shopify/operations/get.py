from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ShopifyCredentials(BaseModel):
    """Credentials for shopify authentication."""
    shopify_api: Optional[Dict[str, Any]] = Field(None, description="shopifyApi")
    shopify_access_token_api: Optional[Dict[str, Any]] = Field(None, description="shopifyAccessTokenApi")
    shopify_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="shopifyOAuth2Api")

class ShopifyGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ShopifyCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    order_id: Optional[str] = Field(None, description="Order ID")
    product_id: Optional[str] = Field(None, description="Product ID")
    operation: Optional[str] = Field(None, description="Operation")


class ShopifyGetTool(BaseTool):
    name = "shopify_get"
    description = "Tool for shopify get operation - get operation"
    
    def __init__(self, credentials: Optional[ShopifyCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the shopify get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running shopify get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running shopify get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the shopify get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
