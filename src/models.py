from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import uuid

@dataclass
class CosmicMessage:
    content: str
    sender: str = "Earth-Node"
    receiver: str = "Universal-Node"
    universe: str = "Universe-Alpha"
    message_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)
    encryption_key: str = "quantum-secure-v1"

@dataclass
class CosmicResponse:
    content: str
    responder: str
    original_message_id: str
    timestamp: datetime = field(default_factory=datetime.now)
    universe_origin: str = "Universe-Beta"
