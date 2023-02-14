import pytest

@pytest.mark.usefixtures("setup")
class BaseTest:
    pass

@pytest.mark.usefixtures("merchant")
class MerchantTest:
    pass
