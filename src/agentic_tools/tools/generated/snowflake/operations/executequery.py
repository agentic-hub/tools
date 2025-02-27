from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SnowflakeCredentials

class SnowflakeExecutequeryToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    query: Optional[str] = Field(None, description="The SQL query to execute")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class SnowflakeExecutequeryTool(BaseTool):
    name: str = "snowflake_executequery"
    connector_id: str = "nodes-base.snowflake"
    description: str = "Tool for snowflake executeQuery operation - executeQuery operation"
    args_schema: type[BaseModel] | None = SnowflakeExecutequeryToolInput
    credentials: Optional[SnowflakeCredentials] = None
