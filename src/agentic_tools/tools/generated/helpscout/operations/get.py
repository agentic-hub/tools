from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HelpscoutGetToolInput(BaseModel):
    mailboxId: Optional[str] = Field(None, description="Mailbox ID")
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


class HelpscoutGetTool(BaseTool):
    name = "helpscout_get"
    description = "Tool for helpScout get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the helpScout get operation."""
        # Implement the tool logic here
        return f"Running helpScout get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the helpScout get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
