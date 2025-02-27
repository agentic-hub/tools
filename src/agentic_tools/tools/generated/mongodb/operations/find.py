from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MongodbCredentials

class MongodbFindToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Add query options")
    collection: Optional[str] = Field(None, description="MongoDB Collection")
    fields: Optional[str] = Field(None, description="Comma-separated list of the fields to be included into the new document")
    query: Optional[str] = Field(None, description="MongoDB Find query")
    operation: Optional[str] = Field(None, description="Operation")


class MongodbFindTool(BaseTool):
    name: str = "mongodb_find"
    description: str = "Tool for mongoDb find operation - find operation"
    args_schema: type[BaseModel] | None = MongodbFindToolInput
    credentials: Optional[MongodbCredentials] = None
