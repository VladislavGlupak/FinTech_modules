# Imports
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import hashlib

# Creating the Block data class
@dataclass # decorator
class Block:
    data: Any # attribute
    creator_id: int
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

# Creating a new block
new_block = Block(data="My First Block!", creator_id=42)
# Print the new block
print(new_block)