from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ZendeskGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    ticketType: Optional[str] = Field(None, description="Ticket Type")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The user's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    ticketFieldId: Optional[str] = Field(None, description="Ticket Field ID")
    authentication: Optional[str] = Field(None, description="Authentication")


class ZendeskGetTool(BaseTool):
    name = "zendesk_get"
    description = "Tool for zendesk get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the zendesk get operation."""
        # Implement the tool logic here
        return f"Running zendesk get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the zendesk get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
