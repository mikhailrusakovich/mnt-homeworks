import sentry_sdk
sentry_sdk.init(
    "https://49d1561af47449bdb2f361eddcb976ae@o1204731.ingest.sentry.io/6331887",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

if __name__ == "__main__":
    division_by_zero = 1 / 0
