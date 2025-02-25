from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ActivecampaignCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="The fields to update")
    externalid: Optional[str] = Field(None, description="The ID of the account in the external service")
    orderProducts: Optional[List[Any]] = Field(None, description="All ordered products")
    contact: Optional[float] = Field(None, description="Contact ID")
    abandonedDate: Optional[str] = Field(None, description="The date the cart was abandoned. REQUIRED ONLY IF INCLUDING EXTERNALCHECKOUTID.")
    connectionId: Optional[float] = Field(None, description="ID of the connection to update")
    ecommerceCustomerId: Optional[float] = Field(None, description="ID of the E-commerce customer to update")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[float] = Field(None, description="The value of the deal in cents")
    logoUrl: Optional[str] = Field(None, description="The URL to a logo image for the external service")
    updateIfExists: Optional[bool] = Field(None, description="Whether to update user if it exists already. If not set and user exists it will error instead.")
    email: Optional[str] = Field(None, description="The email of the contact to create")
    externalCreatedDate: Optional[str] = Field(None, description="The date the order was placed")
    account: Optional[float] = Field(None, description="Account ID")
    totalPrice: Optional[float] = Field(None, description="The total price of the order in cents, including tax and shipping charges. (i.e. $456.78 => 45678). Must be greater than or equal to zero.")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[float] = Field(None, description="ID of the account to update")
    name: Optional[str] = Field(None, description="Name of the new tag")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[float] = Field(None, description="List ID")
    tagId: Optional[float] = Field(None, description="ID of the tag to update")
    customerid: Optional[float] = Field(None, description="The ID of the customer associated with this order")
    accountContactId: Optional[float] = Field(None, description="ID of the account contact to delete")
    group: Optional[str] = Field(None, description="The pipeline ID of the deal")
    stage: Optional[str] = Field(None, description="The stage ID of the deal")
    orderId: Optional[float] = Field(None, description="The ID of the e-commerce order")
    linkUrl: Optional[str] = Field(None, description="The URL to a page where the integration with the external service can be managed in the third-party's website")
    currency: Optional[str] = Field(None, description="The currency of the deal in 3-character ISO format")
    dealId: Optional[float] = Field(None, description="ID of the deal to update")
    dealNote: Optional[str] = Field(None, description="The content of the deal note")
    source: Optional[float] = Field(None, description="The order source code (0 - will not trigger automations, 1 - will trigger automations)")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contactId: Optional[float] = Field(None, description="Contact ID")
    service: Optional[str] = Field(None, description="The name of the service")
    connectionid: Optional[float] = Field(None, description="The ID of the connection from which this order originated")
    title: Optional[str] = Field(None, description="The title of the deal")
    externalcheckoutid: Optional[str] = Field(None, description="The ID of the cart in the external service. ONLY REQUIRED IF EXTERNALID IS NOT INCLUDED.")
    owner: Optional[str] = Field(None, description="The owner ID of the deal")
    tagType: Optional[str] = Field(None, description="Tag-type of the new tag")


class ActivecampaignCreateTool(BaseTool):
    name = "activecampaign_create"
    description = "Tool for activeCampaign create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the activeCampaign create operation."""
        # Implement the tool logic here
        return f"Running activeCampaign create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the activeCampaign create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
