from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AutopilotAddToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[str] = Field(None, description="ID of the list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    contactId: Optional[str] = Field(None, description="Can be ID or email")
    triggerId: Optional[str] = Field(None, description="List ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class AutopilotAddTool(BaseTool):
    name = "autopilot_add"
    description = "Tool for autopilot add operation - add operation"
    
    def _run(self, **kwargs):
        """Run the autopilot add operation."""
        # Implement the tool logic here
        return f"Running autopilot add operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the autopilot add operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
