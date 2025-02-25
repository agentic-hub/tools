from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CopperGetallToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    taskId: Optional[str] = Field(None, description="ID of the task to delete")
    opportunityId: Optional[str] = Field(None, description="ID of the opportunity to delete")
    name: Optional[str] = Field(None, description="Name of the company to create")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    projectId: Optional[str] = Field(None, description="ID of the project to delete")
    personId: Optional[str] = Field(None, description="ID of the person to delete")
    leadId: Optional[str] = Field(None, description="ID of the lead to delete")
    companyId: Optional[str] = Field(None, description="ID of the company to delete")
    operation: Optional[str] = Field(None, description="Operation")
    filterFields: Optional[Dict[str, Any]] = Field(None, description="Filters")


class CopperGetallTool(BaseTool):
    name = "copper_getall"
    description = "Tool for copper getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the copper getAll operation."""
        # Implement the tool logic here
        return f"Running copper getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the copper getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
