from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AutopilotDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    contactId: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutopilotDeleteTool(BaseTool):
    name = "autopilot_delete"
    description = "Tool for autopilot delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the autopilot delete operation."""
        # Implement the tool logic here
        return f"Running autopilot delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the autopilot delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
