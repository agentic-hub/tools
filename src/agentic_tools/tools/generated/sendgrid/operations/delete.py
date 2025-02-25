from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendgridDeleteToolInput(BaseModel):
    ids: Optional[str] = Field(None, description="ID of the contact. Multiple can be added separated by comma.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    deleteContacts: Optional[bool] = Field(None, description="Whether to delete all contacts on the list")
    email: Optional[str] = Field(None, description="Primary email for the contact")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[str] = Field(None, description="ID of the list")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    deleteAll: Optional[bool] = Field(None, description="Whether all contacts will be deleted")


class SendgridDeleteTool(BaseTool):
    name = "sendgrid_delete"
    description = "Tool for sendGrid delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the sendGrid delete operation."""
        # Implement the tool logic here
        return f"Running sendGrid delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendGrid delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
