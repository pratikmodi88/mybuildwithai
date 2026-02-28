import os
import re

models_dir = 'leadership-blueprint/models'

for filename in os.listdir(models_dir):
    if filename.endswith('.html'):
        path = os.path.join(models_dir, filename)
        with open(path, 'r') as f:
            content = f.read()
        
        # Remove the Discussion Section (from <section class="discussion-section"> to the footer)
        # Note: We keep the footer, so we replace the section with just the footer start.
        content = re.sub(r'<section class="discussion-section">.*?(?=<footer>)', '', content, flags=re.DOTALL)
        
        with open(path, 'w') as f:
            f.write(content)

print("Removed discussion section from all model files.")
