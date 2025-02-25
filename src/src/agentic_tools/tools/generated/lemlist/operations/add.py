from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LemlistAddToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    campaignId: Optional[str] = Field(None, description="ID of the campaign to create the lead under. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    email: Optional[str] = Field(None, description="Email to add to the unsubscribes")
    operation: Optional[str] = Field(None, description="Operation")


class LemlistAddTool(BaseTool):
    name = "lemlist_add"
    description = "Tool for lemlist add operation - add operation"
    
    def _run(self, **kwargs):
        """Run the lemlist add operation."""
        # Implement the tool logic here
        return f"Running lemlist add operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the lemlist add operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
