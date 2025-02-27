from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AdaloCredentials

class AdaloDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    collection_id: Optional[str] = Field(None, description="Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation")
    row_id: Optional[str] = Field(None, description="Row ID")
    operation: Optional[str] = Field(None, description="Operation")


class AdaloDeleteTool(BaseTool):
    name: str = "adalo_delete"
    connector_id: str = "nodes-base.adalo"
    description: str = "Tool for adalo delete operation - delete operation"
    args_schema: type[BaseModel] | None = AdaloDeleteToolInput
    credentials: Optional[AdaloCredentials] = None
