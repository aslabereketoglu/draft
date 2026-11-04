"""Evidence card store and retrieval (DECISIONS.md F1 rows 4, 5a, 11, 18).

Retrieval is by dimension tag: the rewriter gets the cards for the dimensions that scored low.
No embedding model is needed (row 5a). Only cards with review decision Approve or Edit are used.
"""
import json
from dataclasses import dataclass
from pathlib import Path

CARDS_PATH = Path(__file__).resolve().parents[2] / "knowledge" / "evidence_cards.json"


@dataclass(frozen=True)
class Card:
    id: str
    rubric: str
    dimension: str
    finding: str
    limits: str
    setting: str
    source: str
    locator: str


def load_cards(path: Path = CARDS_PATH) -> dict[str, Card]:
    data = json.loads(path.read_text(encoding="utf-8"))
    names = data["sources"]
    cards = {}
    for c in data["cards"]:
        if c.get("review", {}).get("decision", "Approve") not in ("Approve", "Edit"):
            continue
        cards[c["id"]] = Card(c["id"], c["rubric"], c["dimension"], c["finding"], c["limits"], c["setting"],
                              f"{names[c['source']]}", c["locator"])
    return cards


def retrieve(cards: dict[str, Card], message_type: str, dimensions: list[str]) -> list[Card]:
    """Cards for the given dimension keys of one rubric, in stable order."""
    wanted = set(dimensions)
    return [c for c in cards.values() if c.rubric == message_type and c.dimension in wanted]
