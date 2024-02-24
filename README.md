# AI Assistant Chat Application

This project is an AI assistant chat application built using FastAPI + LLamaIndex + ChromaDB. The AI assistant is capable of responding to user queries and performing various tasks such as providing information and answering questions.

## Installation

To install and run the AI assistant application locally, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/K4rlosReyes/ai-assistant.git

   ```

2. Navigate to the project directory:
   ```bash
   cd ai-assistant
   ```

3. Install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```bash
   python main.py
   ```

5. Access the AI assistant API at http://localhost:8000.

### To try it in the terminal change step 4:
```bash
python -m core.process.rag
```

## Usage

Once the application is running, you can interact with the AI assistant through requests. The AI assistant will respond accordingly.

## Development Practices

This repository follows the following development practices:

- **Conventional Commits**: Commits follow the conventional commits specification for clear and standardized commit messages.
- **Code Style**: Code adheres to the PEP 8 style guide for Python code.
- **Documentation**: Code is well-documented, and additional documentation is provided where necessary.
- **Testing**: Unit tests are included in the `tests` directory to ensure code reliability and maintainability.
- **Continuous Integration**: Continuous Integration (CI) pipelines are set up to automatically run tests and checks on every push or pull request.

## Contributing

Contributions to the AI assistant chat application are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository and create a new branch for your feature or fix.
2. Make your changes and ensure that the code adheres to the project's development practices.
3. Write tests for your changes to ensure code reliability.
4. Submit a pull request detailing your changes and the problem they solve.

## License

This project is licensed under the [MIT License](LICENSE).
