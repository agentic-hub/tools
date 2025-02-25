from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ZendeskCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    description: Optional[str] = Field(None, description="The first comment on the ticket")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additionalFieldsJson: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://developer.zendesk.com/rest_api/docs/support/tickets\">here</a>")
    id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The user's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class ZendeskCreateTool(BaseTool):
    name = "zendesk_create"
    description = "Tool for zendesk create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the zendesk create operation."""
        # Implement the tool logic here
        return f"Running zendesk create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the zendesk create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
