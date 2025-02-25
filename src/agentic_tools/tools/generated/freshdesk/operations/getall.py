from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshdeskGetallToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    ticketId: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    contactId: Optional[str] = Field(None, description="Contact ID")


class FreshdeskGetallTool(BaseTool):
    name = "freshdesk_getall"
    description = "Tool for freshdesk getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the freshdesk getAll operation."""
        # Implement the tool logic here
        return f"Running freshdesk getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshdesk getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
