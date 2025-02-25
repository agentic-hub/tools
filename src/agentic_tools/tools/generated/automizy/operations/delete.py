from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AutomizyDeleteToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Name")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    listId: Optional[str] = Field(None, description="List ID")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The email address of the contact")
    contactId: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutomizyDeleteTool(BaseTool):
    name = "automizy_delete"
    description = "Tool for automizy delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the automizy delete operation."""
        # Implement the tool logic here
        return f"Running automizy delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the automizy delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
