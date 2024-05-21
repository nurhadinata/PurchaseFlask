#!/bin/bash
DB_USER="purchase"
DB_PASSWORD="root"
DB_NAME="purchase"
DB_HOST="localhost"
PG_USER="postgres"
PG_PASSWORD="12345678"

REPO_URL="https://github.com/alamkamajana/purchaseApp.git"
DESTINATION_DIR="flaskAppCahya"
BRANCH_NAME="cahya"


check_os() {
    # Determine the OS type
    OS_TYPE=$(uname)
    case "$OS_TYPE" in
        "Linux")
            if [ -f /etc/os-release ]; then
                . /etc/os-release
                OS_NAME=$NAME
                OS_VERSION=$VERSION
            elif type lsb_release >/dev/null 2>&1; then
                OS_NAME=$(lsb_release -si)
                OS_VERSION=$(lsb_release -sr)
            elif [ -f /etc/lsb-release ]; then
                . /etc/lsb-release
                OS_NAME=$DISTRIB_ID
                OS_VERSION=$DISTRIB_RELEASE
            elif [ -f /etc/debian_version ]; then
                OS_NAME="Debian"
                OS_VERSION=$(cat /etc/debian_version)
            elif [ -f /etc/redhat-release ]; then
                OS_NAME="Red Hat"
                OS_VERSION=$(cat /etc/redhat-release)
            else
                OS_NAME=$(uname -s)
                OS_VERSION=$(uname -r)
            fi
            ;;
        "Darwin")
            OS_NAME="macOS"
            OS_VERSION=$(sw_vers -productVersion)
            ;;
        "CYGWIN"*|"MINGW"*|"MSYS"*)
            OS_NAME="Windows"
            OS_VERSION=$(uname -r)
            ;;
        *)
            OS_NAME="Unknown"
            OS_VERSION="Unknown"
            ;;
    esac
}

# Check if Homebrew is installed
install_package_manager(){
    local OS=$1
    if [ "$OS" = "macOS" ]; then
        if ! command -v brew &>/dev/null; then
            echo "Homebrew is not installed. Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

            # Add Homebrew to PATH and apply to current session
            echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
            eval "$(/opt/homebrew/bin/brew shellenv)"
        fi

        

        brew update
    elif [ "$OS" = "Windows" ]; then
        if ! command -v choco &>/dev/null; then
            echo "Chocolatey is not installed. Installing Chocolatey..."
            powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
			echo 'export PATH="$PATH:/c/ProgramData/chocolatey/bin"'>>~/.bashrc
			source ~/.bashrc
			
		fi
    fi
}

install_postgresql(){
    local OS=$1
    if [ "$OS" = "macOS" ]; then
        brew update

        # Install PostgreSQL 12
        brew install postgresql@12

        # Start PostgreSQL 12 service
        brew services start postgresql@12 
    elif [ "$OS" = "Windows" ]; then
        # Update Chocolatey
        choco upgrade chocolatey -y

        # Install PostgreSQL using Chocolatey
        choco install postgresql12 --params '/Password:$PG_PASSWORD' -y
		
		echo 'export PATH="$PATH:/c/Program Files/PostgreSQL/12/bin"'>>~/.bashrc
		source ~/.bashrc
		
		
    fi
}

install_pyenv(){
    local OS=$1
    if [ "$OS" = "macOS" ]; then
        brew install pyenv
    elif [ "$OS" = "Windows" ]; then
        choco install pyenv-win -y
		
		echo 'export PYENV_ROOT="$HOME/.pyenv"'>>~/.bashrc
		echo 'export PATH="$PYENV_ROOT/bin:$PATH"'>>~/.bashrc
		echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

		source ~/.bashrc
    fi
}

install_git(){
    local OS=$1
    if [ "$OS" = "macOS" ]; then
        brew install git
    elif [ "$OS" = "Windows" ]; then
        choco install git -y
    fi
}

check_os

install_package_manager "$OS_NAME"

# Check if PostgreSQL is installed
if [ -x "$(command -v psql)" ]; then
    echo "PostgreSQL is already installed."
else
    echo "PostgreSQL is not installed. Proceeding with installation..."

    install_postgresql "$OS_NAME"
fi

# Confirm installation
echo "PostgreSQL version:"
psql --version

user_exists=$(PGPASSWORD=$PG_PASSWORD psql -U $PG_USER -tAc "SELECT 1 FROM pg_roles WHERE rolname='$DB_USER';")
if [ -n "$user_exists" ]; then
    echo "User $DB_USER already exists."
else
    # Create the database user
    echo "Creating database user..."
    PGPASSWORD=$PG_PASSWORD psql -U $PG_USER -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
fi

# echo "Creating database user..."
# PGPASSWORD=12345678 psql -U postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"

# Create the database
db_exists=$(PGPASSWORD=$PG_PASSWORD psql -U $PG_USER -lqt | cut -d \| -f 1 | grep -w "$DB_NAME")
if [ -n "$db_exists" ]; then
    echo "Database $DB_NAME already exists."
else
    # Create the database
    echo "Creating database..."
    PGPASSWORD=$PG_PASSWORD psql -U $PG_USER -c "CREATE DATABASE $DB_NAME;"
fi
# echo "Creating database..."
# PGPASSWORD=12345678 psql -U postgres -c "CREATE DATABASE $DB_NAME;"

# Grant privileges to the user for the database
echo "Granting privileges..."
PGPASSWORD=$PG_PASSWORD psql -U $PG_USER -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"

echo "Database user and database created successfully."

if command -v git &> /dev/null; then
    echo "Git is already installed."
else
    echo "Git is not installed. Proceeding with instalation..."
    install_git "$OS_NAME"
fi

if command -v pyenv &>/dev/null; then
    echo "pyenv is already installed."
else
    echo "pyenv is not installed. Proceeding with installation..."
    install_pyenv "$OS_NAME"

    # Add pyenv to PATH
    echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bash_profile
    echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

    # Initialize pyenv in the current shell
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv virtualenv-init -)"

    echo "pyenv has been successfully installed."
fi

# Check if the destination directory already exists
if [ -d "$DESTINATION_DIR" ]; then
    echo "Destination directory '$DESTINATION_DIR' already exists."
else
    echo "Cloning repository..."
    git clone -b "$BRANCH_NAME" --single-branch "$REPO_URL" "$DESTINATION_DIR"

    echo "Repository cloned successfully."

fi

# Clone the repository


# Install Python 3.10 using pyenv
echo "Installing Python 3.10..."
pyenv install 3.10

# Set Python 3.10 as the global version
pyenv global 3.10

echo "Python 3.10 has been successfully installed."

cd $DESTINATION_DIR

if [ -d "venv" ]; then
    # Delete the directory and its contents
    rm -rf "venv"
fi

echo "Creating virtual environment..."
python3 -m venv venv


source venv/bin/activate
echo "Virtual Environment has been successfully created."

echo "Installing dependencies..."
pip3 install -r data/requirements.txt
echo "Dependencies has been successfully installed."

# export THONUNBUFFERED=1
# export FLASK_APP=run.py
# export FLASK_DEBUG=1

# venv/bin/flask run
