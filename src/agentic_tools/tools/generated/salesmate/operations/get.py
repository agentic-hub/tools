from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SalesmateGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    rawData: Optional[bool] = Field(None, description="Whether the data should include the fields details")
    id: Optional[str] = Field(None, description="Company ID")
    operation: Optional[str] = Field(None, description="Operation")
    filtersJson: Optional[str] = Field(None, description="Filters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title")
    owner: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class SalesmateGetTool(BaseTool):
    name = "salesmate_get"
    description = "Tool for salesmate get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the salesmate get operation."""
        # Implement the tool logic here
        return f"Running salesmate get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the salesmate get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
