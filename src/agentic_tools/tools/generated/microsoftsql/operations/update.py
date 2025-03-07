from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftsqlCredentials

class MicrosoftsqlUpdateToolInput(BaseModel):
    update_key: Optional[str] = Field(None, description="Name of the property which decides which rows in the database should be updated. Normally that would be \"id\".")
    table: Optional[str] = Field(None, description="Name of the table in which to update data in")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for rows to update")


class MicrosoftsqlUpdateTool(BaseTool):
    name: str = "microsoftsql_update"
    connector_id: str = "nodes-base.microsoftSql"
    description: str = "Tool for microsoftSql update operation - update operation"
    args_schema: type[BaseModel] | None = MicrosoftsqlUpdateToolInput
    credentials: Optional[MicrosoftsqlCredentials] = None
