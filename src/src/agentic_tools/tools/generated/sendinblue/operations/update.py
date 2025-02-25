from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendinblueUpdateToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    updateAttributes: Optional[Dict[str, Any]] = Field(None, description="Array of attributes to be updated")
    updateAttributeCategoryList: Optional[Dict[str, Any]] = Field(None, description="List of the values and labels that the attribute can take")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    updateAttributeCategory: Optional[str] = Field(None, description="Category of the attribute")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    updateAttributeName: Optional[str] = Field(None, description="Name of the existing attribute")
    updateAttributeValue: Optional[str] = Field(None, description="Value of the attribute to update")


class SendinblueUpdateTool(BaseTool):
    name = "sendinblue_update"
    description = "Tool for sendInBlue update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the sendInBlue update operation."""
        # Implement the tool logic here
        return f"Running sendInBlue update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendInBlue update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
