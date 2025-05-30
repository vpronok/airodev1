# File: crew.py
from crewai import Crew, Agent, Task
from tools.web_search_tool import WebSearchTool
from tools.wordpress_elementor_tool import WordPressElementorTool
from memory.recall_tool import RecallTool
from utils.page_suggester import suggest_pages_for_website_type

# Tools
web_search_tool = WebSearchTool()
elementor_tool = WordPressElementorTool()
recall_tool = RecallTool()

# Agents
airodev_agent = Agent(
    name="Airodev",
    role="Autonomous WordPress Website Designer using Elementor",
    goal=(
        "Design high-quality, responsive WordPress websites using Elementor Pro,"
        " based on client input, competitive research, and prior learning."
    ),
    tools=[web_search_tool, elementor_tool, recall_tool],
    backstory=(
        "Airodev is a cutting-edge AI web designer trained in modern UI/UX and Elementor development."
        " It continually improves by analyzing its past projects and client feedback."
    ),
    allow_delegation=False
)

# Task (example task setup; dynamically created in real scenarios)
def create_design_task(user_prompt):
    website_type = suggest_pages_for_website_type(user_prompt)
    return Task(
        description=(
            f"Analyze the user request: '{user_prompt}'\n"
            f"Identify it as a '{website_type}' website, suggest pages, search examples,"
            " and build each page using Elementor via API."
        ),
        agent=airodev_agent,
        expected_output=(
            "A completed set of designed pages with Elementor, based on client input,"
            " competitive research, and learned design patterns."
        )
    )

# Crew definition
def create_crew(user_prompt):
    task = create_design_task(user_prompt)
    crew = Crew(
        agents=[airodev_agent],
        tasks=[task],
        verbose=True
    )
    return crew.run()
