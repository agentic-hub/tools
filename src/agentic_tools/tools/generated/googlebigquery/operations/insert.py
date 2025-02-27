from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglebigqueryCredentials

class GooglebigqueryInsertToolInput(BaseModel):
    data_mode: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="By ID")
    dataset_id: Optional[str] = Field(None, description="By ID")
    project_id: Optional[str] = Field(None, description="By URL")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    sql_query: Optional[str] = Field(None, description="SQL query to execute, you can find more information <a href=\"https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax\" target=\"_blank\">here</a>. Standard SQL syntax used by default, but you can also use Legacy SQL syntax by using optinon 'Use Legacy SQL'.")
    operation: Optional[str] = Field(None, description="Operation")
    info: Optional[str] = Field(None, description="In this mode, make sure the incoming data fields are named the same as the columns in BigQuery. (Use an 'Edit Fields' node before this node to change them if required.)")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")


class GooglebigqueryInsertTool(BaseTool):
    name: str = "googlebigquery_insert"
    description: str = "Tool for googleBigQuery insert operation - insert operation"
    args_schema: type[BaseModel] | None = GooglebigqueryInsertToolInput
    credentials: Optional[GooglebigqueryCredentials] = None
