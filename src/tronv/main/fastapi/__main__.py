from tronv.main.common.uvicorn import run_dev


def main() -> None:
    run_dev("tronv.main.fastapi.asgi:app")


if __name__ == "__main__":
    main()
