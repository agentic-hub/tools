from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OnfleetUpdatetaskToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    containerId: Optional[str] = Field(None, description="The object ID according to the container chosen")
    teams: Optional[str] = Field(None, description="teams")
    workers: Optional[str] = Field(None, description="workers")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the admin object for lookup")
    phone: Optional[str] = Field(None, description="The phone of the recipient for lookup")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The administrator's name")
    managers: Optional[str] = Field(None, description="managers")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    tasks: Optional[str] = Field(None, description="Task's ID that are going to be used")
    destination: Optional[Dict[str, Any]] = Field(None, description="Destination")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="The resource to perform operations on")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class OnfleetUpdatetaskTool(BaseTool):
    name = "onfleet_updatetask"
    description = "Tool for onfleet updateTask operation - updateTask operation"
    
    def _run(self, **kwargs):
        """Run the onfleet updateTask operation."""
        # Implement the tool logic here
        return f"Running onfleet updateTask operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the onfleet updateTask operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
