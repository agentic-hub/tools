from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglebigqueryCredentials

class GooglebigqueryExecutequeryToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    project_id: Optional[str] = Field(None, description="By URL")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    sql_query: Optional[str] = Field(None, description="SQL query to execute, you can find more information <a href=\"https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax\" target=\"_blank\">here</a>. Standard SQL syntax used by default, but you can also use Legacy SQL syntax by using optinon 'Use Legacy SQL'.")
    operation: Optional[str] = Field(None, description="Operation")


class GooglebigqueryExecutequeryTool(BaseTool):
    name: str = "googlebigquery_executequery"
    description: str = "Tool for googleBigQuery executeQuery operation - executeQuery operation"
    args_schema: type[BaseModel] | None = GooglebigqueryExecutequeryToolInput
    credentials: Optional[GooglebigqueryCredentials] = None
