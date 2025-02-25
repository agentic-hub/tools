from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConvertkitGetsubscriptionsToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Receive only active subscribers or cancelled subscribers")
    email: Optional[str] = Field(None, description="The subscriber's email address")
    id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class ConvertkitGetsubscriptionsTool(BaseTool):
    name = "convertkit_getsubscriptions"
    description = "Tool for convertKit getSubscriptions operation - getSubscriptions operation"
    
    def _run(self, **kwargs):
        """Run the convertKit getSubscriptions operation."""
        # Implement the tool logic here
        return f"Running convertKit getSubscriptions operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the convertKit getSubscriptions operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
