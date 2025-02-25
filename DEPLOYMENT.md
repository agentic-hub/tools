# Deployment Guide for Agentic Tools Hub

This document provides detailed instructions for deploying the Agentic Tools Hub package to PyPI using GitHub Actions.

## Table of Contents

- [Prerequisites](#prerequisites)
- [GitHub Actions Workflows](#github-actions-workflows)
- [Deployment Process](#deployment-process)
- [Manual Deployment](#manual-deployment)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before deploying, ensure you have:

1. **PyPI Account**: Create an account on [PyPI](https://pypi.org/) if you don't have one.

2. **PyPI API Token**: 
   - Go to your PyPI account settings
   - Create an API token with upload permissions
   - Add this token as a secret named `PYPI_TOKEN` in your GitHub repository

3. **TestPyPI Account** (optional):
   - Create an account on [TestPyPI](https://test.pypi.org/)
   - Create an API token
   - Add this token as a secret named `TEST_PYPI_TOKEN` in your GitHub repository

4. **Write Access to Repository**: Ensure you have write access to the repository to create releases and run workflows.

## GitHub Actions Workflows

The repository contains three main workflows:

### 1. Run Tests (`test.yml`)

This workflow runs automatically on:
- Push to main/master branch
- Pull requests to main/master branch

It performs:
- Linting with flake8
- Running tests with pytest
- Testing on multiple Python versions (3.9, 3.10)

### 2. Bump Version (`bump-version.yml`)

This is a manually triggered workflow that:
- Increments the package version in `pyproject.toml`
- Commits the change
- Creates a git tag for the new version

To run this workflow:
1. Go to the Actions tab in your repository
2. Select "Bump Version" workflow
3. Click "Run workflow"
4. Choose which part of the version to bump (major, minor, patch)
5. Optionally add a prerelease identifier (e.g., "alpha", "beta", "rc")

### 3. Deploy to PyPI (`deploy.yml`)

This workflow is triggered:
- Automatically when a new GitHub Release is created
- Manually through the Actions tab

It performs:
- Running tests
- Verifying the package version matches the release tag
- Building the package
- Publishing to PyPI or TestPyPI

## Deployment Process

### Standard Deployment Flow

1. **Update Code and Documentation**:
   - Make necessary code changes
   - Update documentation
   - Ensure tests pass locally

2. **Bump Version**:
   - Go to Actions → Bump Version → Run workflow
   - Select version part to bump (major, minor, patch)
   - This will create a new tag like `v0.1.1`

3. **Create Release**:
   - Go to the Releases section in your repository
   - Click "Create a new release"
   - Select the tag created by the Bump Version workflow
   - Add release notes describing the changes
   - Click "Publish release"

4. **Monitor Deployment**:
   - The Deploy to PyPI workflow will automatically trigger
   - Check the workflow logs for any errors
   - Verify the package is available on PyPI

### Manual Deployment

For testing or special cases, you can manually deploy:

1. Go to Actions → Deploy to PyPI → Run workflow
2. Select the environment:
   - `pypi` for production
   - `testpypi` for testing
3. Click "Run workflow"

## Manual Deployment (Without GitHub Actions)

If you need to deploy manually from your local machine:

```bash
# Install Poetry if not already installed
curl -sSL https://install.python-poetry.org | python3 -

# Build the package
poetry build

# Publish to PyPI
poetry config pypi-token.pypi your-pypi-token
poetry publish

# Or publish to TestPyPI
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi your-testpypi-token
poetry publish -r testpypi
```

## Troubleshooting

### Common Issues

1. **Version Conflict**:
   - Error: "Version in pyproject.toml does not match tag version"
   - Solution: Ensure the version in `pyproject.toml` matches the release tag (without the 'v' prefix)

2. **PyPI Token Issues**:
   - Error: "Invalid API token"
   - Solution: Regenerate your PyPI token and update the GitHub secret

3. **Package Name Already Exists**:
   - Error: "HTTPError: 403 Forbidden"
   - Solution: Ensure your package name is unique on PyPI or you own the package

4. **Test Failures**:
   - Error: "Tests failed"
   - Solution: Fix failing tests before deployment

### Getting Help

If you encounter issues not covered here:
1. Check the GitHub Actions workflow logs for detailed error messages
2. Consult the [Poetry documentation](https://python-poetry.org/docs/)
3. Refer to the [PyPI help](https://pypi.org/help/) resources 