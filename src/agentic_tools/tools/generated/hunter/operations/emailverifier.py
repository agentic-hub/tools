from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HunterCredentials

class HunterEmailverifierToolInput(BaseModel):
    email: Optional[str] = Field(None, description="The email address you want to verify")
    operation: Optional[str] = Field(None, description="Operation to consume")
    domain: Optional[str] = Field(None, description="Domain name from which you want to find the email addresses. For example, \"stripe.com\".")


class HunterEmailverifierTool(BaseTool):
    name: str = "hunter_emailverifier"
    connector_id: str = "nodes-base.hunter"
    description: str = "Tool for hunter emailVerifier operation - emailVerifier operation"
    args_schema: type[BaseModel] | None = HunterEmailverifierToolInput
    credentials: Optional[HunterCredentials] = None
