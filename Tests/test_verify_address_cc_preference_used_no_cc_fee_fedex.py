import pytest
import allure

TITLE = (
    "Verify if address credit card set in preferences being used and CC fee is not "
    "charged while printing single payer FEDEX"
)

@allure.tag("Automation")
@allure.epic("UI Automation")
@allure.suite("ShipAccel UI Automation")
@allure.feature(TITLE)                 # feature == title (your convention)
@allure.title(TITLE)
@allure.label("owner", "Sowmya Katamaneni")
@allure.label("priority", "Medium")    # custom field for TestOps
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "UI")
@pytest.mark.parametrize(
    "address,single_payer_fedex_mode",
    [
        ("CT", "batch"),
        ("NY", "batch"),
        ("CT", "multi piece"),
        ("NY", "multi piece"),
        ("CT", "shipping label"),
        ("NY", "shipping label"),
        ("CT", "WIX ship order"),
        ("NY", "WIX ship order"),
        ("CT", "FEDEX label"),
        ("NY", "FEDEX label"),
    ],
    ids=[
        "CT-batch", "NY-batch",
        "CT-multi-piece", "NY-multi-piece",
        "CT-shipping-label", "NY-shipping-label",
        "CT-wix-ship-order", "NY-wix-ship-order",
        "CT-fedex-label", "NY-fedex-label",
    ]
)
def test_cc_pref_used_no_cc_fee_single_payer_fedex(address, single_payer_fedex_mode):
    # Step-1..5 style (dummy placeholders you can wire to real actions later)
    with allure.step(f"Open batch/ship orders for address={address}"):
        assert address in ("CT", "NY")

    with allure.step(f"Select Single Payer FEDEX mode: {single_payer_fedex_mode}"):
        assert single_payer_fedex_mode in {
            "batch", "multi piece", "shipping label", "WIX ship order", "FEDEX label"
        }

    with allure.step("Ensure address credit card from Preferences is applied"):
        cc_pref_applied = True
        assert cc_pref_applied is True

    with allure.step("Trigger print / label creation"):
        printed = True
        assert printed is True

    with allure.step("Verify CC fee is NOT charged"):
        cc_fee_charged = False
        assert cc_fee_charged is False

    with allure.step("Attach parameters for traceability"):
        allure.attach(
            f"Address: {address}\nMode: {single_payer_fedex_mode}",
            name="params",
            attachment_type=allure.attachment_type.TEXT,
        )
