import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

db_host = "127.0.0.1"
db_user = "root"
db_name = "patients"

db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    database=db_name
)

cursor = db.cursor()

def save_patient_details(bloodbankname_dropdown, Patient_Namevalue, Mobile_numbervalue, bloodtype_dropdown, Hospital_Adressvalue, Patient_Addressvalue):
    Blood_Bank_Name = bloodbankname_dropdown.get()
    Patient_Name = Patient_Namevalue.get()
    Mobile_number = Mobile_numbervalue.get()
    Blood_Type = bloodtype_dropdown.get()
    Hospital_Adress = Hospital_Adressvalue.get()
    Patient_Address = Patient_Addressvalue.get()

    values = (Blood_Bank_Name, Patient_Name, Mobile_number, Blood_Type, Hospital_Adress, Patient_Address)
    print("Patient details:", values)  # Debug print
    query = "INSERT INTO patients (Blood_Bank_Name, Patient_Name, Mobile_number, Blood_Type, Hospital_Adress, Patient_Address) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, values)
    db.commit()

    messagebox.showinfo("Success", "Patient details saved successfully!")

def save_donor_details(namevalue, gender_dropdown, dobvalue, mobilenovalue, addressvalue, weightvalue, Blood_Pressurevalue, Iron_Contentvalue, doctorname_dropdown, bloodbankname_dropdown, bloodtype_dropdown):
    name = namevalue.get()
    gender = gender_dropdown.get()
    dob = dobvalue.get()
    mobileno = mobilenovalue.get()
    address = addressvalue.get()
    weight = weightvalue.get()
    Blood_Pressure = Blood_Pressurevalue.get()
    Iron_Content = Iron_Contentvalue.get()
    Doctor_Name = doctorname_dropdown.get()
    Blood_Bank_Name = bloodbankname_dropdown.get()
    Blood_type = bloodtype_dropdown.get()

    values = (name, gender, dob, mobileno, address, weight, Blood_Pressure, Iron_Content, Doctor_Name, Blood_Bank_Name, Blood_type)
    print("Donor details:", values)  # Debug print
    query = "INSERT INTO donors (name, gender, dob, mobileno, address, weight, Blood_Pressure, Iron_Content, Doctor_Name, Blood_Bank_Name, Blood_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, values)
    db.commit()

    messagebox.showinfo("Success", "Donor details saved successfully!")

def button():
    root1 = tk.Tk()
    root1.geometry("500x300")

    tk.Label(root1, text="Patient Details", font="arial 15 bold").grid(row=0, column=3)

    Blood_Bank_Name = tk.Label(root1, text="Blood Bank Name")
    Patient_Name = tk.Label(root1, text="Patient Name")
    Mobile_number = tk.Label(root1, text="Mobile Number")
    Blood_Type = tk.Label(root1, text="Blood Type")
    Hospital_Adress = tk.Label(root1, text="Hospital Address")
    Patient_Address = tk.Label(root1, text="Patient Address")

    Blood_Bank_Name.grid(row=1, column=2)
    Patient_Name.grid(row=2, column=2)
    Mobile_number.grid(row=3, column=2)
    Blood_Type.grid(row=4, column=2)
    Hospital_Adress.grid(row=5, column=2)
    Patient_Address.grid(row=6, column=2)

    Patient_Namevalue = tk.StringVar()
    Mobile_numbervalue = tk.StringVar()
    Hospital_Adressvalue = tk.StringVar()
    Patient_Addressvalue = tk.StringVar()

    Patient_Nameentry = tk.Entry(root1, textvariable=Patient_Namevalue)
    Mobile_numberentry = tk.Entry(root1, textvariable=Mobile_numbervalue)
    Hospital_Adressentry = tk.Entry(root1, textvariable=Hospital_Adressvalue)
    Patient_Addressentry = tk.Entry(root1, textvariable=Patient_Addressvalue)

    Patient_Nameentry.grid(row=2, column=3)
    Mobile_numberentry.grid(row=3, column=3)
    Hospital_Adressentry.grid(row=5, column=3)
    Patient_Addressentry.grid(row=6, column=3)

    choices2 = ['None', 'Kasturbha Medical College', 'KIMS Hospital', 'KC General Hospital', 'Victoria Hospital', 'MGM Medical College', 'N.S.C Medical College', 'Sankalp India Foundation', 'Voluntary Health Services', 'Allahabad Medical Association Blood Bank', 'Ramakrishna mission Seva Prathishthan', 'Jeeva Dhara Voluntary Blood bank', 'Surat Raktadan Kendra and Research Centre']
    bloodbankname_dropdown = ttk.Combobox(root1, values=choices2)
    bloodbankname_dropdown.grid(row=1, column=3)

    choices = ['A+', 'B+', 'O+', 'AB+', 'A-', 'B-', 'O-', 'AB-']
    bloodtype_dropdown = ttk.Combobox(root1, values=choices)
    bloodtype_dropdown.grid(row=4, column=3)

    tk.Button(root1, text="Submit", command=lambda: save_patient_details(bloodbankname_dropdown, Patient_Namevalue, Mobile_numbervalue, bloodtype_dropdown, Hospital_Adressvalue, Patient_Addressvalue)).grid(row=7, column=3)

    root1.mainloop()

