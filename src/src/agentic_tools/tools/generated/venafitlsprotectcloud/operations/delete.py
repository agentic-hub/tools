from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class VenafitlsprotectcloudDeleteToolInput(BaseModel):
    certificateIssuingTemplateId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    certificateId: Optional[str] = Field(None, description="Certificate ID")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    applicationId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    certificateSigningRequest: Optional[str] = Field(None, description="Certificate Signing Request")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")


class VenafitlsprotectcloudDeleteTool(BaseTool):
    name = "venafitlsprotectcloud_delete"
    description = "Tool for venafiTlsProtectCloud delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the venafiTlsProtectCloud delete operation."""
        # Implement the tool logic here
        return f"Running venafiTlsProtectCloud delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the venafiTlsProtectCloud delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
