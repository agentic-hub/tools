from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class InvoiceninjatriggerDefaultToolInput(BaseModel):
    event: Optional[str] = Field(None, description="Event")
    apiVersion: Optional[str] = Field(None, description="API Version")


class InvoiceninjatriggerDefaultTool(BaseTool):
    name = "invoiceninjatrigger_default"
    description = "Tool for invoiceNinjaTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the invoiceNinjaTrigger default operation."""
        # Implement the tool logic here
        return f"Running invoiceNinjaTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the invoiceNinjaTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
