from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OpenaiCredentials

class OpenaiCreateToolInput(BaseModel):
    prompt: Optional[str] = Field(None, description="A text description of the desired image(s). The maximum length is 1000 characters.")
    simplify_output: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    input: Optional[str] = Field(None, description="The input text to be edited")
    resource: Optional[str] = Field(None, description="Resource")
    image_model: Optional[str] = Field(None, description="The model to use for image generation")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional options to add")
    model: Optional[str] = Field(None, description="The model to use for image generation")
    notice_advance_ai: Optional[str] = Field(None, description="For more advanced uses, consider using an <a data-action=\"openSelectiveNodeCreator\" data-action-parameter-creatorview=\"AI\">advanced AI</a> node")
    operation: Optional[str] = Field(None, description="Operation")
    response_format: Optional[str] = Field(None, description="The format in which to return the image(s)")


class OpenaiCreateTool(BaseTool):
    name: str = "openai_create"
    connector_id: str = "nodes-base.openAi"
    description: str = "Tool for openAi create operation - create operation"
    args_schema: type[BaseModel] | None = OpenaiCreateToolInput
    credentials: Optional[OpenaiCredentials] = None
