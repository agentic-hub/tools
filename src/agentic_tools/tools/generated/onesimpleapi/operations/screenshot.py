from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OnesimpleapiScreenshotToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Whether to download the screenshot or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Link to webpage to convert")


class OnesimpleapiScreenshotTool(BaseTool):
    name = "onesimpleapi_screenshot"
    description = "Tool for oneSimpleApi screenshot operation - screenshot operation"
    
    def _run(self, **kwargs):
        """Run the oneSimpleApi screenshot operation."""
        # Implement the tool logic here
        return f"Running oneSimpleApi screenshot operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the oneSimpleApi screenshot operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
