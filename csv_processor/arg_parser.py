import argparse
import re

from .args import COMBINED_ARGS_CONFIG, ArgParseConfig, Arguments


def parse_args() -> Arguments:
    arguments = argparse.ArgumentParser()

    for config in COMBINED_ARGS_CONFIG:
        arguments.add_argument(
            *config["flags"],
            dest=config["dest"],
            type=str,
            required=config["required"],
            help=config["help"],
        )

    args = arguments.parse_args(namespace=Arguments())

    for config in COMBINED_ARGS_CONFIG:
        parse_config = config.get("parse_config")
        if parse_config:
            parse_argument(args, parse_config)

    return args


def parse_argument(args: Arguments, config: ArgParseConfig) -> None:
    value = getattr(args, config.arg_name, None)
    if not value:
        for attr in config.attr_names.values():
            if attr:
                setattr(args, attr, None)
        return

    pattern = config.pattern_template.format(
        operators="|".join(map(re.escape, config.operators))
    )
    flags = re.IGNORECASE if config.ignore_case else 0
    match = re.match(pattern, value.strip(), flags)
    if not match:
        raise ValueError(
            config.error_message
            or f"Неверный формат аргумента '{config.arg_name}': {value}"
        )

    if "column" in config.attr_names and config.attr_names["column"]:
        setattr(args, config.attr_names["column"], match.group(1).strip())
    if "op" in config.attr_names and config.attr_names["op"]:
        op_value = match.group(2).strip().lower()
        if op_value not in config.operators:
            raise ValueError(
                f"Неизвестная операция в аргументе '{config.arg_name}': "
                f"{op_value}"
            )
        setattr(args, config.attr_names["op"], op_value)
    if "value" in config.attr_names and config.attr_names["value"]:
        setattr(
            args,
            config.attr_names["value"],
            (
                match.group(3).strip()
                if match.lastindex and match.lastindex >= 3
                else None
            ),
        )
