from models.openai import OpenAI

def test_chat_completion():
    openai = OpenAI()
    open_ai = openai.chat_completion()
    assert 'id' in open_ai["openai"], "id property is missing"
    assert 'choices' in open_ai["openai"], "choices property is missing"
    assert 'message' in open_ai["openai"]["choices"][0], "message property is missing"
    assert 'content' in open_ai["openai"]["choices"][0]["message"], "content property is missing"
    assert 'role' in open_ai["openai"]["choices"][0]["message"], "role property is missing"
    assert 'created' in open_ai["openai"], "created property is missing"
    assert 'model' in open_ai["openai"], "model property is missing"
    assert 'object' in open_ai["openai"], "object property is missing"
    assert 'usage' in open_ai["openai"], "usage property is missing"
