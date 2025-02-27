from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglebigqueryCredentials

class Googlebigquery__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    sql_query: Optional[str] = Field(None, description="SQL query to execute, you can find more information <a href=\"https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax\" target=\"_blank\">here</a>. Standard SQL syntax used by default, but you can also use Legacy SQL syntax by using optinon 'Use Legacy SQL'.")
    operation: Optional[str] = Field(None, description="Operation")


class Googlebigquery__custom_api_call__Tool(BaseTool):
    name: str = "googlebigquery___custom_api_call__"
    description: str = "Tool for googleBigQuery __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googlebigquery__custom_api_call__ToolInput
    credentials: Optional[GooglebigqueryCredentials] = None
