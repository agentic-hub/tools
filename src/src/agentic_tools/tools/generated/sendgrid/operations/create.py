from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendgridCreateToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Primary email for the contact")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[str] = Field(None, description="ID of the list")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class SendgridCreateTool(BaseTool):
    name = "sendgrid_create"
    description = "Tool for sendGrid create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the sendGrid create operation."""
        # Implement the tool logic here
        return f"Running sendGrid create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendGrid create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
