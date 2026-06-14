import sys

with open("head.html", "r") as f:
    head = f.read()

new_body = """
<body class="bg-background text-on-background font-body-md text-body-md min-h-screen flex flex-col antialiased">
    
    <header class="bg-surface text-primary font-body-md border-b border-outline-variant flex justify-center items-center h-16 w-full">
        <h1 class="font-title-lg text-[28px] text-primary tracking-tight font-extrabold flex items-center gap-2">
            <span class="material-symbols-outlined" style="font-size: 32px;">local_hospital</span>
            MedFlow Clinic
        </h1>
    </header>

    <main class="w-full max-w-4xl mx-auto p-4 md:p-8 flex-1">
        <div class="bg-surface-container-lowest border border-outline-variant rounded-xl shadow-sm overflow-hidden">
            <form class="p-6 md:p-8 flex flex-col gap-8">
                
                <section>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="flex flex-col gap-2 md:col-span-2">
                            <label class="font-label-md text-label-md text-on-surface">Patient Full Name</label>
                            <input class="w-full bg-surface-bright border border-outline-variant rounded-lg px-4 py-3 text-on-surface focus:outline-none focus:border-primary transition-all text-lg font-semibold" placeholder="e.g., John Doe" type="text"/>
                        </div>
                        <div class="flex flex-col gap-2 md:col-span-2">
                            <label class="font-label-md text-label-md text-on-surface">Residential Address</label>
                            <input class="w-full bg-surface-bright border border-outline-variant rounded-lg px-4 py-3 text-on-surface focus:outline-none focus:border-primary transition-all" placeholder="Street address, City, ZIP" type="text"/>
                        </div>
                        <div class="flex flex-col gap-2 md:col-span-1">
                            <label class="font-label-md text-label-md text-on-surface">Date of Birth</label>
                            <input class="w-full bg-surface-bright border border-outline-variant rounded-lg px-4 py-3 text-on-surface focus:outline-none focus:border-primary transition-all" type="date"/>
                        </div>
                    </div>
                </section>

                <div class="border-t border-outline-variant/50"></div>

                <section>
                    <div class="flex flex-col gap-6">
                        <div class="flex flex-col gap-2">
                            <label class="font-label-md text-label-md text-on-surface flex items-center gap-1"><span class="material-symbols-outlined" style="font-size:18px;">clinical_notes</span> Clinical Notes / Primary Diagnosis</label>
                            <textarea class="w-full bg-surface-bright border border-outline-variant rounded-lg px-4 py-3 text-on-surface focus:outline-none focus:border-primary transition-all resize-y" placeholder="Describe clinical findings and diagnosis..." rows="4"></textarea>
                        </div>
                    </div>
                </section>

                <div class="border-t border-outline-variant/50"></div>

                <section>
                    <div class="flex flex-col gap-6">
                        <div class="flex flex-col gap-2">
                            <label class="font-label-md text-label-md text-on-surface flex items-center gap-1"><span class="material-symbols-outlined" style="font-size:18px;">prescriptions</span> Prescription (Medications)</label>
                            <textarea class="w-full bg-surface-bright border border-outline-variant rounded-lg px-4 py-3 text-on-surface focus:outline-none focus:border-primary transition-all resize-y font-mono" placeholder="1. Amoxicillin 500mg..." rows="5"></textarea>
                        </div>
                        
                        <div class="flex flex-col gap-2">
                            <label class="font-label-md text-label-md text-on-surface flex items-center gap-1"><span class="material-symbols-outlined" style="font-size:18px;">info</span> How medicine to be taken (Instructions)</label>
                            <textarea class="w-full bg-surface-bright border border-outline-variant rounded-lg px-4 py-3 text-on-surface focus:outline-none focus:border-primary transition-all resize-y font-mono bg-yellow-50" placeholder="e.g., Take 1 tablet after meals with water." rows="3"></textarea>
                        </div>
                    </div>
                </section>

                <div class="flex justify-between items-center pt-4 border-t border-outline-variant/50">
                    <button class="px-6 py-3 rounded-lg border border-outline-variant text-on-surface hover:bg-surface-container-high transition-colors font-bold" type="reset">
                        Clear Form
                    </button>
                    <button onclick="window.print()" class="px-10 py-3 rounded-lg bg-primary text-on-primary hover:bg-surface-tint transition-colors shadow-sm flex items-center gap-2 font-bold text-lg" type="button">
                        <span class="material-symbols-outlined">print</span> Print Prescription
                    </button>
                </div>

            </form>
        </div>
    </main>

    <footer class="text-center py-4 text-on-surface-variant text-sm mt-auto">
        &copy; 2024 MedFlow Clinic. Simplified Prescription Form.
    </footer>

    <script>
        const form = document.querySelector('form');
        if (form) {
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                window.print();
            });
        }
    </script>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(head + "\n" + new_body)

