from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftsqlCredentials

class MicrosoftsqlDeleteToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Name of the table in which to delete data")
    delete_key: Optional[str] = Field(None, description="Name of the property which decides which rows in the database should be deleted. Normally that would be \"id\".")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class MicrosoftsqlDeleteTool(BaseTool):
    name: str = "microsoftsql_delete"
    connector_id: str = "nodes-base.microsoftSql"
    description: str = "Tool for microsoftSql delete operation - delete operation"
    args_schema: type[BaseModel] | None = MicrosoftsqlDeleteToolInput
    credentials: Optional[MicrosoftsqlCredentials] = None
