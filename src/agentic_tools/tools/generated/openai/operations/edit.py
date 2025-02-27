from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OpenaiCredentials

class OpenaiEditToolInput(BaseModel):
    prompt: Optional[Dict[str, Any]] = Field(None, description="Prompt")
    simplify_output: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    input: Optional[str] = Field(None, description="The input text to be edited")
    instruction: Optional[str] = Field(None, description="The instruction that tells the model how to edit the input text")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional options to add")
    model: Optional[str] = Field(None, description="The model which will generate the edited version. <a href=\"https://beta.openai.com/docs/models/overview\">Learn more</a>.")
    notice_advance_ai: Optional[str] = Field(None, description="For more advanced uses, consider using an <a data-action=\"openSelectiveNodeCreator\" data-action-parameter-creatorview=\"AI\">advanced AI</a> node")
    operation: Optional[str] = Field(None, description="Operation")


class OpenaiEditTool(BaseTool):
    name: str = "openai_edit"
    connector_id: str = "nodes-base.openAi"
    description: str = "Tool for openAi edit operation - edit operation"
    args_schema: type[BaseModel] | None = OpenaiEditToolInput
    credentials: Optional[OpenaiCredentials] = None
