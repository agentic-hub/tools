from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwsdynamodbCredentials

class Awsdynamodb__custom_api_call__ToolInput(BaseModel):
    keys_ui: Optional[Dict[str, Any]] = Field(None, description="Item's primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.")
    filter_expression: Optional[str] = Field(None, description="A filter expression determines which items within the Scan results should be returned to you. All of the other results are discarded. Empty value will return all Scan results.")
    select: Optional[str] = Field(None, description="Select")
    operation: Optional[str] = Field(None, description="Operation")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    table_name: Optional[str] = Field(None, description="Table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class Awsdynamodb__custom_api_call__Tool(BaseTool):
    name: str = "awsdynamodb___custom_api_call__"
    description: str = "Tool for awsDynamoDb __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Awsdynamodb__custom_api_call__ToolInput
    credentials: Optional[AwsdynamodbCredentials] = None
