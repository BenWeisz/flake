from typing import List
import re

# Structure

class AtomicNode:
    T: str
    name: str

    def __init__(self) -> None:
        self.T = ""
        self.name = ""

    def __repr__(self) -> str:
        return f"{self.T}: {self.name}"

class ArrayNode(AtomicNode):
    S: str

    def __init__(self) -> None:
        super().__init__()
        self.S = ""

class FlakeNode(AtomicNode):
    children: List[AtomicNode]
    
    def __init__(self) -> None:
        super().__init__()
        self.children = []

# Parsing

def build_ast(lines: List[str]) -> List[AtomicNode]:
    """ Build an ast out of AtomicNode's from the flake source.
    
        Expects the raw lines from the template file.
    """

    # Patterns    
    flake_pattern = r"\*([a-zA-Z]+[a-zA-Z0-9_\s]*)\*"

    # First pass to get all the flake names
    flake_names = []
    for line in lines:
        flake_match = re.match(flake_pattern, line)
        if flake_match:
            # flake_match

    flakes = []
    curr_flake = None

    for line in lines:
        flake_match = re.match(flake_pattern, line)
        if flake_match:
            if curr_flake is not None:
                flakes.append(curr_flake)

            flake_type = flake_match.group(1)
            flake_type = flake_type.replace(" ", "_").upper()
            
            curr_flake = FlakeNode() 
            curr_flake.T = flake_type
            curr_flake.name = "root"
        else:
            pass

    if curr_flake is not None:
        flakes.append(curr_flake)
            
    return flakes