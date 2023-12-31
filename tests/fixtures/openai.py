import pytest

from app.enums.openai import OpenAIModel, OpenAIObjectType
from app.services.openai import OpenAIService

@pytest.fixture
def openai_service():
    service = OpenAIService()
    yield service

openai_request_data = {
	"content": "My client is single, currently employed by Company A as well as consulting contract for Company C. Bought X amount of stocks at Company D at price Y and sold such Company C stock the same year for Z price. X dollars where collected through saving accounts interest. Company stock F distributed X dollars in dividends. Client is shareholder of a s-corporation and c-corporation that had a net income and distributed dividends. Client owns a few properties that are currently rented through a property manager. Some of the propertities had an amortization and depreciation. One of the properties is under a mortgage with around 5% interest rate. Earlier this year one of the properties suffered damages from a natural disaster and had to do repairs, purchase new furnitures and appliances. Show a list of forms and URLs i need to fill, gather and file to the irs please",
	"role": "user"
}
openai_chat_completion_object_response_data = {
    "id": "chatcmpl-8HOfMS2ZZCmYGry1Yz56PfUHks7zD",
    "object": OpenAIObjectType.CHAT_COMPLETION.value,
    "created": 1699157084,
    "model": OpenAIModel.GPT_3_5_TURBO_16K.value,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "<p>The 1099-INT is a tax form used by taxpayers to report interest income to the IRS. It's typically issued by banks and other financial institutions. The form contains information about the interest earned during the year, as well as any federal taxes that were withheld.</p>\n\n<p>Here are some key details you'll find on a 1099-INT form:</p>\n\n<ul>\n    <li><b>Box 1:</b> Interest income</li>\n    <li><b>Box 3:</b> Interest on U.S. Savings Bonds and Treasury obligations</li>\n    <li><b>Box 4:</b> Federal income tax withheld</li>\n    <li><b>Box 8:</b> Tax-exempt interest</li>\n    <li><b>Box 9:</b> Specified private activity bond interest</li>\n</ul>\n\n<p>You should receive a 1099-INT form from each institution that paid you $10 or more in interest during the tax year. If you received less than $10 in interest from a single source, you may not receive a form, but you still need to report the income on your tax return.</p>\n\n<p>You can find more information about the 1099-INT form on the <a target=\"_blank\" href=\"https://www.irs.gov/forms-instructions\">IRS website</a>.</p>",
            },
            "finish_reason": "stop",
        }
    ],
    "usage": {
        "prompt_tokens": 805,
        "completion_tokens": 62,
        "total_tokens": 867,
    }
}