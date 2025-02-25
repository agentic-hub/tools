from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EmailreadimapDefaultToolInput(BaseModel):
    dataPropertyAttachmentsPrefixName: Optional[str] = Field(None, description="Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is \"attachment_\" the first attachment is saved to \"attachment_0\"")
    postProcessAction: Optional[str] = Field(None, description="What to do after the email has been received. If \"nothing\" gets selected it will be processed multiple times.")
    mailbox: Optional[str] = Field(None, description="Mailbox Name")
    downloadAttachments: Optional[bool] = Field(None, description="Whether attachments of emails should be downloaded. Only set if needed as it increases processing.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    format: Optional[str] = Field(None, description="The format to return the message in")


class EmailreadimapDefaultTool(BaseTool):
    name = "emailreadimap_default"
    description = "Tool for emailReadImap default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the emailReadImap default operation."""
        # Implement the tool logic here
        return f"Running emailReadImap default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the emailReadImap default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
