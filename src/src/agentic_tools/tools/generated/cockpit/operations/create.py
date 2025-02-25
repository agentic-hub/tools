from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CockpitCreateToolInput(BaseModel):
    jsonDataFields: Optional[bool] = Field(None, description="Whether new entry fields should be set via the value-key pair UI or JSON")
    form: Optional[str] = Field(None, description="Name of the form to operate on")
    resource: Optional[str] = Field(None, description="Resource")
    singleton: Optional[str] = Field(None, description="Name of the singleton to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    collection: Optional[str] = Field(None, description="Name of the collection to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    dataFieldsUi: Optional[Dict[str, Any]] = Field(None, description="Entry data to send")
    dataFieldsJson: Optional[str] = Field(None, description="Entry data to send as JSON")
    operation: Optional[str] = Field(None, description="Operation")


class CockpitCreateTool(BaseTool):
    name = "cockpit_create"
    description = "Tool for cockpit create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the cockpit create operation."""
        # Implement the tool logic here
        return f"Running cockpit create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cockpit create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
