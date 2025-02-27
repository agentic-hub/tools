from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HubspotCredentials

class HubspotCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    ticket_name: Optional[str] = Field(None, description="Ticket Name")
    type: Optional[str] = Field(None, description="Type")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    engagement_id: Optional[Dict[str, Any]] = Field(None, description="Engagement to Get")
    email: Optional[str] = Field(None, description="Email")
    ticket_id: Optional[Dict[str, Any]] = Field(None, description="Ticket to Update")
    id: Optional[float] = Field(None, description="Contact to Add")
    company_id: Optional[Dict[str, Any]] = Field(None, description="Company to Update")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[float] = Field(None, description="List to Add To")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    stage: Optional[str] = Field(None, description="The deal stage is required when creating a deal. See the CRM Pipelines API for details on managing pipelines and stages. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    stage_id: Optional[str] = Field(None, description="The stage ID of the pipeline the ticket is in; depends on Pipeline ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata")
    deal_id: Optional[Dict[str, Any]] = Field(None, description="Deal to Update")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Company Properties")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[Dict[str, Any]] = Field(None, description="This is not a contact's email but a number like 1485")
    pipeline_id: Optional[str] = Field(None, description="The ID of the pipeline the ticket is in. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    filter_groups_ui: Optional[Dict[str, Any]] = Field(None, description="When multiple filters are provided within a Filter Group, they will be combined using a logical AND operator. When multiple Filter Groups are provided, they will be combined using a logical OR operator. The system supports a maximum of three Filter Groups with up to three filters each. More info <a href=\"https://developers.hubspot.com/docs/api/crm/search\">here</a>")


class HubspotCreateTool(BaseTool):
    name: str = "hubspot_create"
    connector_id: str = "nodes-base.hubspot"
    description: str = "Tool for hubspot create operation - create operation"
    args_schema: type[BaseModel] | None = HubspotCreateToolInput
    credentials: Optional[HubspotCredentials] = None
