from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ActivecampaignCredentials(BaseModel):
    """Credentials for activeCampaign authentication."""
    active_campaign_api: Optional[Dict[str, Any]] = Field(None, description="activeCampaignApi")

class ActivecampaignGetbyproductidToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ActivecampaignCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="The fields to update")
    externalid: Optional[str] = Field(None, description="The ID of the account in the external service")
    procuct_id: Optional[float] = Field(None, description="The ID of the product you'd like returned")
    contact: Optional[float] = Field(None, description="Contact ID")
    connection_id: Optional[float] = Field(None, description="ID of the connection to update")
    ecommerce_customer_id: Optional[float] = Field(None, description="ID of the E-commerce customer to update")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The email of the contact to create")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[float] = Field(None, description="ID of the account to update")
    name: Optional[str] = Field(None, description="Name of the new tag")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[float] = Field(None, description="List ID")
    tag_id: Optional[float] = Field(None, description="ID of the tag to update")
    account_contact_id: Optional[float] = Field(None, description="ID of the account contact to delete")
    order_id: Optional[float] = Field(None, description="The ID of the e-commerce order")
    currency: Optional[str] = Field(None, description="The currency of the deal in 3-character ISO format")
    deal_id: Optional[float] = Field(None, description="ID of the deal to update")
    deal_note: Optional[str] = Field(None, description="The content of the deal note")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[float] = Field(None, description="Contact ID")
    connectionid: Optional[float] = Field(None, description="The ID of the connection from which this order originated")


class ActivecampaignGetbyproductidTool(BaseTool):
    name = "activecampaign_getbyproductid"
    description = "Tool for activeCampaign getByProductId operation - getByProductId operation"
    
    def __init__(self, credentials: Optional[ActivecampaignCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the activeCampaign getByProductId operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running activeCampaign getByProductId operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running activeCampaign getByProductId operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the activeCampaign getByProductId operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
