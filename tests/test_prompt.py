from prompt_builder import build_prompt

def test_prompt_includes_items():
    prompt = build_prompt("milk\nbread")
    assert "milk" in prompt
    assert "bread" in prompt
