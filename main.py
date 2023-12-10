from views.menu import Menu
import sentry_sdk
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SENTRY_DSN = os.getenv("SENTRY_DSN")

sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


if __name__ == "__main__":
    Menu().auth_menu()
