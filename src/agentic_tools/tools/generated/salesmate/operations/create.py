from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SalesmateCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    type: Optional[str] = Field(None, description="This field displays activity type such as call, meeting etc")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    rawData: Optional[bool] = Field(None, description="Whether the data should include the fields details")
    id: Optional[str] = Field(None, description="Company ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    filtersJson: Optional[str] = Field(None, description="Filters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    stage: Optional[str] = Field(None, description="Stage")
    primaryContact: Optional[str] = Field(None, description="Primary contact for the deal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    currency: Optional[str] = Field(None, description="Currency")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    title: Optional[str] = Field(None, description="Title")
    owner: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    pipeline: Optional[str] = Field(None, description="Pipeline")


class SalesmateCreateTool(BaseTool):
    name = "salesmate_create"
    description = "Tool for salesmate create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the salesmate create operation."""
        # Implement the tool logic here
        return f"Running salesmate create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the salesmate create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
