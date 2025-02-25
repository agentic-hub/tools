from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CockpitSubmitToolInput(BaseModel):
    jsonDataFields: Optional[bool] = Field(None, description="Whether form fields should be set via the value-key pair UI or JSON")
    form: Optional[str] = Field(None, description="Name of the form to operate on")
    resource: Optional[str] = Field(None, description="Resource")
    singleton: Optional[str] = Field(None, description="Name of the singleton to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    collection: Optional[str] = Field(None, description="Name of the collection to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    dataFieldsUi: Optional[Dict[str, Any]] = Field(None, description="Form data to send")
    dataFieldsJson: Optional[str] = Field(None, description="Form data to send as JSON")
    operation: Optional[str] = Field(None, description="Operation")


class CockpitSubmitTool(BaseTool):
    name = "cockpit_submit"
    description = "Tool for cockpit submit operation - submit operation"
    
    def _run(self, **kwargs):
        """Run the cockpit submit operation."""
        # Implement the tool logic here
        return f"Running cockpit submit operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cockpit submit operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
