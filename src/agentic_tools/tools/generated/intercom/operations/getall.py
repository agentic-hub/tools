from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IntercomGetallToolInput(BaseModel):
    customAttributesJson: Optional[str] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="View by value")
    selectBy: Optional[str] = Field(None, description="The property to select the user by")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    updateBy: Optional[str] = Field(None, description="The property via which to query the user")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    customAttributesUi: Optional[Dict[str, Any]] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class IntercomGetallTool(BaseTool):
    name = "intercom_getall"
    description = "Tool for intercom getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the intercom getAll operation."""
        # Implement the tool logic here
        return f"Running intercom getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the intercom getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
