from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CratedbCredentials

class CratedbExecutequeryToolInput(BaseModel):
    schema: Optional[str] = Field(None, description="Name of the schema the table belongs to")
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    query: Optional[str] = Field(None, description="The SQL query to execute. You can use n8n expressions or $1 and $2 in conjunction with query parameters.")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class CratedbExecutequeryTool(BaseTool):
    name: str = "cratedb_executequery"
    connector_id: str = "nodes-base.crateDb"
    description: str = "Tool for crateDb executeQuery operation - executeQuery operation"
    args_schema: type[BaseModel] | None = CratedbExecutequeryToolInput
    credentials: Optional[CratedbCredentials] = None
