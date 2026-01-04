# Migration Guide: Copying Test- Repository to SolarEngine

This guide provides step-by-step instructions for copying the contents of the `enginebots370-cmyk/Test-` repository into the `enginebots370-cmyk/SolarEngine` repository.

## Overview

This repository contains a complete Solar Quote Engine application with:
- Standalone HTML version (`index.html`)
- Full Django application (`solar_quote/` directory)
- Comprehensive documentation
- Deployment guides and setup instructions

## Prerequisites

Before starting the migration, ensure you have:
- Git installed on your local machine
- Access to both repositories (Test- and SolarEngine)
- GitHub authentication configured (SSH or HTTPS)

## Migration Options

Choose the method that best fits your needs:

### Option 1: Complete Repository Copy (Recommended for New Repository)

This method copies all files, preserving the complete structure but not the Git history.

```bash
# 1. Clone the Test- repository
git clone https://github.com/enginebots370-cmyk/Test-.git
cd Test-

# 2. Remove the old Git history
rm -rf .git

# 3. Initialize as a new repository
git init

# 4. Add the SolarEngine remote
git remote add origin https://github.com/enginebots370-cmyk/SolarEngine.git

# 5. Add all files
git add .

# 6. Create initial commit
git commit -m "Initial commit: Solar Quote Engine from Test- repository"

# 7. Push to SolarEngine
git branch -M main
git push -u origin main
```

### Option 2: Copy with Full Git History

This method preserves all commit history from the Test- repository.

```bash
# 1. Clone the Test- repository
git clone https://github.com/enginebots370-cmyk/Test-.git solar-engine-copy
cd solar-engine-copy

# 2. Change the remote URL to SolarEngine
git remote set-url origin https://github.com/enginebots370-cmyk/SolarEngine.git

# 3. Push all branches and tags
git push -u origin --all
git push -u origin --tags
```

### Option 3: Selective File Copy

If the SolarEngine repository already has content and you want to add the Solar Quote Engine:

```bash
# 1. Clone both repositories
git clone https://github.com/enginebots370-cmyk/Test-.git
git clone https://github.com/enginebots370-cmyk/SolarEngine.git

# 2. Copy files from Test- to SolarEngine
cd Test-
cp -r * ../SolarEngine/
cp -r .gitignore ../SolarEngine/ # Copy hidden files

# 3. Go to SolarEngine and commit
cd ../SolarEngine
git add .
git commit -m "Add Solar Quote Engine from Test- repository"
git push
```

## What Gets Copied

The following structure will be migrated:

```
Root Directory:
├── .gitignore                  # Git ignore rules
├── README.md                   # Main project documentation
├── index.html                  # Standalone HTML version
├── requirements.txt            # Python dependencies
├── BACKUP_GUIDE.md            # Backup instructions
├── DEPLOYMENT_GUIDE.md        # Deployment instructions
├── DJANGO_SETUP.md            # Django integration guide
├── PROJECT_COMPLETE.md        # Project completion notes
├── QUICK_START.md             # Quick start guide
└── solar_quote/               # Django application
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── setup.sh
    ├── README.md
    ├── SETTINGS_EXAMPLE.py
    ├── URLS_EXAMPLE.py
    ├── static/
    │   ├── css/
    │   └── js/
    └── templates/
        └── solar_quote/
```

## Post-Migration Checklist

After copying the repository, verify the following:

### 1. Files Verification
- [ ] All documentation files are present (README.md, DJANGO_SETUP.md, etc.)
- [ ] The `solar_quote/` directory and all subdirectories are copied
- [ ] Static files (CSS/JS) are in place
- [ ] Templates directory is complete
- [ ] `.gitignore` file is present
- [ ] `requirements.txt` is available

### 2. GitHub Repository Settings
- [ ] Update repository name to "SolarEngine" if needed
- [ ] Update repository description: "Solar Quote Engine - Production-ready solar panel quote calculator"
- [ ] Set repository topics: `django`, `solar`, `calculator`, `quote-engine`, `python`
- [ ] Enable Issues if needed
- [ ] Configure branch protection rules for main branch

### 3. Documentation Updates
- [ ] Update README.md to reflect new repository name (if different)
- [ ] Update any hardcoded URLs that reference "Test-"
- [ ] Verify all links in documentation work correctly

### 4. Functionality Tests
- [ ] Test standalone HTML version by opening `index.html`
- [ ] If using Django:
  - [ ] Install dependencies: `pip install -r requirements.txt`
  - [ ] Run migrations: `python manage.py migrate`
  - [ ] Test the development server: `python manage.py runserver`
  - [ ] Access the application at http://localhost:8000

### 5. Clean Up
- [ ] Remove this MIGRATION_GUIDE.md if no longer needed
- [ ] Update any repository-specific configuration files
- [ ] Remove any test branches that aren't needed

## Updating Repository References

After migration, search and replace any references to the old repository name:

```bash
# Search for references to "Test-" in the codebase
grep -r "Test-" . --include="*.md" --include="*.py" --include="*.html"

# Replace "Test-" with "SolarEngine" where appropriate
# (Manually review each occurrence before replacing)
```

## Common Issues and Solutions

### Issue: Git push rejected
**Solution**: The SolarEngine repository might not be empty. Use Option 3 (Selective File Copy) or force push (⚠️ Warning: This will overwrite existing content):
```bash
git push -u origin main --force
```

### Issue: Conflicts with existing files
**Solution**: If SolarEngine has existing content:
1. Merge carefully to preserve existing work
2. Consider creating a new branch for the Solar Quote Engine
3. Use `git merge` or `git rebase` strategies

### Issue: Large file warnings
**Solution**: The repository should be small, but if issues occur:
```bash
# Check repository size
du -sh .git

# If needed, use Git LFS for large files
git lfs install
```

## Support and Documentation

After migration, refer to these files for setup and usage:

- **[README.md](README.md)** - Main project overview
- **[QUICK_START.md](QUICK_START.md)** - Fast setup instructions
- **[DJANGO_SETUP.md](DJANGO_SETUP.md)** - Complete Django integration
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Production deployment
- **[BACKUP_GUIDE.md](BACKUP_GUIDE.md)** - Backup procedures

## Final Notes

- The Solar Quote Engine is a complete, production-ready application
- All necessary files for both standalone and Django deployment are included
- The migration should be straightforward with no dependencies on the old repository name
- After successful migration, you can archive or delete the Test- repository if needed

## Migration Completion

Once migration is complete and verified:

1. Update the repository README with the new repository URL
2. Notify team members of the new repository location
3. Update any CI/CD pipelines or webhooks
4. Archive the Test- repository on GitHub if no longer needed

---

**Need Help?** Review the comprehensive documentation included in this repository, or refer to the Django and Git documentation for additional support.
