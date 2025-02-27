from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OpenaiCredentials

class Openai__custom_api_call__ToolInput(BaseModel):
    prompt: Optional[Dict[str, Any]] = Field(None, description="Prompt")
    simplify_output: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    input: Optional[str] = Field(None, description="The input text to be edited")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional options to add")
    model: Optional[str] = Field(None, description="The model which will generate the completion. <a href=\"https://beta.openai.com/docs/models/overview\">Learn more</a>.")
    notice_advance_ai: Optional[str] = Field(None, description="For more advanced uses, consider using an <a data-action=\"openSelectiveNodeCreator\" data-action-parameter-creatorview=\"AI\">advanced AI</a> node")
    operation: Optional[str] = Field(None, description="Operation")


class Openai__custom_api_call__Tool(BaseTool):
    name: str = "openai___custom_api_call__"
    description: str = "Tool for openAi __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Openai__custom_api_call__ToolInput
    credentials: Optional[OpenaiCredentials] = None
