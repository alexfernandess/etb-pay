import re

files_to_update = [
    r"c:\workspace\etb-pay\web\etb_arena_de_questoes_2G.html",
    r"c:\workspace\etb-pay\web\etb_arena_de_questoes_3G.html"
]

stopwatch_html = """            <div class="flex items-center gap-3 sm:gap-4 flex-wrap sm:flex-nowrap justify-center">
                <!-- Cronômetro de Prova -->
                <div class="flex items-center gap-3 bg-slate-900/80 px-4 py-2.5 rounded-xl border border-slate-700 shadow-inner print:hidden">
                    <div class="flex flex-col items-center">
                        <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Tempo</span>
                        <span id="stopwatch-display" class="text-xl font-black text-slate-400 font-mono leading-none tracking-widest transition-colors duration-300">00:00</span>
                    </div>
                    <div class="h-8 w-px bg-slate-700"></div>
                    <div class="flex gap-1">
                        <button onclick="toggleStopwatch()" id="btn-stopwatch-toggle" class="p-1.5 rounded-lg hover:bg-slate-700 text-slate-400 hover:text-emerald-400 transition-colors" title="Play/Pause">
                            <svg id="icon-play" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" class="block"><polygon points="5 3 19 12 5 21 5 3"/></svg>
                            <svg id="icon-pause" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" class="hidden"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>
                        </button>
                        <button onclick="resetStopwatch()" class="p-1.5 rounded-lg hover:bg-slate-700 text-slate-400 hover:text-amber-400 transition-colors" title="Zerar">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
                        </button>
                    </div>
                </div>

                <!-- Placar em Tempo Real -->
                <div"""

print_time_html = """            <div class="flex flex-col sm:flex-row gap-6 mt-6 hidden print:flex w-full">
                <div id="print-date-section" class="w-full flex-1">
                    <label class="block text-xs font-bold text-slate-600 uppercase tracking-widest mb-2">Data e Hora de Conclusão</label>
                    <div id="print-date-value" class="w-full print:bg-transparent border print:border-slate-300 rounded-lg px-4 py-3 text-black font-bold"></div>
                </div>
                <div id="print-time-section" class="w-full flex-1">
                    <label class="block text-xs font-bold text-slate-600 uppercase tracking-widest mb-2">Tempo Total de Prova</label>
                    <div id="print-time-value" class="w-full print:bg-transparent border print:border-slate-300 rounded-lg px-4 py-3 text-black font-bold"></div>
                </div>
            </div>"""

stopwatch_js = """        // CRONÔMETRO DE PROVA
        let stopwatchInterval = null;
        let stopwatchSeconds = 0;
        let isStopwatchRunning = false;

        function updateStopwatchDisplay() {
            const display = document.getElementById('stopwatch-display');
            const hrs = Math.floor(stopwatchSeconds / 3600);
            const mins = Math.floor((stopwatchSeconds % 3600) / 60);
            const secs = stopwatchSeconds % 60;
            
            let timeString = '';
            if (hrs > 0) {
                timeString += String(hrs).padStart(2, '0') + ':';
            }
            timeString += String(mins).padStart(2, '0') + ':' + String(secs).padStart(2, '0');
            
            display.textContent = timeString;
        }

        function toggleStopwatch() {
            const display = document.getElementById('stopwatch-display');
            const iconPlay = document.getElementById('icon-play');
            const iconPause = document.getElementById('icon-pause');

            if (isStopwatchRunning) {
                // Pause
                clearInterval(stopwatchInterval);
                isStopwatchRunning = false;
                
                iconPlay.classList.remove('hidden');
                iconPlay.classList.add('block');
                iconPause.classList.remove('block');
                iconPause.classList.add('hidden');
                
                display.classList.remove('text-amber-400', 'animate-pulse');
                display.classList.add('text-slate-400');
            } else {
                // Play
                isStopwatchRunning = true;
                
                iconPlay.classList.remove('block');
                iconPlay.classList.add('hidden');
                iconPause.classList.remove('hidden');
                iconPause.classList.add('block');
                
                display.classList.remove('text-slate-400');
                display.classList.add('text-amber-400', 'animate-pulse');
                
                stopwatchInterval = setInterval(() => {
                    stopwatchSeconds++;
                    updateStopwatchDisplay();
                }, 1000);
            }
        }

        function resetStopwatch() {
            if (isStopwatchRunning) {
                toggleStopwatch(); // pausa
            }
            stopwatchSeconds = 0;
            updateStopwatchDisplay();
        }

        // 3. FUNÇÃO AUXILIAR: CARREGAR EXAME"""

pdf_logic_insert = """            // Pausar o cronômetro automaticamente se estiver rodando
            if (isStopwatchRunning) {
                toggleStopwatch();
            }

            // Injetar tempo de prova no HTML
            const timeString = document.getElementById('stopwatch-display').textContent;
            const timeField = document.getElementById('print-time-value');
            if (timeField) {
                timeField.textContent = timeString;
            }

            // Exibir a seção de data"""

for filepath in files_to_update:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. HTML Header modification
    # Look for <!-- Placar em Tempo Real -->\n            <div
    content = re.sub(
        r'<!-- Placar em Tempo Real -->\s*<div',
        stopwatch_html,
        content
    )
    # Don't forget to close the wrapper div after the Placar
    content = re.sub(
        r'(<span id="score-yield" class="text-xl font-black text-blue-400 leading-none">0%</span>\s*</div>\s*</div>)',
        r'\1\n            </div>',
        content
    )

    # 2. HTML Print Section modification
    old_print_section = r'<div id="print-date-section" class="hidden print:block w-full">.*?</div>\s*</div>'
    content = re.sub(old_print_section, print_time_html, content, flags=re.DOTALL)

    # 3. JS Stopwatch functions
    content = content.replace("// 3. FUNÇÃO AUXILIAR: CARREGAR EXAME", stopwatch_js)
    # For 2G, it might have been numbered differently if the comments shifted, let's just search for the function
    if "// 3. FUNÇÃO AUXILIAR: CARREGAR EXAME" not in content:
        content = re.sub(r'(\s+function loadExam)', '\n' + stopwatch_js.replace("// 3. FUNÇÃO AUXILIAR: CARREGAR EXAME", "") + r'\1', content)

    # 4. PDF Integration
    content = content.replace("// Exibir a seção de data", pdf_logic_insert)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Stopwatch integration complete for both files.")
