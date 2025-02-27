from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MongodbCredentials

class MongodbDeleteToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Add query options")
    collection: Optional[str] = Field(None, description="MongoDB Collection")
    fields: Optional[str] = Field(None, description="Comma-separated list of the fields to be included into the new document")
    query: Optional[str] = Field(None, description="MongoDB Delete query")
    operation: Optional[str] = Field(None, description="Operation")


class MongodbDeleteTool(BaseTool):
    name: str = "mongodb_delete"
    description: str = "Tool for mongoDb delete operation - delete operation"
    args_schema: type[BaseModel] | None = MongodbDeleteToolInput
    credentials: Optional[MongodbCredentials] = None
