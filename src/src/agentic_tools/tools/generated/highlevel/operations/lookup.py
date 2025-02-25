from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HighlevelLookupToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Lookup Contact by Email. If Email is not found it will try to find a contact by phone.")
    phone: Optional[str] = Field(None, description="Lookup Contact by Phone. It will first try to find a contact by Email and than by Phone.")
    operation: Optional[str] = Field(None, description="Operation")
    taskId: Optional[str] = Field(None, description="Task ID")
    opportunityId: Optional[str] = Field(None, description="Opportunity ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contactId: Optional[str] = Field(None, description="Contact ID")
    title: Optional[str] = Field(None, description="Title")


class HighlevelLookupTool(BaseTool):
    name = "highlevel_lookup"
    description = "Tool for highLevel lookup operation - lookup operation"
    
    def _run(self, **kwargs):
        """Run the highLevel lookup operation."""
        # Implement the tool logic here
        return f"Running highLevel lookup operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the highLevel lookup operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
