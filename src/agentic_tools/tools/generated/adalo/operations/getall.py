from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AdaloCredentials

class AdaloGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    collection_id: Optional[str] = Field(None, description="Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation")
    operation: Optional[str] = Field(None, description="Operation")


class AdaloGetallTool(BaseTool):
    name: str = "adalo_getall"
    connector_id: str = "nodes-base.adalo"
    description: str = "Tool for adalo getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = AdaloGetallToolInput
    credentials: Optional[AdaloCredentials] = None
