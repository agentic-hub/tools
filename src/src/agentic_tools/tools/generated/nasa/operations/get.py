from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NasaGetToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="By default just the URL of the image is returned. When set to true the image will be downloaded.")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    lon: Optional[float] = Field(None, description="Longitude for the location of the image")
    asteroidId: Optional[str] = Field(None, description="The ID of the asteroid to be returned")
    lat: Optional[float] = Field(None, description="Latitude for the location of the image")
    operation: Optional[str] = Field(None, description="Operation")


class NasaGetTool(BaseTool):
    name = "nasa_get"
    description = "Tool for nasa get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the nasa get operation."""
        # Implement the tool logic here
        return f"Running nasa get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the nasa get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
