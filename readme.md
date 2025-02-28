# Data Sweeper

Data Sweeper is a user-friendly web application for transforming files between CSV and Excel formats with built-in data cleaning and visualization capabilities.

## 🚀 Features

- **File Format Conversion**: Easily convert between CSV and Excel formats
- **Data Cleaning Tools**: Remove duplicates and fill missing values with a single click
- **Column Selection**: Choose which columns to keep in your final output
- **Data Visualization**: Quick visualization of numeric data
- **Batch Processing**: Process multiple files in one session
- **Interactive UI**: User-friendly interface built with Streamlit

## 📋 Tech Stack

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **BytesIO**: Memory buffer for file handling

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/1089taha/Data-Sweeper-Assignment.git
   cd Data-Sweeper-Assignment

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
    

3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  

## 📊 Usage
 
1. Start the application:
  ```bash
  streamlit run app.py


2. Open your browser and navigate to the displayed URL (typically http://localhost:8501)

3. Upload your CSV or Excel files

4. Use the interface to clean and transform your data:
- Remove duplicates
- Fill missing values
- Select columns to keep
- Visualize data
- Convert between formats

5. Download your processed files

## 📝 Requirements

1. Create a requirements.txt file with these dependencies:
  ```bash
  streamlit>=1.15.0
  pandas>=1.3.0
  openpyxl>=3.0.0
 


## 🔮 Future Enhancements

- Advanced data cleaning options
- Custom visualization tools
- Support for more file formats
- Data profiling and statistics
- Automated data quality assessment