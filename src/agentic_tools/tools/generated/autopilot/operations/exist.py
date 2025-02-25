from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AutopilotExistToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[str] = Field(None, description="ID of the list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    contactId: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutopilotExistTool(BaseTool):
    name = "autopilot_exist"
    description = "Tool for autopilot exist operation - exist operation"
    
    def _run(self, **kwargs):
        """Run the autopilot exist operation."""
        # Implement the tool logic here
        return f"Running autopilot exist operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the autopilot exist operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
