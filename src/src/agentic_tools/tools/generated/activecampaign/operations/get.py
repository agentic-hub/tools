from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ActivecampaignGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="The fields to update")
    externalid: Optional[str] = Field(None, description="The ID of the account in the external service")
    contact: Optional[float] = Field(None, description="Contact ID")
    connectionId: Optional[float] = Field(None, description="ID of the connection to get")
    ecommerceCustomerId: Optional[float] = Field(None, description="ID of the E-commerce customer to get")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The email of the contact to create")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[float] = Field(None, description="ID of the account to get")
    name: Optional[str] = Field(None, description="Name of the new tag")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[float] = Field(None, description="List ID")
    tagId: Optional[float] = Field(None, description="ID of the tag to get")
    accountContactId: Optional[float] = Field(None, description="ID of the account contact to delete")
    orderId: Optional[float] = Field(None, description="The ID of the e-commerce order")
    currency: Optional[str] = Field(None, description="The currency of the deal in 3-character ISO format")
    dealId: Optional[float] = Field(None, description="The ID of the deal to get")
    dealNote: Optional[str] = Field(None, description="The content of the deal note")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contactId: Optional[float] = Field(None, description="ID of the contact to get")
    connectionid: Optional[float] = Field(None, description="The ID of the connection from which this order originated")


class ActivecampaignGetTool(BaseTool):
    name = "activecampaign_get"
    description = "Tool for activeCampaign get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the activeCampaign get operation."""
        # Implement the tool logic here
        return f"Running activeCampaign get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the activeCampaign get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
