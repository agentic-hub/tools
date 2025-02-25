from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HalopsaGetallToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    siteId: Optional[str] = Field(None, description="Site ID")
    userId: Optional[str] = Field(None, description="User ID")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    ticketId: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    clientId: Optional[str] = Field(None, description="Client ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    simplify: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class HalopsaGetallTool(BaseTool):
    name = "halopsa_getall"
    description = "Tool for haloPSA getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the haloPSA getAll operation."""
        # Implement the tool logic here
        return f"Running haloPSA getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the haloPSA getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
