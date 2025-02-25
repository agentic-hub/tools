from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NasaGetallToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="By default just the URL of the image is returned. When set to true the image will be downloaded.")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    operation: Optional[str] = Field(None, description="Operation")


class NasaGetallTool(BaseTool):
    name = "nasa_getall"
    description = "Tool for nasa getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the nasa getAll operation."""
        # Implement the tool logic here
        return f"Running nasa getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the nasa getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
