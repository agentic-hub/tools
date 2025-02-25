from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NetlifyCancelToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    siteId: Optional[str] = Field(None, description="Enter the Site ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    deployId: Optional[str] = Field(None, description="Deploy ID")
    operation: Optional[str] = Field(None, description="Operation")


class NetlifyCancelTool(BaseTool):
    name = "netlify_cancel"
    description = "Tool for netlify cancel operation - cancel operation"
    
    def _run(self, **kwargs):
        """Run the netlify cancel operation."""
        # Implement the tool logic here
        return f"Running netlify cancel operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the netlify cancel operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
