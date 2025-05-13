def build_prompt(items, language="English", style="plain", tips=False):
    base_prompt = f"""
You are an assistant that categorizes and sorts grocery items.

Language: {language}
Output style: {style}
Tips: {'Include shopping tips and healthy substitutes.' if tips else 'No tips required.'}

Here is a list of grocery items:
{items}

Please:
1. Categorize these items into categories such as Produce, Dairy, Meat, Bakery, Beverages, Snacks, etc.
2. Sort items in each category alphabetically.
3. Format output clearly.
"""
    return base_prompt
