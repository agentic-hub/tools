from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AutomizyGetToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Name")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    listId: Optional[str] = Field(None, description="List ID")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The email address of the contact")
    contactId: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutomizyGetTool(BaseTool):
    name = "automizy_get"
    description = "Tool for automizy get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the automizy get operation."""
        # Implement the tool logic here
        return f"Running automizy get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the automizy get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
