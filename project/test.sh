# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi
# Check if pandas package is installed
if ! python -c "import pandas" &> /dev/null; then
    echo "pandas package is not installed. Please install pandas and try again."
    exit 1
fi

# Check if data.sqlite file exists
if [ ! -f "data.sqlite" ]; then
    echo "data.sqlite file does not exist. Please make sure to run the data pipeline to create the file."
    exit 1
fi

# Run the Python script to process and analyze the data
python data.py

# Check if the Python script executed successfully
if [ $? -eq 0 ]; then
    echo "Data pipeline completed successfully."
else
    echo "Error occurred while running the data pipeline."
    exit 1
fi
