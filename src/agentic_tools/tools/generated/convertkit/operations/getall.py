from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConvertkitGetallToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Receive only active subscribers or cancelled subscribers")
    tagId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    email: Optional[str] = Field(None, description="The subscriber's email address")
    id: Optional[str] = Field(None, description="The ID of your custom field")
    operation: Optional[str] = Field(None, description="Operation")


class ConvertkitGetallTool(BaseTool):
    name = "convertkit_getall"
    description = "Tool for convertKit getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the convertKit getAll operation."""
        # Implement the tool logic here
        return f"Running convertKit getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the convertKit getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
