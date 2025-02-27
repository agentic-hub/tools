from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CratedbCredentials

class CratedbUpdateToolInput(BaseModel):
    schema: Optional[str] = Field(None, description="Name of the schema the table belongs to")
    update_key: Optional[str] = Field(None, description="Comma-separated list of the properties which decides which rows in the database should be updated. Normally that would be \"id\".")
    table: Optional[str] = Field(None, description="Name of the table in which to update data in")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_fields: Optional[str] = Field(None, description="Comma-separated list of the fields that the operation will return")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for rows to update")


class CratedbUpdateTool(BaseTool):
    name: str = "cratedb_update"
    connector_id: str = "nodes-base.crateDb"
    description: str = "Tool for crateDb update operation - update operation"
    args_schema: type[BaseModel] | None = CratedbUpdateToolInput
    credentials: Optional[CratedbCredentials] = None
