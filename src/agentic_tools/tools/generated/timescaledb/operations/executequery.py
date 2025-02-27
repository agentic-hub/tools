from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TimescaledbCredentials

class TimescaledbExecutequeryToolInput(BaseModel):
    schema: Optional[str] = Field(None, description="Name of the schema the table belongs to")
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    query: Optional[str] = Field(None, description="The SQL query to execute. You can use n8n expressions or $1 and $2 in conjunction with query parameters.")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class TimescaledbExecutequeryTool(BaseTool):
    name: str = "timescaledb_executequery"
    connector_id: str = "nodes-base.timescaleDb"
    description: str = "Tool for timescaleDb executeQuery operation - executeQuery operation"
    args_schema: type[BaseModel] | None = TimescaledbExecutequeryToolInput
    credentials: Optional[TimescaledbCredentials] = None
