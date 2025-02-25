from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshserviceCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    releaseId: Optional[str] = Field(None, description="ID of the release to delete")
    softwareId: Optional[str] = Field(None, description="ID of the software application to delete")
    locationId: Optional[str] = Field(None, description="ID of the location to delete")
    description: Optional[str] = Field(None, description="HTML supported")
    announcementId: Optional[str] = Field(None, description="ID of the announcement to delete")
    bodyHtml: Optional[str] = Field(None, description="HTML supported")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    agentGroupId: Optional[str] = Field(None, description="ID of the agent group to delete")
    visibleFrom: Optional[str] = Field(None, description="Timestamp at which announcement becomes active")
    subject: Optional[str] = Field(None, description="Subject")
    ticketId: Optional[str] = Field(None, description="ID of the ticket to delete")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    assetTypeId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    agentId: Optional[str] = Field(None, description="ID of the agent to delete")
    requesterId: Optional[str] = Field(None, description="ID of the requester of the change. Choose from the list or specify an ID. You can also specify the ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    changeId: Optional[str] = Field(None, description="ID of the change to delete")
    releaseType: Optional[str] = Field(None, description="Release Type")
    roles: Optional[Dict[str, Any]] = Field(None, description="Role to assign to the agent")
    problemId: Optional[str] = Field(None, description="ID of the problem to delete")
    departmentId: Optional[str] = Field(None, description="ID of the department to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    plannedEndDate: Optional[str] = Field(None, description="Planned End Date")
    firstName: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    visibility: Optional[str] = Field(None, description="Visibility")
    status: Optional[str] = Field(None, description="Status")
    applicationType: Optional[str] = Field(None, description="Application Type")
    dueBy: Optional[str] = Field(None, description="Date when the problem is due to be solved")
    priority: Optional[str] = Field(None, description="Priority")
    title: Optional[str] = Field(None, description="Title")
    plannedStartDate: Optional[str] = Field(None, description="Planned Start Date")
    requesterGroupId: Optional[str] = Field(None, description="ID of the requester group to delete")
    productId: Optional[str] = Field(None, description="ID of the product to delete")
    primaryEmail: Optional[str] = Field(None, description="Primary Email")


class FreshserviceCreateTool(BaseTool):
    name = "freshservice_create"
    description = "Tool for freshservice create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the freshservice create operation."""
        # Implement the tool logic here
        return f"Running freshservice create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshservice create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
