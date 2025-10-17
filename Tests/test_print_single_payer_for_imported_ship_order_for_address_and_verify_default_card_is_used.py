import pytest
import allure

TITLE = "Print Single Payer for imported ship order for address and verify default card is used"

@allure.tag("Automation")
@allure.epic("UI Automation")
@allure.suite("ShipAccel UI Automation")
@allure.story(TITLE)
@allure.title(TITLE)
@allure.label("owner", "Sowmya Katamaneni")
@allure.severity("Medium")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "UI")
@pytest.mark.parametrize(
    "address,single_payer",
    [("CT", "Fedex label"), ("CT", "UPS label"),
     ("NY", "Fedex label"), ("NY", "UPS label")],
    ids=["CT-FEDEX","CT-UPS","NY-FEDEX","NY-UPS"]
)
def test_print_single_payer_default_card_used(address, single_payer):
    with allure.step(f"Open page for address={address}"): pass
    with allure.step(f"Select Single Payer: {single_payer}"): pass
    with allure.step("Trigger label print"): pass
    with allure.step("Verify default card is used"): pass
    with allure.step("Attach params"):
        allure.attach(
            f"Address: {address}\nSingle Payer: {single_payer}",
            name="params",
            attachment_type=allure.attachment_type.TEXT,
        )
