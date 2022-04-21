# Imports
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import hashlib

@dataclass
class Counter:
    count: int = 0

    def update_count(self):
        self.count = self.count + 1

# Create a new instance of Counter
new_counter = Counter()

# Update the count by calling update_count
new_counter.update_count()
new_counter.update_count()

# Print the updated value of count
print("The current count is: ", new_counter.count)

# The Block class
@dataclass
class Block:
    data: Any
    creator_id: int
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

    # Create a method called hash_block
    def hash_block(self):
        sha = hashlib.sha256()

        # Turn the block data into an encoded string
        data = str(self.data).encode()
        sha.update(data)

        # Turn the block timestamp into an encoded string
        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        return sha.hexdigest()

# Create a new block instance using some test data
new_block = Block(data="test", creator_id=42)

# Calculate the block hash using the new method
block_hash = new_block.hash_block()

# Print the block's hash
print(block_hash)