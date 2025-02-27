from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MongodbCredentials

class MongodbAggregateToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Add query options")
    collection: Optional[str] = Field(None, description="MongoDB Collection")
    fields: Optional[str] = Field(None, description="Comma-separated list of the fields to be included into the new document")
    query: Optional[str] = Field(None, description="MongoDB aggregation pipeline query in JSON format")
    operation: Optional[str] = Field(None, description="Operation")


class MongodbAggregateTool(BaseTool):
    name: str = "mongodb_aggregate"
    connector_id: str = "nodes-base.mongoDb"
    description: str = "Tool for mongoDb aggregate operation - aggregate operation"
    args_schema: type[BaseModel] | None = MongodbAggregateToolInput
    credentials: Optional[MongodbCredentials] = None
