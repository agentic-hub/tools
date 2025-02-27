from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwsrekognitionCredentials

class Awsrekognition__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Awsrekognition__custom_api_call__Tool(BaseTool):
    name: str = "awsrekognition___custom_api_call__"
    description: str = "Tool for awsRekognition __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Awsrekognition__custom_api_call__ToolInput
    credentials: Optional[AwsrekognitionCredentials] = None
