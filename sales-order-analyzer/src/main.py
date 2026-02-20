import pandas as pd

data = None

def menu():
    while(True):
        print("\n--------Sales Order Analyzer--------")
        print("1. Load CSV")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":

            data = load_csv("sales-order-analyzer/data/orders.csv")

        elif choice == "2":
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


if __name__ == "__main__":

    menu()
    


   
