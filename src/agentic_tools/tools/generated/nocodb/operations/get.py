from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NocodbCredentials

class NocodbGetToolInput(BaseModel):
    table: Optional[str] = Field(None, description="The table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    primary_key: Optional[str] = Field(None, description="Primary Key Type")
    workspace_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    id: Optional[str] = Field(None, description="The value of the ID field")
    operation: Optional[str] = Field(None, description="Operation")
    download_field_names: Optional[str] = Field(None, description="Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive.")
    version: Optional[str] = Field(None, description="API Version")
    custom_primary_key: Optional[str] = Field(None, description="Field Name")
    resource: Optional[str] = Field(None, description="Resource")
    download_attachments: Optional[bool] = Field(None, description="Whether the attachment fields define in 'Download Fields' will be downloaded")
    project_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    authentication: Optional[str] = Field(None, description="Authentication")
    info: Optional[str] = Field(None, description="In this mode, make sure the incoming data fields are named the same as the columns in NocoDB. (Use an 'Edit Fields' node before this node to change them if required.)")


class NocodbGetTool(BaseTool):
    name: str = "nocodb_get"
    description: str = "Tool for nocoDb get operation - get operation"
    args_schema: type[BaseModel] | None = NocodbGetToolInput
    credentials: Optional[NocodbCredentials] = None
