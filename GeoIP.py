#You can get the countries of the IP addresses you save in a .cvs file.
import pandas as pd
import ipapi


def get_country_from_ip(ip_address):
    try:
        response = ipapi.location(ip_address)
        return response.country_name
    except Exception as e:
        print(f"Error retrieving country for IP {ip_address}: {e}")
        return "Unknown"


def extract_ip_from_csv(file_path, ip_column_name):
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)

        # Extract IP addresses from the specified column
        ip_addresses = data[ip_column_name].tolist()

        # Get the country for each IP address
        countries = [get_country_from_ip(ip) for ip in ip_addresses]

        # Add a new column with the country information
        data["Country"] = countries

        # Save the updated data to a new CSV file
        updated_file_path = file_path.replace(".csv", "_with_country.csv")
        data.to_csv(updated_file_path, index=False)

        print(f"Country information added and saved to '{updated_file_path}'")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")


if __name__ == "__main__":
    # Replace 'file.csv' with your CSV file path and 'IP_Column' with the column containing IP addresses
    csv_file_path = "/Here/goes/your/file.csv"
    ip_column = "IP_Column"

    extract_ip_from_csv(csv_file_path, ip_column)

#This may have a limitation due to the imported module.
