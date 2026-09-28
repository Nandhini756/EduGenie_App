const $ = (id) => document.getElementById(id);

function setBusy(form, busy) {
  const button = form.querySelector('button');
  button.disabled = busy;
  button.textContent = busy ? 'Working…' : button.dataset.label;
}

function setupButtons() {
  document.querySelectorAll('button').forEach((button) => {
    button.dataset.label = button.textContent;
  });
}

async function request(url, options = {}) {
  const response = await fetch(url, {
    headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
    ...options,
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(data.error || data.detail || 'Request failed.');
  return data;
}

function showResult(element, content, isError = false) {
  element.className = `output${isError ? ' error' : ''}`;
  element.textContent = content;
}

$('qaForm').addEventListener('submit', async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const result = $('qaResult');
  setBusy(form, true); showResult(result, 'Thinking…');
  try {
    const data = await request(`/qa?question=${encodeURIComponent($('question').value.trim())}`);
    showResult(result, data.answer);
  } catch (error) { showResult(result, error.message, true); }
  finally { setBusy(form, false); }
});

$('explainForm').addEventListener('submit', async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const result = $('explanationResult');
  setBusy(form, true); showResult(result, 'Explaining…');
  try {
    const data = await request('/explain/', { method: 'POST', body: JSON.stringify({ topic: $('topic').value.trim() }) });
    showResult(result, data.explanation);
  } catch (error) { showResult(result, error.message, true); }
  finally { setBusy(form, false); }
});

$('summaryForm').addEventListener('submit', async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const result = $('summaryResult');
  setBusy(form, true); showResult(result, 'Summarizing…');
  try {
    const data = await request('/summarize/', { method: 'POST', body: JSON.stringify({ text: $('summaryText').value.trim() }) });
    showResult(result, data.summary);
  } catch (error) { showResult(result, error.message, true); }
  finally { setBusy(form, false); }
});

$('quizForm').addEventListener('submit', async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const result = $('quizResult');
  setBusy(form, true); showResult(result, 'Generating quiz…');
  try {
    const data = await request('/quiz', { method: 'POST', body: JSON.stringify({ text: $('quizText').value.trim() }) });
    result.className = 'output';
    result.innerHTML = data.quiz.map((item, index) => `
      <div class="quiz-question">
        <strong>Q${index + 1}: ${escapeHtml(item.question)}</strong>
        ${item.options.map((option, optionIndex) => `
          <label class="option"><input type="radio" name="q${index}" value="${escapeAttr(option)}"> ${escapeHtml(option)}</label>
        `).join('')}
        <button type="button" class="check-answer" data-index="${index}">Check Answer</button>
        <div class="quiz-feedback" id="feedback-${index}"></div>
      </div>
    `).join('');
    result.querySelectorAll('.check-answer').forEach((button) => {
      button.addEventListener('click', () => {
        const index = Number(button.dataset.index);
        const selected = result.querySelector(`input[name="q${index}"]:checked`);
        const feedback = $(`feedback-${index}`);
        if (!selected) { feedback.textContent = 'Select an answer first.'; return; }
        const correct = data.quiz[index].answer;
        feedback.textContent = selected.value === correct ? 'Correct!' : `Incorrect. Correct answer: ${correct}`;
      });
    });
  } catch (error) { showResult(result, error.message, true); }
  finally { setBusy(form, false); }
});

$('learnForm').addEventListener('submit', async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const result = $('learnResult');
  setBusy(form, true); showResult(result, 'Building learning path…');
  try {
    const data = await request(`/learn/recommendations?topic=${encodeURIComponent($('learnTopic').value.trim())}`);
    showResult(result, data.recommendation);
  } catch (error) { showResult(result, error.message, true); }
  finally { setBusy(form, false); }
});

function escapeHtml(value) {
  return String(value).replace(/[&<>'"]/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[char]));
}
function escapeAttr(value) { return escapeHtml(value); }

setupButtons();
