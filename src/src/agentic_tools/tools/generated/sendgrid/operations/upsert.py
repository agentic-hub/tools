from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendgridUpsertToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Primary email for the contact")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[str] = Field(None, description="ID of the list")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class SendgridUpsertTool(BaseTool):
    name = "sendgrid_upsert"
    description = "Tool for sendGrid upsert operation - upsert operation"
    
    def _run(self, **kwargs):
        """Run the sendGrid upsert operation."""
        # Implement the tool logic here
        return f"Running sendGrid upsert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendGrid upsert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
