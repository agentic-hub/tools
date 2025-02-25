from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GristDeleteToolInput(BaseModel):
    docId: Optional[str] = Field(None, description="In your document, click your profile icon, then Document Settings, then copy the value under \"This document's ID\"")
    tableId: Optional[str] = Field(None, description="ID of table to operate on. If unsure, look at the Code View.")
    rowId: Optional[str] = Field(None, description="ID of the row to delete, or comma-separated list of row IDs to delete")
    operation: Optional[str] = Field(None, description="Operation")


class GristDeleteTool(BaseTool):
    name = "grist_delete"
    description = "Tool for grist delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the grist delete operation."""
        # Implement the tool logic here
        return f"Running grist delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the grist delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
