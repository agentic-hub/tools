from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LemlistDeleteToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    campaignId: Optional[str] = Field(None, description="ID of the campaign to remove the lead from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    email: Optional[str] = Field(None, description="Email of the lead to delete")
    operation: Optional[str] = Field(None, description="Operation")


class LemlistDeleteTool(BaseTool):
    name = "lemlist_delete"
    description = "Tool for lemlist delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the lemlist delete operation."""
        # Implement the tool logic here
        return f"Running lemlist delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the lemlist delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
