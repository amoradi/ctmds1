import typer


def validate_non_negative(value: int) -> int:
    if value < 0:
        raise typer.BadParameter("Number must be non-negative")
    return value
