def suggest_pages_for_website_type(prompt: str) -> str:
    prompt_lower = prompt.lower()
    if "e-commerce" in prompt_lower:
        return "e-commerce"
    elif "blog" in prompt_lower:
        return "personal blog"
    elif "news" in prompt_lower:
        return "news website"
    elif "portfolio" in prompt_lower:
        return "portfolio"
    else:
        return "general business"

def get_default_pages(website_type: str) -> list:
    default_pages = {
        "e-commerce": ["Home", "Shop", "Product", "Cart", "Checkout", "Contact"],
        "personal blog": ["Home", "Blog", "About", "Contact"],
        "news website": ["Home", "Latest News", "Categories", "About", "Contact"],
        "portfolio": ["Home", "Portfolio", "About", "Contact"],
        "general business": ["Home", "Services", "About", "Contact"]
    }
    return default_pages.get(website_type, ["Home", "About", "Contact"])
