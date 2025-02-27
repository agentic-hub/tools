from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VenafitlsprotectdatacenterCredentials

class VenafitlsprotectdatacenterGetToolInput(BaseModel):
    policy_dn: Optional[str] = Field(None, description="The Distinguished Name (DN) of the policy folder")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    certificate_id: Optional[str] = Field(None, description="A GUID that uniquely identifies the certificate")


class VenafitlsprotectdatacenterGetTool(BaseTool):
    name: str = "venafitlsprotectdatacenter_get"
    description: str = "Tool for venafiTlsProtectDatacenter get operation - get operation"
    args_schema: type[BaseModel] | None = VenafitlsprotectdatacenterGetToolInput
    credentials: Optional[VenafitlsprotectdatacenterCredentials] = None
