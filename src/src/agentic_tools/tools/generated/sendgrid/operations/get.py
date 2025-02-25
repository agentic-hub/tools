from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendgridGetToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the contact")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[str] = Field(None, description="ID of the list")
    by: Optional[str] = Field(None, description="Search the user by ID or email")
    contactSample: Optional[bool] = Field(None, description="Whether to return the contact sample")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contactId: Optional[str] = Field(None, description="ID of the contact")


class SendgridGetTool(BaseTool):
    name = "sendgrid_get"
    description = "Tool for sendGrid get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the sendGrid get operation."""
        # Implement the tool logic here
        return f"Running sendGrid get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendGrid get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
