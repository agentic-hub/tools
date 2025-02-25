from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OnfleetGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    containerType: Optional[str] = Field(None, description="Container Type")
    containerId: Optional[str] = Field(None, description="The object ID according to the container chosen")
    teams: Optional[str] = Field(None, description="teams")
    workers: Optional[str] = Field(None, description="workers")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the admin object for lookup")
    phone: Optional[str] = Field(None, description="The phone of the recipient for lookup")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the recipient for lookup")
    managers: Optional[str] = Field(None, description="managers")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    destination: Optional[Dict[str, Any]] = Field(None, description="Destination")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    getBy: Optional[str] = Field(None, description="The variable that is used for looking up a recipient")
    resource: Optional[str] = Field(None, description="The resource to perform operations on")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class OnfleetGetTool(BaseTool):
    name = "onfleet_get"
    description = "Tool for onfleet get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the onfleet get operation."""
        # Implement the tool logic here
        return f"Running onfleet get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the onfleet get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
