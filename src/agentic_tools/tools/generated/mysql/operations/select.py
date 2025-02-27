from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MysqlCredentials

class MysqlSelectToolInput(BaseModel):
    sort: Optional[Dict[str, Any]] = Field(None, description="Sort")
    data_mode: Optional[str] = Field(None, description="Whether to map node input properties and the table data automatically or manually")
    resource: Optional[str] = Field(None, description="Resource")
    table: Optional[str] = Field(None, description="Name")
    combine_conditions: Optional[str] = Field(None, description="How to combine the conditions defined in \"Select Rows\": AND requires all conditions to be true, OR requires at least one condition to be true")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    where: Optional[Dict[str, Any]] = Field(None, description="If not set, all rows will be selected")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    column_to_match_on: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\" target=\"_blank\">expression</a>")
    value_to_match_on: Optional[str] = Field(None, description="Rows with a value in the specified \"Column to Match On\" that corresponds to the value in this field will be updated")
    notice: Optional[str] = Field(None, description="
		In this mode, make sure incoming data fields are named the same as the columns in your table. If needed, use an 'Edit Fields' node before this node to change the field names.
		")
    operation: Optional[str] = Field(None, description="Operation")
    values_to_send: Optional[Dict[str, Any]] = Field(None, description="Values to Send")


class MysqlSelectTool(BaseTool):
    name: str = "mysql_select"
    description: str = "Tool for mySql select operation - select operation"
    args_schema: type[BaseModel] | None = MysqlSelectToolInput
    credentials: Optional[MysqlCredentials] = None
