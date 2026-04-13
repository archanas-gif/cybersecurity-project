from src.data_loader import load_data
from src.model import train_model

def main():
    df = load_data()
    model = train_model(df)

    print("\nThreat Detection Results:")
    print(df.head())

if __name__ == "__main__":
    main()