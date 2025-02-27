from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MailerliteCredentials

class MailerliteCreateToolInput(BaseModel):
    subscriber_id: Optional[str] = Field(None, description="Email of subscriber")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="Email of new subscriber")
    operation: Optional[str] = Field(None, description="Operation")


class MailerliteCreateTool(BaseTool):
    name: str = "mailerlite_create"
    description: str = "Tool for mailerLite create operation - create operation"
    args_schema: type[BaseModel] | None = MailerliteCreateToolInput
    credentials: Optional[MailerliteCredentials] = None
