import os
import re

css_canonical = """        :root {
            --bg: #0b0e14;
            --card-bg: #161b22;
            --text-main: #e6edf3;
            --text-dim: #7d8590;
            --accent: #22a6b3;
            --border: #30363d;
            --card-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        }
        body { font-family: 'Inter', sans-serif; line-height: 1.8; color: var(--text-main); background: var(--bg); margin: 0; padding: 0; }
        nav.main-nav { padding: 1.5rem 0; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: rgba(11, 14, 20, 0.8); backdrop-filter: blur(12px); z-index: 1000; }
        .nav-content { display: flex; justify-content: center; gap: 3rem; align-items: center; }
        .nav-link { color: var(--text-dim); text-decoration: none; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.15em; transition: 0.3s; font-family: 'Inter', sans-serif; position: relative; }
        .nav-link:hover, .nav-link.active { color: var(--accent); }

        /* Dropdown Menu */
        .nav-item-dropdown { position: relative; display: inline-block; }
        .dropdown-menu { display: none; position: absolute; top: 100%; left: 50%; transform: translateX(-50%); background: rgba(22, 27, 34, 0.95); border: 1px solid var(--border); border-radius: 4px; box-shadow: var(--card-shadow); padding: 0.5rem 0; min-width: 220px; backdrop-filter: blur(12px); z-index: 1001; }
        .dropdown-menu::before { content: ""; position: absolute; top: -15px; left: 0; width: 100%; height: 15px; background: transparent; }
        .nav-item-dropdown:hover .dropdown-menu { display: block; }
        .dropdown-link { display: block; padding: 0.8rem 1.5rem; color: var(--text-dim); text-decoration: none; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; transition: 0.2s; white-space: nowrap; }
        .dropdown-link:hover { background: rgba(34, 166, 179, 0.1); color: var(--accent); }"""

nav_canonical = """    <nav class="main-nav">
        <div class="nav-content">
            <a href="/" class="nav-link">Home</a>
            <a href="/#impact" class="nav-link">Impact</a>
            <a href="/#highlights" class="nav-link">Highlights</a>
            
            <div class="nav-item-dropdown">
                <a href="#" class="nav-link active">My Projects <span style="font-size: 0.6rem; opacity: 0.6;">▼</span></a>
                <div class="dropdown-menu">
                    <a href="/leadership-blueprint/" class="dropdown-link active">Leadership Blueprint</a>
                </div>
            </div>
        </div>
    </nav>"""

models_dir = 'leadership-blueprint/models'

for filename in os.listdir(models_dir):
    if filename.endswith('.html'):
        path = os.path.join(models_dir, filename)
        with open(path, 'r') as f:
            content = f.read()
        
        # Replace CSS
        content = re.sub(r'<style>.*?</style>', f'<style>\n{css_canonical}\n        .container {{ max-width: 800px; margin: 0 auto; padding: 6rem 1.5rem; }}\n        .metadata {{ font-size: 0.85rem; color: var(--accent); text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; margin-bottom: 1rem; }}\n        h1 {{ font-family: \'Playfair Display\', serif; font-size: 3.2rem; margin: 0 0 0.5rem 0; color: #ffffff; }}\n        .published-info {{ font-size: 0.9rem; color: var(--text-dim); margin-bottom: 3rem; border-bottom: 1px solid var(--border); padding-bottom: 1.5rem; }}\n        .hero-image-container {{ width: 100%; border-radius: 12px; border: 1px solid var(--border); margin: 2rem 0; background: var(--card-bg); padding: 2rem; display: flex; justify-content: center; }}\n        .hero-image-container svg {{ width: 100%; height: auto; max-width: 600px; }}\n        .meat-section h2 {{ font-family: \'Playfair Display\', serif; color: var(--accent); margin-top: 4.5rem; font-size: 2.2rem; }}\n        .action-box {{ background: rgba(34, 166, 179, 0.05); border-left: 5px solid var(--accent); padding: 3rem; border-radius: 8px; margin: 4rem 0; }}\n        .discussion-section {{ margin-top: 8rem; border-top: 1px solid var(--border); padding-top: 4rem; }}\n        .insight-form {{ background: var(--card-bg); padding: 2.5rem; border-radius: 12px; border: 1px solid var(--border); margin-top: 2rem; }}\n        .insight-form textarea, .insight-form input {{ width: 100%; background: #0b0e14; border: 1px solid var(--border); border-radius: 8px; padding: 1rem 1.5rem; color: #fff; margin-bottom: 1rem; box-sizing: border-box; }}\n        .submit-btn {{ background: var(--accent); color: #fff; border: none; padding: 1rem 2.5rem; border-radius: 4px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; cursor: pointer; transition: all 0.3s ease; }}\n        footer {{ padding: 4rem 1.5rem; text-align: center; border-top: 1px solid var(--border); color: var(--text-dim); font-size: 0.85rem; background: #080a0f; }}\n        @media (max-width: 768px) {{ h1 {{ font-size: 2.5rem; }} nav.main-nav {{ gap: 1.5rem; padding: 1rem; }} .nav-link {{ font-size: 0.7rem; }} }}\n    </style>', content, flags=re.DOTALL)
        
        # Replace Nav
        content = re.sub(r'<nav.*?</nav>', nav_canonical, content, flags=re.DOTALL)
        
        with open(path, 'w') as f:
            f.write(content)

print("Updated all model files.")
