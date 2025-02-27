from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DemioCredentials

class DemioGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    event_id: Optional[str] = Field(None, description="Event ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    operation: Optional[str] = Field(None, description="Operation")


class DemioGetallTool(BaseTool):
    name: str = "demio_getall"
    connector_id: str = "nodes-base.demio"
    description: str = "Tool for demio getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = DemioGetallToolInput
    credentials: Optional[DemioCredentials] = None
