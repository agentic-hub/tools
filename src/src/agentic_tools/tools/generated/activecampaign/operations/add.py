from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ActivecampaignAddToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="The fields to update")
    externalid: Optional[str] = Field(None, description="The ID of the account in the external service")
    contact: Optional[float] = Field(None, description="Contact ID")
    connectionId: Optional[float] = Field(None, description="ID of the connection to update")
    ecommerceCustomerId: Optional[float] = Field(None, description="ID of the E-commerce customer to update")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The email of the contact to create")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[float] = Field(None, description="ID of the account to update")
    name: Optional[str] = Field(None, description="Name of the new tag")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[float] = Field(None, description="List ID")
    tagId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    accountContactId: Optional[float] = Field(None, description="ID of the account contact to delete")
    orderId: Optional[float] = Field(None, description="The ID of the e-commerce order")
    currency: Optional[str] = Field(None, description="The currency of the deal in 3-character ISO format")
    dealId: Optional[float] = Field(None, description="ID of the deal to update")
    dealNote: Optional[str] = Field(None, description="The content of the deal note")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contactId: Optional[float] = Field(None, description="Contact ID")
    connectionid: Optional[float] = Field(None, description="The ID of the connection from which this order originated")


class ActivecampaignAddTool(BaseTool):
    name = "activecampaign_add"
    description = "Tool for activeCampaign add operation - add operation"
    
    def _run(self, **kwargs):
        """Run the activeCampaign add operation."""
        # Implement the tool logic here
        return f"Running activeCampaign add operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the activeCampaign add operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
