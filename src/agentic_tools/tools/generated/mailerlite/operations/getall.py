from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MailerliteCredentials

class MailerliteGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    subscriber_id: Optional[str] = Field(None, description="Email of subscriber")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    operation: Optional[str] = Field(None, description="Operation")


class MailerliteGetallTool(BaseTool):
    name: str = "mailerlite_getall"
    connector_id: str = "nodes-base.mailerLite"
    description: str = "Tool for mailerLite getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = MailerliteGetallToolInput
    credentials: Optional[MailerliteCredentials] = None
