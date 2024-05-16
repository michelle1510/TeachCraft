import tkinter as tk
import sqlite3

class MultiSelect(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("MultiSelect Example")
        self.geometry("400x300")

        # Connect to the SQLite database
        self.conn = sqlite3.connect('C:\\Users\\abroo\\Documents\\projects\\TeachCraft\\table.db')
        self.cursor = self.conn.cursor()

        # Retrieve data from the database
        self.data = self.get_data_from_database()

        # Display data in Tkinter
        self.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)
        for item in self.data:
            self.listbox.insert(tk.END, item)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        # Button to get selected items
        self.button = tk.Button(self, text="Get Selected", command=self.get_selected_items)
        self.button.pack()

    def get_data_from_database(self):
        # Execute SQL query to fetch data from the database
        self.cursor.execute("SELECT name FROM pros")
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def get_selected_items(self):
        selected_indices = self.listbox.curselection()
        selected_items = [self.listbox.get(index) for index in selected_indices]
        print("Selected items:", selected_items)

    def __del__(self):
        # Close the database connection when the application is closed
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiSelect()
    app.mainloop()
