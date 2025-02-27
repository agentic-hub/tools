from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GristCredentials

class GristDeleteToolInput(BaseModel):
    doc_id: Optional[str] = Field(None, description="In your document, click your profile icon, then Document Settings, then copy the value under \"This document's ID\"")
    table_id: Optional[str] = Field(None, description="ID of table to operate on. If unsure, look at the Code View.")
    row_id: Optional[str] = Field(None, description="ID of the row to delete, or comma-separated list of row IDs to delete")
    operation: Optional[str] = Field(None, description="Operation")


class GristDeleteTool(BaseTool):
    name: str = "grist_delete"
    description: str = "Tool for grist delete operation - delete operation"
    args_schema: type[BaseModel] | None = GristDeleteToolInput
    credentials: Optional[GristCredentials] = None
