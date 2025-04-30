import os

# Load base domain
with open("domain.txt") as f:
    base_url = f.read().strip().rstrip("/")

# Create output folder if it doesn't exist
os.makedirs("meme", exist_ok=True)

# Generate 10 meme pages
for i in range(1, 11):
    n = f"{i:02}"
    prev = f"{(i - 2) % 10 + 1:02}"
    next = f"{i % 10 + 1:02}"
    img = f"{n}.png"
    share_url = f"{base_url}/meme/{n}.html"

    with open("template.html") as tpl:
        html = tpl.read()
        html = html.replace("{{n}}", n)
        html = html.replace("{{prev}}", prev)
        html = html.replace("{{next}}", next)
        html = html.replace("{{img}}", img)
        html = html.replace("{{share_url}}", share_url)

    with open(f"meme/{n}.html", "w") as out:
        out.write(html)

print("✅ Meme pages generated in /meme/")
