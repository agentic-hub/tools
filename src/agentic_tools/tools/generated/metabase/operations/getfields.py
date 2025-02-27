from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MetabaseCredentials

class MetabaseGetfieldsToolInput(BaseModel):
    database_id: Optional[str] = Field(None, description="Database ID")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MetabaseGetfieldsTool(BaseTool):
    name: str = "metabase_getfields"
    connector_id: str = "nodes-base.metabase"
    description: str = "Tool for metabase getFields operation - getFields operation"
    args_schema: type[BaseModel] | None = MetabaseGetfieldsToolInput
    credentials: Optional[MetabaseCredentials] = None
