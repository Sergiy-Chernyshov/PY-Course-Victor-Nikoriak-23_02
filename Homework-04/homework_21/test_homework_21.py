# task1

import logging
from pathlib import Path
from typing import IO, Any, Optional


class FileContextManager:

    total_opened = 0
    total_closed = 0
    active_contexts = 0

    def __init__(
        self,
        file: str | Path,
        mode: str = "r",
        buffering: int = -1,
        encoding: Optional[str] = None,
        errors: Optional[str] = None,
        newline: Optional[str] = None,
        closefd: bool = True,
        opener: Any = None,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        self.file = file
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.logger = logger or logging.getLogger(self.__class__.__name__)
        self._file: Optional[IO[Any]] = None

    def __enter__(self) -> IO[Any]:
        self._file = open(
            file=self.file,
            mode=self.mode,
            buffering=self.buffering,
            encoding=self.encoding,
            errors=self.errors,
            newline=self.newline,
            closefd=self.closefd,
            opener=self.opener,
        )
        type(self).total_opened += 1
        type(self).active_contexts += 1
        self.logger.info("Opened %s in mode %s", self.file, self.mode)
        return self._file

    def __exit__(self, exc_type, exc_value, traceback) -> bool:

        try:
            if self._file is not None and not self._file.closed:
                self._file.close()
                type(self).total_closed += 1
                self.logger.info("Closed %s", self.file)
        finally:
            if type(self).active_contexts > 0:
                type(self).active_contexts -= 1

        if exc_type is not None:
            self.logger.exception(
                "Exception while using %s: %s",
                self.file,
                exc_value,
                exc_info=(exc_type, exc_value, traceback),
            )

        return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    with FileContextManager("../example.txt", "w", encoding="utf-8") as file:
        file.write("Hello from FileContextManager\n")

    print("Opened:", FileContextManager.total_opened)
    print("Closed:", FileContextManager.total_closed)
    print("Active:", FileContextManager.active_contexts)

print("\n")

#task2

import logging
from pathlib import Path
from typing import IO, Any, Optional


class FileContextManager:

    total_opened = 0
    total_closed = 0
    active_contexts = 0

    def __init__(
        self,
        file: str | Path,
        mode: str = "r",
        buffering: int = -1,
        encoding: Optional[str] = None,
        errors: Optional[str] = None,
        newline: Optional[str] = None,
        closefd: bool = True,
        opener: Any = None,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        self.file = file
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.logger = logger or logging.getLogger(self.__class__.__name__)
        self._file: Optional[IO[Any]] = None

    def __enter__(self) -> IO[Any]:
        self._file = open(
            file=self.file,
            mode=self.mode,
            buffering=self.buffering,
            encoding=self.encoding,
            errors=self.errors,
            newline=self.newline,
            closefd=self.closefd,
            opener=self.opener,
        )
        type(self).total_opened += 1
        type(self).active_contexts += 1
        self.logger.info("Opened %s in mode %s", self.file, self.mode)
        return self._file

    def __exit__(self, exc_type, exc_value, traceback) -> bool:

        try:
            if self._file is not None and not self._file.closed:
                self._file.close()
                type(self).total_closed += 1
                self.logger.info("Closed %s", self.file)
        finally:
            if type(self).active_contexts > 0:
                type(self).active_contexts -= 1

        if exc_type is not None:
            self.logger.exception(
                "Exception while using %s: %s",
                self.file,
                exc_value,
                exc_info=(exc_type, exc_value, traceback),
            )

        return False

print("\n")

# Task3

def test(file_obj):

    content = file_obj.read()
    words = content.split()
    lines = [line.strip() for line in content.splitlines() if line.strip()]

    return {
        "characters": len(content),
        "words": len(words),
        "lines": len(lines),
        "uppercase": content.upper(),
    }

from pathlib import Path
import uuid

import pytest

from file_context_manager import FileContextManager
from text_logic import test


@pytest.fixture
def file_obj():
    file_path = Path("C:/CODEX") / f"pytest_text_{uuid.uuid4().hex}.txt"
    file_path.write_text("Hello world\nPytest fixture example\n", encoding="utf-8")

    with FileContextManager(file_path, "r", encoding="utf-8") as opened_file:
        yield opened_file

    if file_path.exists():
        file_path.unlink()


def test_text_processing_with_context_manager_fixture(file_obj):
    result = test(file_obj)

    assert result["characters"] == len("Hello world\nPytest fixture example\n")
    assert result["words"] == 5
    assert result["lines"] == 2
    assert result["uppercase"] == "HELLO WORLD\nPYTEST FIXTURE EXAMPLE\n"