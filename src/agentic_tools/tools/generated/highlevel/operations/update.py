from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HighlevelUpdateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email or Phone are required to create contact")
    phone: Optional[str] = Field(None, description="Phone or Email are required to create contact. Phone number has to start with a valid <a href=\"https://en.wikipedia.org/wiki/List_of_country_calling_codes\">country code</a> leading with + sign.")
    operation: Optional[str] = Field(None, description="Operation")
    taskId: Optional[str] = Field(None, description="Task ID")
    opportunityId: Optional[str] = Field(None, description="Opportunity ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contactId: Optional[str] = Field(None, description="Contact ID")
    pipelineId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    title: Optional[str] = Field(None, description="Title")


class HighlevelUpdateTool(BaseTool):
    name = "highlevel_update"
    description = "Tool for highLevel update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the highLevel update operation."""
        # Implement the tool logic here
        return f"Running highLevel update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the highLevel update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
