from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HelpscoutGetallToolInput(BaseModel):
    mailboxId: Optional[str] = Field(None, description="ID of a mailbox where the conversation is being created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    customerId: Optional[str] = Field(None, description="Customer ID")
    type: Optional[str] = Field(None, description="Conversation type")
    resolveData: Optional[bool] = Field(None, description="By default the response only contain the ID to resource. If this option gets activated, it will resolve the data automatically.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    conversationId: Optional[str] = Field(None, description="Conversation ID")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class HelpscoutGetallTool(BaseTool):
    name = "helpscout_getall"
    description = "Tool for helpScout getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the helpScout getAll operation."""
        # Implement the tool logic here
        return f"Running helpScout getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the helpScout getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
