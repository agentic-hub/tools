from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NasaCredentials

class NasaGetToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="By default just the URL of the image is returned. When set to true the image will be downloaded.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    lon: Optional[float] = Field(None, description="Longitude for the location of the image")
    asteroid_id: Optional[str] = Field(None, description="The ID of the asteroid to be returned")
    lat: Optional[float] = Field(None, description="Latitude for the location of the image")
    operation: Optional[str] = Field(None, description="Operation")


class NasaGetTool(BaseTool):
    name: str = "nasa_get"
    description: str = "Tool for nasa get operation - get operation"
    args_schema: type[BaseModel] | None = NasaGetToolInput
    credentials: Optional[NasaCredentials] = None
