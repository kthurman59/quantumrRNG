document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate');
    const bitsSelect = document.getElementById('bits');
    const decimalResult = document.getElementById('decimal-result');
    const binaryResult = document.getElementById('binary-result');
    const errorDisplay = document.getElementById('error');

    const API_URL = 'http://localhost:5000';

    async function generateNumber() {
        const bits = bitsSelect.value;
        generateBtn.disabled = true;
        
        try {
            const response = await fetch(`${API_URL}/generate/${bits}`);
            const data = await response.json();
            
            if (data.error) {
                throw new Error(data.error);
            }
            
            decimalResult.textContent = data.decimal;
            binaryResult.textContent = data.binary;
            errorDisplay.textContent = '';
        } catch (error) {
            decimalResult.textContent = '-';
            binaryResult.textContent = '-';
            errorDisplay.textContent = `Error: ${error.message}`;
        } finally {
            generateBtn.disabled = false;
        }
    }

    generateBtn.addEventListener('click', generateNumber);
});
