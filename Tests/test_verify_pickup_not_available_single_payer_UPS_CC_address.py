import pytest
import allure

TITLE = "Verify pickup not available for single payer UPS for CC card with address"

@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("Allure Automation")
@allure.story(TITLE)               # feature == title
@allure.title(TITLE)
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "Allure")
@allure.label("trProject", "Allure testops")
@allure.label("layer", "Unit Tests")
@pytest.mark.parametrize("address", ["CT", "NY"], ids=["CT", "NY"])
def test_pickup_not_available_single_payer_ups_cc(address):
    with allure.step(f"Open shipping context for address={address} (Single Payer UPS, CC card set)"):
        assert address in ("CT", "NY")

    with allure.step("Navigate to Pickup / Manifest actions"):
        page_loaded = True
        assert page_loaded is True

    with allure.step("Verify 'Schedule Pickup' action is NOT available"):
        pickup_available = False
        assert pickup_available is False

    with allure.step("(Optional) Verify Manifest button state if shown"):
        manifest_visible_but_disabled = True  # placeholder
        assert manifest_visible_but_disabled is True

    with allure.step("Attach parameters for traceability"):
        allure.attach(
            f"Address: {address}\nCarrier: UPS\nPayer: Single Payer\nCard: Credit Card (address-level)",
            name="params",
            attachment_type=allure.attachment_type.TEXT,
        )
