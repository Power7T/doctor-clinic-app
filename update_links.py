import os
import glob

files = glob.glob('*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Determine current file
    filename = os.path.basename(filepath)
    
    # Replace links
    # Dashboard: line 173
    content = content.replace('href="#"', 'href="dashboard.html"', 1)
    # Patients: line 177
    content = content.replace('href="#"', 'href="patients.html"', 1)
    # New Entry: line 182
    content = content.replace('href="#"', 'href="index.html"', 1)
    # Prescriptions: line 186
    content = content.replace('href="#"', 'href="prescriptions.html"', 1)
    
    # Remove the alert javascript for links
    content = content.replace("""    // Sidebar links (prevent jump to top)
    document.querySelectorAll('a[href="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            alert("This is just a prototype link for " + this.innerText.trim());
        });
    });""", "")

    # For the individual files, update the active state so the UI shows which tab is active
    # The active state is classes: bg-secondary-container text-on-secondary-container font-bold
    # Inactive is: text-on-surface-variant hover:bg-surface-container-high
    if filename == 'dashboard.html':
        content = content.replace('Dashboard</span>\n</a>', 'Dashboard</span>\n</a><!-- DASH_ACTIVE -->')
        content = content.replace('New Entry</span>\n</a>', 'New Entry</span>\n</a><!-- NEW_ACTIVE -->')
        # swap styles...
        # Just use simple regex or string replacement if possible, or leave styles unchanged if too complex.
    
    # Actually, for dashboard, let's just put a massive placeholder in the <main> block
    if filename != 'index.html':
        # Replace the main content
        import re
        content = re.sub(r'<main.*?</main>', f'<main class="w-full md:ml-[280px] p-4 md:p-8 flex flex-col items-center justify-center min-h-[50vh]"><h1 class="text-4xl text-primary mb-4">{filename.replace(".html", "").title()}</h1><p class="text-on-surface-variant text-lg">This page is active and ready to be built out.</p></main>', content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)

