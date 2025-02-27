from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwsdynamodbCredentials

class AwsdynamodbDeleteToolInput(BaseModel):
    keys_ui: Optional[Dict[str, Any]] = Field(None, description="Item's primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.")
    filter_expression: Optional[str] = Field(None, description="A filter expression determines which items within the Scan results should be returned to you. All of the other results are discarded. Empty value will return all Scan results.")
    select: Optional[str] = Field(None, description="Select")
    operation: Optional[str] = Field(None, description="Operation")
    return_values: Optional[str] = Field(None, description="Use ReturnValues if you want to get the item attributes as they appeared before they were deleted")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    table_name: Optional[str] = Field(None, description="Table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class AwsdynamodbDeleteTool(BaseTool):
    name: str = "awsdynamodb_delete"
    description: str = "Tool for awsDynamoDb delete operation - delete operation"
    args_schema: type[BaseModel] | None = AwsdynamodbDeleteToolInput
    credentials: Optional[AwsdynamodbCredentials] = None
