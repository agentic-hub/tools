from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshdeskGetToolInput(BaseModel):
    ticketId: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    contactId: Optional[str] = Field(None, description="Contact ID")


class FreshdeskGetTool(BaseTool):
    name = "freshdesk_get"
    description = "Tool for freshdesk get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the freshdesk get operation."""
        # Implement the tool logic here
        return f"Running freshdesk get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshdesk get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
