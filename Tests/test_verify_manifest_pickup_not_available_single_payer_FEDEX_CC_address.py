import pytest
import allure

TITLE = "Verify manifest and pickup not available for single payer FEDEX for CC card with address"

@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("Allure Automation")
@allure.story(TITLE)
@allure.title(TITLE)
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "Allure")
@allure.label("trProject", "Allure testops")
@allure.label("layer", "Unit Tests")
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

    # ❌ INTENTIONAL FAILURE STEP
    with allure.step("Force test failure for demo purposes"):
        raise AssertionError("Intentional failure: Expected behavior mismatch for demo in Allure TestOps")

    with allure.step("Attach parameters for traceability"):
        allure.attach(
            f"Address: {address}\nCarrier: FEDEX\nPayer: Single Payer\nCard: Credit Card (address-level)",
            name="params",
            attachment_type=allure.attachment_type.TEXT,
        )
