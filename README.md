# 10-meme-challenge

This repo is forkable template for self-expression via memes. Its designed to work with github pages. Just fork, put your memes in the folder and deploy. Have fun!

## How to use this

1. **Fork this repo** to your own GitHub account.

2. **Create 10 memes** using any meme generator (e.g. [imgflip meme generator](https://imgflip.com/memegenerator)).

3. **Replace the memes** in the `memes/` folder (`01.png` to `10.png`) with your own. Use the same filenames.

4. **Edit `domain.txt`** and update it with your GitHub Pages URL:  
   Example:  
   ```
   https://yourusername.github.io/your-repo-name/
   ```

5. **(Optional)** Edit `index.html` or `template.html` to change the title or add personal touches.

6. **Run the generator script** to create individual pages for each meme:  
   ```bash
   python generate_pages.py
   ```

7. **Commit and push** your changes back to GitHub:  
   ```bash
   git add .
   git commit -m "My 10 meme challenge"
   git push origin main
   ```

8. **Enable GitHub Pages** in your repo:
   - Go to **Settings > Pages**
   - Set **Source** to `Deploy from branch: main` and select the root (`/`)
   - GitHub will show you your live site URL

9. **Visit and share your link** (from GitHub Pages) with friends!