from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NasaCredentials

class NasaGetallToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="By default just the URL of the image is returned. When set to true the image will be downloaded.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    operation: Optional[str] = Field(None, description="Operation")


class NasaGetallTool(BaseTool):
    name: str = "nasa_getall"
    description: str = "Tool for nasa getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = NasaGetallToolInput
    credentials: Optional[NasaCredentials] = None
