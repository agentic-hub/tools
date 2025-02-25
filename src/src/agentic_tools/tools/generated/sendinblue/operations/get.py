from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendinblueGetToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")


class SendinblueGetTool(BaseTool):
    name = "sendinblue_get"
    description = "Tool for sendInBlue get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the sendInBlue get operation."""
        # Implement the tool logic here
        return f"Running sendInBlue get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendInBlue get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
