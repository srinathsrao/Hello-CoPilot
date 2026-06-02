import argparse


def greet(name: str) -> None:
    print(f"Hello  World-- {name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Name to greet")
    args = parser.parse_args()
    greet(args.name)
