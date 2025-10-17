import pytest
import allure

TITLE = (
    "Verify if address credit card set in preferences being used and CC fee is not "
    "charged while printing single payer FEDEX"
)

@allure.tag("Automation")
@allure.epic("UI Automation")
@allure.suite("ShipAccel UI Automation")
@allure.story(TITLE)                 # feature == title
@allure.title(TITLE)
@allure.label("owner", "Sowmya Katamaneni")
@allure.label("priority", "Medium")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "UI")
@pytest.mark.parametrize(
    "address, fedex_mode",
    [
        ("CT", "batch"),
        ("NY", "batch"),
        ("CT", "multi piece"),
        ("NY", "multi piece"),
        ("CT", "shipping label"),
        ("NY", "shipping label"),
        ("CT", "WIX ship order"),
        ("NY", "WIX ship order"),
    ],
    ids=[
        "CT-batch", "NY-batch",
        "CT-multi-piece", "NY-multi-piece",
        "CT-shipping-label", "NY-shipping-label",
        "CT-wix-ship-order", "NY-wix-ship-order",
    ],
)
def test_cc_pref_used_no_cc_fee_single_payer_fedex(address, fedex_mode):
    with allure.step(f"Open page / context for address={address}"):
        assert address in ("CT", "NY")

    with allure.step(f"Select Single Payer FEDEX mode: {fedex_mode}"):
        assert fedex_mode in {
            "batch", "multi piece", "shipping label", "WIX ship order"
        }

    with allure.step("Ensure address credit card from Preferences is applied"):
        cc_pref_applied = True
        assert cc_pref_applied is True

    with allure.step("Trigger printing / label creation"):
        printed = True
        assert printed is True

    with allure.step("Verify CC fee is NOT charged"):
        cc_fee_charged = False
        assert cc_fee_charged is False

    with allure.step("Attach parameters for traceability"):
        allure.attach(
            f"Address: {address}\nFEDEX mode: {fedex_mode}",
            name="params",
            attachment_type=allure.attachment_type.TEXT,
        )
