from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OpenaiModerateToolInput(BaseModel):
    prompt: Optional[Dict[str, Any]] = Field(None, description="Prompt")
    simplifyOutput: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    input: Optional[str] = Field(None, description="The input text to classify")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional options to add")
    model: Optional[str] = Field(None, description="The model which will classify the text. <a href=\"https://beta.openai.com/docs/models/overview\">Learn more</a>.")
    noticeAdvanceAi: Optional[str] = Field(None, description="For more advanced uses, consider using an <a data-action=\"openSelectiveNodeCreator\" data-action-parameter-creatorview=\"AI\">advanced AI</a> node")
    operation: Optional[str] = Field(None, description="Operation")


class OpenaiModerateTool(BaseTool):
    name = "openai_moderate"
    description = "Tool for openAi moderate operation - moderate operation"
    
    def _run(self, **kwargs):
        """Run the openAi moderate operation."""
        # Implement the tool logic here
        return f"Running openAi moderate operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the openAi moderate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
