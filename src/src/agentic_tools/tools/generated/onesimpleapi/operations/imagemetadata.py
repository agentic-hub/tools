from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OnesimpleapiImagemetadataToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Whether to download the PDF or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Image to get metadata from")


class OnesimpleapiImagemetadataTool(BaseTool):
    name = "onesimpleapi_imagemetadata"
    description = "Tool for oneSimpleApi imageMetadata operation - imageMetadata operation"
    
    def _run(self, **kwargs):
        """Run the oneSimpleApi imageMetadata operation."""
        # Implement the tool logic here
        return f"Running oneSimpleApi imageMetadata operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the oneSimpleApi imageMetadata operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
