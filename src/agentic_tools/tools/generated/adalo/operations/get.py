from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AdaloCredentials

class AdaloGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    collection_id: Optional[str] = Field(None, description="Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation")
    row_id: Optional[str] = Field(None, description="Row ID")
    operation: Optional[str] = Field(None, description="Operation")


class AdaloGetTool(BaseTool):
    name: str = "adalo_get"
    description: str = "Tool for adalo get operation - get operation"
    args_schema: type[BaseModel] | None = AdaloGetToolInput
    credentials: Optional[AdaloCredentials] = None
