from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OnfleetGetallToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    latitude: Optional[float] = Field(None, description="The latitude component of the coordinate pair")
    teams: Optional[str] = Field(None, description="teams")
    workers: Optional[str] = Field(None, description="workers")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the admin object for lookup")
    byLocation: Optional[bool] = Field(None, description="Whether to search for only those workers who are currently within a certain target area")
    phone: Optional[str] = Field(None, description="The phone of the recipient for lookup")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The administrator's name")
    managers: Optional[str] = Field(None, description="managers")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    longitude: Optional[float] = Field(None, description="The longitude component of the coordinate pair")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    destination: Optional[Dict[str, Any]] = Field(None, description="Destination")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="The resource to perform operations on")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class OnfleetGetallTool(BaseTool):
    name = "onfleet_getall"
    description = "Tool for onfleet getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the onfleet getAll operation."""
        # Implement the tool logic here
        return f"Running onfleet getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the onfleet getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
