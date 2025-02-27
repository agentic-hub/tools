from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import UnleashedsoftwareCredentials

class UnleashedsoftwareGetToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    product_id: Optional[str] = Field(None, description="Product ID")
    operation: Optional[str] = Field(None, description="Operation")


class UnleashedsoftwareGetTool(BaseTool):
    name: str = "unleashedsoftware_get"
    connector_id: str = "nodes-base.unleashedSoftware"
    description: str = "Tool for unleashedSoftware get operation - get operation"
    args_schema: type[BaseModel] | None = UnleashedsoftwareGetToolInput
    credentials: Optional[UnleashedsoftwareCredentials] = None
