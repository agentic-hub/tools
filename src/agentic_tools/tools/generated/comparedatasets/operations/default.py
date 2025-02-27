from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ComparedatasetsDefaultToolInput(BaseModel):
    fuzzy_compare: Optional[bool] = Field(None, description="Whether to tolerate small type differences when comparing fields. E.g. the number 3 and the string '3' are treated as the same.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resolve: Optional[str] = Field(None, description="When There Are Differences")
    info_box: Optional[str] = Field(None, description="Items from different branches are paired together when the fields below match. If paired, the rest of the fields are compared to determine whether the items are the same or different")
    merge_by_fields: Optional[Dict[str, Any]] = Field(None, description="Fields to Match")
    prefer_when_mix: Optional[str] = Field(None, description="Prefer")
    except_when_mix: Optional[str] = Field(None, description="For Everything Except")


class ComparedatasetsDefaultTool(BaseTool):
    name: str = "comparedatasets_default"
    description: str = "Tool for compareDatasets default operation - default operation"
    args_schema: type[BaseModel] | None = ComparedatasetsDefaultToolInput
