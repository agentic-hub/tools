from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IntercomCreateToolInput(BaseModel):
    customAttributesJson: Optional[str] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="View by value")
    email: Optional[str] = Field(None, description="The email of the user")
    selectBy: Optional[str] = Field(None, description="The property to select the user by")
    companyId: Optional[str] = Field(None, description="The company ID you have defined for the company")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    updateBy: Optional[str] = Field(None, description="The property via which to query the user")
    identifierType: Optional[str] = Field(None, description="Unique string identifier")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    idValue: Optional[str] = Field(None, description="Unique string identifier value")
    customAttributesUi: Optional[Dict[str, Any]] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class IntercomCreateTool(BaseTool):
    name = "intercom_create"
    description = "Tool for intercom create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the intercom create operation."""
        # Implement the tool logic here
        return f"Running intercom create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the intercom create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
