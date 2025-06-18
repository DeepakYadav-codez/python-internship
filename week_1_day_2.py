contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact added: {name} - {phone}")

# Add two sample contacts
add_contact("Anil", "9999999999")
add_contact("Bhumika", "8888888888")

# Print all contacts
print("\nContact List:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")
