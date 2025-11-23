# Sentence-By-Sentence Writing Coach

A lightweight Flask app that coaches students through their drafts one sentence at a time. Paste any short passage and the coach will:

- Extract the first sentence and quickly judge whether it is strong or could use an edit.
- Suggest one focused improvement area (specificity, clarity, concision, development, or voice) and show a model sentence that demonstrates the move without reusing student text.
- Let students accept the suggestion, revise in place, and get immediate feedback on whether the change worked.
- Allow skipping any edit and moving to the next sentence whenever the student chooses.

## Running locally

```bash
pip install -r requirements.txt
python app.py
```

The app listens on port 8080 by default.
