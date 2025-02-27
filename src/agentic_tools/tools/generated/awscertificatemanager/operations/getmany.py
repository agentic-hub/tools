from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwscertificatemanagerCredentials

class AwscertificatemanagerGetmanyToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class AwscertificatemanagerGetmanyTool(BaseTool):
    name: str = "awscertificatemanager_getmany"
    description: str = "Tool for awsCertificateManager getMany operation - getMany operation"
    args_schema: type[BaseModel] | None = AwscertificatemanagerGetmanyToolInput
    credentials: Optional[AwscertificatemanagerCredentials] = None
