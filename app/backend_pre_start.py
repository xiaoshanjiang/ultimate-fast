import logging

from tenacity import (after_log, before_log, retry, stop_after_attempt,
                      wait_fixed)

from db.base_class import Base  # noqa: F401
from db.session import engine  # noqa: F401
from db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def test_connection() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e

def create_tables():
    Base.metadata.create_all(bind=engine)


def main() -> None:
    logger.info("Testing Connection...")
    try:
        test_connection()
    except Exception as e:
        logger.error("Connection failed: ", e)
    else:
        logger.info("Connected.")

    logger.info("Creating tables...")
    try:
        create_tables()
    except Exception as e:
        logger.error("Failed to create tables: ", e)
    else:
        logger.info("Tables created.")


if __name__ == "__main__":
    main()
