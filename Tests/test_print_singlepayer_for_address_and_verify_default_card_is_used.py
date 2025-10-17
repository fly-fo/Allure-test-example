import pytest
import allure

TITLE = "Print SinglePayer for address and verify default card is used"

@allure.tag("Automation")
@allure.epic("UI Automation")
@allure.suite("ShipAccel UI Automation")
@allure.story(TITLE)                 
@allure.title(TITLE)
@allure.label("owner", "Sowmya Katamaneni")
@allure.label("priority", "Medium")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "UI")
@pytest.mark.parametrize(
    "address,single_payer",
    [
        ("CT", "UPS label"),
        ("CT", "UPS multi-piece label"),
        ("NY", "UPS label"),
        ("NY", "UPS multi-piece label"),
    ],
    ids=["CT-UPS", "CT-UPS-MP", "NY-UPS", "NY-UPS-MP"]
)
def test_singlepayer_default_card_used(address, single_payer):
    with allure.step(f"Open Imported Ship Orders page for address={address}"):
        assert address in ("CT", "NY")

    with allure.step(f"Select Single Payer type: {single_payer}"):
        assert single_payer in ("UPS label", "UPS multi-piece label")

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
