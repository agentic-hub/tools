from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendinblueDeleteToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    id: Optional[str] = Field(None, description="ID of the sender to delete")
    deleteAttributeName: Optional[str] = Field(None, description="Name of the attribute")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    deleteAttributeCategory: Optional[str] = Field(None, description="Category of the attribute")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")


class SendinblueDeleteTool(BaseTool):
    name = "sendinblue_delete"
    description = "Tool for sendInBlue delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the sendInBlue delete operation."""
        # Implement the tool logic here
        return f"Running sendInBlue delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendInBlue delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
