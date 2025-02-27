from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import EmailsendCredentials

class EmailsendDefaultToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    email_format: Optional[str] = Field(None, description="Email Format")


class EmailsendDefaultTool(BaseTool):
    name: str = "emailsend_default"
    connector_id: str = "nodes-base.emailSend"
    description: str = "Tool for emailSend default operation - default operation"
    args_schema: type[BaseModel] | None = EmailsendDefaultToolInput
    credentials: Optional[EmailsendCredentials] = None
