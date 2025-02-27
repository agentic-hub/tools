from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GristCredentials

class GristGetallToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    doc_id: Optional[str] = Field(None, description="In your document, click your profile icon, then Document Settings, then copy the value under \"This document's ID\"")
    table_id: Optional[str] = Field(None, description="ID of table to operate on. If unsure, look at the Code View.")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    row_id: Optional[str] = Field(None, description="ID of the row to delete, or comma-separated list of row IDs to delete")
    operation: Optional[str] = Field(None, description="Operation")


class GristGetallTool(BaseTool):
    name: str = "grist_getall"
    description: str = "Tool for grist getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = GristGetallToolInput
    credentials: Optional[GristCredentials] = None
