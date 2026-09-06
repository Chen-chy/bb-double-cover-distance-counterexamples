"""Fixed, independently certified examples; no general distance prediction."""
import json
from importlib.resources import files
from .code import BBCode


def records() -> dict:
    return json.loads(files("bbcover").joinpath("examples.json").read_text(encoding="utf-8"))


def names() -> tuple[str, ...]:
    return tuple(records())


def get_example(name: str) -> tuple[BBCode, int, dict]:
    data = records()
    if name not in data:
        raise ValueError(f"Unknown example {name!r}; choose from {', '.join(data)}")
    d = data[name]
    code = BBCode(*d["periods"], tuple(map(tuple, d["A"])), tuple(map(tuple, d["B"])))
    witness = code.chain(map(tuple, d["logical_left"]), map(tuple, d["logical_right"]))
    return code, witness, d
