from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CockpitUpdateToolInput(BaseModel):
    jsonDataFields: Optional[bool] = Field(None, description="Whether new entry fields should be set via the value-key pair UI or JSON")
    form: Optional[str] = Field(None, description="Name of the form to operate on")
    resource: Optional[str] = Field(None, description="Resource")
    singleton: Optional[str] = Field(None, description="Name of the singleton to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    collection: Optional[str] = Field(None, description="Name of the collection to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    dataFieldsUi: Optional[Dict[str, Any]] = Field(None, description="Entry data to send")
    id: Optional[str] = Field(None, description="Entry ID")
    dataFieldsJson: Optional[str] = Field(None, description="Entry data to send as JSON")
    operation: Optional[str] = Field(None, description="Operation")


class CockpitUpdateTool(BaseTool):
    name = "cockpit_update"
    description = "Tool for cockpit update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the cockpit update operation."""
        # Implement the tool logic here
        return f"Running cockpit update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cockpit update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
