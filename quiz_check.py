import yaml
import sys

filename = sys.argv[1]

assert filename.endswith('.yaml') or filename.endswith('.yml'), f"'{filename}' must be .yaml or .yml extension"


with open(filename, "r") as file:
    quiz = yaml.safe_load(file)

fields = ["title", "version", "quizVersion", "questions", "title"]

for field in fields:
    assert field in quiz, f"field '{field}' missing from quiz"

assert len(quiz["questions"]) == 6

for i, question in enumerate(quiz["questions"]):
    assert "question" in question, f"question {i} missing 'question' field"
    assert "choices" in question, f"question {i} missing 'choices' field"
    has_correct = False

    for j, choice in enumerate(question["choices"]):
        assert "text" in choice, f"question {j} missing 'text' field"
        assert "correct" in choice, f"question {j} missing 'correct' field"
        if choice["correct"]:
            has_correct = True
        assert type(
            choice["correct"] == bool
        ), f"question {j} 'correct' field is not type 'bool'"
        
    assert has_correct, f"question {i} does not have answer where correct == True"

print("No problems found!")