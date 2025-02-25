from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GsuiteadminGetallToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    userId: Optional[str] = Field(None, description="The value can be the user's primary email address, alias email address, or unique user ID")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    groupId: Optional[str] = Field(None, description="Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.")
    projection: Optional[str] = Field(None, description="What subset of fields to fetch for this user")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class GsuiteadminGetallTool(BaseTool):
    name = "gsuiteadmin_getall"
    description = "Tool for gSuiteAdmin getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the gSuiteAdmin getAll operation."""
        # Implement the tool logic here
        return f"Running gSuiteAdmin getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gSuiteAdmin getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
