from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GristGetallToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    docId: Optional[str] = Field(None, description="In your document, click your profile icon, then Document Settings, then copy the value under \"This document's ID\"")
    tableId: Optional[str] = Field(None, description="ID of table to operate on. If unsure, look at the Code View.")
    additionalOptions: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    rowId: Optional[str] = Field(None, description="ID of the row to delete, or comma-separated list of row IDs to delete")
    operation: Optional[str] = Field(None, description="Operation")


class GristGetallTool(BaseTool):
    name = "grist_getall"
    description = "Tool for grist getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the grist getAll operation."""
        # Implement the tool logic here
        return f"Running grist getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the grist getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
