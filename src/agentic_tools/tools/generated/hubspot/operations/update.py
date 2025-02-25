from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HubspotUpdateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    engagementId: Optional[Dict[str, Any]] = Field(None, description="Engagement to Get")
    email: Optional[str] = Field(None, description="Email")
    ticketId: Optional[Dict[str, Any]] = Field(None, description="Ticket to Update")
    id: Optional[float] = Field(None, description="Contact to Add")
    companyId: Optional[Dict[str, Any]] = Field(None, description="Company to Update")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[float] = Field(None, description="List to Add To")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata")
    dealId: Optional[Dict[str, Any]] = Field(None, description="Deal to Update")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Contact Properties")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contactId: Optional[Dict[str, Any]] = Field(None, description="This is not a contact's email but a number like 1485")
    filterGroupsUi: Optional[Dict[str, Any]] = Field(None, description="When multiple filters are provided within a Filter Group, they will be combined using a logical AND operator. When multiple Filter Groups are provided, they will be combined using a logical OR operator. The system supports a maximum of three Filter Groups with up to three filters each. More info <a href=\"https://developers.hubspot.com/docs/api/crm/search\">here</a>")


class HubspotUpdateTool(BaseTool):
    name = "hubspot_update"
    description = "Tool for hubspot update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the hubspot update operation."""
        # Implement the tool logic here
        return f"Running hubspot update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the hubspot update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
