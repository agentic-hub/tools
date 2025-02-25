# Deployment Guide for Agentic Tools Hub

This document explains how to use the GitHub Actions workflows to version and deploy the Agentic Tools Hub package.

## GitHub Actions Workflows

The repository includes the following GitHub Actions workflows:

1. **Lint Workflow** - Runs linting on push to main and pull requests
2. **Deploy Workflow** - Builds and publishes the package to PyPI when a new release is created
3. **Version Bump Workflow** - Automatically bumps the version number based on semantic versioning

## Setting Up PyPI Deployment

To deploy to PyPI, you need to set up a PyPI API token:

1. Create an account on [PyPI](https://pypi.org/) if you don't have one
2. Go to your account settings and create an API token with upload permissions
3. In your GitHub repository, go to Settings > Secrets and variables > Actions
4. Add a new repository secret named `PYPI_TOKEN` with the value of your PyPI API token

## Deployment Process

### Automatic Linting

The lint workflow runs automatically on:
- Every push to the `main` branch
- Every pull request to the `main` branch

This ensures that the code follows the project's style guidelines.

### Version Bumping

To bump the version number:

1. Go to the "Actions" tab in your GitHub repository
2. Select the "Version Bump" workflow
3. Click "Run workflow"
4. Select the type of version bump:
   - `patch` for bug fixes (e.g., 1.0.0 -> 1.0.1)
   - `minor` for new features (e.g., 1.0.0 -> 1.1.0)
   - `major` for breaking changes (e.g., 1.0.0 -> 2.0.0)
5. Click "Run workflow"

This will:
- Update the version in `pyproject.toml`
- Commit the changes
- Create a new tag with the version number
- Push the changes and tag to GitHub

### Creating a Release

To deploy a new version to PyPI:

1. Go to the "Releases" tab in your GitHub repository
2. Click "Create a new release"
3. Select the tag that was created by the Version Bump workflow
4. Add a title and description for the release
5. Click "Publish release"

This will trigger the Deploy workflow, which will:
- Build the package
- Publish it to PyPI

## Manual Deployment

If you need to deploy manually:

```bash
# Install Poetry if not already installed
pip install poetry

# Configure PyPI token
poetry config pypi-token.pypi YOUR_PYPI_TOKEN

# Build the package
poetry build

# Publish to PyPI
poetry publish
```

## Troubleshooting

If you encounter issues with the deployment:

1. Check the workflow logs in the GitHub Actions tab
2. Ensure that the `PYPI_TOKEN` secret is correctly set
3. Verify that the version number in `pyproject.toml` has been incremented
4. Make sure you have the necessary permissions to push to the repository 