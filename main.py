# Import the client
import yapper, os
from xdk import Client
from dotenv import load_dotenv
load_dotenv()
# Replace with your actual Bearer Token
bot = yapper.Bot()
client = Client(bearer_token=os.environ.get("X_API_KEY"))
# Fetch recent Posts mentioning "api"
# search_recent returns an Iterator, so iterate over it
for page in client.posts.search_recent(query="api", max_results=10):
    if page.data and len(page.data) > 0:
        # Access first Post - Pydantic models support both attribute and dict access
        first_post = page.data[0]
        post_text = first_post.text if hasattr(first_post, 'text') else first_post.get('text', '')
        print(f"Latest Post: {post_text}")
        break
    else:
        print("No Posts found.")
        break

@bot.command("test")
def test_cmd(interaction):
    interaction.reply("Test Worked.")

bot.run()
