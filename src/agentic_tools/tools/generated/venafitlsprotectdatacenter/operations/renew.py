from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VenafitlsprotectdatacenterCredentials

class VenafitlsprotectdatacenterRenewToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    certificate_dn: Optional[str] = Field(None, description="The Distinguished Name (DN) of the certificate to renew")
    operation: Optional[str] = Field(None, description="Operation")


class VenafitlsprotectdatacenterRenewTool(BaseTool):
    name: str = "venafitlsprotectdatacenter_renew"
    connector_id: str = "nodes-base.venafiTlsProtectDatacenter"
    description: str = "Tool for venafiTlsProtectDatacenter renew operation - renew operation"
    args_schema: type[BaseModel] | None = VenafitlsprotectdatacenterRenewToolInput
    credentials: Optional[VenafitlsprotectdatacenterCredentials] = None
