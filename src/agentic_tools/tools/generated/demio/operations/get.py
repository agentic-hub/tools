from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DemioCredentials

class DemioGetToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    event_id: Optional[str] = Field(None, description="Event ID")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    date_id: Optional[str] = Field(None, description="ID of the session. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class DemioGetTool(BaseTool):
    name: str = "demio_get"
    connector_id: str = "nodes-base.demio"
    description: str = "Tool for demio get operation - get operation"
    args_schema: type[BaseModel] | None = DemioGetToolInput
    credentials: Optional[DemioCredentials] = None
