from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class KitemakerGetallToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    spaceId: Optional[str] = Field(None, description="ID of the space to retrieve the work items from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    workItemId: Optional[str] = Field(None, description="ID of the work item to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class KitemakerGetallTool(BaseTool):
    name = "kitemaker_getall"
    description = "Tool for kitemaker getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the kitemaker getAll operation."""
        # Implement the tool logic here
        return f"Running kitemaker getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the kitemaker getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
