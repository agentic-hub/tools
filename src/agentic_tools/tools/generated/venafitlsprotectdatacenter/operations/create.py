from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VenafitlsprotectdatacenterCredentials

class VenafitlsprotectdatacenterCreateToolInput(BaseModel):
    subject: Optional[str] = Field(None, description="The Common Name field for the certificate Subject (DN)")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    policy_dn: Optional[str] = Field(None, description="The folder DN for the new certificate. If the value is missing, the folder name is the system default. If no system default is configured")
    operation: Optional[str] = Field(None, description="Operation")


class VenafitlsprotectdatacenterCreateTool(BaseTool):
    name: str = "venafitlsprotectdatacenter_create"
    description: str = "Tool for venafiTlsProtectDatacenter create operation - create operation"
    args_schema: type[BaseModel] | None = VenafitlsprotectdatacenterCreateToolInput
    credentials: Optional[VenafitlsprotectdatacenterCredentials] = None
