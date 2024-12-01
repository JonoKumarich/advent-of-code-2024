from typing import Literal
import typer
from typer.main import Path
from importlib import import_module

app = typer.Typer()

@app.command()
def run(day: int, part: int):
    ans = calculate_answer("main", day, part)
    print(ans)



@app.command()
def test(day: int, part: int):
    ans = calculate_answer("test", day, part)
    print(ans)

def calculate_answer(answer_type: Literal["test", "main"], day: int, part: int) -> str:
    day_str = f"day_{str(day).zfill(2)}"
    part_str = f"part_{str(part).zfill(2)}"
    with open(Path(__file__).parents[2] / f"inputs/{answer_type}" / f"{day_str}.txt") as f:
        file = f.read()

    func = import_module(f'aoc.{day_str}').__dict__[part_str]
    return func(file)


def main():
    app()
