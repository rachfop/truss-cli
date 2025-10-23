from typing import Any, Dict, List


class Model:
    def __init__(self, **kwargs: Any) -> None:
        # No-op init; included for baseline interface completeness.
        pass

    def predict(self, request: Dict[str, Any]) -> List[int]:
        """Double each input value from the incoming request payload."""
        inputs = request.get("inputs", [])
        return [value * 2 for value in inputs]
