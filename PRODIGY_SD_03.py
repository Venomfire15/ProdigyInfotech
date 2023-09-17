import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # Initialize an empty list to store contacts
        self.contacts = []

        # Create and set up GUI elements
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, columnspan=2, padx=10, pady=10)

        self.contact_listbox = tk.Listbox(root)
        self.contact_listbox.grid(row=4, columnspan=2, padx=10, pady=10)

        self.edit_button = tk.Button(root, text="Edit Contact", command=self.edit_contact)
        self.edit_button.grid(row=5, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=1, padx=10, pady=10)

        self.load_example_data()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            contact = {
                "Name": name,
                "Phone": phone,
                "Email": email
            }
            self.contacts.append(contact)
            self.update_contact_listbox()
            self.clear_input_fields()
        else:
            messagebox.showerror("Error", "Please enter all contact details.")

    def edit_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            contact = self.contacts[selected_index]

            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()

            if name and phone and email:
                contact["Name"] = name
                contact["Phone"] = phone
                contact["Email"] = email
                self.update_contact_listbox()
                self.clear_input_fields()
            else:
                messagebox.showerror("Error", "Please enter all contact details.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            self.contacts.pop(selected_index)
            self.update_contact_listbox()
            self.clear_input_fields()

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            name = contact["Name"]
            phone = contact["Phone"]
            self.contact_listbox.insert(tk.END, f"{name} ({phone})")

    def clear_input_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def load_example_data(self):
        example_contacts = [
            {"Name": "John Doe", "Phone": "123-456-7890", "Email": "john@example.com"},
            {"Name": "Jane Smith", "Phone": "987-654-3210", "Email": "jane@example.com"}
        ]
        self.contacts.extend(example_contacts)
        self.update_contact_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
