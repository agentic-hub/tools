from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OpenaiEditToolInput(BaseModel):
    prompt: Optional[Dict[str, Any]] = Field(None, description="Prompt")
    simplifyOutput: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    input: Optional[str] = Field(None, description="The input text to be edited")
    instruction: Optional[str] = Field(None, description="The instruction that tells the model how to edit the input text")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional options to add")
    model: Optional[str] = Field(None, description="The model which will generate the edited version. <a href=\"https://beta.openai.com/docs/models/overview\">Learn more</a>.")
    noticeAdvanceAi: Optional[str] = Field(None, description="For more advanced uses, consider using an <a data-action=\"openSelectiveNodeCreator\" data-action-parameter-creatorview=\"AI\">advanced AI</a> node")
    operation: Optional[str] = Field(None, description="Operation")


class OpenaiEditTool(BaseTool):
    name = "openai_edit"
    description = "Tool for openAi edit operation - edit operation"
    
    def _run(self, **kwargs):
        """Run the openAi edit operation."""
        # Implement the tool logic here
        return f"Running openAi edit operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the openAi edit operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
