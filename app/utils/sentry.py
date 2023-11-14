import sentry_sdk

from app.config import APP_ENV

dsn_prod = "https://0d5b4affa4bb6de26500adb548c89615@o4506084321984512.ingest.sentry.io/4506215990755328"
dsn_dev = "https://6109e8b98dd30fb722b3770de8ef54e7@o4506084321984512.ingest.sentry.io/4506210817277952"

dsn = dsn_prod if APP_ENV == 'production' else None
dsn = dsn_dev if APP_ENV == 'development' else None

traces_sample_rate = 1.0
profiles_sample_rate = 1.0


def sentry_init():
    try:
        sentry_sdk.init(
            dsn = dsn,
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            traces_sample_rate = traces_sample_rate,
            # Set profiles_sample_rate to 1.0 to profile 100%
            # of sampled transactions.
            # We recommend adjusting this value in production.
            profiles_sample_rate = profiles_sample_rate,
        )
    except Exception as error:
        print('utils/sentry.py::sentry_init() error:', error)
        sentry_sdk.capture_exception(error)
        sentry_sdk.flush()
        raise error
    
def configure_sentry(app):
    sentry_init()
        # Test sentry is up and running
    @app.get("/sentry-debug", tags = ["Sentry #1"])
    async def trigger_error():
        division_by_zero = 1 / 0
    @app.get("/sentry_is_working", tags = ["Sentry #2"])
    async def sentry_works():
        sentry_is_working()

    return