"""valid.py
This file includes mostly of our input sanitation code.
"""

import pathlib
import logging
import traceback
import sys

import turingmachinelang
from textx import TextXSyntaxError


logger = logging.getLogger(__name__)


def language_file_path(file_path: pathlib.Path) -> bool:
    if not file_path.exists():
        logger.error("file path invalid: File does not exist")
        return False

    if not file_path.is_file():
        logger.error("file path invalid: Path does not point to File")
        return False

    # Ignore this check. suffix is a suggestion of file type

    # suffix: str = turingmachinelang.tml_language.pattern
    # suffix = suffix.removeprefix('*')

    # if file_path.suffix != suffix:
    #     logger.error("file path invalid: file suffix is incorrect. expected file to end with %s", suffix)
    #     return False

    return True


def language_syntax(file_path: pathlib.Path):

    mm = turingmachinelang.tml_language.metamodel()

    try:
        model = mm.model_from_file(file_path)
    except TextXSyntaxError as e:
        # logger.error("Syntax Error: %s", e)
        # traceback.print_exc(chain=False, limit=1, file=sys.stderr)
        print(f"Syntax Error: {e}", file=sys.stderr)
        return None

    return model
