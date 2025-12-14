import openai


async def generate_page_summary(page):
prompt = f"""
Page Name: {page.name}
Industry: {page.industry}
Followers: {page.followers}


Generate a professional LinkedIn insights summary.
"""


response = openai.ChatCompletion.create(
model="gpt-4",
messages=[{"role": "user", "content": prompt}]
)


return response.choices[0].message.content