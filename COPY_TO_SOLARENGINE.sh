#!/bin/bash

# Migration Script: Copy Test- Repository to SolarEngine
# This script automates the process of copying this repository to SolarEngine

set -e  # Exit on any error

echo "=========================================="
echo "Solar Quote Engine - Repository Migration"
echo "From: Test- → To: SolarEngine"
echo "=========================================="
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if git is installed
if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install Git and try again."
    exit 1
fi

print_info "Git is installed ✓"

# Get user confirmation
echo ""
echo "This script will help you copy this repository to SolarEngine."
echo "Please choose a migration method:"
echo ""
echo "1) Complete Copy (No Git History) - Recommended for clean start"
echo "2) Copy with Git History - Preserves all commits"
echo "3) Generate Manual Instructions - Just show the commands"
echo ""
read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo ""
        print_info "Method 1: Complete Copy (No Git History)"
        echo ""
        echo "Run these commands in order:"
        echo ""
        echo "# 1. Create a temporary copy of this repository"
        echo "cd .."
        echo "cp -r Test- SolarEngine-copy"
        echo "cd SolarEngine-copy"
        echo ""
        echo "# 2. Remove old Git history"
        echo "rm -rf .git"
        echo ""
        echo "# 3. Initialize as new repository"
        echo "git init"
        echo "git remote add origin https://github.com/enginebots370-cmyk/SolarEngine.git"
        echo ""
        echo "# 4. Add and commit all files"
        echo "git add ."
        echo "git commit -m \"Initial commit: Solar Quote Engine\""
        echo ""
        echo "# 5. Push to SolarEngine"
        echo "git branch -M main"
        echo "git push -u origin main"
        echo ""
        print_warning "Note: This will overwrite the SolarEngine repository if it has content!"
        ;;
    
    2)
        echo ""
        print_info "Method 2: Copy with Git History"
        echo ""
        echo "Run these commands in order:"
        echo ""
        echo "# 1. Clone this repository with a new name"
        echo "cd .."
        echo "git clone https://github.com/enginebots370-cmyk/Test-.git SolarEngine-copy"
        echo "cd SolarEngine-copy"
        echo ""
        echo "# 2. Change remote to SolarEngine"
        echo "git remote set-url origin https://github.com/enginebots370-cmyk/SolarEngine.git"
        echo ""
        echo "# 3. Push everything"
        echo "git push -u origin --all"
        echo "git push -u origin --tags"
        echo ""
        print_warning "Note: This preserves commit history but may conflict with existing content!"
        ;;
    
    3)
        echo ""
        print_info "Method 3: Manual Instructions"
        echo ""
        print_info "Please refer to MIGRATION_GUIDE.md for detailed instructions."
        echo ""
        echo "Quick summary:"
        echo "1. Clone or copy this repository"
        echo "2. Either keep or remove .git directory"
        echo "3. Configure remote to point to SolarEngine"
        echo "4. Push to SolarEngine repository"
        echo ""
        ;;
    
    *)
        print_error "Invalid choice. Please run the script again and select 1, 2, or 3."
        exit 1
        ;;
esac

echo ""
echo "=========================================="
print_info "For complete documentation, see:"
echo "  - MIGRATION_GUIDE.md - Detailed migration steps"
echo "  - README.md - Project overview"
echo "  - DJANGO_SETUP.md - Django integration"
echo "=========================================="
echo ""

# Display post-migration checklist
echo ""
print_info "Post-Migration Checklist:"
echo "  □ Verify all files copied successfully"
echo "  □ Update repository settings on GitHub"
echo "  □ Test standalone HTML version"
echo "  □ Test Django application (if using)"
echo "  □ Update team on new repository location"
echo ""

exit 0
