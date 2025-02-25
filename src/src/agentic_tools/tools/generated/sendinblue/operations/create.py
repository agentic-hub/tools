from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendinblueCreateToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    attributeCategoryList: Optional[Dict[str, Any]] = Field(None, description="Contact Attribute List")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    attributeType: Optional[str] = Field(None, description="Attribute Type")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the sender")
    attributeValue: Optional[str] = Field(None, description="Value of the attribute")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    attributeCategory: Optional[str] = Field(None, description="Category of the attribute")
    attributeName: Optional[str] = Field(None, description="Name of the attribute")
    createContactAttributes: Optional[Dict[str, Any]] = Field(None, description="Array of attributes to be added")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")


class SendinblueCreateTool(BaseTool):
    name = "sendinblue_create"
    description = "Tool for sendInBlue create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the sendInBlue create operation."""
        # Implement the tool logic here
        return f"Running sendInBlue create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendInBlue create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
