import tkinter as tk
from tkinter import messagebox, scrolledtext
import pandas as pd
import os
#hi hello there !!!
# ----- Dummy Credentials -----
USER_FILE = 'user_accounts.csv'

# ---------- Data Setup ----------
def create_crop_dataset():
    crops = [
        {'CName': 'Rice', 'Temp (°C)': '20-30', 'Hum (%)': '70-85', 'Mois (%)': '60-80', 'Rain (mm)': '1000-1500', 'Sun (hrs/day)': '4-6', 'Soil': 'Clayey', 'pH Level': '5.0-6.5', 'Water Needed (L/day)': '12-16'},
        {'CName': 'Maize', 'Temp (°C)': '18-27', 'Hum (%)': '60-70', 'Mois (%)': '50-70', 'Rain (mm)': '500-800', 'Sun (hrs/day)': '8-10', 'Soil': 'Sandy Loam', 'pH Level': '5.5-7.0', 'Water Needed (L/day)': '6-9'},
        {'CName': 'Sorghum', 'Temp (°C)': '25-32', 'Hum (%)': '50-60', 'Mois (%)': '40-60', 'Rain (mm)': '400-750', 'Sun (hrs/day)': '6-9', 'Soil': 'Sandy Loam', 'pH Level': '5.5-7.5', 'Water Needed (L/day)': '4-8'},
        {'CName': 'Pearl Millet', 'Temp (°C)': '25-35', 'Hum (%)': '40-60', 'Mois (%)': '30-50', 'Rain (mm)': '200-600', 'Sun (hrs/day)': '6-9', 'Soil': 'Sandy', 'pH Level': '5.0-7.5', 'Water Needed (L/day)': '3-6'},
        {'CName': 'Finger Millet', 'Temp (°C)': '20-30', 'Hum (%)': '50-65', 'Mois (%)': '50-70', 'Rain (mm)': '500-1000', 'Sun (hrs/day)': '5-8', 'Soil': 'Loamy', 'pH Level': '5.0-6.5', 'Water Needed (L/day)': '5-8'},
        {'CName': 'Sugarcane', 'Temp (°C)': '20-35', 'Hum (%)': '65-80', 'Mois (%)': '70-85', 'Rain (mm)': '1500-2500', 'Sun (hrs/day)': '6-9', 'Soil': 'Alluvial', 'pH Level': '6.5-7.5', 'Water Needed (L/day)': '15-20'},
        {'CName': 'Cotton', 'Temp (°C)': '21-30', 'Hum (%)': '50-75', 'Mois (%)': '50-65', 'Rain (mm)': '700-1300', 'Sun (hrs/day)': '6-10', 'Soil': 'Black Soil', 'pH Level': '5.5-7.5', 'Water Needed (L/day)': '8-12'},
        {'CName': 'Tomato', 'Temp (°C)': '18-27', 'Hum (%)': '50-70', 'Mois (%)': '50-70', 'Rain (mm)': '600-800', 'Sun (hrs/day)': '6-8', 'Soil': 'Loamy', 'pH Level': '5.5-7.5', 'Water Needed (L/day)': '4-6'},
        {'CName': 'Coconut', 'Temp (°C)': '27-32', 'Hum (%)': '60-80', 'Mois (%)': '50-70', 'Rain (mm)': '1500-2500', 'Sun (hrs/day)': '6-8', 'Soil': 'Sandy Loam', 'pH Level': '5.0-7.5', 'Water Needed (L/day)': '10-15'},
        {'CName': 'Banana', 'Temp (°C)': '26-30', 'Hum (%)': '70-90', 'Mois (%)': '60-80', 'Rain (mm)': '1200-2500', 'Sun (hrs/day)': '5-7', 'Soil': 'Loamy', 'pH Level': '5.5-7.5', 'Water Needed (L/day)': '10-20'}
    ]
    df = pd.DataFrame(crops)
    df.to_csv('crop_dataset.csv', index=False)
    messagebox.showinfo("Dataset", "Crop dataset created successfully!")

def details(crop_name):
    if not os.path.exists('crop_dataset.csv'):
        return "Dataset not found. Please create the dataset first."
    
    df = pd.read_csv('crop_dataset.csv')
    crop_info = df[df['CName'].str.lower().str.strip() == crop_name.lower().strip()]
    
    if not crop_info.empty:
        return crop_info.to_string(index=False)
    else:
        return f"Crop '{crop_name}' not found in the dataset."

