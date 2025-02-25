from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IntercomDeleteToolInput(BaseModel):
    customAttributesJson: Optional[str] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="Delete by value")
    selectBy: Optional[str] = Field(None, description="The property to select the user by")
    id: Optional[str] = Field(None, description="The Intercom defined ID representing the Lead")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    updateBy: Optional[str] = Field(None, description="The property via which to query the user")
    deleteBy: Optional[str] = Field(None, description="Delete By")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    customAttributesUi: Optional[Dict[str, Any]] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class IntercomDeleteTool(BaseTool):
    name = "intercom_delete"
    description = "Tool for intercom delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the intercom delete operation."""
        # Implement the tool logic here
        return f"Running intercom delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the intercom delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
