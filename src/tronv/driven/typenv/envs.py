from dataclasses import dataclass

import typenv


@dataclass(kw_only=True, frozen=True, slots=True)
class Envs:
    postgres_url: str
    page_size: int
    tron_grid_api_key: str

    @classmethod
    def load(cls) -> "Envs":
        env = typenv.Env()

        return Envs(
            postgres_url=env.str("POSTGRES_URL"),
            page_size=env.int("PAGE_SIZE"),
            tron_grid_api_key=env.str("TRON_GRID_API_KEY"),
        )
