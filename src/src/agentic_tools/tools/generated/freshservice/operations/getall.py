from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshserviceGetallToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    releaseId: Optional[str] = Field(None, description="ID of the release to delete")
    softwareId: Optional[str] = Field(None, description="ID of the software application to delete")
    locationId: Optional[str] = Field(None, description="ID of the location to delete")
    announcementId: Optional[str] = Field(None, description="ID of the announcement to delete")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    agentGroupId: Optional[str] = Field(None, description="ID of the agent group to delete")
    subject: Optional[str] = Field(None, description="Subject")
    ticketId: Optional[str] = Field(None, description="ID of the ticket to delete")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    assetTypeId: Optional[str] = Field(None, description="ID of the asset type to delete")
    agentId: Optional[str] = Field(None, description="ID of the agent to delete")
    requesterId: Optional[str] = Field(None, description="ID of the requester of the change. Choose from the list or specify an ID. You can also specify the ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    changeId: Optional[str] = Field(None, description="ID of the change to delete")
    problemId: Optional[str] = Field(None, description="ID of the problem to delete")
    departmentId: Optional[str] = Field(None, description="ID of the department to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    plannedEndDate: Optional[str] = Field(None, description="Planned End Date")
    firstName: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    priority: Optional[str] = Field(None, description="Priority")
    plannedStartDate: Optional[str] = Field(None, description="Planned Start Date")
    requesterGroupId: Optional[str] = Field(None, description="ID of the requester group to delete")
    productId: Optional[str] = Field(None, description="ID of the product to delete")


class FreshserviceGetallTool(BaseTool):
    name = "freshservice_getall"
    description = "Tool for freshservice getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the freshservice getAll operation."""
        # Implement the tool logic here
        return f"Running freshservice getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshservice getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
