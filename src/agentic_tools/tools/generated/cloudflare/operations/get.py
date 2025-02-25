from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CloudflareGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    zoneId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    certificateId: Optional[str] = Field(None, description="Certificate ID")


class CloudflareGetTool(BaseTool):
    name = "cloudflare_get"
    description = "Tool for cloudflare get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the cloudflare get operation."""
        # Implement the tool logic here
        return f"Running cloudflare get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cloudflare get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
