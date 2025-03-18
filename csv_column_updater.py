import pandas as pd
import os

def update_excel_column_name(excel_file_path, sheet_name=0):
    """
    Read an Excel file and update all column names to uppercase.
    
    Args:
        excel_file_path (str): Path to the Excel file
        sheet_name (str or int, optional): Name or index of the sheet to process. 
                                         Defaults to 0 (first sheet).
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Validate file path
        if not os.path.exists(excel_file_path):
            raise FileNotFoundError(f"Excel file not found: {excel_file_path}")
            
        # Read all sheets to get sheet names
        excel_file = pd.ExcelFile(excel_file_path)
        sheet_names = excel_file.sheet_names
        
        if not sheet_names:
            raise ValueError("Excel file contains no sheets")
            
        # If sheet_name is an integer, convert to actual sheet name
        if isinstance(sheet_name, int):
            if sheet_name >= len(sheet_names):
                raise ValueError(f"Sheet index {sheet_name} is out of range. File has {len(sheet_names)} sheets.")
            sheet_name = sheet_names[sheet_name]
            
        # Validate sheet name
        if sheet_name not in sheet_names:
            raise ValueError(f"Sheet '{sheet_name}' not found in Excel file. Available sheets: {sheet_names}")
            
        # Read the specific sheet
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        
        if df.empty:
            raise ValueError(f"Sheet '{sheet_name}' is empty")
            
        # Get current column names and convert to uppercase
        new_columns = {col: col.upper() for col in df.columns}
        
        # Rename the columns
        df.rename(columns=new_columns, inplace=True)
        
        # Create ExcelWriter with the original file
        with pd.ExcelWriter(excel_file_path, mode='a', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        print(f"Successfully updated column names in sheet '{sheet_name}' of {excel_file_path}")
        print("New column names:", list(df.columns))
        return True
        
    except Exception as e:
        print(f"Error updating column names: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    # Example Excel file path
    file_path = "composeio_mcp_test/data/product_details_1.xlsx"
    update_excel_column_name(file_path) 