from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GristCreateToolInput(BaseModel):
    docId: Optional[str] = Field(None, description="In your document, click your profile icon, then Document Settings, then copy the value under \"This document's ID\"")
    tableId: Optional[str] = Field(None, description="ID of table to operate on. If unsure, look at the Code View.")
    fieldsToSend: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    dataToSend: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputsToIgnore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    rowId: Optional[str] = Field(None, description="ID of the row to delete, or comma-separated list of row IDs to delete")
    operation: Optional[str] = Field(None, description="Operation")


class GristCreateTool(BaseTool):
    name = "grist_create"
    description = "Tool for grist create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the grist create operation."""
        # Implement the tool logic here
        return f"Running grist create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the grist create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
