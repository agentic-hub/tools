from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MailerliteCredentials

class MailerliteUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    subscriber_id: Optional[str] = Field(None, description="Email of subscriber")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class MailerliteUpdateTool(BaseTool):
    name: str = "mailerlite_update"
    description: str = "Tool for mailerLite update operation - update operation"
    args_schema: type[BaseModel] | None = MailerliteUpdateToolInput
    credentials: Optional[MailerliteCredentials] = None
