from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ConvertkitCredentials

class ConvertkitAddsubscriberToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="The subscriber's email address")
    id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class ConvertkitAddsubscriberTool(BaseTool):
    name: str = "convertkit_addsubscriber"
    description: str = "Tool for convertKit addSubscriber operation - addSubscriber operation"
    args_schema: type[BaseModel] | None = ConvertkitAddsubscriberToolInput
    credentials: Optional[ConvertkitCredentials] = None
