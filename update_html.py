import re

with open('playground/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the content before <script> and after </script>
pre = content[:content.find('<script>')]

new_script = """<script type="module">
    import init, { run_tilk_code } from './pkg/oz_wasm.js';

    // UI Elements
    const codeEditor = document.getElementById('codeEditor');
    const lineNumbers = document.getElementById('lineNumbers');
    const runBtn = document.getElementById('runBtn');
    const consoleOutput = document.getElementById('consoleOutput');
    const astOutput = document.getElementById('astOutput');
    const tokenOutput = document.getElementById('tokenOutput');

    // Editor Logic
    function updateLineNumbers() {
        const lines = codeEditor.value.split('\\n').length;
        let numbersHTML = '';
        for (let i = 1; i <= lines; i++) {
            numbersHTML += i + '<br>';
        }
        lineNumbers.innerHTML = numbersHTML;
    }
    
    codeEditor.addEventListener('input', updateLineNumbers);
    codeEditor.addEventListener('scroll', () => {
        lineNumbers.scrollTop = codeEditor.scrollTop;
    });
    
    codeEditor.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            e.preventDefault();
            const start = this.selectionStart;
            const end = this.selectionEnd;
            this.value = this.value.substring(0, start) + "    " + this.value.substring(end);
            this.selectionStart = this.selectionEnd = start + 4;
            updateLineNumbers();
        }
    });
    
    updateLineNumbers();

    // Tab Logic
    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.output-content').forEach(c => c.classList.remove('active'));
            tab.classList.add('active');
            const target = tab.getAttribute('data-target');
            document.getElementById(target).classList.add('active');
        });
    });

    // WASM Initialization
    runBtn.textContent = 'Yükleniyor...';
    runBtn.disabled = true;

    init().then(() => {
        runBtn.textContent = 'Çalıştır';
        runBtn.disabled = false;
        
        runBtn.addEventListener('click', () => {
            consoleOutput.innerHTML = '';
            astOutput.innerHTML = '<span style="color: var(--text-muted);">WASM entegrasyonu sebebiyle AST ve Token görüntüleyici geçici olarak devre dışı bırakılmıştır. Sadece Çıktı (Console) aktiftir.</span>';
            tokenOutput.innerHTML = '';
            
            const code = codeEditor.value;
            try {
                const result = run_tilk_code(code);
                const logSpan = document.createElement('span');
                
                if (result.includes("HATA:")) {
                    logSpan.className = 'console-error';
                } else {
                    logSpan.className = 'console-log';
                }
                
                logSpan.textContent = result + '\\n';
                consoleOutput.appendChild(logSpan);
            } catch (err) {
                const errSpan = document.createElement('span');
                errSpan.className = 'console-error';
                errSpan.textContent = err.toString();
                consoleOutput.appendChild(errSpan);
            }
        });
    });
</script>
</body>
</html>
"""

with open('playground/index.html', 'w', encoding='utf-8') as f:
    f.write(pre + new_script)
