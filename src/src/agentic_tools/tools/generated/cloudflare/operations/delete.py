from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CloudflareDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    zoneId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    certificateId: Optional[str] = Field(None, description="Certificate ID")


class CloudflareDeleteTool(BaseTool):
    name = "cloudflare_delete"
    description = "Tool for cloudflare delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the cloudflare delete operation."""
        # Implement the tool logic here
        return f"Running cloudflare delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cloudflare delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
