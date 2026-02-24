import pandas as pd

data = None

def menu():
    global data
    while(True):
        print("\n--------Sales Order Analyzer--------")
        print("1. Load CSV")
        print("2. Revenue Per product")
        print("3. Revenue Per Category")
        print("4. Revenue Per Country")
        print("5. Total Revenue")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            data = load_csv("sales-order-analyzer/data/orders.csv")

        elif choice == "2":
            revenue_per_product()

        elif choice == "3":
            revenue_per_category()

        elif choice == "4":
            revenue_per_country()

        elif choice == "5":
            total_revenue()

        elif choice == "6":
            print("Thank you for using Sales Order Analyzer")
            break

        else:
            print("Invalid choice. Try again.")

        
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Data Loaded Succesfully. {len(df)} rows total")
        return df
    except FileNotFoundError:
        print("CSV file not found")
        return None
    

def revenue_per_product():
    global data

    if data is None:
        print("Please load the CSV file first")
        return
    
    data["Revenue"] = data["Quantity"] * data["Price"]

    result = data.groupby("Product")["Revenue"].sum()

    print("\n--- Total Revenue Per Product ---")
    print(result)


def revenue_per_category():
    global data

    if data is None:
        print("Please load the CSV file first")
        return
    
    data["Revenue"] = data["Quantity"] * data["Price"]

    result = data.groupby("Category")["Revenue"].sum()

    print("\n--- Total Revenue Per Category ---")
    print(result)

def revenue_per_country():
    global data

    if data is None:
        print("Please load the CSV file first")
        return
    
    data["Revenue"] = data["Quantity"] * data["Price"]

    result = data.groupby("Country")["Revenue"].sum()

    print("\n--- Total Revenue Per Country ---")
    print(result)


def total_revenue():
    global data

    if data is None:
        print("Please load the CSV file first")
        return
    
    data["Revenue"] = data["Quantity"] * data["Price"]

    result = data["Revenue"].sum()

    print("\n--- Total Revenue ---")
    print(result)
    



if __name__ == "__main__":
    
    menu()
    


   
