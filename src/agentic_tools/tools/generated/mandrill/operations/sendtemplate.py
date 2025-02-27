from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MandrillCredentials

class MandrillSendtemplateToolInput(BaseModel):
    headers_json: Optional[str] = Field(None, description="Optional extra headers to add to the message (most headers are allowed)")
    metadata_ui: Optional[Dict[str, Any]] = Field(None, description="Metadata an associative array of user metadata. Mandrill will store this metadata and make it available for retrieval. In addition, you can select up to 10 metadata fields to index and make searchable using the Mandrill search api.")
    resource: Optional[str] = Field(None, description="Resource")
    merge_vars_ui: Optional[Dict[str, Any]] = Field(None, description="Per-recipient merge variables")
    merge_vars_json: Optional[str] = Field(None, description="Global merge variables")
    to_email: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    template: Optional[str] = Field(None, description="The template you want to send. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    attachments_ui: Optional[Dict[str, Any]] = Field(None, description="Array of supported attachments to add to the message")
    headers_ui: Optional[Dict[str, Any]] = Field(None, description="Optional extra headers to add to the message (most headers are allowed)")
    metadata_json: Optional[str] = Field(None, description="Metadata an associative array of user metadata. Mandrill will store this metadata and make it available for retrieval. In addition, you can select up to 10 metadata fields to index and make searchable using the Mandrill search api.")
    from_email: Optional[str] = Field(None, description="Email address of the sender optional with name")
    operation: Optional[str] = Field(None, description="Operation")
    attachments_json: Optional[str] = Field(None, description="An array of supported attachments to add to the message")


class MandrillSendtemplateTool(BaseTool):
    name: str = "mandrill_sendtemplate"
    description: str = "Tool for mandrill sendTemplate operation - sendTemplate operation"
    args_schema: type[BaseModel] | None = MandrillSendtemplateToolInput
    credentials: Optional[MandrillCredentials] = None
