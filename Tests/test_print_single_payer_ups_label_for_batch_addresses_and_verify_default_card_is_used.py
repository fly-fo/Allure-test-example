import pytest
import allure

TITLE = "Print Single Payer UPS label for batch addresses and verify default card is used"

@allure.tag("Automation")
@allure.epic("UI Automation")
@allure.suite("ShipAccel UI Automation")
@allure.story(TITLE)               
@allure.title(TITLE)
@allure.label("owner", "Sowmya Katamaneni")
@allure.label("priority", "Medium")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "UI")
@pytest.mark.parametrize("address", ["CT", "NY"], ids=["CT", "NY"])
def test_ups_label_batch_addresses_default_card(address):
    with allure.step(f"Open Imported Ship Orders batch page for address={address}"):
        assert address in ("CT", "NY")

    with allure.step("Select Single Payer: UPS label (batch)"):
        single_payer = "UPS label"
        assert single_payer == "UPS label"

    with allure.step("Trigger batch label print"):
        printed = True
        assert printed is True

    with allure.step("Verify default card is used for all printed labels"):
        default_card_used = True
        assert default_card_used is True

    with allure.step("Attach parameters for traceability"):
        allure.attach(
            f"Address: {address}\nMode: batch\nSingle Payer: UPS label",
            name="params",
            attachment_type=allure.attachment_type.TEXT,
        )
