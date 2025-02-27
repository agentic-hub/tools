from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SecurityscorecardCredentials

class SecurityscorecardGetscoreToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    scorecard_identifier: Optional[str] = Field(None, description="Primary identifier of a company or scorecard, i.e. domain.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    industry: Optional[str] = Field(None, description="Industry")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    portfolio_id: Optional[str] = Field(None, description="Portfolio ID")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")


class SecurityscorecardGetscoreTool(BaseTool):
    name: str = "securityscorecard_getscore"
    description: str = "Tool for securityScorecard getScore operation - getScore operation"
    args_schema: type[BaseModel] | None = SecurityscorecardGetscoreToolInput
    credentials: Optional[SecurityscorecardCredentials] = None
