from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    message = "Hello {} {}!".format(event.get("first_name", "John"), event.get("last_name", "Doe"))
    return {
        "message": message,
    }
