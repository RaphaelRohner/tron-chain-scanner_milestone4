from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """
        REQUIRED BY DJANGO
        APP DOES NOT RUN WITHOUT THE "NEVER USED" SIGNALS IMPORT
        """
        import checkout.signals  # noqa: F401
