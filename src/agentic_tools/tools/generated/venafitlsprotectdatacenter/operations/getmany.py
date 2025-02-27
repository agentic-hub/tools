from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VenafitlsprotectdatacenterCredentials

class VenafitlsprotectdatacenterGetmanyToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class VenafitlsprotectdatacenterGetmanyTool(BaseTool):
    name: str = "venafitlsprotectdatacenter_getmany"
    connector_id: str = "nodes-base.venafiTlsProtectDatacenter"
    description: str = "Tool for venafiTlsProtectDatacenter getMany operation - getMany operation"
    args_schema: type[BaseModel] | None = VenafitlsprotectdatacenterGetmanyToolInput
    credentials: Optional[VenafitlsprotectdatacenterCredentials] = None
