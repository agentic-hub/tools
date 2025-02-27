from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftsqlCredentials

class MicrosoftsqlExecutequeryToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    query: Optional[str] = Field(None, description="The SQL query to execute")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class MicrosoftsqlExecutequeryTool(BaseTool):
    name: str = "microsoftsql_executequery"
    connector_id: str = "nodes-base.microsoftSql"
    description: str = "Tool for microsoftSql executeQuery operation - executeQuery operation"
    args_schema: type[BaseModel] | None = MicrosoftsqlExecutequeryToolInput
    credentials: Optional[MicrosoftsqlCredentials] = None
