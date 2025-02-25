from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PaddleCredentials(BaseModel):
    """Credentials for paddle authentication."""
    paddle_api: Optional[Dict[str, Any]] = Field(None, description="paddleApi")

class PaddleCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PaddleCredentials] = Field(None, description="Custom credentials for authentication")
    discount_amount: Optional[float] = Field(None, description="Discount amount in currency")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    coupon_type: Optional[str] = Field(None, description="Either product (valid for specified products or subscription plans) or checkout (valid for any checkout)")
    additional_fields_json: Optional[str] = Field(None, description="Attributes in JSON form")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    product_ids: Optional[str] = Field(None, description="productIds")
    discount_type: Optional[str] = Field(None, description="Either flat or percentage")
    currency: Optional[str] = Field(None, description="The currency must match the balance currency specified in your account")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class PaddleCreateTool(BaseTool):
    name = "paddle_create"
    description = "Tool for paddle create operation - create operation"
    
    def __init__(self, credentials: Optional[PaddleCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the paddle create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running paddle create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running paddle create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the paddle create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
