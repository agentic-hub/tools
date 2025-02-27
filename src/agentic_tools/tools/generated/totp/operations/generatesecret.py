from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TotpCredentials

class TotpGeneratesecretToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class TotpGeneratesecretTool(BaseTool):
    name: str = "totp_generatesecret"
    connector_id: str = "nodes-base.totp"
    description: str = "Tool for totp generateSecret operation - generateSecret operation"
    args_schema: type[BaseModel] | None = TotpGeneratesecretToolInput
    credentials: Optional[TotpCredentials] = None
