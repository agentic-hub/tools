from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SecurityscorecardCredentials

class SecurityscorecardGetscoreplanToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    scorecard_identifier: Optional[str] = Field(None, description="Primary identifier of a company or scorecard, i.e. domain.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    score: Optional[float] = Field(None, description="Score target")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    portfolio_id: Optional[str] = Field(None, description="Portfolio ID")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")


class SecurityscorecardGetscoreplanTool(BaseTool):
    name: str = "securityscorecard_getscoreplan"
    connector_id: str = "nodes-base.securityScorecard"
    description: str = "Tool for securityScorecard getScorePlan operation - getScorePlan operation"
    args_schema: type[BaseModel] | None = SecurityscorecardGetscoreplanToolInput
    credentials: Optional[SecurityscorecardCredentials] = None
