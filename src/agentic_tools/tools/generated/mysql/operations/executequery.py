from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MysqlCredentials

class MysqlExecutequeryToolInput(BaseModel):
    data_mode: Optional[str] = Field(None, description="Whether to map node input properties and the table data automatically or manually")
    resource: Optional[str] = Field(None, description="Resource")
    table: Optional[str] = Field(None, description="Name")
    combine_conditions: Optional[str] = Field(None, description="How to combine the conditions defined in \"Select Rows\": AND requires all conditions to be true, OR requires at least one condition to be true")
    where: Optional[Dict[str, Any]] = Field(None, description="If not set, all rows will be selected")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    column_to_match_on: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\" target=\"_blank\">expression</a>")
    value_to_match_on: Optional[str] = Field(None, description="Rows with a value in the specified \"Column to Match On\" that corresponds to the value in this field will be updated")
    notice: Optional[str] = Field(None, description="
		In this mode, make sure incoming data fields are named the same as the columns in your table. If needed, use an 'Edit Fields' node before this node to change the field names.
		")
    query: Optional[str] = Field(None, description="The SQL query to execute. You can use n8n expressions and $1, $2, $3, etc to refer to the 'Query Parameters' set in options below.")
    operation: Optional[str] = Field(None, description="Operation")
    values_to_send: Optional[Dict[str, Any]] = Field(None, description="Values to Send")


class MysqlExecutequeryTool(BaseTool):
    name: str = "mysql_executequery"
    description: str = "Tool for mySql executeQuery operation - executeQuery operation"
    args_schema: type[BaseModel] | None = MysqlExecutequeryToolInput
    credentials: Optional[MysqlCredentials] = None
