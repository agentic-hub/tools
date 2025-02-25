from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HalopsaCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    siteId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    summary: Optional[str] = Field(None, description="Summary")
    selectOption: Optional[bool] = Field(None, description="Whether client can be selected by ID")
    ticketType: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    details: Optional[str] = Field(None, description="Details")
    userId: Optional[str] = Field(None, description="User ID")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    ticketId: Optional[str] = Field(None, description="Ticket ID")
    clientName: Optional[str] = Field(None, description="Enter client name")
    operation: Optional[str] = Field(None, description="Operation")
    clientId: Optional[str] = Field(None, description="Client ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    simplify: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    userName: Optional[str] = Field(None, description="Enter user name")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    siteName: Optional[str] = Field(None, description="Enter site name")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class HalopsaCreateTool(BaseTool):
    name = "halopsa_create"
    description = "Tool for haloPSA create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the haloPSA create operation."""
        # Implement the tool logic here
        return f"Running haloPSA create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the haloPSA create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
