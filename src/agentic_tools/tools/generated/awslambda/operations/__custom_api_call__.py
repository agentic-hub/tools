from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwslambdaCredentials

class Awslambda__custom_api_call__ToolInput(BaseModel):
    operation: Optional[str] = Field(None, description="Operation")


class Awslambda__custom_api_call__Tool(BaseTool):
    name: str = "awslambda___custom_api_call__"
    description: str = "Tool for awsLambda __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Awslambda__custom_api_call__ToolInput
    credentials: Optional[AwslambdaCredentials] = None
