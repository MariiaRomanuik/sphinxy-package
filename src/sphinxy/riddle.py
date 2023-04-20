from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """Checks the answer.

        Args:
            answer (str): The given answer to the riddle.

        Returns:
            bool: The result of the check of the answer.
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """Get a hint.

        Returns:
            Iterator: Iterable of strings of the hint to the riddle.
        """
        yield from iter(self.answer)
