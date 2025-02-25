from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PipedriveGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resolveProperties: Optional[bool] = Field(None, description="By default do custom properties get returned only as ID instead of their actual name. Also option fields contain only the ID instead of their actual value. If this option gets set they get automatically resolved.")
    fileId: Optional[float] = Field(None, description="ID of the file to get")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryPropertyName: Optional[str] = Field(None, description="Input Binary Field")
    person_id: Optional[float] = Field(None, description="ID of the person this deal will be associated with")
    activityId: Optional[float] = Field(None, description="ID of the activity to get")
    operation: Optional[str] = Field(None, description="Operation")
    productAttachmentId: Optional[str] = Field(None, description="ID of the deal-product (the ID of the product attached to the deal). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    name: Optional[str] = Field(None, description="The name of the organization to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    associateWith: Optional[str] = Field(None, description="Type of entity to link to this deal")
    personId: Optional[float] = Field(None, description="ID of the person to get")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    dealId: Optional[float] = Field(None, description="ID of the deal to get")
    term: Optional[str] = Field(None, description="The search term to look for. Minimum 2 characters (or 1 if using exact_match).")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    organizationId: Optional[float] = Field(None, description="ID of the organization to get")
    authentication: Optional[str] = Field(None, description="Authentication")
    noteId: Optional[float] = Field(None, description="ID of the note to get")
    title: Optional[str] = Field(None, description="The title of the deal to create")
    leadId: Optional[str] = Field(None, description="ID of the lead to retrieve")


class PipedriveGetTool(BaseTool):
    name = "pipedrive_get"
    description = "Tool for pipedrive get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the pipedrive get operation."""
        # Implement the tool logic here
        return f"Running pipedrive get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pipedrive get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
