from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwscertificatemanagerCredentials

class Awscertificatemanager__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Awscertificatemanager__custom_api_call__Tool(BaseTool):
    name: str = "awscertificatemanager___custom_api_call__"
    description: str = "Tool for awsCertificateManager __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Awscertificatemanager__custom_api_call__ToolInput
    credentials: Optional[AwscertificatemanagerCredentials] = None
