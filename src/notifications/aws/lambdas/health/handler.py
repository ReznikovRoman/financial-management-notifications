from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

from .constants import HEALTH

logger = Logger()


def health_handler(event: dict, context: LambdaContext) -> dict:
    logger.info("Debug health %s", HEALTH)
    message = "Hello {} {}!".format(event.get("first_name", "John"), event.get("last_name", "Doe"))
    return {
        "message": message,
    }
