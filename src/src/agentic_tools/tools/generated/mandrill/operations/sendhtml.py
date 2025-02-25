from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MandrillSendhtmlToolInput(BaseModel):
    headersJson: Optional[str] = Field(None, description="Optional extra headers to add to the message (most headers are allowed)")
    metadataUi: Optional[Dict[str, Any]] = Field(None, description="Metadata an associative array of user metadata. Mandrill will store this metadata and make it available for retrieval. In addition, you can select up to 10 metadata fields to index and make searchable using the Mandrill search api.")
    resource: Optional[str] = Field(None, description="Resource")
    mergeVarsUi: Optional[Dict[str, Any]] = Field(None, description="Per-recipient merge variables")
    mergeVarsJson: Optional[str] = Field(None, description="Global merge variables")
    toEmail: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    attachmentsUi: Optional[Dict[str, Any]] = Field(None, description="Array of supported attachments to add to the message")
    headersUi: Optional[Dict[str, Any]] = Field(None, description="Optional extra headers to add to the message (most headers are allowed)")
    metadataJson: Optional[str] = Field(None, description="Metadata an associative array of user metadata. Mandrill will store this metadata and make it available for retrieval. In addition, you can select up to 10 metadata fields to index and make searchable using the Mandrill search api.")
    fromEmail: Optional[str] = Field(None, description="Email address of the sender optional with name")
    operation: Optional[str] = Field(None, description="Operation")
    attachmentsJson: Optional[str] = Field(None, description="An array of supported attachments to add to the message")


class MandrillSendhtmlTool(BaseTool):
    name = "mandrill_sendhtml"
    description = "Tool for mandrill sendHtml operation - sendHtml operation"
    
    def _run(self, **kwargs):
        """Run the mandrill sendHtml operation."""
        # Implement the tool logic here
        return f"Running mandrill sendHtml operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mandrill sendHtml operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
