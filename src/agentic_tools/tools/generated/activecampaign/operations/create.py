from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ActivecampaignCredentials(BaseModel):
    """Credentials for activeCampaign authentication."""
    active_campaign_api: Optional[Dict[str, Any]] = Field(None, description="activeCampaignApi")

class ActivecampaignCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ActivecampaignCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="The fields to update")
    externalid: Optional[str] = Field(None, description="The ID of the account in the external service")
    order_products: Optional[List[Any]] = Field(None, description="All ordered products")
    contact: Optional[float] = Field(None, description="Contact ID")
    abandoned_date: Optional[str] = Field(None, description="The date the cart was abandoned. REQUIRED ONLY IF INCLUDING EXTERNALCHECKOUTID.")
    connection_id: Optional[float] = Field(None, description="ID of the connection to update")
    ecommerce_customer_id: Optional[float] = Field(None, description="ID of the E-commerce customer to update")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[float] = Field(None, description="The value of the deal in cents")
    logo_url: Optional[str] = Field(None, description="The URL to a logo image for the external service")
    update_if_exists: Optional[bool] = Field(None, description="Whether to update user if it exists already. If not set and user exists it will error instead.")
    email: Optional[str] = Field(None, description="The email of the contact to create")
    external_created_date: Optional[str] = Field(None, description="The date the order was placed")
    account: Optional[float] = Field(None, description="Account ID")
    total_price: Optional[float] = Field(None, description="The total price of the order in cents, including tax and shipping charges. (i.e. $456.78 => 45678). Must be greater than or equal to zero.")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[float] = Field(None, description="ID of the account to update")
    name: Optional[str] = Field(None, description="Name of the new tag")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[float] = Field(None, description="List ID")
    tag_id: Optional[float] = Field(None, description="ID of the tag to update")
    customerid: Optional[float] = Field(None, description="The ID of the customer associated with this order")
    account_contact_id: Optional[float] = Field(None, description="ID of the account contact to delete")
    group: Optional[str] = Field(None, description="The pipeline ID of the deal")
    stage: Optional[str] = Field(None, description="The stage ID of the deal")
    order_id: Optional[float] = Field(None, description="The ID of the e-commerce order")
    link_url: Optional[str] = Field(None, description="The URL to a page where the integration with the external service can be managed in the third-party's website")
    currency: Optional[str] = Field(None, description="The currency of the deal in 3-character ISO format")
    deal_id: Optional[float] = Field(None, description="ID of the deal to update")
    deal_note: Optional[str] = Field(None, description="The content of the deal note")
    source: Optional[float] = Field(None, description="The order source code (0 - will not trigger automations, 1 - will trigger automations)")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[float] = Field(None, description="Contact ID")
    service: Optional[str] = Field(None, description="The name of the service")
    connectionid: Optional[float] = Field(None, description="The ID of the connection from which this order originated")
    title: Optional[str] = Field(None, description="The title of the deal")
    externalcheckoutid: Optional[str] = Field(None, description="The ID of the cart in the external service. ONLY REQUIRED IF EXTERNALID IS NOT INCLUDED.")
    owner: Optional[str] = Field(None, description="The owner ID of the deal")
    tag_type: Optional[str] = Field(None, description="Tag-type of the new tag")


class ActivecampaignCreateTool(BaseTool):
    name = "activecampaign_create"
    description = "Tool for activeCampaign create operation - create operation"
    
    def __init__(self, credentials: Optional[ActivecampaignCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the activeCampaign create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running activeCampaign create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running activeCampaign create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the activeCampaign create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
