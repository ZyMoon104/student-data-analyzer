## Project Structure

```text
Student Data Analyzer/
├── data/
│   ├── students.csv
│   └── students_dirty.csv
├── analyzer.py
├── test_analyzer.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Main Functions

### `load_student(filename)`

Loads student records from a CSV file.

If the file does not exist, the function handles `FileNotFoundError` and returns a failure result.

### `validate_student(student)`

Validates one student record.

It checks:

- whether the name exists
- whether age can be converted to an integer
- whether score can be converted to a number
- whether score is between 0 and 100

### `clean_students(students)`

Checks multiple student records.

The function separates them into:

- valid students
- invalid students

Invalid records are stored together with the reason they failed validation.

### `calculate_score(students)`

Calculates the average score.

### `find_top_student(students)`

Finds the student with the highest score.

### `count_students(students)`

Counts how many students have a score greater than or equal to 60.

### `process_students_file(filename)`

Combines file loading, validation, and data cleaning into one simple processing pipeline.

## How to Run

```bash
python analyzer.py
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

Current dependency:

```text
pytest==9.1.1
```

The `csv` module is part of Python's standard library, so it does not need to be installed separately.

## How to Test

```bash
pytest
```

Current tests include:

- pass score boundary test
- student validation test
- dirty data cleaning test
- successful CSV loading test
- missing file test

Example result:

```text
collected 5 items

test_analyzer.py ..... [100%]

5 passed
```

## What I Learned

Through this project, I learned how to:

- Work with lists, dictionaries, CSV files, loops, and functions
- Convert string data into numbers
- Separate different responsibilities into different functions
- Use `FileNotFoundError`, `ValueError`, and `KeyError`
- Validate external data before using it
- Separate valid and invalid data
- Record validation failure reasons
- Build a simple data processing pipeline
- Use `assert` and pytest for automated testing
- Test normal cases, boundary cases, and error cases
- Use Git to track project changes with multiple commits

## Data Processing Flow

```text
CSV File
   ↓
Load Data
   ↓
Validate Data
   ↓
Clean Data
   ↓
Use Valid Data
```

## Git History

The project was developed step by step.

Example commit history:

```text
add student data processing pipeline
remove temporary data generation script
add pytest tests and project documentation
```

## Project Purpose

This is a small Python engineering practice project.

Its purpose is to build the basic programming and engineering skills needed for later AI / LLM application projects.

The next stage will focus on APIs, LLM integration, RAG, Agent workflows, and evaluation.