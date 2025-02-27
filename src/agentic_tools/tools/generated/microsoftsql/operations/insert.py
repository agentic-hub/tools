from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftsqlCredentials

class MicrosoftsqlInsertToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class MicrosoftsqlInsertTool(BaseTool):
    name: str = "microsoftsql_insert"
    connector_id: str = "nodes-base.microsoftSql"
    description: str = "Tool for microsoftSql insert operation - insert operation"
    args_schema: type[BaseModel] | None = MicrosoftsqlInsertToolInput
    credentials: Optional[MicrosoftsqlCredentials] = None
