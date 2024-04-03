import argparse
import logging
import pathlib

from turingmachinetranspiler import (
    __name__ as __package__name__,
    __doc__ as __package__doc__,
)
from turingmachinetranspiler import valid

logger = logging.getLogger(__name__)


def main():
    parser = init_parser()
    args = parser.parse_args()

    # logging
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    elif args.quiet:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=logging.INFO)

    logger.debug("loading arguments")
    file_path = args.file_path

    # This is handled by setting the type to FilePath
    logger.debug("checking file path")
    if not valid.language_file_path(file_path):
        return -1

    logger.debug("checking language syntax")
    model = valid.language_syntax(file_path)
    if model is None:
        return -1

    # Valid language.
    model.states
    return 0


def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=__package__name__, description=__package__doc__
    )

    # parser.add_argument("file_path", type=argparse.FileType("r"), help="path to tm file")
    parser.add_argument("file_path", type=pathlib.Path, help="path to tm file")

    log_levels = parser.add_mutually_exclusive_group()

    log_levels.add_argument(
        "--verbose", action="store_true", help="print debug messages"
    )
    log_levels.add_argument("--quiet", action="store_true", help="print less messages")

    return parser


if __name__ == "__main__":
    main()
