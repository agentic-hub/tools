from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IntercomUpdateToolInput(BaseModel):
    customAttributesJson: Optional[str] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="Value of the property to identify the user to update")
    selectBy: Optional[str] = Field(None, description="The property to select the user by")
    companyId: Optional[str] = Field(None, description="The company ID you have defined for the company")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    updateBy: Optional[str] = Field(None, description="The property via which to query the user")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    customAttributesUi: Optional[Dict[str, Any]] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class IntercomUpdateTool(BaseTool):
    name = "intercom_update"
    description = "Tool for intercom update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the intercom update operation."""
        # Implement the tool logic here
        return f"Running intercom update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the intercom update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
