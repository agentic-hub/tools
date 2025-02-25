from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PipedriveSearchToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    fileId: Optional[float] = Field(None, description="ID of the file to delete")
    exactMatch: Optional[bool] = Field(None, description="Whether only full exact matches against the given term are returned. It is not case sensitive.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryPropertyName: Optional[str] = Field(None, description="Input Binary Field")
    person_id: Optional[float] = Field(None, description="ID of the person this deal will be associated with")
    activityId: Optional[float] = Field(None, description="ID of the activity to delete")
    operation: Optional[str] = Field(None, description="Operation")
    productAttachmentId: Optional[str] = Field(None, description="ID of the deal-product (the ID of the product attached to the deal). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    name: Optional[str] = Field(None, description="The name of the organization to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    associateWith: Optional[str] = Field(None, description="Type of entity to link to this deal")
    personId: Optional[float] = Field(None, description="ID of the person to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    dealId: Optional[float] = Field(None, description="ID of the deal to delete")
    term: Optional[str] = Field(None, description="The search term to look for. Minimum 2 characters (or 1 if using exact_match).")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    organizationId: Optional[float] = Field(None, description="ID of the organization to delete")
    authentication: Optional[str] = Field(None, description="Authentication")
    noteId: Optional[float] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="The title of the deal to create")
    leadId: Optional[str] = Field(None, description="ID of the lead to delete")


class PipedriveSearchTool(BaseTool):
    name = "pipedrive_search"
    description = "Tool for pipedrive search operation - search operation"
    
    def _run(self, **kwargs):
        """Run the pipedrive search operation."""
        # Implement the tool logic here
        return f"Running pipedrive search operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pipedrive search operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
