from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HomeassistantGetscreenshotToolInput(BaseModel):
    entityId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    operation: Optional[str] = Field(None, description="Operation")
    cameraEntityId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class HomeassistantGetscreenshotTool(BaseTool):
    name = "homeassistant_getscreenshot"
    description = "Tool for homeAssistant getScreenshot operation - getScreenshot operation"
    
    def _run(self, **kwargs):
        """Run the homeAssistant getScreenshot operation."""
        # Implement the tool logic here
        return f"Running homeAssistant getScreenshot operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the homeAssistant getScreenshot operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
