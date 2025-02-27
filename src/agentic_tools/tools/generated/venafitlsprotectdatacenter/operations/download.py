from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VenafitlsprotectdatacenterCredentials

class VenafitlsprotectdatacenterDownloadToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    certificate_dn: Optional[str] = Field(None, description="Certificate DN")
    binary_property: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded")
    password: Optional[str] = Field(None, description="Password")
    operation: Optional[str] = Field(None, description="Operation")
    include_private_key: Optional[bool] = Field(None, description="Include Private Key")


class VenafitlsprotectdatacenterDownloadTool(BaseTool):
    name: str = "venafitlsprotectdatacenter_download"
    connector_id: str = "nodes-base.venafiTlsProtectDatacenter"
    description: str = "Tool for venafiTlsProtectDatacenter download operation - download operation"
    args_schema: type[BaseModel] | None = VenafitlsprotectdatacenterDownloadToolInput
    credentials: Optional[VenafitlsprotectdatacenterCredentials] = None
