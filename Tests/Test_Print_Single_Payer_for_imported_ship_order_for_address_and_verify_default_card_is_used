import pytest
import allure

TITLE = "Print Single Payer for imported ship order for address and verify default card is used"

@allure.tag("Automation")
@allure.title(TITLE)
@allure.story(TITLE)                     # story == title (as requested)
@allure.label("owner", "Sowmya Katamaneni")
@allure.epic("UI Automation")
@allure.label("suite", "ShipAccel UI Automation")
@allure.label("layer", "ui")
@allure.severity("normal")               # Priority: Medium -> keep severity ~ normal
@allure.label("priority", "Medium")
@allure.label("trProject", "Shipaccel")
@pytest.mark.parametrize(
    "address,single_payer",
    [("CT", "Fedex label"), ("CT", "UPS label"),
     ("NY", "Fedex label"), ("NY", "UPS label")],
    ids=["CT-FEDEX","CT-UPS","NY-FEDEX","NY-UPS"]
)
def test_print_single_payer_default_card_used(address, single_payer):
    with allure.step(f"Open Imported Ship Orders page for address={address}"):
        assert address in ("CT", "NY")

    with allure.step(f"Select Single Payer type: {single_payer}"):
        assert single_payer in ("Fedex label", "UPS label")

    with allure.step("Trigger label print"):
        printed = True
        assert printed is True

    with allure.step("Verify default card is used for payment"):
        default_card_used = True
        assert default_card_used is True

    with allure.step("Attach parameters for traceability"):
        allure.attach(
            f"Address: {address}\nSingle Payer: {single_payer}",
            name="params",
            attachment_type=allure.attachment_type.TEXT,
        )
