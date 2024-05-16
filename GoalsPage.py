import tkinter as tk
import sqlite3

class Goals:

    class MultiInputFrame(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.create_table()
            self.create_widgets()

        def create_widgets(self):
            # Create an entry widget for text input
            self.entry = tk.Entry(self)
            self.entry.grid(row=0, column=1, sticky="nw")  
            self.entry.config(width=50)  # Set width of the entry box

            # Create a label
            self.label = tk.Label(self, text="Enter goal:")
            self.label.grid(row=0, column=0, sticky="w")

            # Create a Text widget to display previous inputs
            self.text_display = tk.Text(self, state="disabled")
            self.text_display.grid(row=2, column=0, columnspan=2, sticky="nsew")  # Span two columns and fill the space

            # Make the text widget read-only
            self.text_display.config(state="normal", exportselection=False)

            # Disable editing by binding to an event that prevents changes
            self.text_display.bind("<KeyPress>", lambda e: "break")

            # Populate text widget with previous inputs from the database
            self.populate_previous_inputs()

            # Create a button
            self.button = tk.Button(self, text="Submit", command=self.get_input)
            self.button.grid(row=1, column=2, columnspan=1, sticky="nsew")  # Span two columns and fill the space

            # Create a clear button
            self.clear_button = tk.Button(self, text="Clear", command=self.clear_text)
            self.clear_button.grid(row=3, column=1, columnspan=1, sticky="se")  # Place at bottom right

        def get_input(self):
            input_text = self.entry.get()
            print("Input:", input_text)
            self.text_display.insert(tk.END, input_text + '\n')
            self.save_input_data(input_text)  # Save input data to the database
            self.entry.delete(0, tk.END)

        def create_table(self):
            # Connect to SQLite database (creates a new database if it doesn't exist)
            conn = sqlite3.connect('TeachCraft/table.db')

            # Create a cursor object
            cursor = conn.cursor()

            # Create a new table if it doesn't exist
            cursor.execute('''CREATE TABLE IF NOT EXISTS goals (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

            # Commit the changes and close the connection
            conn.commit()
            conn.close()

        def save_input_data(self, data):
            # Connect to SQLite database
            conn = sqlite3.connect('TeachCraft/table.db')

            # Create a cursor object
            cursor = conn.cursor()

            # Insert data into the table using parameterized query
            cursor.execute("INSERT INTO goals (data) VALUES (?)", (data,))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()


        def populate_previous_inputs(self):
            # Connect to SQLite database
            conn = sqlite3.connect('TeachCraft/table.db')

            # Create a cursor object
            cursor = conn.cursor()

            # Execute a query to fetch all previous inputs
            cursor.execute("SELECT data FROM goals")

            # Fetch all rows from the result set
            rows = cursor.fetchall()

            # Insert previous inputs into the text widget
            for row in rows:
                self.text_display.insert(tk.END, row[0] + '\n')

            # Close the connection
            conn.close()
        
        def clear_text(self):
            # Clear the text widget
            self.text_display.delete(1.0, tk.END)

            # Delete data from the SQL table
            conn = sqlite3.connect('TeachCraft/table.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM goals")
            conn.commit()
            conn.close()

    if __name__ == "__main__":
        root = tk.Tk()
        root.title("Page Title")

        # Create a frame for the tall rectangle
        tall_rectangle_frame = tk.Frame(root, width=100, bg="blue")
        tall_rectangle_frame.pack(side="left", fill="y")

        # Create a frame for the MultiInput
        multi_input_frame = MultiInputFrame(root)
        multi_input_frame.pack(side="left", padx=10, pady=10)

       

        root.mainloop()

    # slos = list()
    # asareas = list()

    # def __init__(self, goal):
    #     self.goal= goal

    # def display_info(self):
    #         print(f"Goal: {self.goal}")
    #         print(f"AsAreas: ")
    #         for area in self.asareas:
    #             print(f" - {area}")
    #             print(f"SLO :")
    #             for slo in self.slos:
    #                 print(f" - {slo}")
# class MyClass:
#     slos = list()
#     asareas = list()

#     def __init__(self, goal):
#         self.goal = goal

#     def add_slo(self, slo):
#         MyClass.slos.append(slo)

#     def add_asarea(self, asarea):
#         MyClass.asareas.append(asarea)

#     def display_info(self):
#         print(f"Goal: {self.goal}")
#         print("AsAreas:")
#         for area in MyClass.asareas:
#             print(f" - {area}")

#         print("SLOs:")
#         for slo in MyClass.slos:
#             print(f" - {slo}")

# # Example usage:
# my_instance = MyClass("My goal")

# # Add SLOs and AsAreas
# my_instance.add_slo("SLO 1")
# my_instance.add_slo("SLO 2")

# my_instance.add_asarea("Area 1")
# my_instance.add_asarea("Area 2")

# # Display information
# my_instance.display_info()


#create helper function to fill in other vars 