# ---------- Feed to System Logic ----------
def feed_to_system():
    messagebox.showinfo("System Feed", "Fed to system successfully!")

    system_window = tk.Toplevel(root)
    system_window.title("System Operations")
    system_window.geometry("300x200")
    system_window.configure(bg="#f5f5f5")

    tk.Label(system_window, text="Choose Operation", font=("Arial", 14, "bold"), bg="#f5f5f5").pack(pady=15)

    def perform_harvest():
        messagebox.showinfo("Harvest", "Due to harvesting, the system has been shut down.")
        root.destroy()

    def show_maintenance_window():
        maintenance_window = tk.Toplevel(root)
        maintenance_window.title("Maintenance Panel")
        maintenance_window.geometry("300x350")
        maintenance_window.configure(bg="#f0f8ff")

        tk.Label(maintenance_window, text="Maintenance Panel", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(pady=15)

        def open_water_level():
            water_level_window = tk.Toplevel(root)
            water_level_window.title("Water Level Update")
            water_level_window.geometry("300x200")
            water_level_window.configure(bg="#f5f5f5")

            tk.Label(water_level_window, text="Update Water Level", font=("Arial", 12), bg="#f5f5f5").pack(pady=10)
            water_level_entry = tk.Entry(water_level_window, font=("Arial", 12))
            water_level_entry.pack(pady=10)
            def modify_water_level():
                messagebox.showinfo("Water Level", "Manual update of the water level is achieved.")
            tk.Button(water_level_window, text="Modify", font=("Arial", 12), command=modify_water_level, bg="#4CAF50", fg="white").pack(pady=5)

        def open_climatics():
            climatics_window = tk.Toplevel(root)
            climatics_window.title("Climatics Update")
            climatics_window.geometry("300x200")
            climatics_window.configure(bg="#f5f5f5")

            tk.Label(climatics_window, text="Update Climatics", font=("Arial", 12), bg="#f5f5f5").pack(pady=10)
            climatics_entry = tk.Entry(climatics_window, font=("Arial", 12))
            climatics_entry.pack(pady=10)
            def modify_climatics():
                messagebox.showinfo("Climatics", "Manual update of the climatics is achieved.")
            tk.Button(climatics_window, text="Modify", font=("Arial", 12), command=modify_climatics, bg="#4CAF50", fg="white").pack(pady=5)

        def open_fertilizers():
            fertilizers_window = tk.Toplevel(root)
            fertilizers_window.title("Update Fertilizer Level")
            fertilizers_window.geometry("300x200")
            fertilizers_window.configure(bg="#f5f5f5")

            tk.Label(fertilizers_window, text="Update Fertilizer Level", font=("Arial", 12), bg="#f5f5f5").pack(pady=10)
            fertilizers_entry = tk.Entry(fertilizers_window, font=("Arial", 12))
            fertilizers_entry.pack(pady=10)
            def modify_fertilizers():
                messagebox.showinfo("Fertilizers", "Manual update of the fertilizers is achieved.")
            tk.Button(fertilizers_window, text="Modify", font=("Arial", 12), command=modify_fertilizers, bg="#4CAF50", fg="white").pack(pady=5)

        def open_sunlight():
            sunlight_window = tk.Toplevel(root)
            sunlight_window.title("Update Sunlight density")
            sunlight_window.geometry("300x200")
            sunlight_window.configure(bg="#f5f5f5")

            tk.Label(sunlight_window, text="Update Sunlight Density", font=("Arial", 12), bg="#f5f5f5").pack(pady=10)
            sunlight_entry = tk.Entry(sunlight_window, font=("Arial", 12))
            sunlight_entry.pack(pady=10)
            def modify_sunlight():
                messagebox.showinfo("Sunlight", "Manual update of the sunlight is achieved.")
            tk.Button(sunlight_window, text="Modify", font=("Arial", 12), command=modify_sunlight, bg="#4CAF50", fg="white").pack(pady=5)

        # Buttons for Maintenance Options
        tk.Button(maintenance_window, text="Water Level", font=("Arial", 12), width=20, command=open_water_level, bg="#607d8b", fg="white").pack(pady=10)
        tk.Button(maintenance_window, text="Climatics", font=("Arial", 12), width=20, command=open_climatics, bg="#607d8b", fg="white").pack(pady=10)
        tk.Button(maintenance_window, text="Fertilizers", font=("Arial", 12), width=20, command=open_fertilizers, bg="#607d8b", fg="white").pack(pady=10)
        tk.Button(maintenance_window, text="Sunlight", font=("Arial", 12), width=20, command=open_sunlight, bg="#607d8b", fg="white").pack(pady=10)

    tk.Button(system_window, text="Harvest", font=("Arial", 12), bg="#4CAF50", fg="white", width=20,
              command=perform_harvest).pack(pady=10)

    tk.Button(system_window, text="Maintenance", font=("Arial", 12), bg="#2196F3", fg="white", width=20,
              command=show_maintenance_window).pack(pady=10)

# ---------- Account Creation Logic ----------
def create_new_account():
    def save_account():
        username = new_username_entry.get()
        password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()
        
        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        if os.path.exists(USER_FILE):
            existing_users = pd.read_csv(USER_FILE)
            if username in existing_users['Username'].values:
                messagebox.showerror("Error", "Username already taken!")
                return
        
        new_user = pd.DataFrame({'Username': [username], 'Password': [password]})
        new_user.to_csv(USER_FILE, mode='a', header=not os.path.exists(USER_FILE), index=False)
        messagebox.showinfo("Success", "Account created successfully!")
        new_account_window.destroy()

    new_account_window = tk.Toplevel(root)
    new_account_window.title("Create New Account")
    new_account_window.geometry("300x250")
    
    tk.Label(new_account_window, text="Create New Account", font=("Arial", 14)).pack(pady=10)
    tk.Label(new_account_window, text="Username:", font=("Arial", 12)).pack(pady=5)
    new_username_entry = tk.Entry(new_account_window, font=("Arial", 12))
    new_username_entry.pack(pady=5)
    tk.Label(new_account_window, text="Password:", font=("Arial", 12)).pack(pady=5)
    new_password_entry = tk.Entry(new_account_window, show="*", font=("Arial", 12))
    new_password_entry.pack(pady=5)
    tk.Label(new_account_window, text="Confirm Password:", font=("Arial", 12)).pack(pady=5)
    confirm_password_entry = tk.Entry(new_account_window, show="*", font=("Arial", 12))
    confirm_password_entry.pack(pady=5)
    tk.Button(new_account_window, text="Create Account", command=save_account, font=("Arial", 12), bg="#33cc33").pack(pady=15)

# ---------- Login Logic ----------
def attempt_login():
    entered_user = username_entry.get()
    entered_pass = password_entry.get()
    
    if os.path.exists(USER_FILE):
        users_df = pd.read_csv(USER_FILE)
        user_data = users_df[users_df['Username'] == entered_user]
        
        if not user_data.empty and user_data['Password'].values[0] == entered_pass:
            show_dashboard()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password!")
    else:
        messagebox.showerror("Login Failed", "No users found. Please create an account.")

# ---------- GUI Windows ----------
def show_dashboard():
    login_frame.destroy()

    dashboard = tk.Frame(root, bg="#e6f7ff")
    dashboard.pack(fill=tk.BOTH, expand=True)

    header = tk.Label(dashboard, text="!!E-FARMTECH GLADLY WELCOMES YOU!!", font=("Helvetica", 20, "bold"),
                      bg="#3399ff", fg="white", pady=10)
    header.pack(fill=tk.X)

    main_frame = tk.Frame(dashboard, bg="#e6f7ff")
    main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    left_frame = tk.Frame(main_frame, bg="#cceeff", bd=2, relief=tk.RIDGE, padx=10, pady=10)
    left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

    tk.Label(left_frame, text="Enter Crop Name:", font=("Arial", 12, "bold"), bg="#cceeff").pack(pady=5)
    crop_name_entry = tk.Entry(left_frame, font=("Arial", 12), width=25)
    crop_name_entry.pack(pady=5)

    def show_details():
        crop_name = crop_name_entry.get()
        result = details(crop_name)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)

    tk.Button(left_frame, text="Show Details", command=show_details, bg="#3399ff", fg="white",
              font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(left_frame, text="Create Dataset", command=create_crop_dataset, bg="#33cc33", fg="white",
              font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(left_frame, text="Feed to System", command=feed_to_system, bg="#ff9933", fg="white",
              font=("Arial", 12), width=20).pack(pady=5)

    right_frame = tk.Frame(main_frame, bg="#e6f7ff", bd=2, relief=tk.RIDGE, padx=10, pady=10)
    right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

    result_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
    result_text.pack(pady=10)

    tk.Button(dashboard, text="Log out", font=("Arial", 12), bg="#ff4d4d", fg="white", command=root.quit).pack(pady=10)

# ---------- Main Window ----------
root = tk.Tk()
root.title("E-FARMTECH Login")
root.geometry("400x400")
root.configure(bg="#dff0ea")
login_frame = tk.Frame(root, bg="#dff0ea")
login_frame.pack(expand=True)

tk.Label(login_frame, text="🌱 E-FARMTECH 🌱", font=("Helvetica", 18, "bold"), bg="#dff0ea").pack(pady=10)

tk.Label(login_frame, text="Username:", font=("Arial", 12), bg="#dff0ea").pack()
username_entry = tk.Entry(login_frame, font=("Arial", 12))
username_entry.pack(pady=5)

tk.Label(login_frame, text="Password:", font=("Arial", 12), bg="#dff0ea").pack()
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

tk.Button(
    login_frame,
    text="LOGIN",
    command=attempt_login,
    font=("Arial", 18, "bold"),
    bg="#007acc",
    fg="white",
    height=1,
    width=10
).pack(pady=25)

tk.Button(
    login_frame,
    text="Create New Account",
    command=create_new_account,
    font=("Arial", 12),
    bg="#33cc33",
    fg="white"
).pack(pady=10)

# ---------- Run ----------
root.mainloop()
