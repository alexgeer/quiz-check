# quiz-check

## installation and setup
```
> git clone https://github.com/alexgeer/quiz-check
> cd quiz-check
> python -m venv env
> env\Scripts\activate
> pip install -r requirements.txt
```

## usage
This script automatically checks for these conditions
- body has fields for `title` , `version`, `quizVersion`, `questions`, `title`
- six elements in `questions`
- each element has fields for `question` and `choices`
- each element in choices has `text` and `correct` field
- `correct` field is `bool` type
- each question has one and only one answer where `correct` is `true`

create your .yaml file in the directory and run

```bash
 python quiz_check.py yourquiz.yaml
 ```
or create a file called `quiz.yaml` and use the `check.bat` or `check.sh` script
```bash

./check
 ```

Put your quiz in a file named `quiz.yaml` to use the `check` script. Using the `check` script doesn't require activating the virtual environment.
