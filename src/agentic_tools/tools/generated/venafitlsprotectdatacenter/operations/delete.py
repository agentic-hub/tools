from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VenafitlsprotectdatacenterCredentials

class VenafitlsprotectdatacenterDeleteToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    certificate_id: Optional[str] = Field(None, description="A GUID that uniquely identifies the certificate")


class VenafitlsprotectdatacenterDeleteTool(BaseTool):
    name: str = "venafitlsprotectdatacenter_delete"
    description: str = "Tool for venafiTlsProtectDatacenter delete operation - delete operation"
    args_schema: type[BaseModel] | None = VenafitlsprotectdatacenterDeleteToolInput
    credentials: Optional[VenafitlsprotectdatacenterCredentials] = None
