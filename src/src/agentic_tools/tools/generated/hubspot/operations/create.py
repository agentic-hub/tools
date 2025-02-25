from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HubspotCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    ticketName: Optional[str] = Field(None, description="Ticket Name")
    type: Optional[str] = Field(None, description="Type")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    engagementId: Optional[Dict[str, Any]] = Field(None, description="Engagement to Get")
    email: Optional[str] = Field(None, description="Email")
    ticketId: Optional[Dict[str, Any]] = Field(None, description="Ticket to Update")
    id: Optional[float] = Field(None, description="Contact to Add")
    companyId: Optional[Dict[str, Any]] = Field(None, description="Company to Update")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[float] = Field(None, description="List to Add To")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    stage: Optional[str] = Field(None, description="The deal stage is required when creating a deal. See the CRM Pipelines API for details on managing pipelines and stages. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    stageId: Optional[str] = Field(None, description="The stage ID of the pipeline the ticket is in; depends on Pipeline ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata")
    dealId: Optional[Dict[str, Any]] = Field(None, description="Deal to Update")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Company Properties")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contactId: Optional[Dict[str, Any]] = Field(None, description="This is not a contact's email but a number like 1485")
    pipelineId: Optional[str] = Field(None, description="The ID of the pipeline the ticket is in. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    filterGroupsUi: Optional[Dict[str, Any]] = Field(None, description="When multiple filters are provided within a Filter Group, they will be combined using a logical AND operator. When multiple Filter Groups are provided, they will be combined using a logical OR operator. The system supports a maximum of three Filter Groups with up to three filters each. More info <a href=\"https://developers.hubspot.com/docs/api/crm/search\">here</a>")


class HubspotCreateTool(BaseTool):
    name = "hubspot_create"
    description = "Tool for hubspot create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the hubspot create operation."""
        # Implement the tool logic here
        return f"Running hubspot create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the hubspot create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
