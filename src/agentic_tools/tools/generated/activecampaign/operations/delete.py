from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ActivecampaignCredentials

class ActivecampaignDeleteToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="The fields to update")
    externalid: Optional[str] = Field(None, description="The ID of the account in the external service")
    contact: Optional[float] = Field(None, description="Contact ID")
    connection_id: Optional[float] = Field(None, description="ID of the connection to delete")
    ecommerce_customer_id: Optional[float] = Field(None, description="ID of the E-commerce customer to delete")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The email of the contact to create")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[float] = Field(None, description="ID of the account to delete")
    name: Optional[str] = Field(None, description="Name of the new tag")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[float] = Field(None, description="List ID")
    tag_id: Optional[float] = Field(None, description="ID of the tag to delete")
    account_contact_id: Optional[float] = Field(None, description="ID of the account contact to delete")
    order_id: Optional[float] = Field(None, description="The ID of the e-commerce order")
    currency: Optional[str] = Field(None, description="The currency of the deal in 3-character ISO format")
    deal_id: Optional[float] = Field(None, description="The ID of the deal to delete")
    deal_note: Optional[str] = Field(None, description="The content of the deal note")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[float] = Field(None, description="ID of the contact to delete")
    connectionid: Optional[float] = Field(None, description="The ID of the connection from which this order originated")


class ActivecampaignDeleteTool(BaseTool):
    name: str = "activecampaign_delete"
    description: str = "Tool for activeCampaign delete operation - delete operation"
    args_schema: type[BaseModel] | None = ActivecampaignDeleteToolInput
    credentials: Optional[ActivecampaignCredentials] = None
