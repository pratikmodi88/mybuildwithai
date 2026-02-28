import os
import glob

nav_css = """
        /* Navigation */
        nav.main-nav {
            padding: 1.5rem 0;
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            background: rgba(11, 14, 20, 0.8);
            backdrop-filter: blur(12px);
            z-index: 1000;
        }
        .nav-content { display: flex; justify-content: center; gap: 3rem; align-items: center; }
        .nav-link {
            color: var(--text-dim);
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            transition: 0.3s;
            font-family: 'Inter', sans-serif;
            position: relative;
        }
        .nav-link:hover, .nav-link.active { color: var(--accent); }

        /* Dropdown Menu */
        .nav-item-dropdown {
            position: relative;
            display: inline-block;
        }
        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(22, 27, 34, 0.95);
            border: 1px solid var(--border);
            border-radius: 4px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
            padding: 0.5rem 0;
            min-width: 220px;
            backdrop-filter: blur(12px);
            z-index: 1001;
        }
        .dropdown-menu::before {
            content: "";
            position: absolute;
            top: -15px;
            left: 0;
            width: 100%;
            height: 15px;
            background: transparent;
        }
        .nav-item-dropdown:hover .dropdown-menu {
            display: block;
        }
        .dropdown-link {
            display: block;
            padding: 0.8rem 1.5rem;
            color: var(--text-dim);
            text-decoration: none;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            transition: 0.2s;
            white-space: nowrap;
        }
        .dropdown-link:hover {
            background: rgba(34, 166, 179, 0.1);
            color: var(--accent);
        }
"""

nav_html = """
    <nav class="main-nav">
        <div class="nav-content" style="max-width: 1200px; margin: 0 auto; padding: 0 2rem;">
            <a href="/" class="nav-link">Home</a>
            <a href="/#impact" class="nav-link">Impact</a>
            <a href="/#highlights" class="nav-link">Highlights</a>
            
            <div class="nav-item-dropdown">
                <a href="#" class="nav-link active">My Projects <span style="font-size: 0.6rem; opacity: 0.6;">▼</span></a>
                <div class="dropdown-menu">
                    <a href="/leadership-blueprint/" class="dropdown-link">Leadership Blueprint</a>
                </div>
            </div>
        </div>
    </nav>
"""

for filepath in glob.glob('leadership-blueprint/models/*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace CSS
    start_marker = 'nav.main-nav {'
    end_marker = '}'
    # This is tricky because there might be multiple blocks. 
    # We want to replace the whole nav section in CSS.
    
    import re
    # Match the entire nav styling section
    content = re.sub(r'nav\.main-nav\s*{[^}]*}', nav_css, content)
    content = re.sub(r'\.nav-link\s*{[^}]*}', '', content)
    content = re.sub(r'\.nav-link:hover[^}]*}', '', content)
    
    # Replace HTML
    content = re.sub(r'<nav class="main-nav">.*?</nav>', nav_html, content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)
