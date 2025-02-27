from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VenafitlsprotectcloudCredentials

class VenafitlsprotectcloudGetmanyToolInput(BaseModel):
    certificate_issuing_template_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    certificate_id: Optional[str] = Field(None, description="Certificate ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    application_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    certificate_signing_request: Optional[str] = Field(None, description="Certificate Signing Request")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")


class VenafitlsprotectcloudGetmanyTool(BaseTool):
    name: str = "venafitlsprotectcloud_getmany"
    connector_id: str = "nodes-base.venafiTlsProtectCloud"
    description: str = "Tool for venafiTlsProtectCloud getMany operation - getMany operation"
    args_schema: type[BaseModel] | None = VenafitlsprotectcloudGetmanyToolInput
    credentials: Optional[VenafitlsprotectcloudCredentials] = None
