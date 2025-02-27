from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MailerliteCredentials

class MailerliteGetToolInput(BaseModel):
    subscriber_id: Optional[str] = Field(None, description="Email of subscriber to get")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class MailerliteGetTool(BaseTool):
    name: str = "mailerlite_get"
    connector_id: str = "nodes-base.mailerLite"
    description: str = "Tool for mailerLite get operation - get operation"
    args_schema: type[BaseModel] | None = MailerliteGetToolInput
    credentials: Optional[MailerliteCredentials] = None
