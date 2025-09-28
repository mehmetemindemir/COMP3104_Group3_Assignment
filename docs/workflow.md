# Git Workflow Guidelines

## Branch Strategy
We follow a GitFlow-inspired workflow for this project:

### Main Branches
- **`main`**: Production-ready code, always deployable
- **`develop`**: Integration branch for features (to be created when needed)

### Supporting Branches
- **`feature/*`**: New features or enhancements
- **`bugfix/*`**: Bug fixes
- **`hotfix/*`**: Critical fixes for production

## Workflow Steps

### Starting New Work
1. **Update your local main branch**
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/description-of-feature
   ```

### Working on Your Feature
1. **Make small, focused commits**
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

2. **Use descriptive commit messages**
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for modifications
   - `Remove:` for deletions
   - `Docs:` for documentation changes

### Submitting Your Work
1. **Push your feature branch**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request**
   - Go to GitHub and create a PR from your feature branch to main
   - Add a descriptive title and description
   - Request review from team members
   - Link any relevant issues

### Code Review Process
- All changes must be reviewed by at least one team member
- Address review comments promptly
- Keep PRs focused and reasonably sized
- Update documentation as needed

### Best Practices
- Keep commits atomic and focused
- Write clear commit messages
- Test your changes before pushing
- Keep your feature branches up to date with main
- Delete feature branches after they're merged