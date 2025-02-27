from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import EmailreadimapCredentials

class EmailreadimapDefaultToolInput(BaseModel):
    data_property_attachments_prefix_name: Optional[str] = Field(None, description="Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is \"attachment_\" the first attachment is saved to \"attachment_0\"")
    post_process_action: Optional[str] = Field(None, description="What to do after the email has been received. If \"nothing\" gets selected it will be processed multiple times.")
    mailbox: Optional[str] = Field(None, description="Mailbox Name")
    download_attachments: Optional[bool] = Field(None, description="Whether attachments of emails should be downloaded. Only set if needed as it increases processing.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    format: Optional[str] = Field(None, description="The format to return the message in")


class EmailreadimapDefaultTool(BaseTool):
    name: str = "emailreadimap_default"
    description: str = "Tool for emailReadImap default operation - default operation"
    args_schema: type[BaseModel] | None = EmailreadimapDefaultToolInput
    credentials: Optional[EmailreadimapCredentials] = None
