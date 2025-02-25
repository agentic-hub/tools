from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CockpitGetallToolInput(BaseModel):
    jsonDataFields: Optional[bool] = Field(None, description="Whether new entry fields should be set via the value-key pair UI or JSON")
    form: Optional[str] = Field(None, description="Name of the form to operate on")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    singleton: Optional[str] = Field(None, description="Name of the singleton to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    collection: Optional[str] = Field(None, description="Name of the collection to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    dataFieldsUi: Optional[Dict[str, Any]] = Field(None, description="Entry data to send")
    dataFieldsJson: Optional[str] = Field(None, description="Entry data to send as JSON")
    operation: Optional[str] = Field(None, description="Operation")


class CockpitGetallTool(BaseTool):
    name = "cockpit_getall"
    description = "Tool for cockpit getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the cockpit getAll operation."""
        # Implement the tool logic here
        return f"Running cockpit getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cockpit getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
