import pandas as pd
import os

def generate_invoices(input_csv, output_dir, num_invoices=50):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(input_csv)
    
    # Select a subset
    subset = df.head(num_invoices)
    
    for index, row in subset.iterrows():
        # Assign a mock routing number based on customer number for realism
        cust_num_str = str(row['cust_number'])
        mock_routing = f"000{cust_num_str[:6]}"
        invoice_text = f"""
=========================================
               INVOICE
=========================================
Invoice ID: {row['invoice_id']}
Business Code: {row['business_code']}
Customer Name: {row['name_customer']}
Customer Number: {row['cust_number']}

Date Information:
- Document Create Date: {row['document_create_date']}
- Posting Date: {row['posting_date']}
- Due Date: {row['due_in_date']}
- Clear Date: {row['clear_date']}

Billing Details:
- Total Open Amount: {row['total_open_amount']} {row['invoice_currency']}
- Payment Terms: {row['cust_payment_terms']}
- Routing Number: {mock_routing}

=========================================
"""
        with open(os.path.join(output_dir, f"invoice_{index}.txt"), "w") as f:
            f.write(invoice_text)
            
    print(f"Successfully generated {num_invoices} invoices in {output_dir}")

if __name__ == "__main__":
    generate_invoices("data/dataset.csv", "data/invoices", num_invoices=300)
