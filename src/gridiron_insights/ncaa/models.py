from pydantic import BaseModel, Field
from typing import List, Optional


class Conference(BaseModel):
    conferenceName: str
    conferenceSeo: str


class TeamNames(BaseModel):
    char6: str
    short: str
    seo: str
    full: str


class Team(BaseModel):
    score: Optional[str] = ""
    names: TeamNames
    winner: bool
    seed: Optional[str] = ""
    description: Optional[str] = ""
    rank: Optional[str] = ""
    conferences: List[Conference]


class GameDetails(BaseModel):
    gameID: str
    away: Team
    home: Team
    finalMessage: Optional[str] = ""
    bracketRound: Optional[str] = ""
    title: str
    contestName: Optional[str] = ""
    url: str
    network: Optional[str] = ""
    liveVideoEnabled: bool
    startTime: str
    startTimeEpoch: str
    bracketId: Optional[str] = ""
    gameState: str
    startDate: str
    currentPeriod: Optional[str] = ""
    videoState: Optional[str] = ""
    bracketRegion: Optional[str] = ""
    contestClock: Optional[str] = ""


class Game(BaseModel):
    game: GameDetails


class RootModel(BaseModel):
    inputMD5Sum: str
    instanceId: str
    updated_at: str
    games: List[Game]
    hideRank: bool
