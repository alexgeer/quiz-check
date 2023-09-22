import yaml
import sys

filename = sys.argv[1]

assert filename.endswith('.yaml') or filename.endswith('.yml'), f"'{filename}' must be .yaml or .yml extension"

try:
    with open(filename, "r") as file:
        quiz = yaml.safe_load(file)
except yaml.parser.ParserError as err:
    print(err)
    exit()
finally:
    file.close()

fields = ["title", "version", "quizVersion", "questions"]

for field in fields:
    assert field in quiz, f"field '{field}' missing from quiz"

assert len(quiz["questions"]) == 6, f"expected 6 questions, found {len(quiz['questions'])}"

preview = ""

for i, q in enumerate(quiz["questions"], 1):
    assert "question" in q, f"question {i} missing 'question' field"
    assert isinstance(q["question"], str), f"question {i} 'question' field: got {type(q['question'])} expected {type('')}"

    assert "choices" in q, f"question {i} missing 'choices' field"
    assert isinstance(q["choices"], list), f"question {i} 'choices' field: got {type(q['choices'])} expected {type([])}"
    assert len(q["choices"]) > 1, f"question {i} 'choices' field: only one answer in list!"
    
    has_correct = False
    q_text = q['question'].replace("\\n", "\n").replace("\\\"", "\"")
    preview += f"{i}. {q_text}\n"

    for j, choice in enumerate(q["choices"], 1):
        assert "text" in choice, f"question {i} choice {j} missing 'text' field"
        assert type(choice["text"]) == str, f"question {i} choice{j}: 'question' field: got {type(choice['text'])} expected {type('')}"

        assert "correct" in choice, f"question {i} choice {j}  missing 'correct' field"
        if choice["correct"]:
            assert not has_correct, f"question {i} choice {j} >1 answer marked correct"
            has_correct = True
        assert type(choice["correct"]) == bool, f"question {i} choice {j}  'correct' field: got {type(choice['correct'])} expected {type(True)}"
        choice_text = choice["text"].replace("\n", "\\n").replace("\\\"", "\"")
        preview += f"  - {choice_text} {'-correct' if choice['correct'] else ''}\n"
    preview += "\n"
    assert has_correct, f"question {i} does not have answer where correct == True"

print(preview)
with open("quiz_preview.md", "w") as file:
        file.write(preview)
print("No problems found!")