import warnings

warnings.filterwarnings("ignore", category=UserWarning, message="The `dict` method is deprecated; use `model_dump` instead.*")
warnings.filterwarnings("ignore", category=UserWarning, message="Support for class-based `config` is deprecated, use ConfigDict instead.*")
