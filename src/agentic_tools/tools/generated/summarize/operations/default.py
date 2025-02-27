from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SummarizeDefaultToolInput(BaseModel):
    fields_to_summarize: Optional[Dict[str, Any]] = Field(None, description="Fields to Summarize")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_split_by: Optional[str] = Field(None, description="The name of the input fields that you want to split the summary by")


class SummarizeDefaultTool(BaseTool):
    name: str = "summarize_default"
    connector_id: str = "nodes-base.summarize"
    description: str = "Tool for summarize default operation - default operation"
    args_schema: type[BaseModel] | None = SummarizeDefaultToolInput
