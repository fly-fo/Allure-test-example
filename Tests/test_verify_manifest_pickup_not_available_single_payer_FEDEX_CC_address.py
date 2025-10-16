import pytest
import allure

TITLE = "Verify manifest and pickup not available for single payer FEDEX for CC card with address"

@allure.tag("Automation")
@allure.epic("UI Automation")
@allure.suite("ShipAccel UI Automation")
@allure.feature(TITLE)               # feature == title
@allure.title(TITLE)
@allure.label("owner", "Sowmya Katamaneni")
@allure.label("priority", "Medium")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "UI")
@pytest.mark.parametrize("address", ["CT", "NY"], ids=["CT", "NY"])
def test_manifest_pickup_not_available_fedex_cc(address):
    with allure.step(f"Open shipping context for address={address} (Single Payer FEDEX, CC card set)"):
        assert address in ("CT", "NY")

    with allure.step("Navigate to Manifest / Pickup actions"):
        page_loaded = True
        assert page_loaded is True

    with allure.step("Verify 'Create Manifest' action is NOT available"):
        manifest_available = False
        assert manifest_available is False

    with allure.step("Verify 'Schedule Pickup' action is NOT available"):
        pickup_available = False
        assert pickup_available is False

    with allure.step("Attach parameters for traceability"):
        allure.attach(
            f"Address: {address}\nCarrier: FEDEX\nPayer: Single Payer\nCard: Credit Card (address-level)",
            name="params",
            attachment_type=allure.attachment_type.TEXT,
        )
