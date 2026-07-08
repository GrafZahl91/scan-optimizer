# Contributing

First of all, thank you for your interest in Scan Optimizer!

Contributions are welcome and appreciated.

## Development Workflow

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Update regression tests if necessary.
5. Update the CHANGELOG for user-visible changes.
6. Open a Pull Request.

## Coding Guidelines

- Keep pipeline steps modular.
- Prefer configuration over hard-coded values.
- Add logging for new processing steps.
- Write readable and maintainable code.
- Preserve backward compatibility whenever possible.

## Testing

Before submitting a Pull Request, please verify your changes using the regression test documents located in:

tests/

Please ensure that:

- Scanned PDFs are processed correctly.
- Digital PDFs bypass the image pipeline.
- Blank page detection still works.
- Existing regression tests continue to pass.

## Reporting Issues

Please include:

- Operating System
- Docker version
- Python version
- Sample PDF (if possible)
- Relevant log output

Thank you for helping improve Scan Optimizer!
