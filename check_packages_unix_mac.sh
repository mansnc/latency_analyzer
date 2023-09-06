# Determine if we should use pip or pip3
python_version=$(python --version 2>&1 | awk '{print $2}' | cut -d'.' -f1)
if [ "$python_version" -eq "3" ]; then
    PIP_COMMAND="pip3"
else
    PIP_COMMAND="pip"
fi

# Check if pip is installed
if ! command -v $PIP_COMMAND &> /dev/null; then
	echo "$PIP_COMMAND is not installed. Installing..."
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python get-pip.py
	rm get-pip.py
else
	echo "$PIP_COMMAND is installed; move on with packages installation"
fi

# List of packages to check
packages=("statistics" "matplotlib" "scapy")

for pkg in "${packages[@]}"; do
    if ! $PIP_COMMAND list | grep -q "$pkg"; then
        echo "$pkg is not installed. Installing..."
        $PIP_COMMAND install "$pkg"
    else
        echo "$pkg is already installed."
    fi
done
