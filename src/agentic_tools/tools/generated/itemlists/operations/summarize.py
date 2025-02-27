from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ItemlistsSummarizeToolInput(BaseModel):
    fields_to_exclude: Optional[str] = Field(None, description="Fields To Exclude")
    fields_to_summarize: Optional[Dict[str, Any]] = Field(None, description="Fields to Summarize")
    fields_to_split_by: Optional[str] = Field(None, description="The name of the input fields that you want to split the summary by")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_include: Optional[str] = Field(None, description="Fields To Include")
    resource: Optional[str] = Field(None, description="Resource")
    include: Optional[str] = Field(None, description="Include")


class ItemlistsSummarizeTool(BaseTool):
    name: str = "itemlists_summarize"
    description: str = "Tool for itemLists summarize operation - summarize operation"
    args_schema: type[BaseModel] | None = ItemlistsSummarizeToolInput