def button2():
    root2 = tk.Tk()
    root2.geometry("500x300")

    tk.Label(root2, text="Donor Details", font="ar 15 bold").grid(row=0, column=3)

    name = tk.Label(root2, text="Donor Name")
    gender = tk.Label(root2, text="Gender")
    dob = tk.Label(root2, text="Date Of Birth")
    mobileno = tk.Label(root2, text="Mobile Number")
    address = tk.Label(root2, text="Address")
    weight = tk.Label(root2, text="Weight")
    Blood_Pressure = tk.Label(root2, text="Blood Pressure")
    Iron_Content = tk.Label(root2, text="Iron Content")
    Doctor_Name = tk.Label(root2, text="Doctor Name")
    Blood_Bank_Name = tk.Label(root2, text="Blood Bank Name")
    Blood_type = tk.Label(root2, text="Blood Type")

    name.grid(row=1, column=2)
    gender.grid(row=2, column=2)
    dob.grid(row=3, column=2)
    mobileno.grid(row=4, column=2)
    address.grid(row=5, column=2)
    weight.grid(row=6, column=2)
    Blood_Pressure.grid(row=7, column=2)
    Iron_Content.grid(row=8, column=2)
    Doctor_Name.grid(row=9, column=2)
    Blood_Bank_Name.grid(row=10, column=2)
    Blood_type.grid(row=11, column=2)

    namevalue = tk.StringVar()
    dobvalue = tk.StringVar()
    mobilenovalue = tk.StringVar()
    addressvalue = tk.StringVar()
    weightvalue = tk.StringVar()
    Blood_Pressurevalue = tk.StringVar()
    Iron_Contentvalue = tk.StringVar()

    gender_dropdown = ttk.Combobox(root2, values=["Male", "Female"])
    gender_dropdown.grid(row=2, column=3)

    choices2 = ['None', 'Kasturbha Medical College', 'KIMS Hospital', 'KC General Hospital', 'Victoria Hospital', 'MGM Medical College', 'N.S.C Medical College', 'Sankalp India Foundation', 'Voluntary Health Services', 'Allahabad Medical Association Blood Bank', 'Ramakrishna mission Seva Prathishthan', 'Jeeva Dhara Voluntary Blood bank', 'Surat Raktadan Kendra and Research Centre']
    bloodbankname_dropdown = ttk.Combobox(root2, values=choices2)
    bloodbankname_dropdown.grid(row=10, column=3)

    choices = ['A+', 'B+', 'O+', 'AB+', 'A-', 'B-', 'O-', 'AB-']
    bloodtype_dropdown = ttk.Combobox(root2, values=choices)
    bloodtype_dropdown.grid(row=11, column=3)

    doctorname_dropdown = ttk.Combobox(root2, values=["None", "Dr.Anish pandry", "Dr.Manish Shetty", "Dr.Das", "Dr.Swathi", "Dr.Varshitha", "Dr.Faras", "Dr.Vasdevi", "Dr.Upasana"])
    doctorname_dropdown.grid(row=9, column=3)

    nameentry = tk.Entry(root2, textvariable=namevalue)
    dobentry = tk.Entry(root2, textvariable=dobvalue)
    mobilenoentry = tk.Entry(root2, textvariable=mobilenovalue)
    addressentry = tk.Entry(root2, textvariable=addressvalue)
    weightentry = tk.Entry(root2, textvariable=weightvalue)
    Blood_Pressureentry = tk.Entry(root2, textvariable=Blood_Pressurevalue)
    Iron_Contententry = tk.Entry(root2, textvariable=Iron_Contentvalue)

    nameentry.grid(row=1, column=3)
    dobentry.grid(row=3, column=3)
    mobilenoentry.grid(row=4, column=3)
    addressentry.grid(row=5, column=3)
    weightentry.grid(row=6, column=3)
    Blood_Pressureentry.grid(row=7, column=3)
    Iron_Contententry.grid(row=8, column=3)

    tk.Button(root2, text="Submit", command=lambda: save_donor_details(namevalue, gender_dropdown, dobvalue, mobilenovalue, addressvalue, weightvalue, Blood_Pressurevalue, Iron_Contentvalue, doctorname_dropdown, bloodbankname_dropdown, bloodtype_dropdown)).grid(row=13, column=3)

    root2.mainloop()

root = tk.Tk()
root.geometry("500x300")

tk.Label(root, text="BLOOD BANK MANAGEMENT SYSTEM", font="arial 15 bold").grid(row=0, column=3)
tk.Button(root, text="Patient Details", command=button).grid(row=1, column=3)
tk.Button(root, text="Donor Details", command=button2).grid(row=2, column=3)

root.mainloop()