from jinja2 import Template
import json
from datetime import date

today = date.today()

markdown_template = open("TEMPLATE.md").read()
template = Template(markdown_template)
config = json.load(open("config.json"))
config.update({"last_updated": today.strftime("%B %d, %Y")})
readme_content = template.render(config)
with open("README.md", "w", encoding="utf-8") as readme_file:
    print(readme_content, file=readme_file)
