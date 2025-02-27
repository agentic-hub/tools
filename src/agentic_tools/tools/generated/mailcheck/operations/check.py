from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MailcheckCredentials

class MailcheckCheckToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="Email address to check")
    operation: Optional[str] = Field(None, description="Operation")


class MailcheckCheckTool(BaseTool):
    name: str = "mailcheck_check"
    description: str = "Tool for mailcheck check operation - check operation"
    args_schema: type[BaseModel] | None = MailcheckCheckToolInput
    credentials: Optional[MailcheckCredentials] = None
