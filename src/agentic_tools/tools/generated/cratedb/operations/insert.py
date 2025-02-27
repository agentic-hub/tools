from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CratedbCredentials

class CratedbInsertToolInput(BaseModel):
    schema: Optional[str] = Field(None, description="Name of the schema the table belongs to")
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_fields: Optional[str] = Field(None, description="Comma-separated list of the fields that the operation will return")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class CratedbInsertTool(BaseTool):
    name: str = "cratedb_insert"
    description: str = "Tool for crateDb insert operation - insert operation"
    args_schema: type[BaseModel] | None = CratedbInsertToolInput
    credentials: Optional[CratedbCredentials] = None
