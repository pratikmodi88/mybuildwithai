import os
import re

# Standardized footer content
footer_html = """    <footer>
        <div class="container">
            <p>&copy; 2026 <strong>Pratik Kumar Modi</strong>. All Rights Reserved.</p>
            <p class="footer-note">
                This portfolio is a live demonstration of AI-assisted development, built and maintained using Aurora, my custom AI system.
            </p>
        </div>
    </footer>"""

# Standardized footer CSS
# Note: We need to ensure .footer-note is defined and footer padding is consistent.
footer_css = """        footer {
            padding: 5rem 0;
            background: #080a0f;
            border-top: 1px solid var(--border);
            text-align: center;
            color: var(--text-dim);
            font-size: 0.9rem;
            margin-top: 8rem;
        }
        .footer-note {
            margin-top: 0.8rem;
            font-size: 0.8rem;
            opacity: 0.5;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.6;
        }"""

def unify_footer(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # 1. Update HTML footer
    # Matches from <footer to </footer>
    content = re.sub(r'<footer.*?>.*?</footer>', footer_html, content, flags=re.DOTALL)
    
    # 2. Update CSS
    # If the file has a <style> block, we look for footer { ... } and replace/add .footer-note
    if '<style>' in content:
        # Replace existing footer style
        content = re.sub(r'footer\s*\{[^}]*\}', footer_css, content)
        # Check if .footer-note is already there, if not, it's included in our footer_css replacement
        # (Though our regex above replaces the whole block, so it's clean)
        
        # Some files might have .footer-note defined separately, let's clean that up
        content = re.sub(r'\.footer-note\s*\{[^}]*\}', '', content)
        content = re.sub(r'\.copyright\s*\{[^}]*\}', '', content)
        
    with open(file_path, 'w') as f:
        f.write(content)

# Target files
files_to_update = ['index.html', 'leadership-blueprint/index.html']
models_dir = 'leadership-blueprint/models'
for filename in os.listdir(models_dir):
    if filename.endswith('.html'):
        files_to_update.append(os.path.join(models_dir, filename))

for file in files_to_update:
    unify_footer(file)
    print(f"Unified footer in {file}")
