from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MongodbCredentials

class MongodbUpdateToolInput(BaseModel):
    update_key: Optional[str] = Field(None, description="Name of the property which decides which rows in the database should be updated. Normally that would be \"id\".")
    upsert: Optional[bool] = Field(None, description="Whether to perform an insert if no documents match the update key")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    collection: Optional[str] = Field(None, description="MongoDB Collection")
    fields: Optional[str] = Field(None, description="Comma-separated list of the fields to be included into the new document")
    query: Optional[str] = Field(None, description="MongoDB aggregation pipeline query in JSON format")
    operation: Optional[str] = Field(None, description="Operation")


class MongodbUpdateTool(BaseTool):
    name: str = "mongodb_update"
    connector_id: str = "nodes-base.mongoDb"
    description: str = "Tool for mongoDb update operation - update operation"
    args_schema: type[BaseModel] | None = MongodbUpdateToolInput
    credentials: Optional[MongodbCredentials] = None
