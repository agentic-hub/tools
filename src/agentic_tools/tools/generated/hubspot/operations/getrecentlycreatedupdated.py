from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HubspotCredentials

class HubspotGetrecentlycreatedupdatedToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    engagement_id: Optional[Dict[str, Any]] = Field(None, description="Engagement to Get")
    email: Optional[str] = Field(None, description="Email")
    ticket_id: Optional[Dict[str, Any]] = Field(None, description="Ticket to Update")
    id: Optional[float] = Field(None, description="Contact to Add")
    company_id: Optional[Dict[str, Any]] = Field(None, description="Company to Update")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[float] = Field(None, description="List to Add To")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Options")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata")
    deal_id: Optional[Dict[str, Any]] = Field(None, description="Deal to Update")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[Dict[str, Any]] = Field(None, description="This is not a contact's email but a number like 1485")
    filter_groups_ui: Optional[Dict[str, Any]] = Field(None, description="When multiple filters are provided within a Filter Group, they will be combined using a logical AND operator. When multiple Filter Groups are provided, they will be combined using a logical OR operator. The system supports a maximum of three Filter Groups with up to three filters each. More info <a href=\"https://developers.hubspot.com/docs/api/crm/search\">here</a>")


class HubspotGetrecentlycreatedupdatedTool(BaseTool):
    name: str = "hubspot_getrecentlycreatedupdated"
    connector_id: str = "nodes-base.hubspot"
    description: str = "Tool for hubspot getRecentlyCreatedUpdated operation - getRecentlyCreatedUpdated operation"
    args_schema: type[BaseModel] | None = HubspotGetrecentlycreatedupdatedToolInput
    credentials: Optional[HubspotCredentials] = None
