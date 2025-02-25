from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Magento2Credentials(BaseModel):
    """Credentials for magento2 authentication."""
    magento2_api: Optional[Dict[str, Any]] = Field(None, description="magento2Api")

class Magento2CancelToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[Magento2Credentials] = Field(None, description="Custom credentials for authentication")
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
    name = "magento2_cancel"
    description = "Tool for magento2 cancel operation - cancel operation"
    
    def __init__(self, credentials: Optional[Magento2Credentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the magento2 cancel operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running magento2 cancel operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running magento2 cancel operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the magento2 cancel operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
