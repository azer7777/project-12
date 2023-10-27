from views.menu import Menu
import sentry_sdk

sentry_sdk.init(
    dsn="https://1773bbfa60a2c88c5fcd04844d9360f0@o4506122951262208.ingest.sentry.io/4506122955456512",
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